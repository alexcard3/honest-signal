---
id: P-TOOL-1
claim: >
  A pre-registration gate, shipped as an installable CI check, is adopted by
  external researchers or teams.
hypothesis: >
  If the discipline in this repository is delivered as software rather than as
  prose, at least one party outside our own account will install it (reference the
  Action in their own workflow), fork it and build on it, or engage with it
  substantively (issue / PR / discussion). If nobody does, the "usable tool" thesis
  is weak: we wrote something that reads well and that no one runs.
prediction: >
  We expect to be killed. Base rate for an unknown repository is zero. Our
  pre-committed point estimate: M1 = 0 external workflow references, M2 = 0 active
  forks, M3 = 0-2 substantive issues/PRs/discussions from non-owner accounts. We
  state this before the fact so that a NO cannot later be dressed up as "expected
  all along, therefore not informative", and so that a YES is genuinely surprising.
kill_criterion: >
  KILL if and only if, on the verification date, M1 == 0 AND M2 == 0 AND M3 == 0,
  with precondition P satisfied. Stars and plain forks (no commits) do NOT count
  and cannot prevent the kill.
survive_criterion: >
  NOT killed if any of M1 >= 1, M2 >= 1, M3 >= 1. A single external workflow
  reference, a single fork carrying its own commits, or a single substantive issue,
  PR or discussion from an account that is not ours is sufficient.
verification_date: 2026-09-08
outcome_if_kill: >
  We declare the "installable tool" thesis WEAK and RECONSIDER the lane. We do not
  insist, and we do not quietly extend the window. The NO is published as a row,
  like every other NO in this repository.
outcome_if_void: >
  De-prioritise the lane anyway. A VOID here means we never distributed it, which
  is a worse finding about the lane than a NO, not a reprieve.
measured_by:
  - id: M1
    what: External public repositories referencing this Action in a workflow file.
    how: >
      GitHub code search, query: "alexcard3/honest-signal" path:.github/workflows
      Count hits whose owner is not alexcard3. Anyone can run this query.
    counts_zero_as: kill-eligible
  - id: M2
    what: Active forks - forks carrying at least one commit not present in our main.
    how: >
      gh api repos/alexcard3/honest-signal/forks --paginate
      then, per fork, gh api repos/OWNER/honest-signal/compare/alexcard3:main...OWNER:main
      and read ahead_by. Active iff ahead_by >= 1.
    counts_zero_as: kill-eligible
  - id: M3
    what: Substantive issues, PRs or discussions opened by accounts that are not ours.
    how: >
      gh api repos/alexcard3/honest-signal/issues --state all --paginate
      filtered to user.login != alexcard3 and user.type != Bot (the issues endpoint
      also returns PRs); plus the repository Discussions tab, same filter.
      "Substantive" excludes spam and pure-praise comments with no content.
    counts_zero_as: kill-eligible
precondition:
  id: P
  what: At least one act of distribution actually happened.
  how: >
    At least one public distribution act, evidenced by a URL, performed by
    2026-08-11 (four weeks after registration, leaving four weeks for adoption).
    A post, a submission to an aggregator, a mailing-list message - anything a third
    party can point to. Silence is not a distribution act.
  if_false: >
    The verdict is VOID, not NO: a zero reading would measure our silence, not the
    tool. See outcome_if_void - VOID is not a reprieve.
known_blind_spots:
  - >
    GitHub code search indexes public repositories only. An adopter working in a
    private repository is invisible to M1. M1 therefore measures VISIBLE adoption,
    and undercounts. We are killing on visible adoption and we say so.
  - >
    Code search indexing has a lag of days. A reference added shortly before the
    verification date may not be indexed.
  - >
    None of the three metrics distinguish someone who installed the Action and ran
    it from someone who installed it and ignored the result. We measure installation,
    not compliance. We cannot measure compliance from outside, and we do not claim to.
  - >
    LOW STATISTICAL POWER, ACCEPTED DELIBERATELY. Tooling adoption is slow: the normal
    path is bookmark now, try it in three months. Four weeks after distribution is a
    low-power test - it detects a success, but a failure is weak evidence of
    non-adoption in the longer run. We accept that asymmetry on purpose. A longer
    window would keep this lane open for months on no evidence, and our binding
    constraint is TIME, not certainty. We kill fast, and we say why. This is a limit
    declared, not a test tuned.
