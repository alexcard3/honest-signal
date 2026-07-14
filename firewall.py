#!/usr/bin/env python3
"""
firewall - the pre-registration gate of honest-signal, as software.

A pre-registration is worth something only if it provably came FIRST. Git can prove
that. This tool makes git say it out loud, and fails your build when it cannot.

    firewall preregister <ID>    scaffold a pre-registration, validate it, commit it
    firewall verify              check every claim against the git record

`verify` enforces four rules, and reports a fifth thing it refuses to judge:

    (a) a result must have a pre-registration            FAIL if missing
    (b) the pre-registration commit must STRICTLY        FAIL if the same commit,
        precede the commit carrying the result                or a later one
    (c) the pre-registration must not have changed       FAIL if the blob differs
        after it was registered
    (d) the kill criterion must not be structurally      FAIL if vacuous
        vacuous
    (e) the gap between the two commits                  PRINTED, never a failure

Rule (e) is deliberate. A short gap is not a violation, and hiding it would be the
kind of tidiness this repository exists to refuse. We print ours: they include
twenty-three minutes.

WHAT THIS DOES NOT DO. It does not make you honest. It makes retrofitting visible
and expensive. Rule (d) is a linter, not a judge: it checks that a criterion carries
a threshold, a stated way to measure it, and a date in the future. It cannot tell you
whether the thing you promised to measure means anything. A determined author can
satisfy every rule here and still fool themselves - with a written record of having
done so, which is the most any tool can offer.

ONE FILE, ONE DEPENDENCY - and the honest version of that claim. This tool is a single
file you can copy, but it is not dependency-free: it needs PyYAML, because the alternative
was a hand-rolled YAML parser that would mis-read a user's valid file and report a verdict
that was quietly wrong. That is the one failure this tool may never have. The adoption path
we actually care about costs you nothing anyway: if you install the GitHub Action, it
installs PyYAML inside the runner and you install nothing.

We would have preferred the standard library's TOML parser. We could not switch: changing
the format means editing our own pre-registration, and that fails rule (c). The firewall
said no. See incident-log.md, Entry 2.

Requires: git, Python 3.11+, PyYAML.
"""
import argparse
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path

import yaml

PREREG_DIR = "preregistrations"
RESULT_DIR = "results"
TEMPLATE_NAME = "TEMPLATE.md"

REQUIRED_FIELDS = (
    "id",
    "claim",
    "hypothesis",
    "kill_criterion",
    "survive_criterion",
    "verification_date",
    "measured_by",
    "status",
)
VALID_STATUS = {"open", "killed", "survived", "void"}

# Rule (d) is structural. These are the phrases that let an author write a criterion
# that cannot fail - the placeholders of a promise never made. They are PHRASES, not
# words: a bare "later" would reject legitimate prose, and a false positive here bites
# the adopter, who is the thing we are trying to measure.
VACUOUS_PHRASES = (
    "tbd",
    "to be defined",
    "to be decided",
    "to be determined",
    "we will see",
    "somehow",
    "n/a",
    "not applicable",
    "unclear",
    "measure later",
    "decide later",
    "figure out later",
    "figure out",
    "as appropriate",
    "if it feels",
)
# A kill criterion has to point at a number. "Zero" is a number written out; "no" is not -
# it lets "we'll know it when we see it, no doubt" through. Make the author name the number.
HAS_THRESHOLD = re.compile(r"\d|\bzero\b|\bnone\b", re.IGNORECASE)
ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")

FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


# --------------------------------------------------------------------------- git
# Thin, honest wrappers. Every fact this tool reports comes from one of these.


def git(repo: Path, *args: str) -> str:
    """Run git and return stdout. Raises on a git error, so a broken assumption is loud."""
    out = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return out.stdout.strip()


def git_ok(repo: Path, *args: str) -> bool:
    """Run git for its exit code alone (the ancestry test)."""
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True
    ).returncode == 0


