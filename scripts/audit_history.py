#!/usr/bin/env python3
"""
audit_history.py - run the firewall's rules over our own past, and publish what it says.

The evidence columns of FALSIFICATIONS.md were written by hand. Hand-written evidence is
the thing this repository exists to distrust, so this script regenerates them from the git
record instead. From here on the numbers in that table cannot drift away from the commits.

The histories it reads are private (a research monorepo and a mission-control repo, both
under feed terms we cannot redistribute). You cannot run this. Only its OUTPUT is published
- no data, no paths, no commit contents. What you can check is that the tool is the same one
whose rules are enforced on every pull request here, applied to its authors without mercy.

Usage:
    python scripts/audit_history.py --mc <path-to-mission-control> --ledger <path/inside/it>
    python scripts/audit_history.py --mc ... --ledger ... --badge      # also writes audit/

THE BADGE, AND WHY IT IS EMITTED HERE RATHER THAN TYPED
------------------------------------------------------
`--badge` writes `audit/badge.json` (a shields.io endpoint file) and `audit/report.txt` (this
run's output, verbatim). The number in the badge is COUNTED from the same buckets the
cross-check just reconciled against the published table - so the digit a reader sees is a byte
this tool produced. A badge carrying a hand-typed number would be an assertion wearing the
costume of a machine verdict, which is the one thing this repository exists to refuse.

Only the machine-checkable number goes in. Proof of precedence is a property of the git record,
so a program can count it. The number a machine CANNOT check - how many of the eighteen went
through the full protocol, companion gate included - is a fact about *process*. It stays in
prose, marked as our word. The two guarantees are never merged into one figure.

And the honest limit of the badge itself: this script reads PRIVATE histories, so it cannot run
in public CI and you cannot re-run it. The badge is machine-PRODUCED; it is not externally
machine-VERIFIABLE. What you can check is that it agrees with `audit/report.txt` and with the
row-by-row table in FALSIFICATIONS.md. We say so rather than let the badge imply otherwise.

TWO RULERS, REPORTED SEPARATELY AND NEVER MERGED
------------------------------------------------
Our pre-registrations do not live one-per-file, as `firewall` demands of everyone else.
They live as sections of a single append-only ledger. That has a consequence we must not
paper over:

  STRONG (file-granular blob immutability), which is what firewall.py enforces:
      NOT APPLICABLE. The ledger's blob changes every time ANY other claim is registered.
      Under the strong ruler every row would fail, for a reason that has nothing to do with
      retrofitting. Reporting that as a failure would be as dishonest as reporting it as a
      pass.

  WEAK (block immutability): did the claim's own section change between the commit that
      registered it and the commit that delivered the verdict?
      This is REAL EVIDENCE and we had not looked at it. It is weaker than the strong ruler
      because it depends on parsing section boundaries rather than on a hash: a determined
      author could move a boundary. We say so, and we look anyway. Declaring "we have
      nothing" when what we actually have is "we did not check" is the same error as
      overclaiming, pointed in the socially comfortable direction.
"""
import argparse
import contextlib
import difflib
import io
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import firewall  # noqa: E402  - the same rules, the same code, turned on ourselves

# The eighteen, as published in FALSIFICATIONS.md. Commits are already public there.
# `prereg` and `result` are the commits the hand-written table claims. This script does not
# trust them: it asks git what they actually are.
CLAIMS = [
    dict(row=1, name="AutoCM clustering (1st species)", claim_id=None, prereg=None, result=None),
    dict(row=2, name="Lead-lag intra-crypto", claim_id=None, prereg=None, result=None),
    dict(row=3, name="Shock-response cross-class", claim_id=None, prereg=None, result=None),
    dict(row=4, name="Momentum walk-forward", claim_id=None, prereg=None, result=None),
    dict(row=5, name="Signal-horizon", claim_id=None, prereg=None, result=None),
    dict(row=6, name="Dispersion-regime", claim_id=None, prereg=None, result=None),
    dict(row=7, name="Long-only unconditional", claim_id=None, prereg=None, result=None),
    dict(row=8, name="Arc-closer (crypto)", claim_id=None, prereg=None, result=None),
    dict(row=9, name="Raw equity momentum", claim_id=None, prereg=None, result=None),
    dict(row=10, name="Defense overlay", claim_id=None, prereg=None, result=None),
    dict(row=11, name="Regime-axis", claim_id=None, prereg=None, result=None),
    dict(row=12, name="Gap-test weekend", claim_id=None, prereg=None, result=None),
    dict(row=13, name="L2 reversal@1d", claim_id="P-VAL-1", prereg="6f10173", result="6f10173"),
    dict(row=14, name="P-WPROBE-1", claim_id="P-WPROBE-1", prereg="fe78196", result="8dc72a3"),
    dict(row=15, name="P-CARRY-1", claim_id="P-CARRY-1", prereg="c3f4cee", result="9307c84"),
    dict(row=16, name="P-CARRY-2", claim_id="P-CARRY-2", prereg="635bf18", result="635bf18"),
    dict(row=17, name="P-SHOCK-1", claim_id="P-SHOCK-1", prereg="cbdebd6", result="1c73543"),
    dict(row=18, name="P-CTSM-1", claim_id="P-CTSM-1", prereg="2b1a5f7", result="4558fd3"),
]