status: open
---

# P-TOOL-1 — will anyone actually install this?

## EN

This repository argues that the defence against self-deception is not good faith but
that **the artifact does not compile**. Version 0.3 turns that sentence into software:
a pre-registration gate that fails your CI when the evidence is not there.

A method that pre-registers everything except *its own tooling* would be exempting the
one artifact that claims to enforce pre-registration. So we do not exempt it. This file
is committed **before the first line of the tool is written**, and the tool it gates is
the tool that will read this file.

### What is being claimed

That the gap between "I am convinced" and "I have installed it" can be closed by
shipping the discipline as a CI check. Our own history is the argument for it: fourteen
of our eighteen hypotheses have no pre-registration commit at all — not because the
pre-registrations were written badly, but because **they did not exist**. A tool that
only verifies would not have saved us. One that also scaffolds might have.

That is a hypothesis, not a fact. This file is where it goes to die if it is wrong.

### What would kill it

Eight weeks. Three metrics, all of which anyone can recompute from public GitHub data:
an external workflow referencing the Action (M1), a fork carrying its own commits (M2),
a substantive issue / PR / discussion from an account that is not ours (M3). If all
three are zero on **2026-09-08**, the thesis is weak and the lane is reconsidered.

**Stars do not count. Plain forks do not count.** Those are bookmarks, and a bookmark is
not an installation. We name the escape hatches here, before the fact, so that we cannot
reach for them afterwards.

### The test is under-powered, and we chose that

Tooling adoption is slow — the normal path is *bookmark now, try it in three months*. Four
weeks after distribution detects a success but cannot rule out a later one: a NO here is
weak evidence about the long run, and we are not going to pretend otherwise by calling it
a clean falsification.

We accept the asymmetry deliberately. **A longer window would keep this lane open for
months on no evidence, and the resource we are actually protecting is time, not certainty.**
So we kill fast, and we state the cost of killing fast. The limit is declared; the test is
not tuned to make the limit go away.

### The confound we are not allowed to hide

A zero reading is only evidence about the *tool* if the tool was actually put in front of
anyone. If we publish it and never distribute it, then zero adoption measures **our
silence**, not the tool's usability — and quietly reading that as a NO would be a
falsification we did not earn.

So distribution is a stated **precondition** (P), with its own date. And the VOID branch
is not a reprieve: if P fails, we de-prioritise the lane anyway, for the more embarrassing
reason. There is no outcome of this pre-registration in which we get to keep insisting
without external evidence. That closure is deliberate.

### Relation to `P-PUB-1`

[`PREREGISTRATION.md`](../PREREGISTRATION.md) already pre-registers whether the
*publication* lands — whether anyone reads it. `P-TOOL-1` is a strictly stronger and
different test: whether anyone **installs** it. The two are deliberately not merged,
because the outcome that would teach us the most is the one where they disagree: read and
agreed with, but never installed. That specific result would falsify the premise on which
v0.3 was built — that shipping the discipline as software is what closes the gap — and a
single combined test could not tell it apart from indifference.

### The date

Eight weeks from this commit: **2026-09-08**. The v0.3 merge is expected within days of
it. If the merge slips, we will **not** edit this file — editing a firewall after the fact
is the exact thing the tool exists to catch, and it would fail its own check. We accept
the shorter window instead, and record the actual merge date in the verdict.

### Honest limit of this pre-registration

It cannot prove we had not already formed a view about how this lands. **No commit can
prove that.** It proves only that the criterion, the metrics and the escape hatches we
disallowed could not be edited once the outcome was known. That is a guard against
retrofitting, not a guarantee of blindness — the same limit we state everywhere else, and
it does not become weaker by being applied to ourselves.