def repo_root(start: Path) -> Path:
    return Path(git(start, "rev-parse", "--show-toplevel"))


def name_status(repo: Path, commit: str) -> list[tuple[str, str]]:
    """(status, resulting path) for every file in a commit's FULL diff, renames detected.

    The full diff is the point. `git log --diff-filter=A -- <path>` cannot be trusted here:
    the pathspec filters the diff before rename detection runs, so the delete half of a
    rename is never seen, the pair is never made, and a moved-in file still reports as an
    addition. Rename detection needs both halves, so we ask for the whole commit.
    """
    out = git(repo, "show", "-M", "--name-status", "--format=", commit)
    rows = []
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            rows.append((parts[0], parts[-1]))  # "R100 old new" -> ("R100", "new")
    return rows


def commit_that_introduced(repo: Path, path: str) -> str | None:
    """The commit that ADDED `path` - the registration commit. None if nothing added it.

    This closes a laundering recipe that is three commands long: write a draft somewhere
    else, tune it once you have seen the result, `git mv` it into place, and the tuned
    text acquires a fresh, innocent-looking registration commit that precedes the verdict.

    So: we find the oldest commit that touched the path, and demand that it ADDED the file
    there. A file that arrived by rename has no registration commit and fails closed.
    A pre-registration must be born at its final path.

    Rename detection is pinned with `-M` rather than left to the user's `diff.renames`
    config. A tool that sells determinism cannot give different verdicts on different
    laptops - and this one would have, in the fail-OPEN direction.
    """
    if not git_ok(repo, "rev-parse", "--quiet", "--verify", "HEAD"):
        return None  # a repository with no commits has registered nothing
    touching = [line for line in git(repo, "log", "--format=%H", "--", path).splitlines() if line]
    if not touching:
        return None
    oldest = touching[-1]
    for status, resulting_path in name_status(repo, oldest):
        if resulting_path == path and status.startswith("A"):
            return oldest
    return None  # the path first appears by rename or copy: nothing was registered here


def is_shallow(repo: Path) -> bool:
    """A truncated history cannot establish precedence, and would fail claims silently."""
    return git(repo, "rev-parse", "--is-shallow-repository") == "true"


def blob_at(repo: Path, commit: str, path: str) -> str | None:
    """Hash of the file's content as of `commit`, or None if it did not exist then."""
    try:
        return git(repo, "rev-parse", f"{commit}:{path}")
    except subprocess.CalledProcessError:
        return None


def strictly_precedes(repo: Path, earlier: str, later: str) -> bool:
    """True iff `earlier` is an ancestor of `later` AND is not the same commit.

    The strictness is rule (b). Prediction and verdict in one commit prove nothing
    about which came first - and that is a row in our own FALSIFICATIONS.md.
    """
    if earlier == later:
        return False
    return git_ok(repo, "merge-base", "--is-ancestor", earlier, later)


def committed_at(repo: Path, commit: str) -> datetime:
    return datetime.fromisoformat(git(repo, "show", "-s", "--format=%cI", commit))


def humanised(delta_seconds: float) -> str:
    minutes = delta_seconds / 60
    if minutes < 90:
        return f"{minutes:.0f} min"
    hours = minutes / 60
    if hours < 48:
        return f"{hours:.1f} h"
    return f"{hours / 24:.1f} days"


# -------------------------------------------------------------------- validation
# Rule (d). Pure functions over the parsed front-matter: no git, no I/O.


def read_frontmatter(text: str) -> dict:
    match = FRONTMATTER.match(text)
    if not match:
        raise ValueError("no YAML front-matter (the file must start with a --- block)")
    parsed = yaml.safe_load(match.group(1))
    if not isinstance(parsed, dict):
        raise ValueError("front-matter is not a mapping of fields")
    return parsed


def is_vacuous(value: str) -> bool:
    lowered = value.lower()
    return any(phrase in lowered for phrase in VACUOUS_PHRASES)


