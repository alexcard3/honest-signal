# METHOD — how honest-signal keeps AI-assisted research honest

## EN

The problem: an AI agent (or an enthusiastic human) running a research loop can
fool itself. It can pick the test after seeing the data, harden a rule until a
result "passes", or simply **report a verification that never ran**. Backtest
overfitting is the finance-specific name; self-deception is the general one. In
2026 this became a first-order concern for autonomous agents (fabricated success,
"scheming", plausible-but-wrong numeric checks). honest-signal is our working,
battle-tested answer, distilled to five mechanisms. The fifth we learned the hard
way — from this method catching *us*.

### 1. Pre-registration firewall
Before any number is computed, the exact recipe and the falsification criterion
are written down and committed: universe, windows, estimator, thresholds, the
noise-floor definition, the seeds, and — crucially — what result would count as a
**NO**. Nothing downstream may be chosen after seeing the data. A result that
required a post-hoc choice is an invalid result, re-frozen and re-run. This kills
the garden of forking paths at the root.

Since v0.3 this mechanism is no longer a discipline: it is [`firewall.py`](firewall.py),
a CI check that fails the build when a result is not backed by a pre-registration that
provably came first and has not been edited since. It is installed on this repository,
and it has already refused a pull request of ours. Of the mechanisms here it is the one
that could be made mechanical — and, awkwardly, it is not the one we call the moat.
Mechanism #2 is, and #2 is a fact about process that no tool can read from a git log.

### 2. Companion gate — independent byte-exact recompute
The agent that runs the experiment (the "executor") never adjudicates it. A
**second, independent agent** ("companion") re-implements the frozen recipe from
scratch and recomputes the decisive cell **directly from the raw data**, then
compares byte-for-byte against what the executor reported. Not a hash check of an
artifact — an independent recomputation of the result. If the numbers diverge, the
executor's verdict is void, regardless of how confident its prose was. This is the
mechanism that caught a real fabrication in our pipeline (see `incident-log.md`),
and it is the part most people's setups lack.

### 3. Adversarial red-team of the plan
Before an experiment is blessed, its design is attacked by independent reviewers
whose default is to reject it: does it reopen an already-falsified question in
disguise? Is the prediction actually falsifiable with numbers, or vague? Is the
result byte-reproducible by two independent implementations, or is a convention
left unpinned (RNG, percentile method, tie-breaks) so that two honest coders
diverge? Every unpinned degree of freedom is a place a result can be un-reproducible
"without anyone lying" — the red-team's job is to find them before the run.

### 4. Neutral falsification counter + honesty-from-defeat
Measurement probes (cartography) never touch the "edge" counter; only genuine
edge claims do. And a **NO is a first-class deliverable**: we certify dead
hypotheses instead of quietly dropping them. Killing 16 of our own favorites is not
a consolation prize — it is the evidence that the method bites.

But the mechanisms above were not all in force from day one, and we will not backdate
them. The independent byte-exact companion gate became protocol partway through
(2026-06-25); the earlier kills were checked with determinism — pinned seeds and BLAS,
byte-identical re-runs, published output hashes — which is good practice, but is not a
second pair of eyes. [`FALSIFICATIONS.md`](FALSIFICATIONS.md) states, for every one of
the eighteen, what actually verified it, what was committed before the data, and what
killed it. The count of 16 stands; the claim that all 16 were verified with equal
severity did not, and we graded it down rather than restate it — see
[`incident-log.md`](incident-log.md), Entry 1.

### 5. Substantiation as a discipline (and why it is not a gate)
> **This section used to be called "Substantiation as a gate". It was misnamed, and we renamed it
> rather than let the name stand.** By our own rule — *a gate that nothing depends on is not a gate,
> it is a log line* ([`incident-log.md`](incident-log.md), Entry 3) — this is not a gate: **nothing in
> this repository fails when a claim is unsubstantiated.** No tool tells you *"you claimed sixteen —
> now tabulate them."* It is a discipline we keep because it burned us once, not a mechanism we
> enforce, and it is deliberately absent from [`GLOSSARY.md`](GLOSSARY.md) for exactly that reason —
> see *What is deliberately not in this glossary*. If we ever build the thing that turns a build red on
> an unsubstantiated claim, this heading gets its word back.