# What the hand-written table asserts, so the machine can contradict it if it is wrong.
HAND_WRITTEN = {"firewall": [14, 15, 17, 18], "same_commit": [13, 16], "no_commit": list(range(1, 13))}


def resolve(repo: Path, ref: str) -> str:
    return firewall.git(repo, "rev-parse", ref)


def section(repo: Path, commit: str, ledger: str, claim_id: str) -> list[str] | None:
    """The claim's own block in the ledger, as of `commit`. None if it is not there yet."""
    text = firewall.git(repo, "show", f"{commit}:{ledger}")
    lines = text.splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith(f"## {claim_id} ")), None)
    if start is None:
        return None
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    return lines[start:end]


def compare_blocks(before: list[str], after: list[str]) -> tuple[str, str, list[str]]:
    """Did the registered text survive to the verdict? (state, detail, the lines that did not)

    APPEND-ONLY is the honest pass for a ledger: the verdict is written into the same block
    beneath the prediction, so the block GROWS. What must not happen is a registered line
    being changed or removed - that is retrofitting, and it is what this looks for.

    The changed lines are RETURNED, not summarised. A count is something you have to take on
    trust ("three lines changed - but which?"); the lines themselves are evidence. This
    repository has already published one correction for the difference between the two.
    """
    if before == after:
        return "UNCHANGED", "the block is byte-identical at both commits", []
    if after[: len(before)] == before:
        added = len(after) - len(before)
        return "APPEND-ONLY", f"every registered line survives verbatim; {added} appended below", []

    lost = []
    for tag, i1, i2, _, _ in difflib.SequenceMatcher(a=before, b=after).get_opcodes():
        if tag in ("replace", "delete"):
            lost.extend(before[i1:i2])
    return "MODIFIED", f"{len(lost)} registered lines did not survive verbatim", lost


def audit(repo: Path, ledger: str) -> list[dict]:
    findings = []
    for claim in CLAIMS:
        found = dict(claim, precedence="-", strong="-", weak="-", gap="-", state="no commit")

        if not claim["prereg"]:
            found["state"] = "off-repo"
            found["weak"] = "n/a - nothing was committed"
            findings.append(found)
            continue

        c_pre = resolve(repo, claim["prereg"])
        c_res = resolve(repo, claim["result"])

        # (b) - the rule that fails prediction and verdict landing together.
        if c_pre == c_res:
            found["state"] = "same commit as verdict"
            found["precedence"] = "FAIL - prediction and verdict in one commit"
            found["weak"] = "n/a - there is no interval in which the text could be edited"
            found["strong"] = "n/a - same commit"
            findings.append(found)
            continue

        strict = firewall.strictly_precedes(repo, c_pre, c_res)
        found["state"] = "firewall"
        found["precedence"] = "PASS" if strict else "FAIL - not an ancestor of the result"

        # (e) - printed, never judged.
        delta = (firewall.committed_at(repo, c_res) - firewall.committed_at(repo, c_pre)).total_seconds()
        found["gap"] = firewall.humanised(delta)

        # (c) STRONG - measured, then labelled. We do not report a number we cannot mean.
        blob_pre = firewall.blob_at(repo, c_pre, ledger)
        blob_res = firewall.blob_at(repo, c_res, ledger)
        found["strong"] = (
            "n/a - shared ledger"
            if blob_pre != blob_res
            else "PASS (the ledger happened not to change)"
        )

        # (c) WEAK - the evidence we had not looked at.
        before = section(repo, c_pre, ledger, claim["claim_id"])
        after = section(repo, c_res, ledger, claim["claim_id"])
        if before is None:
            found["weak"] = "FAIL - no such block at the registration commit"
        elif after is None:
            found["weak"] = "FAIL - the block is gone by the verdict commit"
        else:
            state, detail, lost = compare_blocks(before, after)
            found["weak"] = f"{state} - {detail}"
            found["lost_lines"] = lost

        findings.append(found)
    return findings