def validate(front: dict, claim_id: str, registered_on: date | None) -> list[str]:
    """Rule (d), in full. Returns the reasons this pre-registration is not usable."""
    failures: list[str] = []

    for key in REQUIRED_FIELDS:
        value = front.get(key)
        if value is None or (isinstance(value, str) and not value.strip()):
            failures.append(f"missing or empty required field: {key}")

    if front.get("id") != claim_id:
        failures.append(f"id '{front.get('id')}' does not match the filename '{claim_id}'")

    kill = str(front.get("kill_criterion") or "")
    if kill.strip():
        if not HAS_THRESHOLD.search(kill):
            failures.append(
                "kill_criterion states no threshold - a criterion without a number "
                "cannot be met or missed. Write 'zero' rather than 'no': name the number."
            )
        if is_vacuous(kill):
            failures.append("kill_criterion is vacuous (it contains a placeholder phrase)")

    survive = str(front.get("survive_criterion") or "")
    if survive.strip() and is_vacuous(survive):
        failures.append("survive_criterion is vacuous (it contains a placeholder phrase)")

    verification_date = front.get("verification_date")
    if verification_date is not None:
        if isinstance(verification_date, datetime):
            verification_date = verification_date.date()
        if not isinstance(verification_date, date):
            failures.append("verification_date is not an ISO date (YYYY-MM-DD)")
        elif registered_on and verification_date <= registered_on:
            failures.append(
                f"verification_date {verification_date} is not after the registration "
                f"date {registered_on} - you cannot pre-register a verdict for the past"
            )

    measured_by = front.get("measured_by")
    if measured_by is not None:
        if not isinstance(measured_by, list) or not measured_by:
            failures.append("measured_by must be a non-empty list of metrics")
        else:
            for index, metric in enumerate(measured_by):
                label = (metric.get("id") if isinstance(metric, dict) else None) or f"#{index + 1}"
                if not isinstance(metric, dict):
                    failures.append(f"measured_by {label} is not a mapping")
                    continue
                for key in ("what", "how"):
                    text = str(metric.get(key) or "").strip()
                    if not text:
                        failures.append(f"measured_by {label}: missing '{key}'")
                    elif is_vacuous(text):
                        failures.append(f"measured_by {label}: '{key}' is a placeholder, not a procedure")
                how = str(metric.get("how") or "").strip()
                if how and len(how) < 20:
                    failures.append(
                        f"measured_by {label}: 'how' is too short to be a procedure "
                        f"someone else could follow"
                    )

    status = front.get("status")
    if status is not None and status not in VALID_STATUS:
        failures.append(f"status '{status}' is not one of {sorted(VALID_STATUS)}")

    return failures


# ------------------------------------------------------------------------ verify


@dataclass
class Evidence:
    """What the git record says about one claim. This is the whole output."""

    claim_id: str
    prereg_commit: str | None = None
    result_commit: str | None = None
    gap: str | None = None
    failures: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.failures


def claim_ids(repo: Path) -> list[str]:
    """Every claim the repository knows about: a pre-registration, a result, or both."""
    found = set()
    for directory in (PREREG_DIR, RESULT_DIR):
        for path in sorted((repo / directory).glob("*.md")):
            if path.name != TEMPLATE_NAME:
                found.add(path.stem)
    return sorted(found)