**A claim you cannot tabulate row by row, with the evidence beside each row, is a claim
you have not verified.** We learned this on ourselves. "16 falsifications, byte-exact"
went unchallenged for as long as it stayed a *number* — including by us. The moment we
tried to build the index — one row per hypothesis, one cell per hash — fourteen of the
eighteen rows had nothing to put in the cell. Nobody had lied. The artifact simply did
not compile.

So: before a claim ships, force it into a shape where every element must carry its own
evidence. **The table is the test.** An empty cell is not a formatting problem — it is
the claim telling you it was never checked. Publish the empty cell; that is the whole
mechanism. It is the cheapest of the five and it caught the biggest thing.

### What killed the eighteen — the G0–G3 scale
Every falsification in [`FALSIFICATIONS.md`](FALSIFICATIONS.md) is tagged with the first
gate it failed: **G0** (was there a real gross edge at all?), **G1** (bad prints), **G2**
(the cost wall), **G3** (the tax wall). The finding — which contradicted our own comfortable
framing, so we pre-registered the opposite and tabulated it — is that **G0 accounts for ~13–14
of the 18**. The dominant killer is not the walls; it is the absence of an edge to defend.
The scale, and why it transfers to anyone else's strategy, is set out at the end of that file.

### Determinism
Everything is deterministic: pinned seeds, pinned BLAS/threading, pinned percentile
method and RNG calls. Byte-exact reproduction is only meaningful if the pipeline is
byte-stable. This is a feature of the method (independent verifiability), documented
as such.

### Where this sits relative to prior work
We are contributors inside a lineage, not lone founders. On the finance side:
López de Prado & Bailey on backtest overfitting / PBO / the Deflated Sharpe Ratio;
Hou-Xue-Zhang and Chen-Zimmermann on how few anomalies survive out-of-sample; the
registered-reports and replication movement (Institute for Replication). On the AI
side: the 2026 wave of anti-fabrication harnesses and verification gates for
autonomous agents, and pre-registration proposals for AI experiments. Our specific
delta is mechanism **#2** applied *a priori* together with **#1**: an independent
byte-exact recompute, pre-registered, that has caught a real fabrication.
([`FALSIFICATIONS.md`](FALSIFICATIONS.md) records how many hypotheses went through
both, and when.)

---

## IT

Il problema: un agente AI (o un umano entusiasta) in un loop di ricerca può
auto-ingannarsi — scegliere il test dopo aver visto i dati, indurire una regola
finché un risultato "passa", o **riportare una verifica mai avvenuta**. L'overfitting
del backtest è il nome finanziario; l'auto-inganno è quello generale. Nel 2026 è
diventato un problema di prim'ordine per gli agenti autonomi. honest-signal è la
nostra risposta funzionante, distillata in cinque meccanismi. Il quinto l'abbiamo
imparato nel modo duro: da questo metodo che ha beccato *noi*.

1. **Firewall di pre-registrazione** — ricetta esatta + criterio di falsificazione
   committati PRIMA di calcolare qualunque numero (universo, finestre, stimatore,
   soglie, noise-floor, seed, e cosa conterebbe come NO). Nulla si sceglie dopo aver
   visto i dati. Uccide il "garden of forking paths" alla radice.
2. **Gate companion — ricalcolo indipendente byte-esatto** — l'esecutore non
   aggiudica mai; un secondo agente indipendente ri-implementa la ricetta e ricalcola
   la cella decisiva **dal dato grezzo**, poi confronta byte-per-byte col report
   dell'esecutore. Non un check di hash: un ricalcolo indipendente. Se i numeri
   divergono, il verdetto dell'esecutore è nullo. È il meccanismo che ha beccato una
   fabbricazione reale (`incident-log.md`) — e il pezzo che manca a quasi tutti.
3. **Red-team avversariale del piano** — il design è attaccato da revisori il cui
   default è bocciare: riapre una domanda già falsificata? la predizione è davvero
   falsificabile? ogni convenzione (RNG, percentile, tie-break) è inchiodata così che
   due implementazioni indipendenti convergano? Ogni grado di libertà non pinnato è un
   punto dove un risultato diventa non-riproducibile "senza che nessuno menta".
