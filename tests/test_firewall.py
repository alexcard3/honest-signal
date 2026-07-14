"""Tests for `firewall`.

The tests that matter here are the FAILING ones. A gate that only confirms good
behaviour has not been shown to bite; these show it biting, on each of the four rules
it enforces — including rule (b) failing exactly the way we ourselves failed it
(prediction and verdict in one commit: FALSIFICATIONS.md, row 16).

Run:  python -m unittest discover -s tests
"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import firewall  # noqa: E402

VALID = """---
id: {id}
claim: >
  A pre-registration gate is adopted by people who are not us.
hypothesis: >
  If we ship it, at least one external party installs it.
kill_criterion: >
  KILL if on the verification date the count of external installations is 0.
survive_criterion: >
  NOT killed if at least 1 external installation exists.
verification_date: 2099-01-01
measured_by:
  - id: M1
    what: External repositories referencing the Action in a workflow.
    how: >
      GitHub code search for the action reference, counting hits whose owner is
      not us. Anyone can run this query.
status: open
---

# {id}
"""

RESULT = """---
result_for: {id}
verdict: NO
---

# {id} — dead
"""


class Sandbox:
    """A throwaway git repository. Every fact the tool reports comes from this history."""

    def __init__(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "test@example.com")
        self.git("config", "user.name", "test")
        (self.path / firewall.PREREG_DIR).mkdir()
        (self.path / firewall.RESULT_DIR).mkdir()

    def git(self, *args: str) -> None:
        subprocess.run(["git", "-C", str(self.path), *args], check=True, capture_output=True)

    def write(self, relative: str, text: str) -> None:
        (self.path / relative).write_text(text, encoding="utf-8")

    def commit(self, message: str) -> None:
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)

    def preregister(self, claim_id: str, text: str | None = None) -> None:
        self.write(f"{firewall.PREREG_DIR}/{claim_id}.md", text or VALID.format(id=claim_id))

    def result(self, claim_id: str) -> None:
        self.write(f"{firewall.RESULT_DIR}/{claim_id}.md", RESULT.format(id=claim_id))

    def cleanup(self) -> None:
        self._tmp.cleanup()


class FirewallTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = Sandbox()
        self.addCleanup(self.repo.cleanup)

    def gather(self, claim_id: str = "P-TEST-1") -> firewall.Evidence:
        return firewall.gather(self.repo.path, claim_id)

    def reasons(self, evidence: firewall.Evidence) -> str:
        return " | ".join(evidence.failures)

    # --------------------------------------------------------------- it passes

    def test_preregistration_then_result_passes_and_reports_the_gap(self) -> None:
        self.repo.preregister("P-TEST-1")
        self.repo.commit("firewall: pre-register P-TEST-1")
        self.repo.result("P-TEST-1")
        self.repo.commit("result: P-TEST-1 is dead")

        evidence = self.gather()
        self.assertTrue(evidence.passed, self.reasons(evidence))
        self.assertIsNotNone(evidence.prereg_commit)
        self.assertIsNotNone(evidence.result_commit)
        self.assertIsNotNone(evidence.gap, "rule (e): the gap is reported, never hidden")

    def test_a_registration_with_no_result_yet_is_fine(self) -> None:
        self.repo.preregister("P-TEST-1")
        self.repo.commit("firewall: pre-register P-TEST-1")

        evidence = self.gather()
        self.assertTrue(evidence.passed, self.reasons(evidence))
        self.assertIn("no result yet", " ".join(evidence.notes))

    # ------------------------------------------------ (a) no pre-registration

    def test_a_result_with_no_preregistration_fails(self) -> None:
        self.repo.result("P-TEST-1")
        self.repo.commit("result: P-TEST-1 — a claim with nothing behind it")

        evidence = self.gather()
        self.assertFalse(evidence.passed)
        self.assertIn("(a)", self.reasons(evidence))

    # --------------------------------------------------- (b) no precedence

    def test_prediction_and_verdict_in_the_same_commit_fails(self) -> None:
        """This is our own row 16. The gate we now publish would have failed it."""
        self.repo.preregister("P-TEST-1")
        self.repo.result("P-TEST-1")
        self.repo.commit("everything at once — the failure this rule exists to catch")

        evidence = self.gather()
        self.assertFalse(evidence.passed)
        self.assertIn("same commit", self.reasons(evidence))

    def test_a_preregistration_written_after_the_result_fails(self) -> None:
        self.repo.result("P-TEST-1")
        self.repo.commit("result first")
        self.repo.preregister("P-TEST-1")
        self.repo.commit("...and the 'prediction' afterwards")

        evidence = self.gather()
        self.assertFalse(evidence.passed)
        self.assertIn("(b)", self.reasons(evidence))

    def test_an_uncommitted_preregistration_cannot_precede_anything(self) -> None:
        self.repo.preregister("P-TEST-1")
        self.repo.result("P-TEST-1")

        evidence = self.gather()
        self.assertFalse(evidence.passed)
        self.assertIn("(b)", self.reasons(evidence))

    def test_a_preregistration_moved_into_place_is_not_a_preregistration(self) -> None:
        """The laundering recipe, in three commands: draft it somewhere, tune it once you
        have seen the result, `git mv` it into place, and the tuned text acquires a fresh
        registration commit. Rename detection is what closes it."""
        (self.repo.path / "drafts").mkdir()
        self.repo.write("drafts/P-TEST-1.md", VALID.format(id="P-TEST-1"))
        self.repo.commit("a harmless draft, somewhere out of the way")
        self.repo.git("mv", "drafts/P-TEST-1.md", f"{firewall.PREREG_DIR}/P-TEST-1.md")
        self.repo.commit("tidy up the repository layout")
        self.repo.result("P-TEST-1")
        self.repo.commit("result: P-TEST-1")

        evidence = self.gather()
        self.assertFalse(evidence.passed, "a pre-registration must be born at its final path")
        self.assertIn("moved here", self.reasons(evidence))

    def test_the_verdict_does_not_depend_on_the_users_git_config(self) -> None:
        """`git log --diff-filter=A` changes meaning with diff.renames: fail-closed when
        it is on, fail-OPEN when it is off. If this test ever fails, the tool's answer
        depends on the .gitconfig of whoever runs it, and it is worthless."""
        (self.repo.path / "drafts").mkdir()
        self.repo.write("drafts/P-TEST-1.md", VALID.format(id="P-TEST-1"))
        self.repo.commit("draft")
        self.repo.git("mv", "drafts/P-TEST-1.md", f"{firewall.PREREG_DIR}/P-TEST-1.md")
        self.repo.commit("move")

        verdicts = {}
        for setting in ("true", "false"):
            self.repo.git("config", "diff.renames", setting)
            verdicts[setting] = self.gather().passed

        self.assertEqual(verdicts["true"], verdicts["false"], f"config-dependent: {verdicts}")
        self.assertFalse(verdicts["true"], "and the shared answer must be the closed one")

    # ------------------------------------------------------- (c) it was edited

    def test_editing_the_preregistration_after_registering_it_fails(self) -> None:
        self.repo.preregister("P-TEST-1")
        self.repo.commit("firewall: pre-register P-TEST-1")

        softened = VALID.format(id="P-TEST-1").replace(
            "the count of external installations is 0",
            "the count of external installations is 0 (unless we were busy)",
        )
        self.repo.preregister("P-TEST-1", softened)
        self.repo.commit("a small clarification, entirely in good faith")

        evidence = self.gather()
        self.assertFalse(evidence.passed)
        self.assertIn("(c)", self.reasons(evidence))

    def test_an_uncommitted_edit_is_still_an_edit(self) -> None:
        """Found by running the tool on this repository, not by writing a test: an edit
        that is only in the working tree used to report PASS. It is still an edit."""
        self.repo.preregister("P-TEST-1")
        self.repo.commit("firewall: pre-register P-TEST-1")
        self.repo.preregister("P-TEST-1", VALID.format(id="P-TEST-1") + "\nnot committed\n")

        evidence = self.gather()
        self.assertFalse(evidence.passed)
        self.assertIn("working tree", self.reasons(evidence))

    def test_the_edit_fails_even_before_any_result_exists(self) -> None:
        """The cost is paid at edit time. You do not get to soften it quietly and
        then decide whether to publish."""
        self.repo.preregister("P-TEST-1")
        self.repo.commit("firewall: pre-register P-TEST-1")
        self.repo.preregister("P-TEST-1", VALID.format(id="P-TEST-1") + "\nan afterthought\n")
        self.repo.commit("tidy up")

        evidence = self.gather()
        self.assertFalse(evidence.passed)
        self.assertIn("(c)", self.reasons(evidence))

    # ------------------------------------------------------ (d) vacuous criterion

    def test_a_kill_criterion_with_no_threshold_fails(self) -> None:
        vague = VALID.format(id="P-TEST-1").replace(
            "KILL if on the verification date the count of external installations is 0.",
            "KILL if adoption turns out to be disappointing.",
        )
        self.repo.preregister("P-TEST-1", vague)
        self.repo.commit("firewall: pre-register P-TEST-1")

        evidence = self.gather()
        self.assertFalse(evidence.passed)
        self.assertIn("threshold", self.reasons(evidence))

    def test_a_placeholder_kill_criterion_fails(self) -> None:
        placeholder = VALID.format(id="P-TEST-1").replace(
            "KILL if on the verification date the count of external installations is 0.",
            "KILL criterion: TBD, we will see how it goes after 3 months.",
        )
        self.repo.preregister("P-TEST-1", placeholder)
        self.repo.commit("firewall: pre-register P-TEST-1")

        evidence = self.gather()
        self.assertFalse(evidence.passed)
        self.assertIn("vacuous", self.reasons(evidence))

    def test_a_verification_date_in_the_past_fails(self) -> None:
        backdated = VALID.format(id="P-TEST-1").replace(
            "verification_date: 2099-01-01", "verification_date: 2020-01-01"
        )
        self.repo.preregister("P-TEST-1", backdated)
        self.repo.commit("firewall: pre-register P-TEST-1")

        evidence = self.gather()
        self.assertFalse(evidence.passed)
        self.assertIn("not after the registration date", self.reasons(evidence))

    def test_a_measurement_nobody_else_could_run_fails(self) -> None:
        unmeasurable = VALID.format(id="P-TEST-1").replace(
            """    how: >
      GitHub code search for the action reference, counting hits whose owner is
      not us. Anyone can run this query.""",
            "    how: TBD",
        )
        self.repo.preregister("P-TEST-1", unmeasurable)
        self.repo.commit("firewall: pre-register P-TEST-1")

        evidence = self.gather()
        self.assertFalse(evidence.passed)
        self.assertIn("placeholder, not a procedure", self.reasons(evidence))

    def test_the_template_itself_is_never_verified_as_a_claim(self) -> None:
        self.repo.write(f"{firewall.PREREG_DIR}/{firewall.TEMPLATE_NAME}", VALID.format(id="X"))
        self.repo.commit("add the template")

        self.assertEqual(firewall.claim_ids(self.repo.path), [])


if __name__ == "__main__":
    unittest.main()
