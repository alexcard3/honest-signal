# Contributing to honest-signal

Thank you for wanting to make this better — external judgment is the whole point.

This project has one non-negotiable standard: **claims must be verifiable, and
verification is never self-certified.** Contributions are held to the same bar the
method holds itself to.

## Ground rules
- **Reproducibility first.** Any change to the demo or a claim must keep the demo
  passing. CI runs `python examples/synthetic_gate_demo/gate_demo.py` on every PR;
  a red check blocks the merge.
- **No hardcoded results.** The gate compares a fresh recompute *within a run*, never
  against pinned numbers. Don't add assertions against machine-specific decimals.
- **Honesty over polish.** If you found a real error in our method or claims, that is
  a first-class contribution — open an issue or PR and we will credit it. A NO is a
  result here too.
- **Say what you verified.** In a PR, state what you ran and observed. "It should work"
  is not verification.

## How to contribute
1. Open an **issue** first for anything non-trivial (question, bug, proposed change).
2. Fork, branch, make the change, ensure the demo still passes locally
   (`python examples/synthetic_gate_demo/gate_demo.py`).
3. Open a PR describing the claim and how you checked it. CI must be green.
4. A maintainer verifies independently before merging — we do not merge on a
   contributor's word (that is the method).

## Scope
This repo is the *method* (the five mechanisms + a synthetic demo + the index of what it killed), not a market discovery.
Contributions that sharpen the method, its clarity, or its reproducibility are most
welcome. Market "edge" proposals are out of scope — that search is closed, with evidence.

---

*IT:* Standard non negoziabile: **le claim devono essere verificabili, e la verifica non
è mai auto-certificata.** La demo deve restare verde (CI la rilancia su ogni PR). Niente
numeri hardcoded. Se trovi un nostro errore reale → contributo di prima classe, lo
accreditiamo. In PR, dichiara cosa hai eseguito e osservato. Un maintainer verifica in
modo indipendente prima del merge — non si mergia sulla parola.
