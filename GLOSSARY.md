# GLOSSARY — the concepts, named

## EN

An idea without a name cannot be cited, argued with, or refused. So the concepts this
repository works with are named here, in one place.

**Naming is not claiming invention.** Every entry below states, explicitly:

- **Prior art** — what existed before, with names. Pre-registration comes from clinical
  trials. Independent replication is a century old. Backtest overfitting was measured by
  López de Prado and Bailey. None of that is ours, and a glossary that quietly implied
  otherwise would deserve everything it got.
- **Our delta** — what is specifically ours. In almost every case it is **not the idea**: it
  is the **mechanism**, and its **enforcement**. Knowing that you should pre-register is old.
  Having your build fail when you did not is the part we shipped.

An entry that cannot state an honest delta does not belong in this file. One has already been
removed under that rule — see [*What is deliberately not in this glossary*](#what-is-deliberately-not-in-this-glossary).

The full lineage, with citations, is in [`METHOD.md` § References](METHOD.md#references).

---

### The firewall commit

A prediction is worth something only if it provably came **first**. A *firewall commit* is the
commit that carries the pre-registration — the hypothesis, the kill criterion with a number in
it, the procedure that would measure it, and the date — into the git history **before the data
exists**. From that moment the text is fixed: editing it is visible, and it fails the gate.

**Prior art.** Pre-registration in clinical trials (ICMJE; trial registration a condition of
publication since 2005). Registered Reports (Chambers, 2013). OSF / AsPredicted in the social
sciences. Proving precedence by publishing a hash or a timestamp is older still, and is the
ordinary business of trusted timestamping. **None of this is ours.**

**Our delta.** Not the idea — the **mechanism and its imposition**. The pre-registration is
bound to a commit, and a program ([`firewall.py`](firewall.py)) reads the git record and
**fails the build** when the pre-registration is missing, does not *strictly* precede the
result, was edited afterwards, or carries a criterion with no number in it. The discipline
stops being a virtue you claim and becomes a check you cannot merge past.

**Its honest limit, stated where the term is defined:** it cannot catch a pre-registration you
tuned *before* committing it. Git cannot tell that apart from honesty, and neither can we. See
[`incident-log.md`](incident-log.md), Entry 2 — we publish the recipe rather than let you find it.

*Lives in:* [`firewall.py`](firewall.py), [`preregistrations/`](preregistrations/).

---

### The companion gate

The executor **never adjudicates its own result**. A second, independent agent recomputes the
decisive number from the **raw data**, with its own code, and the result stands only if the two
agree. A fabrication and an honest bug fail the same check, because the check judges
**reproducibility, not intent** — you are never asked to assess anyone's good faith.

**Prior art.** Independent replication, which is roughly as old as experimental science. The
four-eyes principle. Double data entry in clinical data management. N-version programming
(Avižienis & Chen, 1977) and differential testing in software. **The idea that a result must be
independently recomputed is not ours and we do not pretend it is.**

**Our delta.** Applying it to **AI agents**, where the failure mode is new: an agent can report
a verification that never ran, and be entirely convincing while doing it. Ours did — it is
[Entry 0](incident-log.md). The rule *the agent that produced the number may never be the one
that certifies it* is the mechanism; catching a real fabrication with it is the evidence.

**Its honest limit:** this one is a fact about **process**, not about a repository. No tool can
read it out of a git log — so it is the mechanism we merely *assert*, while enforcing the
weaker one. That is the wrong way round, and we say so in the README rather than let the
firewall's green tick imply otherwise.

*Lives in:* [`METHOD.md`](METHOD.md) § 2, [`examples/synthetic_gate_demo/`](examples/synthetic_gate_demo/),
[`incident-log.md`](incident-log.md) Entry 0.

---

### The G0–G3 wall taxonomy

Every dead hypothesis is tagged with **the first gate it failed**: **G0** — was there a real
gross edge at all? **G1** — bad prints (feed glitches manufacturing false survivors). **G2** —
the cost wall. **G3** — the tax wall.

The finding, on our own eighteen: **G0 accounts for roughly 13–14 of 18.** The dominant killer
is **not the walls — it is the absence of an edge to defend**. We had framed our own defeats
the comfortable way (*"costs and taxes got us"*), pre-registered the opposite prediction, and
tabulated it. The opposite held.

**Prior art.** Every wall is standard and none is ours: transaction-cost analysis and
implementation shortfall (Perold, 1988); capital-gains taxation; data quality and bad-print
filtering. The observation that most anomalies do not survive out-of-sample is Hou-Xue-Zhang
and Chen-Zimmermann, and the machinery for measuring backtest overfitting is López de Prado
and Bailey.

**Our delta.** The **classification** — one scale, four gates, *first gate failed* — and the
**empirical result on our own corpus**, produced under the full protocol and pre-registered
against our own preferred story. The transferable part is a question, not a discovery:
*before you blame the walls, did your gross edge ever beat buy & hold risk-adjusted?* Usually
it did not.

*Lives in:* [`FALSIFICATIONS.md`](FALSIFICATIONS.md) § the G0–G3 scale, [`METHOD.md`](METHOD.md).

---

### "The artifact does not compile"

The defence against self-deception is **not good faith** — it is that the thing you built
**refuses to build** when the evidence is not there. Good faith is not checkable and does not
scale; a failing build is both. This is the sentence the whole repository is organised around.

**Prior art.** Mechanism over intention is not a new thought: fail-closed design, checks and
balances, *make invalid states unrepresentable* in type-system design. The insight is common
property.

**Our delta.** The **application to research honesty, taken literally**: here the sentence is
not a metaphor. The claim without a pre-registration turns a CI check red and the pull request
does not merge. And the phrase earned its place empirically — when we tried to build the
evidence table, fourteen of eighteen rows had nothing to put in the cell. **Nobody had lied.
The artifact simply did not compile.**

*Lives in:* [`METHOD.md`](METHOD.md), [`incident-log.md`](incident-log.md) Entry 1.

---

### "A gate that nothing depends on is not a gate — it is a log line"

A check that runs, goes red, and **blocks nothing** is not enforcement. It is decoration that
feels like enforcement, which is worse than no check at all, because it buys you the confidence
without the constraint.

**Prior art.** Alert fatigue, non-blocking CI checks, warnings nobody reads, security theatre.
Any engineer who has ignored a red advisory check already knows this. **The insight is not ours.**

**Our delta.** Not the insight — **the incident**. We shipped exactly that bug: `v0.3` published
a gate that enforced nothing. The check ran, went red, and a pull request could have merged
straight over it. We found it by luck, minutes after publishing, and we **left the `v0.3` tag
where it is** — moving it would have erased the only physical evidence of what happened. The
term is ours because the failure is ours, and it is on the record with a commit attached.

*Lives in:* [`incident-log.md`](incident-log.md) Entry 3; the `v0.3` tag; `git rev-parse v0.3`.

---

### What is deliberately not in this glossary

**Substantiation** — *a claim you cannot tabulate row by row, with the evidence beside each row, is
a claim you have not verified.* It is mechanism #5 in [`METHOD.md`](METHOD.md), it is the discipline
that caught the biggest thing we have ever caught about ourselves ([`incident-log.md`](incident-log.md),
Entry 1), and it is **not in this glossary**.

Until this release that section was called *"Substantiation as a **gate**"*. Writing this file is what
made us read the two documents side by side, and the name did not survive it: by our own rule, *a gate
that nothing depends on is not a gate — it is a log line*. **So we renamed it**, in `METHOD.md`, to
*"Substantiation as a discipline (and why it is not a gate)"*. We would rather correct our own
front-page vocabulary than ship two files that contradict each other.

The rule of this file is that our delta must be a **mechanism and its enforcement**. For
substantiation, there is no mechanism. **Nothing in this repository fails when a claim is
unsubstantiated.** No tool tells you *"you claimed sixteen — now tabulate them."* We do it
because we were burned once, and a habit we happen to keep is not a contribution we get to name.

If we ever build the thing that turns a build red on an unsubstantiated claim, it earns an entry
here. Until then it stays where it belongs: in the method, and in the incident log.

---

### How to cite, and how to reach the author

Machine-readable attribution is in [`CITATION.cff`](CITATION.cff) — GitHub renders it as *"Cite
this repository"*. If you use a term from this file, the citation is the repository; the credit
for the ideas underneath it belongs to the prior art named in each entry.

Contact is in the [README](README.md#contact). Corrections to this glossary — especially *"you are
claiming something that was already X's"* — are the most useful thing anyone could send us. Nobody has
yet, because nobody has read this yet. If one lands, it goes in the incident log with attribution, not
in a footnote.

---

## IT — sintesi

Un'idea senza nome non è citabile, né discutibile, né rifiutabile. Qui i concetti hanno un nome.

**Battezzare non è rivendicare l'invenzione.** Ogni voce dichiara (i) **cosa esisteva prima**,
coi nomi — la pre-registrazione viene dai trial clinici, la replica indipendente ha un secolo,
l'overfitting dei backtest l'hanno misurato López de Prado e Bailey — e (ii) **qual è il nostro
delta**, che quasi sempre **non è l'idea**: è il **meccanismo** e la sua **imposizione**. Sapere
che si dovrebbe pre-registrare è vecchio. Avere la build che fallisce quando non l'hai fatto è
la parte che abbiamo spedito noi. Una voce che non sa dichiarare un delta onesto **non entra**.

- **The firewall commit** — la pre-registrazione legata a un commit, e un programma che
  **fa fallire la CI** se manca, se non precede *strettamente* il risultato, se è stata
  modificata dopo, o se il criterio non ha un numero dentro. *Prior art:* trial clinici,
  Registered Reports (Chambers 2013), OSF. *Limite onesto:* non becca la pre-registrazione che
  hai accordato *prima* di committarla (Entry 2).
- **The companion gate** — l'esecutore non aggiudica **mai** il proprio risultato: un secondo
  agente indipendente ricalcola la cella decisiva dal **dato grezzo**, con codice proprio.
  Giudica **la riproducibilità, non l'intenzione**. *Prior art:* replica indipendente,
  four-eyes, N-version programming (Avižienis & Chen 1977). *Nostro:* l'applicazione **agli
  agenti AI**, e una fabbricazione vera beccata (Entry 0). *Limite onesto:* è un fatto di
  **processo** — nessun tool lo legge da un git log.
- **The G0–G3 wall taxonomy** — ogni ipotesi morta è etichettata col **primo gate fallito**:
  **G0** (c'era davvero un edge lordo?), **G1** (bad print), **G2** (muro dei costi), **G3**
  (muro fiscale). Reperto: **G0 ≈ 13–14 su 18** — il killer dominante **non sono i muri, è
  l'assenza di edge**. *Prior art:* i muri sono tutti standard (Perold 1988; fiscalità; data
  quality). *Nostro:* la **classificazione** e il **risultato empirico**, pre-registrato contro
  la nostra stessa storia comoda.
- **"The artifact does not compile"** — la difesa dall'auto-inganno non è la buona fede: è che
  l'artefatto **si rifiuta di compilare**. *Prior art:* il meccanismo sopra l'intenzione non è
  un pensiero nuovo. *Nostro:* l'applicazione **letterale** alla ricerca — qui il claim senza
  pre-registrazione fa diventare rossa una CI e la PR non mergia.
- **"A gate that nothing depends on is not a gate — it is a log line"** — un check che diventa
  rosso e **non blocca niente** non è imposizione: è decorazione che *sembra* imposizione, e
  quindi è peggio di nessun check. *Prior art:* alert fatigue, check non-bloccanti, security
  theatre. *Nostro:* **non l'intuizione — l'incidente.** Quel bug l'abbiamo spedito noi (`v0.3`),
  e il tag l'abbiamo **lasciato dov'è**: spostarlo avrebbe cancellato l'unica prova fisica.

**Cosa NON c'è, di proposito.** *Substantiation* — «un claim che non sai tabulare riga
per riga non l'hai verificato» — è il meccanismo #5 di `METHOD.md` ed è ciò che ha beccato la
cosa più grossa che ci siamo mai beccati addosso (Entry 1). **Non è in questo glossario**, e il
motivo è la regola di questo file: il nostro delta dev'essere un **meccanismo e la sua
imposizione**. Per la substantiation **non esiste un meccanismo**: niente, in questo repository,
fallisce quando un claim non è sostanziato. Nessun tool ti dice *«hai dichiarato sedici — ora
tabulali»*. Lo facciamo perché ci siamo bruciati una volta, e un'abitudine che ci capita di
tenere **non è un contributo che possiamo battezzare**. Se un giorno costruiremo la cosa che fa
diventare rossa una build su un claim non sostanziato, si guadagnerà la sua voce. Fino ad allora
resta dov'è: nel metodo, e nell'incident log.

Fino a questa release quella sezione si chiamava *«La sostanziazione come **gate**»*. Scrivere questo
file è ciò che ci ha costretti a leggere i due documenti affiancati, e il nome non è sopravvissuto:
per la nostra stessa regola, *un gate da cui non dipende nulla non è un gate, è una riga di log*.
**L'abbiamo rinominata** in `METHOD.md`. Meglio correggere il proprio vocabolario di facciata che
spedire due file che si contraddicono.

**Come citare:** [`CITATION.cff`](CITATION.cff). **Contatto:** [README](README.md#contact). Le
correzioni a questo glossario — soprattutto *«questa cosa era già di X»* — sono la posta più
utile che possiamo ricevere, e finiscono nell'incident log con attribuzione, non in una nota a
piè di pagina.
