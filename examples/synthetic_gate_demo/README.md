# Synthetic companion-gate demo

A 30-second, self-contained proof of the core mechanism (mechanism #2 in
[`../../METHOD.md`](../../METHOD.md)): an **independent recompute** that confirms an
honest result and catches both a fabrication and an honest bug.

## Run

```bash
python gate_demo.py
```

Only dependency: `numpy`. Deterministic given the fixed seed: the executor and the
gate agree byte-for-byte **within a run, on any machine**. (The exact decimals you
print may differ from ours at the last digit across BLAS/CPU — which is exactly why
the gate compares the executor against a fresh recompute *within the same run*, never
against hardcoded numbers. That is the point, not a caveat.)

## What it shows

- **Scenario 1 — real class structure, honest executor.** The executor reports a
  measure (LIFT = within-class minus between-class correlation) and its permutation
  noise-floor. The gate recomputes both from the raw data with independent code →
  match → **TRUSTED**.
- **Scenario 2 — pure noise, fabricating executor.** On data with no structure
  (true LIFT ≈ 0), the executor reports an inflated LIFT and claims a "discovery".
  The gate recomputes from raw → the reported LIFT does not match → **caught**.
- **Scenario 3 — real structure, honest executor with a bug.** The executor
  correlates on the wrong axis (a classic real mistake) and fully believes its wrong
  number. The gate catches it the same way → **caught**. The gate judges
  *reproducibility, not intent*: fabrication and honest bug fall to the same check.

Expected output ends with:

```
honest + real structure   -> TRUSTED & PASS
fabricated discovery      -> CAUGHT
honest bug (no malice)    -> CAUGHT
```

## Why it's built this way

The gate **trusts nothing the executor said**. It re-derives the decisive numbers
from the raw data itself. That is why it catches a claim that isn't there even when
the reported numbers are plausible — exactly the real episode recorded in
[`../../incident-log.md`](../../incident-log.md), reproduced here on data anyone can
regenerate.

---

*IT:* Demo self-contained (solo `numpy`) del meccanismo #2: un ricalcolo indipendente
che **conferma** un risultato onesto (scenario 1), **becca** una scoperta fabbricata
su rumore puro (scenario 2), e **becca** anche un bug in buona fede (scenario 3, asse
sbagliato). Il gate giudica la *riproducibilità, non l'intenzione*: fabbricazione e
bug onesto cadono sullo stesso controllo. Deterministica a seed fisso: esecutore e
gate coincidono byte-per-byte *dentro la stessa run*, su qualunque macchina (le cifre
esatte possono variare all'ultimo decimale tra BLAS/CPU — ed è proprio per questo che
il gate confronta con un ricalcolo fresco nella stessa run, non con numeri hardcoded).
Riproduce per chiunque l'episodio reale in `incident-log.md`.
