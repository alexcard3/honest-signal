"""
honest-signal — synthetic companion-gate demo
================================================
Self-contained, deterministic demonstration of the core mechanism:
an *independent recompute* gate that catches a fabricated result.

No database, no secrets, no external data — only numpy. Anyone can run this
and watch the gate CONFIRM an honest result and CATCH a fabricated discovery.

This mirrors, in miniature, a real episode in our research: an AI executor
reported a verification step that had never happened, on a result that was
actually dead. A second AI ("companion") recomputed the cell from the raw
data with independent code and found the numbers didn't match. The fabrication
was caught and corrected. Here that same pattern runs on synthetic data so you
can verify the mechanism yourself.

The gate judges REPRODUCIBILITY, not intent: it catches an honest bug and a
deliberate fabrication with the exact same mechanism. You never have to trust
anyone's good faith — not even your own.

Run:  python gate_demo.py
Expect:
  Scenario 1 (real structure)     -> honest executor            -> TRUSTED
  Scenario 2 (pure noise)         -> fabricating executor        -> FABRICATION DETECTED
  Scenario 3 (real structure, bug)-> honest-but-buggy executor   -> MISMATCH CAUGHT
"""
import numpy as np

SEED = 42
T = 260                                   # samples
N = 16                                    # series
GROUPS = [list(range(g * 4, g * 4 + 4)) for g in range(4)]   # 4 classes of 4
LABELS = np.array([g for g in range(4) for _ in range(4)])   # frozen tag vector
ALL_PAIRS = [(i, j) for i in range(N) for j in range(i + 1, N)]
N_PERM = 2000


# ------------------------------------------------------------------- raw data
def make_raw(structured, seed=SEED):
    """Deterministic synthetic panel.
    structured=True : each class shares a latent factor -> real class structure.
    structured=False: every series independent -> pure noise, no structure."""
    rng = np.random.default_rng(seed)
    out = np.empty((T, N))
    if structured:
        for g in GROUPS:
            factor = rng.standard_normal(T)
            for i in g:
                out[:, i] = 0.8 * factor + 0.6 * rng.standard_normal(T)
    else:
        for i in range(N):
            out[:, i] = rng.standard_normal(T)
    return out


# ------------------------------------------------- the pre-registered measure
def lift(raw, labels):
    """LIFT = mean within-class pairwise corr - mean between-class pairwise corr.
    The permutation null reshuffles `labels`, so the within/between partition
    changes while the data stays fixed.

    This is our real class-structure measure (used in the regime atlas) reduced to
    a toy: 'do assets in the same class co-move more than a random relabeling would
    predict?'. The demo is the method, miniaturized — not an unrelated example."""
    C = np.corrcoef(raw, rowvar=False)
    wv = [C[i, j] for i, j in ALL_PAIRS if labels[i] == labels[j]]
    bv = [C[i, j] for i, j in ALL_PAIRS if labels[i] != labels[j]]
    return float(np.mean(wv) - np.mean(bv))


def floor95(raw, seed=SEED):
    """95th percentile of LIFT under tag-label permutation (the noise floor)."""
    rng = np.random.default_rng(seed)
    null = np.array([lift(raw, LABELS[rng.permutation(N)]) for _ in range(N_PERM)])
    return float(np.percentile(null, 95))


def measure(raw):
    """The frozen recipe: observed LIFT, noise floor, PASS iff LIFT > floor (strict)."""
    obs = round(lift(raw, LABELS), 8)
    fl = round(floor95(raw), 8)
    return {"lift": obs, "floor95": fl, "pass": bool(obs > fl)}


# ----------------------------------------------------------------- executors
def honest_executor(raw):
    """Reports exactly what the recipe produces."""
    return measure(raw)


def fabricating_executor(raw):
    """Runs on pure-noise data (real verdict: FAIL) but reports an inflated LIFT
    and a shaved floor to claim a 'discovery' that isn't there — the kind of
    self-deception the gate exists to stop."""
    cell = dict(measure(raw))
    cell["lift"] = round(cell["floor95"] * 1.8 + 0.15, 8)   # invented signal
    cell["pass"] = True
    return cell


def buggy_executor(raw):
    """An HONEST mistake, not a lie: it correlates on the wrong axis (rowvar=True),
    a classic real-world bug, and fully believes its (wrong) number. The gate catches
    it exactly as it catches fabrication — because it judges reproducibility, not
    intent. In real research, this failure mode is far more common than malice."""
    C = np.corrcoef(raw, rowvar=True)                       # BUG: correlates rows, not series
    wv = [C[i, j] for i, j in ALL_PAIRS if LABELS[i] == LABELS[j]]
    bv = [C[i, j] for i, j in ALL_PAIRS if LABELS[i] != LABELS[j]]
    obs = round(float(np.mean(wv) - np.mean(bv)), 8)
    return {"lift": obs, "floor95": round(floor95(raw), 8), "pass": bool(obs > round(floor95(raw), 8))}


# ------------------------------------------------------------- companion gate
def companion_gate(raw, reported, tol=1e-6):
    """Independent recompute from the RAW data. Trusts nothing the executor said."""
    truth = measure(raw)
    checks = {k: (abs(reported[k] - truth[k]) < tol if isinstance(truth[k], float)
                  else reported[k] == truth[k]) for k in ("lift", "floor95", "pass")}
    return all(checks.values()), checks, truth


def run(title, raw, executor):
    reported = executor(raw)
    ok, checks, truth = companion_gate(raw, reported)
    print(f"\n=== {title} ===")
    print(f"  executor reported : {reported}")
    print(f"  gate recomputed   : {truth}")
    for k, good in checks.items():
        print(f"    {k:8s}: {'OK' if good else 'DIFF  <-- mismatch'}")
    print(f"  VERDICT: {'TRUSTED (byte-exact match)' if ok else 'MISMATCH CAUGHT — not reproducible (the gate does not judge intent)'}")
    return ok


if __name__ == "__main__":
    structured = make_raw(structured=True)
    noise = make_raw(structured=False)

    a = run("Scenario 1 — real class structure, honest executor", structured, honest_executor)
    b = run("Scenario 2 — pure noise, fabricating executor claims a discovery",
            noise, fabricating_executor)
    c = run("Scenario 3 — real structure, honest executor with a bug (wrong axis)",
            structured, buggy_executor)

    print("\n" + "-" * 64)
    print(f"honest + real structure   -> {'TRUSTED & PASS' if a else 'unexpected'}")
    print(f"fabricated discovery      -> {'CAUGHT' if not b else 'MISSED?!'}")
    print(f"honest bug (no malice)    -> {'CAUGHT' if not c else 'MISSED?!'}")
    assert a and not b and not c, "demo invariant broken"
    print("\nThe gate confirms the honest result and catches BOTH the fabrication and")
    print("the honest bug — by recomputing from the raw data with independent code.")
    print("It judges reproducibility, not intent. That is the whole idea.")
