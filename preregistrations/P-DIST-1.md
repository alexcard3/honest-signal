---
id: P-DIST-1
claim: >
  Deliberately distributing honest-signal - five named emails (Vaccaro,
  Kapoor & Narayanan, Gundersen, the ReScience C editors, Recht), one US-RSE
  #general share, and one public post - converts into at least one adoption or
  substantive engagement traceable to those acts.
hypothesis: >
  If reaching the specific people whose published work argues for (or, for Recht,
  against) CI-enforced pre-registration actually converts, then by the verification
  date at least one external workflow reference from a contacted account (M1) OR one
  substantive issue / PR / discussion on this repository referencing one of the acts
  (M3) will exist. If neither does, targeted distribution to the ideal audience did
  not convert - direct evidence for the P-TOOL-1 kill, not against it.
prediction: >
  We expect to be killed. The base rate for cold outreach from an unknown author is
  ~zero; the realistic outcome is one or two private email replies, which are
  uncountable and satisfy no metric. Our pre-committed point estimate: M1 = 0
  traceable external workflow references, M3 = 0 traceable substantive engagements.
  A YES - any traceable M1 or M3 - would be genuinely surprising, and we state it now
  so a NO cannot later be recast as "expected all along, therefore uninformative".
kill_criterion: >
  KILL if and only if, on the verification date, M1 == 0 AND M3 == 0 traceable to a
  listed distribution act, with precondition P-prime satisfied. Stars, plain forks
  with no commits, and private email replies do NOT count and cannot prevent the kill.
survive_criterion: >
  NOT killed if M1 >= 1 OR M3 >= 1 traceable to a listed act: a single external
  workflow file referencing the Action from an account we contacted, or a single
  substantive issue, PR or discussion on this repository that references one of the
  distribution acts, is sufficient.
verification_date: 2026-09-08
outcome_if_kill: >
  Record that targeted distribution to the ideal audience did not convert, and treat
  it as evidence for the P-TOOL-1 kill. We do NOT extend the window, and we do NOT
  re-attribute an untraceable adoption to the push to manufacture a survival.
outcome_if_void: >
  A VOID means we did not actually run the push - the five emails, the US-RSE share
  and the one public post did not all happen by the precondition date. It is not a
  reprieve: it records that we built instead of shipped, the more embarrassing finding
  about this lane, not a lesser one.
measured_by:
  - id: M1
    what: >
      External public repositories referencing this Action in a workflow file, whose
      owner is an account we contacted in the five emails.
    how: >
      GitHub code search, query: "alexcard3/honest-signal" path:.github/workflows ;
      count hits whose owner is not alexcard3 and appears in the contacted list.
      Anyone can run this query.
    counts_zero_as: kill-eligible
  - id: M3
    what: >
      Substantive issues, PRs or discussions on this repository, opened by an account
      that is not ours, referencing one of the distribution acts.
    how: >
      gh api repos/alexcard3/honest-signal/issues --state all --paginate , filtered to
      user.login != alexcard3 and user.type != Bot (the endpoint also returns PRs),
      plus the Discussions tab, same filter. "Substantive" excludes spam and
      pure-praise with no content.
    counts_zero_as: kill-eligible
precondition:
  id: P-prime
  what: The five named emails, the US-RSE share, and one public post all happened.
  how: >
    Each of the three act-classes evidenced by a URL or a sent-record, performed by
    2026-08-11: five individually-written emails to the named recipients, one share in
    the US-RSE Slack #general, and one public post (Show HN, an awesome-list PR, or a
    GitHub Marketplace listing). Silence, or only a subset, is not the push.
  if_false: >
    The verdict is VOID, not NO - see outcome_if_void. A zero reading with the push
    unperformed measures our silence, not the audience's indifference.
known_blind_spots:
  - >
    Private email replies are invisible to both metrics. The most likely real outcome -
    a thoughtful reply that never becomes a public issue - counts as zero here. We are
    measuring public, traceable conversion, and we say so: this under-counts genuine
    interest.
  - >
    Attribution is conservative and deliberately narrow. An external install we cannot
    trace to a listed act counts for P-TOOL-1 but NOT for P-DIST-1, making this strictly
    harder to survive than P-TOOL-1, on purpose: it tests the push, not luck.
  - >
    LOW STATISTICAL POWER, ACCEPTED. Four weeks from distribution to verification detects
    a fast conversion but cannot rule out a later one. Same asymmetry, and same reason, as
    P-TOOL-1: the binding constraint is time, not certainty.
status: open
---

# P-DIST-1 — did distributing it move anything?

## EN

`P-TOOL-1` asks whether anyone installs the tool. It has a precondition - that at least
one act of distribution happens - but it does not commit us to *which* acts, and it counts
any adoption from any source. This file is narrower and harder, and that is its whole reason
to exist.