---

## IT — sintesi

Questo repository sostiene che la difesa contro l'auto-inganno non è la buona fede: è che
**l'artefatto non compila**. La v0.3 trasforma quella frase in software — un gate di
pre-registrazione che fa fallire la CI quando l'evidenza non c'è. Un metodo che
pre-registra tutto *tranne il proprio strumento* esenterebbe l'unico artefatto che
pretende di imporre la pre-registrazione: quindi non lo esentiamo. Questo file è
committato **prima della prima riga di codice del tool**, e il tool che lo gatta è quello
che leggerà questo file.

**La tesi.** Che l'abisso fra "sono convinto" e "l'ho installato" si colmi spedendo la
disciplina come CI check. L'argomento a favore è la nostra stessa storia: quattordici delle
nostre diciotto ipotesi non hanno alcun commit di pre-registrazione — non perché fossero
scritte male, ma perché **non esistevano**. Un tool che solo verifica non ci avrebbe
salvati; uno che scaffolda, forse. È un'ipotesi, non un fatto: questo file è dove muore se
è sbagliata.

**Cosa la uccide.** Otto settimane, tre metriche ricalcolabili da chiunque su dati GitHub
pubblici: un workflow esterno che referenzia l'Action (M1), un fork con commit propri (M2),
una issue/PR/discussione sostanziale da un account non nostro (M3). Se al **2026-09-08**
sono tutte e tre zero, la tesi è debole e la lane si riconsidera. **Le star non contano. I
fork senza commit non contano** — sono segnalibri, non installazioni. Nominiamo le vie di
fuga prima, così non possiamo prenderle dopo.

**Il test è sotto-potenziato, e l'abbiamo scelto.** L'adozione di tooling è lenta: la via
normale è *segnalibro oggi, provo fra tre mesi*. Quattro settimane dopo la distribuzione
rilevano un successo ma non escludono un successo tardivo: un NO qui è evidenza debole sul
lungo periodo, e non facciamo finta del contrario spacciandolo per una falsificazione pulita.
L'asimmetria è accettata di proposito. **Una finestra più lunga terrebbe aperta questa lane
per mesi senza evidenza, e la risorsa che stiamo davvero proteggendo è il tempo, non la
certezza.** Uccidiamo in fretta e dichiariamo il costo di uccidere in fretta: il limite si
dichiara, il test non si aggiusta per farlo sparire.

**Il confound che non ci è permesso nascondere.** Uno zero è evidenza sul *tool* solo se il
tool è stato messo davanti a qualcuno. Se pubblichiamo e non distribuiamo, zero adozioni
misura il **nostro silenzio**, non l'usabilità. Perciò la distribuzione è una
**precondizione** dichiarata (P, entro il 2026-08-11), e il ramo VOID non è una grazia: se P
fallisce, la lane si de-prioritizza comunque, per la ragione più imbarazzante. Non esiste
esito di questa pre-registrazione in cui possiamo continuare a insistere senza evidenza
esterna. La chiusura è voluta.

**Rapporto con `P-PUB-1`.** Quella pre-registra se la *pubblicazione* atterra (se qualcuno
legge). Questa è un test strettamente più forte: se qualcuno **installa**. Non le fondiamo,
perché l'esito che insegnerebbe di più è quello in cui divergono — letto e condiviso, mai
installato: falsificherebbe la premessa stessa su cui la v0.3 è costruita.

**Limite onesto.** Non prova che non ci fossimo già fatti un'idea di come andrà a finire.
**Nessun commit lo prova.** Prova solo che criterio, metriche e vie di fuga vietate non
erano più modificabili una volta noto l'esito: una guardia contro il retrofitting, non una
garanzia di cecità — lo stesso limite che dichiariamo ovunque, e non si indebolisce per il
fatto di essere applicato a noi.
