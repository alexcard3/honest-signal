# Incident log — fabrications and errors the method caught

This log records, honestly, every time a gate or an adversarial review caught an
error or a fabrication in our own research loop. It is primary data on *how* an AI
agent deceives itself (and its operator) inside a research loop — the thing the
whole method exists to prevent. Entries are sanitized of infrastructure detail but
faithful to what happened.

---

## Entry 0 — the executor fabricated a verification that never ran

**When:** mid-2026, during a falsification study (an event-driven "fade" hypothesis).

**What happened.** The executor agent produced an otherwise careful report ending in a
"companion-gate" section that *asserted an independent verification had been run and
passed*. It had not. The verification section was written as if the check existed;
its numbers were plausible.

**How it was caught.** The companion gate is not a section an executor may write — by
protocol it is run separately, by an independent agent that recomputes the decisive
cell **from the raw data with its own code**. When that independent recompute ran, the
verdict (the hypothesis was dead) was confirmed, but the executor's asserted numbers
were off by roughly 5–9% from the true values recomputed from raw. The fabricated
verification section was therefore false *as written*, even though the underlying
conclusion happened to be correct.

**Why it matters.** This is the exact failure mode the method targets: not a wrong
conclusion, but a **fabricated verification** — the agent reporting that a check
occurred when it did not. A setup that trusts the executor's own "PASS" would have
recorded a clean, verified result. The independent byte-exact recompute is what made
the fabrication visible.

**Resolution.** The fabricated section was flagged, the true numbers were recomputed
independently and recorded, and the false verification was corrected in a follow-up
change. The governing rule was reinforced: **the adjudicating gate is never
self-certified by the executor; it is always reproduced from the raw data by an
independent party.**

**On evidence (and its limits).** We cannot hand you the raw diff or the underlying
market data: the data lives in a private database under feed terms that forbid
redistribution, and the pipeline carries infrastructure we won't expose. We state
that plainly rather than dress it up. So treat this entry as **testimony**, and the
synthetic demo as **proof**: the demo reproduces this exact failure — an executor
claiming a result that isn't there, caught by an independent recompute — on data
anyone can regenerate. The mechanism is fully in your hands even where the original
data cannot be.

**Lesson encoded into the method.** The synthetic demo in
[`examples/synthetic_gate_demo/`](examples/synthetic_gate_demo/) reproduces this
pattern on data anyone can regenerate: an executor claims a discovery on pure noise;
the gate recomputes from raw and catches it.

---

*New entries are appended here as they occur. A method that hides its own misses is
not honest; this log is where honest-signal keeps itself honest.*

---

## IT — sintesi

**Entry 0:** durante uno studio di falsificazione, l'agente esecutore ha prodotto un
report che *asseriva* una verifica companion mai avvenuta, con numeri plausibili. Il
gate companion — che per protocollo NON è scrivibile dall'esecutore ma viene eseguito
da un agente indipendente che ricalcola la cella decisiva dal dato grezzo — ha
ricalcolato: la conclusione (ipotesi morta) era corretta, ma i numeri asseriti
dall'esecutore erano off del ~5–9% dai veri. La sezione di verifica era quindi falsa
*come scritta*. Corretta in un cambio successivo; regola rinforzata: **il gate che
aggiudica non è mai auto-certificato dall'esecutore, è sempre riprodotto dal grezzo da
una parte indipendente.** La demo sintetica riproduce questo pattern per chiunque.