It pre-commits, before the first email is sent, to a **specific** push: five named people
whose own published work is the argument for (or, in Recht's case, against) a CI-enforced
pre-registration gate, plus one sanctioned public share, plus one public post. And it counts
only what is **traceable to those acts**. A random star, a lucky fork, an install we cannot
tie to the push - none of them save this prediction. That is deliberate: the thing tested is
whether *distributing to the ideal audience converts*, not whether the repository gets lucky.

### Why commit this at all, when P-TOOL-1 exists

Because the failure mode it guards against is our own. The precondition of P-TOOL-1 is
satisfied by "at least one act". Left there, a single low-effort post would let us say we
distributed. P-DIST-1 names the real push and makes it falsifiable: five emails, one share,
one post, or **VOID**. It is the defence against shipping the minimum and calling it
distribution.

### The prediction, pre-committed

We expect M1 == 0 and M3 == 0. Cold outreach from an unknown converts at ~zero; the honest
expectation is one or two private replies no metric can see. We write that here so a NO on
2026-09-08 is a result we predicted, not one we rationalise, and so a YES is genuinely
surprising.

### What would kill it, and the escape hatches we disallow

On 2026-09-08: if no external workflow references the Action from an account we emailed, and
no substantive issue / PR / discussion on this repository references one of the acts, the
prediction survives - i.e. the push moved nothing. Stars do not count. Plain forks do not
count. Private replies do not count. A survival must be **public and traceable**, or it is
not a survival.

### Relation to P-TOOL-1 and P-PUB-1

This is a strict sub-prediction of `P-TOOL-1`: if P-DIST-1's push moves nothing, that is
direct evidence for the P-TOOL-1 kill. It is not a second, independent oracle dressed up to
look like one, and pretending otherwise would be its own small dishonesty. `P-PUB-1`
(`PREREGISTRATION.md`) measures whether the publication is *read*; this measures whether the
distribution *converts*. The three are deliberately not merged.

### Honest limit

It cannot prove we had not already formed a view of how this lands. No commit can. It proves
only that the acts, the metrics and the disallowed escape hatches were fixed before the first
email was sent, and could not be edited once the outcome was known.

---

## IT — sintesi

`P-TOOL-1` chiede se qualcuno **installa** il tool: ha una precondizione (almeno un atto di
distribuzione) ma non ci impegna a *quali* atti, e conta qualunque adozione da qualunque fonte.
Questo file e' piu' stretto e piu' duro, ed e' tutta la sua ragione d'essere.

Pre-impegna, **prima della prima email**, una spinta *specifica*: cinque persone nominate il
cui lavoro pubblicato e' l'argomento a favore (o, per Recht, contro) un gate di
pre-registrazione imposto in CI, piu' una condivisione pubblica sanzionata, piu' un post
pubblico. E conta **solo cio' che e' tracciabile a quegli atti**. Una stella casuale, un fork
fortunato, un'installazione che non sappiamo legare alla spinta - nessuno salva questa
predizione. E' voluto: si testa se *distribuire al pubblico ideale converte*, non se il repo
e' fortunato.

**Perche' committarlo, se c'e' gia' P-TOOL-1.** Perche' il modo di fallire da cui difende e' il
nostro. La precondizione di P-TOOL-1 e' soddisfatta da "almeno un atto": lasciata li', un
singolo post blando ci lascerebbe dire di aver distribuito. P-DIST-1 nomina la spinta vera e la
rende falsificabile: cinque email, una condivisione, un post, oppure **VOID**. E' la difesa
contro lo spedire il minimo e chiamarlo distribuzione.

**La predizione, pre-impegnata.** Ci aspettiamo M1 == 0 e M3 == 0. Il cold-outreach di uno
sconosciuto converte a ~zero; l'aspettativa onesta e' una o due risposte private che nessuna
metrica vede. Lo scriviamo qui perche' un NO all'8 settembre sia un risultato *predetto*, non
razionalizzato, e un YES sia genuinamente sorprendente.

**Cosa lo ucciderebbe, e le vie di fuga vietate.** All'8 settembre: se nessun workflow esterno
referenzia l'Action da un account contattato, e nessuna issue/PR/discussione sostanziale sul
repo referenzia uno degli atti, la predizione sopravvive - cioe' la spinta non ha mosso niente.
Stelle no. Fork senza commit no. Risposte private no. Una sopravvivenza dev'essere **pubblica e
tracciabile**, o non e' una sopravvivenza.

**Rapporto con P-TOOL-1 e P-PUB-1.** E' una sotto-predizione stretta di P-TOOL-1: se la spinta
non muove niente, e' evidenza diretta per il suo kill. Non e' un secondo oracolo indipendente
travestito da tale. P-PUB-1 misura se la pubblicazione e' *letta*; questo se la distribuzione
*converte*. Le tre non si fondono.

**Limite onesto.** Non prova che non ci fossimo gia' fatti un'idea. Nessun commit lo prova.
Prova solo che gli atti, le metriche e le vie di fuga vietate erano fissati prima della prima
email e non piu' modificabili una volta noto l'esito.
