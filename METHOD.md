# METHOD — how honest-signal keeps AI-assisted research honest

## EN

The problem: an AI agent (or an enthusiastic human) running a research loop can
fool itself. It can pick the test after seeing the data, harden a rule until a
result "passes", or simply **report a verification that never ran**. Backtest
overfitting is the finance-specific name; self-deception is the general one. In
2026 this became a first-order concern for autonomous agents (fabricated success,
"scheming", plausible-but-wrong numeric checks). honest-signal is our working,
battle-tested answer, distilled to four mechanisms.

### 1. Pre-registration firewall
Before any number is computed, the exact recipe and the falsification criterion
are written down and committed: universe, windows, estimator, thresholds, the
noise-floor definition, the seeds, and — crucially — what result would count as a
**NO**. Nothing downstream may be chosen after seeing the data. A result that
required a post-hoc choice is an invalid result, re-frozen and re-run. This kills
the garden of forking paths at the root.

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
hypotheses instead of quietly dropping them. Killing 16 of our own favorites,
with byte-exact reproduction, is not a consolation prize — it is the evidence that
the method works (it kills real edges), and the moat is precisely that honesty.

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

---

## IT

Il problema: un agente AI (o un umano entusiasta) in un loop di ricerca può
auto-ingannarsi — scegliere il test dopo aver visto i dati, indurire una regola
finché un risultato "passa", o **riportare una verifica mai avvenuta**. L'overfitting
del backtest è il nome finanziario; l'auto-inganno è quello generale. Nel 2026 è
diventato un problema di prim'ordine per gli agenti autonomi. honest-signal è la
nostra risposta funzionante, distillata in quattro meccanismi.

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
   16 propri beniamini con riproduzione byte-esatta non è un premio di consolazione: è
   la prova che il metodo funziona, e il fossato è quell'onestà.

**Determinismo:** seed/threading/percentile/RNG pinnati — la riproduzione byte-esatta
ha senso solo se la pipeline è byte-stabile.

**Rispetto alla letteratura:** siamo contributori dentro una lineage (López de Prado
su PBO/DSR; Hou-Xue-Zhang, Chen-Zimmermann sulle anomalie che non sopravvivono;
registered reports / Institute for Replication; e l'ondata 2026 di harness
anti-fabbricazione per agenti). Il nostro delta specifico è il meccanismo #2 applicato
*a priori* insieme al #1: un ricalcolo indipendente byte-esatto, pre-registrato, che
ha beccato una fabbricazione reale.

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