def gather(repo: Path, claim_id: str) -> Evidence:
    """Apply rules (a)-(e) to one claim. Every branch here is a rule in the docstring."""
    evidence = Evidence(claim_id)
    prereg_path = f"{PREREG_DIR}/{claim_id}.md"
    result_path = f"{RESULT_DIR}/{claim_id}.md"

    prereg_file = repo / prereg_path
    result_file = repo / result_path

    # (a) a result with no pre-registration is not a result. It is a claim.
    if not prereg_file.exists():
        evidence.failures.append(
            f"(a) {result_path} claims a result, but {prereg_path} does not exist - "
            f"nothing was pre-registered"
        )
        return evidence

    c_pre = commit_that_introduced(repo, prereg_path)
    evidence.prereg_commit = c_pre

    # (d) structural validity of the pre-registration itself.
    registered_on = committed_at(repo, c_pre).date() if c_pre else None
    try:
        front = read_frontmatter(prereg_file.read_text(encoding="utf-8"))
    except ValueError as error:
        evidence.failures.append(f"(d) {prereg_path}: {error}")
        return evidence
    evidence.failures.extend(f"(d) {reason}" for reason in validate(front, claim_id, registered_on))

    if c_pre is None:
        # No commit ever ADDED this path. Either it is not committed at all, or it was
        # moved here from somewhere else - and a file that arrives by `git mv` carries no
        # proof of when its content was written. Both fail; they fail differently.
        if blob_at(repo, "HEAD", prereg_path) is not None:
            evidence.failures.append(
                f"(b) {prereg_path} is committed, but no commit ever added it at this "
                f"path - it was moved here. A pre-registration that arrives by rename "
                f"proves nothing about when it was written. Register it at its final path."
            )
            return evidence
        evidence.notes.append("not yet committed - this run registers it")
        if result_file.exists():
            evidence.failures.append(
                "(b) the pre-registration is not committed, so it cannot be shown to "
                "precede anything - commit it before the result exists"
            )
        return evidence

    # (c) immutability. An edit after registration fails here even when no result exists
    # yet: the cost is paid at edit time, not at publication time.
    #
    # We check the working tree as well as the record. An uncommitted edit is still an
    # edit - reporting PASS on a file the author has already changed would be precisely
    # the quietly-wrong answer this tool exists to prevent.
    blob_registered = blob_at(repo, c_pre, prereg_path)
    if blob_at(repo, "HEAD", prereg_path) != blob_registered:
        evidence.failures.append(
            f"(c) {prereg_path} was modified after it was registered in {c_pre[:7]} - "
            f"a pre-registration that can still be edited is not a pre-registration"
        )
    elif not git_ok(repo, "diff", "--quiet", c_pre, "--", prereg_path):
        evidence.failures.append(
            f"(c) {prereg_path} is modified in the working tree, uncommitted. It differs "
            f"from what was registered in {c_pre[:7]}. Committing it will not help."
        )

    if not result_file.exists():
        evidence.notes.append("registered; no result yet")
        return evidence

    c_res = commit_that_introduced(repo, result_path)
    if c_res is None:
        evidence.failures.append(
            f"(b) {result_path} is not committed - precedence cannot be established"
        )
        return evidence
    evidence.result_commit = c_res

    # (b) strict precedence. Same commit is a failure, and it is the one we ourselves failed.
    if not strictly_precedes(repo, c_pre, c_res):
        reason = (
            "prediction and verdict landed in the same commit"
            if c_pre == c_res
            else "the pre-registration does not precede the result in the history"
        )
        evidence.failures.append(f"(b) {reason} ({c_pre[:7]} -> {c_res[:7]})")

    # (c) again, at the moment of the result - the reading that the rule actually names.
    # If the file did not exist yet at the result commit, (b) has already said so; a
    # second complaint about it would be noise, not evidence.
    blob_at_result = blob_at(repo, c_res, prereg_path)
    if blob_at_result is not None and blob_at_result != blob_registered:
        evidence.failures.append(
            f"(c) {prereg_path} differed at the result commit {c_res[:7]} from the "
            f"version registered in {c_pre[:7]}"
        )

    # (e) the gap. Reported, never judged.
    if c_pre != c_res:
        delta = (committed_at(repo, c_res) - committed_at(repo, c_pre)).total_seconds()
        evidence.gap = humanised(delta) if delta >= 0 else "negative (!)"

    return evidence


