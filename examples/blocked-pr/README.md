# A pull request the gate refused

## EN

Everything else in this repository describes what the firewall does. This is the record of it
**doing it**, in public, on this repository:

> **[PR #6 — "DEMO: a result claimed with no pre-registration (GitHub must refuse to merge this)"](https://github.com/alexcard3/honest-signal/pull/6)**
> Opened 2026-07-14. `firewall` failed. **GitHub refused the merge.** Closed, never merged, and
> left in the record on purpose.

### First, a correction — because the first version of this page was false as written

This page originally pointed at [**PR #5**](https://github.com/alexcard3/honest-signal/pull/5) and
said the gate had **blocked** it. **It had not.** At that moment the `firewall` job was not a
required status check on `main`: the gate ran, failed, printed exit 1 — and then a **human closed
the pull request.**

It was not blocked. **It was merely red.** We had built the enforcement mechanism and never wired
it to the switch, and then we wrote up the result as though the switch had been on. Nobody lied;
the sentence was simply stronger than the configuration. That is
[`incident-log.md`](../../incident-log.md), **Entry 3**, and it is the fourth time this repository
has caught itself claiming something the record did not support.

We are not quietly editing that away. PR #5 stays open in the record, this paragraph stays above
the demonstration, and the demonstration was **run again**, properly, once the switch was on.

### What PR #6 contained

One file — `results/P-ALPHA-1.md` — announcing a tradeable edge:

> *Sharpe **1.9**, net of costs, out-of-sample. Holding period 1–4 weeks. The signal is strong
> and it survives the cost wall. We are confident in this result.*

**Nothing in it is a lie, and that is the point.** Every word could be sincerely believed by the
person who wrote it. What it does not have is a pre-registration: no recipe frozen before the data
existed, no criterion that could have killed it. From the record, there is no way to distinguish
this result from one chosen after seeing the numbers — and being sincere does not fix that. Neither
does being clever. Only the record does.

*(The real version of this hypothesis is row 18 of [`FALSIFICATIONS.md`](../../FALSIFICATIONS.md).
We pre-registered it, ran it, and it died: net-net ≈ 0% against buy & hold's +33%.)*

### What the gate said

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

### And what GitHub did about it — which is the part that was missing the first time

```
firewall  fail        demo  pass        tests  pass

mergeStateStatus: BLOCKED

$ gh pr merge 6 --merge
X Pull request #6 is not mergeable: the base branch policy prohibits the merge.
```

Two jobs passed, so this was not a broken build: it was the gate refusing. And the refusal has
teeth, because `firewall` is a **required status check** on `main`
(`required_status_checks.contexts = ["demo", "tests", "firewall"]`). The pull request does not
merge — not because a maintainer decided, and not because anyone judged the author's good faith.
Because the artifact does not compile, and the branch policy will not take it.

**That last line is the whole difference between PR #5 and PR #6**, and it is worth being precise
about, because it is exactly the kind of distinction a repository like this one gets to be held to.

### Why this file exists at all

**GitHub Actions logs expire.** In about ninety days the links above will show runs whose logs are
gone, and this demonstration would quietly decay into another claim you had to take on trust — the
exact failure mode this repository exists to name. So the output is copied here, into the
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

Tutto il resto di questo repository *descrive* cosa fa il firewall. Questo è il record del firewall
**che lo fa**: **[PR #6](https://github.com/alexcard3/honest-signal/pull/6)** — aperta il
2026-07-14, `firewall` fallito, **GitHub ha rifiutato il merge**, PR chiusa e mai mergiata,
lasciata apposta nel record.

**Prima, una correzione — perché la prima versione di questa pagina era falsa come scritta.**
Puntava alla **[PR #5](https://github.com/alexcard3/honest-signal/pull/5)** e diceva che il gate
l'aveva **bloccata**. **Non l'aveva bloccata.** In quel momento il job `firewall` non era un check
*obbligatorio* su `main`: il gate è girato, ha fallito, ha stampato exit 1 — e poi **un umano ha
chiuso la PR**. Non è stata bloccata: **era soltanto rossa.** Avevamo costruito l'imposizione e non
l'avevamo mai attaccata all'interruttore, e poi abbiamo raccontato il risultato come se
l'interruttore fosse acceso. Nessuno ha mentito: la frase era semplicemente più forte della
configurazione. È la **Entry 3** di `incident-log.md`, ed è la quarta volta che questo repository
becca sé stesso a rivendicare qualcosa che il record non sosteneva. Non la cancelliamo in silenzio:
la PR #5 resta nel record, questo paragrafo resta sopra la dimostrazione, e la dimostrazione è stata
**rifatta** una volta acceso l'interruttore.

**Cosa conteneva la PR #6.** Un file, `results/P-ALPHA-1.md`, che annunciava un edge tradabile
(Sharpe 1.9 netto costi, out-of-sample). **Non c'è una bugia dentro, ed è il punto:** ogni parola
potrebbe essere creduta in perfetta buona fede. Ciò che manca è la pre-registrazione — nessuna
ricetta congelata prima del dato, nessun criterio che avrebbe potuto ucciderlo. Dal record, non c'è
modo di distinguerlo da un risultato scelto *dopo* aver visto i numeri: la sincerità non lo aggiusta,
l'intelligenza nemmeno. Solo il record lo fa.

**Cosa ha detto il gate, e cosa ha fatto GitHub** — che è la parte che mancava la prima volta: due
job passati (quindi non era una build rotta), `firewall` fallito, `mergeStateStatus: BLOCKED`, e il
tentativo di merge respinto: *"the base branch policy prohibits the merge"*. Il rifiuto ha i denti
perché `firewall` è un **check obbligatorio** su `main`. La PR non mergia: non perché un maintainer
abbia deciso, non perché qualcuno abbia giudicato la buona fede dell'autore. Perché **l'artefatto
non compila**, e la branch policy non lo accetta.

**Perché questo file esiste.** I log di GitHub Actions **scadono**: fra novanta giorni i link
mostrerebbero run senza log, e questa dimostrazione decadrebbe in un altro claim da credere sulla
parola — precisamente il fallimento che questo repo esiste per nominare. Il log muore, l'artefatto no.

**Il limite onesto.** Qui il gate becca un risultato **senza alcuna** pre-registrazione: la regola
(a), la più facile delle quattro. Non dimostra che il gate sia imbattibile, perché non lo è: puoi
sempre scrivere una pre-registrazione già accordata e committarla fresca, al path giusto, prima del
risultato. Git non la distingue dall'onestà, e nemmeno questo tool (`incident-log.md`, Entry 2).
Rende il retrofitting visibile e costoso; non rende onesti.