4. **Contatore falsificazioni neutro + onestà-dalla-sconfitta** — le sonde di misura
   non toccano il contatore "edge"; un NO è un deliverable di prima classe. Uccidere
   16 propri beniamini non è un premio di consolazione: è la prova che il metodo morde.
   **Ma i meccanismi sopra non erano tutti in vigore dal primo giorno, e non li
   retrodatiamo:** il gate companion byte-esatto diventa protocollo a metà strada
   (2026-06-25); le morti precedenti furono verificate col determinismo (seed/BLAS
   pinnati, re-run byte-identici, hash pubblicati) — buona pratica, non un secondo paio
   d'occhi. `FALSIFICATIONS.md` dichiara, per tutte e diciotto, cosa le ha davvero
   verificate. Il conteggio di 16 regge; il claim che tutte e 16 fossero verificate con
   pari severità no — l'abbiamo graduato invece di ribadirlo (`incident-log.md`, Entry 1).
5. **La sostanziazione come disciplina (e perché *non* è un gate)** — **un claim che non sai tabulare riga per riga, con
   l'evidenza accanto a ogni riga, è un claim che non hai verificato.** L'abbiamo imparato
   su di noi: "16 falsificazioni, byte-esatte" è rimasto incontestato finché è rimasto un
   *numero* — anche da parte nostra. Nel momento in cui abbiamo provato a costruire
   l'indice (una riga per ipotesi, una cella per hash), **quattordici righe su diciotto
   non avevano nulla da mettere nella cella.** Nessuno aveva mentito: semplicemente
   l'artefatto non compilava. Quindi: prima che un claim esca, costringilo in una forma
   in cui ogni elemento deve portare la propria evidenza. **La tabella è il test.** Una
   cella vuota non è un problema di formattazione: è il claim che ti dice che non è mai
   stato verificato. Pubblica la cella vuota.
   > **Questa sezione si chiamava "La sostanziazione come gate". Era un nome sbagliato, e
   > l'abbiamo cambiato invece di lasciarlo in piedi.** Per la nostra stessa regola — *un gate da cui
   > non dipende nulla non è un gate, è una riga di log* (`incident-log.md`, Entry 3) — questo **non è
   > un gate: niente, in questo repository, fallisce quando un claim non è sostanziato.** È una
   > disciplina che teniamo perché ci siamo bruciati una volta, non un meccanismo che imponiamo — ed è
   > per questo che è **deliberatamente assente** da [`GLOSSARY.md`](GLOSSARY.md).

**Determinismo:** seed/threading/percentile/RNG pinnati — la riproduzione byte-esatta
ha senso solo se la pipeline è byte-stabile.

**Rispetto alla letteratura:** siamo contributori dentro una lineage (López de Prado
su PBO/DSR; Hou-Xue-Zhang, Chen-Zimmermann sulle anomalie che non sopravvivono;
registered reports / Institute for Replication; e l'ondata 2026 di harness
anti-fabbricazione per agenti). Il nostro delta specifico è il meccanismo #2 applicato
*a priori* insieme al #1: un ricalcolo indipendente byte-esatto, pre-registrato, che
ha beccato una fabbricazione reale. (`FALSIFICATIONS.md` registra quante ipotesi sono
passate da entrambi, e da quando.)

---

## References

The method sits inside an existing lineage. Key works we build on or position against
(each verified at source):

- Bailey, Borwein, López de Prado & Zhu — *Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance*. Notices of the AMS 61(5), 2014. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2308659
- Bailey & López de Prado — *The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting, and Non-Normality*. Journal of Portfolio Management 40(5), 2014. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551
- Chen & Zimmermann — *Publication Bias in Asset Pricing Research*. arXiv:2209.13623. https://arxiv.org/abs/2209.13623
- Hou, Xue & Zhang — *Replicating Anomalies*. Review of Financial Studies 33(5), 2020.
- Deng — *Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents*. arXiv:2606.11688. https://arxiv.org/abs/2606.11688
- QuantPedia — *Guardrails Make the Researcher: What an AI Agent Got Right (And Wrong) Replicating Nine Equity Anomalies*. 30 Jun 2026. https://quantpedia.com/guardrails-make-the-researcher-what-an-ai-agent-got-right-and-wrong-replicating-nine-equity-anomalies/