def report(evidences: list[Evidence]) -> int:
    if not evidences:
        print("firewall: no claims found. Nothing to verify.")
        return 0

    for evidence in evidences:
        mark = "PASS" if evidence.passed else "FAIL"
        print(f"\n[{mark}] {evidence.claim_id}")
        if evidence.prereg_commit:
            print(f"       pre-registered : {evidence.prereg_commit[:10]}")
        if evidence.result_commit:
            print(f"       result         : {evidence.result_commit[:10]}")
        if evidence.gap:
            print(f"       gap            : {evidence.gap}   (reported, not judged)")
        for note in evidence.notes:
            print(f"       note           : {note}")
        for failure in evidence.failures:
            print(f"       -> {failure}")

    failed = [evidence for evidence in evidences if not evidence.passed]
    print("\n" + "-" * 72)
    print(f"{len(evidences) - len(failed)} passed, {len(failed)} failed.")
    if failed:
        print("The artifact does not compile. That is the gate working, not a bug.")
        return 1
    print("Every claim in this repository is backed by a pre-registration that")
    print("provably came first and has not been touched since.")
    return 0


# ------------------------------------------------------------------- preregister


def scaffold(repo: Path, claim_id: str) -> Path:
    template = repo / PREREG_DIR / TEMPLATE_NAME
    if not template.exists():
        raise SystemExit(f"firewall: no template at {template}")
    destination = repo / PREREG_DIR / f"{claim_id}.md"
    if destination.exists():
        raise SystemExit(
            f"firewall: {destination} already exists. A pre-registration is written "
            f"once. If it is wrong, withdraw it in the open and register a new id."
        )
    destination.write_text(
        template.read_text(encoding="utf-8").replace("<ID>", claim_id), encoding="utf-8"
    )
    return destination


def preregister(repo: Path, claim_id: str, do_commit: bool) -> int:
    if not ID_PATTERN.match(claim_id):
        raise SystemExit(f"firewall: '{claim_id}' is not a usable claim id")

    destination = scaffold(repo, claim_id)
    relative = destination.relative_to(repo).as_posix()
    print(f"firewall: wrote {relative}")

    front = read_frontmatter(destination.read_text(encoding="utf-8"))
    failures = validate(front, claim_id, registered_on=None)
    if failures:
        print("\nStill to fill in before this can be committed:")
        for failure in failures:
            print(f"  -> {failure}")
        print("\nThis is the gate giving you the questions before it takes anything away.")
        if do_commit:
            print("\nNot committing: an invalid pre-registration is not a pre-registration.")
            return 1
        return 0

    print("\nThis pre-registration is valid: it states what would kill the claim, how that")
    print("would be measured, and by when.")
    if do_commit:
        git(repo, "add", relative)
        git(repo, "commit", "-m", f"firewall: pre-register {claim_id}")
        print(f"\nCommitted. From here on, editing {relative} fails rule (c), in the open.")
    return 0


# -------------------------------------------------------------------------- main


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="firewall",
        description="The pre-registration gate: prove the prediction came first, or fail.",
    )
    subcommands = parser.add_subparsers(dest="command", required=True)

    new = subcommands.add_parser("preregister", help="scaffold and validate a pre-registration")
    new.add_argument("id", help="the claim id, e.g. P-TOOL-1")
    new.add_argument("--commit", action="store_true", help="commit it if it is valid")

    check = subcommands.add_parser("verify", help="check every claim against the git record")
    check.add_argument("ids", nargs="*", help="claim ids (default: all of them)")

    args = parser.parse_args(argv)
    repo = repo_root(Path.cwd())

    if args.command == "preregister":
        return preregister(repo, args.id, args.commit)

    if is_shallow(repo):
        print(
            "firewall: this is a shallow clone. The history is truncated, so a "
            "pre-registration commit cannot be found even when it exists.\n"
            "          Use `fetch-depth: 0` on actions/checkout. Refusing to report a "
            "verdict on a history we cannot see.",
            file=sys.stderr,
        )
        return 1

    wanted = args.ids or claim_ids(repo)
    return report([gather(repo, claim_id) for claim_id in wanted])


if __name__ == "__main__":
    sys.exit(main())