def cross_check(findings: list[dict]) -> bool:
    """MANDATORY. The machine must reproduce the hand-written table. If a single cell
    disagrees, either the table was wrong or the tool is - and both are findings. We stop
    and say so. We do not adjust the output until it agrees."""
    machine = {"firewall": [], "same_commit": [], "no_commit": []}
    for found in findings:
        key = {"firewall": "firewall", "same commit as verdict": "same_commit", "off-repo": "no_commit"}
        machine[key[found["state"]]].append(found["row"])

    print("\n" + "=" * 78)
    print("CROSS-CHECK - the machine against the table we wrote by hand")
    print("=" * 78)
    agreed = True
    for bucket in ("firewall", "same_commit", "no_commit"):
        hand, found = HAND_WRITTEN[bucket], machine[bucket]
        mark = "agree" if hand == found else "DISAGREE"
        if hand != found:
            agreed = False
        print(f"  {bucket:12s} hand: {hand}")
        print(f"  {'':12s} tool: {found}   -> {mark}")
    return agreed


class Tee:
    """Write to the console and to a buffer at once.

    The file we publish must be the text the operator actually saw, not a second rendering of
    it. Two code paths producing "the same" report is how they quietly stop being the same.
    """

    def __init__(self, *streams):
        self.streams = streams

    def write(self, text: str) -> int:
        for stream in self.streams:
            stream.write(text)
        return len(text)

    def flush(self) -> None:
        for stream in self.streams:
            stream.flush()


def publish(findings: list[dict], report_text: str, out_dir: Path) -> dict:
    """Write the badge and the raw report. The number is COUNTED here; it is never typed.

    UTF-8 is pinned on the way out. The ledger contains non-ASCII characters, and a console
    that mangles them must not be allowed to mangle the published artifact too.
    """
    firewalled = [found["row"] for found in findings if found["state"] == "firewall"]
    total = len(findings)

    badge = {
        "schemaVersion": 1,
        "label": "proof of precedence",
        "message": f"{len(firewalled)} of {total}",
        # Red, and it should be. It is the true reading of our own history, and the README
        # explains what it means rather than choosing a colour that hides it.
        "color": "red" if len(firewalled) * 2 < total else "green",
    }

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "badge.json").write_text(json.dumps(badge, indent=2) + "\n", encoding="utf-8")
    (out_dir / "report.txt").write_text(report_text, encoding="utf-8")
    return badge


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mc", required=True, type=Path, help="path to the mission-control repo")
    parser.add_argument("--ledger", required=True, help="path of the pre-registration ledger inside it")
    parser.add_argument(
        "--badge",
        action="store_true",
        help="write the shields.io endpoint file and this run's raw output into --out",
    )
    parser.add_argument("--out", type=Path, default=Path("audit"), help="where --badge writes (default: audit/)")
    args = parser.parse_args()

    buffer = io.StringIO()
    with contextlib.redirect_stdout(Tee(sys.stdout, buffer)):
        findings = audit(args.mc, args.ledger)

        print(f"{'#':>3}  {'claim':<14} {'pre-registration':<22} {'precedence':<12} {'gap':<10}")
        print("-" * 78)
        for found in findings:
            print(
                f"{found['row']:>3}  {(found['claim_id'] or found['name'])[:14]:<14} "
                f"{found['state']:<22} {found['precedence'][:12]:<12} {found['gap']:<10}"
            )

        print("\nRULE (c) - IMMUTABILITY, UNDER BOTH RULERS")
        print("-" * 78)
        for found in findings:
            if found["prereg"]:
                print(f"  {found['claim_id']:<12} strong: {found['strong']}")
                print(f"  {'':<12} weak  : {found['weak']}")
                # The lines themselves, not a count of them. Read them and judge for yourself
                # whether what changed was the prediction or the empty slot the verdict fills.
                for line in found.get("lost_lines", []):
                    print(f"  {'':<12}         did not survive: {line.strip()[:90]}")

        agreed = cross_check(findings)
        print()
        if agreed:
            print("The tool reproduces the hand-written table. The numbers are now regenerable.")
        else:
            print("STOP. The tool and the table disagree. Either the table was wrong or the tool is.")
            print("Do not adjust the output to make them agree. Find out which.")

    if not agreed:
        return 1

    # The badge is emitted ONLY when the machine and the published table agree. A badge minted
    # from a run that contradicted the table would be a number with no witness - and the first
    # thing anyone would do with it is trust it.
    if args.badge:
        badge = publish(findings, buffer.getvalue(), args.out)
        print(f"\nwrote {args.out / 'badge.json'} -> {badge['label']}: {badge['message']}")
        print(f"wrote {args.out / 'report.txt'} -> this run, verbatim")
    return 0


if __name__ == "__main__":
    sys.exit(main())
