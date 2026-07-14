# A pull request the gate refused

## EN

Everything else in this repository describes what the firewall does. This is the record of it
**doing it**, in public, on this repository, with a log anyone can still open:

> **[PR #5 — "DEMO: a result claimed with no pre-registration (this PR must not merge)"](https://github.com/alexcard3/honest-signal/pull/5)**
> Opened 2026-07-14. Failed CI. **Closed, never merged.** It stays in the record on purpose.

We left it there because we had just spent an entire release
([`incident-log.md`](../../incident-log.md), Entry 1) correcting claims that rested on our word.
A gate demonstrated in prose is a gate you are being asked to take on trust. So here is the
corpse, in the window.

### What the pull request contained

One file — `results/P-ALPHA-1.md` — announcing a tradeable edge:

> *Sharpe **1.9**, net of costs, out-of-sample. Holding period 1–4 weeks. The signal is strong
> and it survives the cost wall. We are confident in this result.*

**Nothing in it is a lie, and that is the point.** Every word could be sincerely believed by the
person who wrote it. What it does not have is a pre-registration: no recipe frozen before the
data existed, no criterion that could have killed it. From the record, there is no way to
distinguish this result from one chosen after seeing the numbers — and being sincere does not
fix that. Neither does being clever. Only the record does.

*(The real version of this hypothesis is row 18 of [`FALSIFICATIONS.md`](../../FALSIFICATIONS.md).
We pre-registered it, ran it, and it died: net-net ≈ 0% against buy & hold's +33%.)*

### What CI said

Three jobs ran. Two passed — so this was not a broken build. The third is the gate:

```
[FAIL] P-ALPHA-1
       -> (a) results/P-ALPHA-1.md claims a result, but preregistrations/P-ALPHA-1.md
              does not exist - nothing was pre-registered

[PASS] P-TOOL-1
       pre-registered : d82e6f8eca
       note           : registered; no result yet

------------------------------------------------------------------------
1 passed, 1 failed.
The artifact does not compile. That is the gate working, not a bug.

##[error]Process completed with exit code 1.
```

| Job | Result |
|---|---|
| The companion gate catches a fabrication | pass |
| The gate bites (firewall test suite) | pass |
| **This repository submits to its own gate** | **fail** |

Exit code 1. The build fails. The pull request does not merge — not by anyone's decision, and
not because anyone judged the author. Because the artifact does not compile.

### Why this file exists at all

**GitHub Actions logs expire.** In about ninety days the link above will show a run whose log is
gone, and this demonstration would quietly decay into another claim you had to take on trust —
the exact failure mode this repository exists to name. So the output is copied here, into the
repository, where it is versioned and permanent. The log dies; the artifact does not.

### The honest limit

This shows the gate catching a result with **no** pre-registration — rule (a), the easiest of the
four. It does not show that the gate is unbeatable, because it is not. You can still write a
pre-registration you have already tuned and commit it, fresh and innocent-looking, at the right
path, before the result. Git cannot tell that apart from honesty, and neither can this tool.
See [`incident-log.md`](../../incident-log.md), Entry 2, where we publish that recipe rather than
leave you to find it.

It makes retrofitting visible and expensive. It does not make anyone honest.

---

## IT — sintesi

Tutto il resto di questo repository *descrive* cosa fa il firewall. Questo è il record del
firewall **che lo fa**, in pubblico, su questo repository:
**[PR #5](https://github.com/alexcard3/honest-signal/pull/5)** — aperta il 2026-07-14, CI rossa,
**chiusa e mai mergiata**, lasciata apposta nel record.

L'abbiamo lasciata lì perché avevamo appena passato un'intera release a correggere claim che
poggiavano sulla nostra parola (`incident-log.md`, Entry 1). Un gate dimostrato *in prosa* è un
gate che ti chiedono di credere. Quindi: il cadavere, in vetrina.

**Cosa conteneva.** Un file, `results/P-ALPHA-1.md`, che annunciava un edge tradabile (Sharpe 1.9
netto costi, out-of-sample). **Non c'è una bugia dentro, ed è esattamente il punto:** ogni parola
potrebbe essere creduta in perfetta buona fede da chi l'ha scritta. Ciò che manca è la
pre-registrazione — nessuna ricetta congelata prima del dato, nessun criterio che avrebbe potuto
ucciderlo. Dal record, non c'è modo di distinguere quel risultato da uno scelto *dopo* aver visto
i numeri: e la sincerità non lo aggiusta. Solo il record lo fa. *(La versione vera di questa
ipotesi è la riga 18 di `FALSIFICATIONS.md`: pre-registrata, eseguita, morta — net-net ≈ 0%
contro il +33% di buy & hold.)*

**Cosa ha detto la CI.** Tre job: due passati (quindi non era una build rotta), il terzo — il
gate — fallito con **exit code 1**, output qui sopra. La PR non mergia: non perché qualcuno abbia
deciso, non perché qualcuno abbia giudicato l'autore. Perché **l'artefatto non compila**.

**Perché questo file esiste.** I log di GitHub Actions **scadono**: fra novanta giorni il link
mostrerebbe una run senza log, e questa dimostrazione decadrebbe in un altro claim da credere
sulla parola — precisamente il fallimento che questo repo esiste per nominare. Il log muore,
l'artefatto no.

**Il limite onesto.** Qui il gate becca un risultato **senza alcuna** pre-registrazione: la regola
(a), la più facile delle quattro. Non dimostra che il gate sia imbattibile, perché non lo è: puoi
sempre scrivere una pre-registrazione già accordata e committarla fresca, al path giusto, prima
del risultato. Git non la distingue dall'onestà, e nemmeno questo tool. La ricetta la pubblichiamo
noi (`incident-log.md`, Entry 2) invece di lasciartela scoprire. Rende il retrofitting visibile e
costoso; non rende onesti.
