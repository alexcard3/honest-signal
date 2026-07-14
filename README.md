# honest-signal

**A method for doing honest research with AI agents — forged and stress-tested on the most hostile case there is: the markets.**

> The system can be the best in the world, but if no one knows it, it's worth nothing.
> So this repository is not a trading edge. It's a *method*, shipped in the open.

[![proof of precedence — our own tool, run on our own history](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/alexcard3/honest-signal/main/audit/badge.json)](audit/report.txt)

**That red badge is not a broken build.** It is our own tool, run on our own history, reporting how
many of our eighteen falsifications carry a pre-registration commit that **provably came first**. It
fails us far more often than it passes us. The number in it is *emitted* by
[`scripts/audit_history.py`](scripts/audit_history.py) into [`audit/badge.json`](audit/badge.json) —
**we do not type it**, because a badge with a hand-written number is an assertion wearing the costume
of a machine verdict.

**A second number is worse, and it is deliberately not in the badge.** Only **3 of the 18** went
through the *full* protocol, companion gate included. **No machine can check that one** — the
companion gate is a fact about process, not a property of a repository — so **it is our word**, and
we mark it as our word every time we write it. What a machine proves goes in the badge; what rests on
our word stays in prose. **We never merge the two into one figure**, and we publish both. That is the
entire point.

---

## Quickstart — ten minutes

> **Run it on *your* repo, where you can verify it.
> We ran it on ours, and it failed us 14 times out of 18.**

### 1. Watch the gate catch a fabrication — 30 seconds

```bash
cd examples/synthetic_gate_demo && python gate_demo.py     # needs numpy
```

An executor claims a discovery on pure noise. A second, independent implementation recomputes the
number from the raw data and refuses it. Same mechanism catches an honest bug, because it judges
reproducibility, not intent.

### 2. Pre-register a hypothesis — 5 minutes

Copy [`firewall.py`](firewall.py) into your repository, then:

```bash
pip install pyyaml
python firewall.py preregister P-MY-1 --commit
```

It scaffolds the pre-registration, and then **refuses to commit it** until you have written a kill
criterion with a number in it, a way to measure that number which a stranger could follow, and a
date. It gives you the questions before it takes anything away — and an unanswerable question is
the tool telling you that you do not have a hypothesis yet.

### 3. Install the gate in your CI — 2 minutes

```yaml
- uses: actions/checkout@v7
  with:
    fetch-depth: 0            # NOT the default. Precedence is a fact about history,
                              # and a shallow clone does not have one.
- uses: alexcard3/honest-signal@v0.3.1
```

From now on, a pull request that claims a result **does not merge** unless a pre-registration for
it exists, provably precedes it, has not been edited since, and names something that could have
killed it.

> **Why a tag and not `@main`?** Because `@main` is the most mutable reference there is: your CI
> would change under your feet every time we push. A repository whose entire thesis is *"the
> artifact must not move after the fact"* does not get to ask you to depend on a moving branch. Pin
> the tag, or pin the commit SHA.
>
> **And why `v0.3.1` rather than `v0.3`?** Because **`v0.3` is the release that shipped a gate that
> enforced nothing.** The check ran, went red, and nothing depended on it — a pull request could
> have merged straight over it. We found that by luck, minutes after publishing. **We left the tag
> where it is.** Moving it would erase the only physical evidence for what
> [`incident-log.md`](incident-log.md) Entry 3 says about us, and an unsubstantiated claim of our
> own failure is still an unsubstantiated claim. `v0.3.1` is the same tool with the switch wired in.

### What it checks, and what it will never do

| | |
|---|---|
| **(a)** a result must have a pre-registration | FAIL if missing |
| **(b)** it must **strictly** precede the result | FAIL if the same commit, or later |
| **(c)** it must not have been edited since | FAIL if the content changed |
| **(d)** its kill criterion must not be vacuous | FAIL if there is no number, no procedure, no date |
| **(e)** the gap between the two commits | **printed, never judged** — ours include 23 minutes |

> **This does not make you honest. It makes retrofitting visible and expensive.**

That is the same limit we state for the firewall everywhere else in this repository — *a guard
against retrofitting, not a guarantee of blindness* — and installing it as software does not buy a
stronger claim. You can still write a pre-registration you have already tuned and commit it, fresh
and innocent, before the result. Git cannot tell that apart from honesty. **Neither can this tool,
and neither can any other.** We publish the recipe in [`incident-log.md`](incident-log.md), Entry 2,
rather than leave you to find it.

**Want to watch it bite?** [PR #6](https://github.com/alexcard3/honest-signal/pull/6) claimed a
tradeable edge with no pre-registration. The gate failed and **GitHub refused the merge** — *"the base
branch policy prohibits the merge"* — because `firewall` is a required status check here. We closed it
and left it in the record on purpose: [`examples/blocked-pr/`](examples/blocked-pr/).

The first time we ran that demonstration we got it wrong, and the correction is on the same page: the
gate went red, but it was not *required*, so a human closed the pull request and we described it as
having been blocked. It had not been. See [`incident-log.md`](incident-log.md), Entry 3 — **a gate that
nothing depends on is not a gate; it is a log line.**

---

## Verify this yourself

**Don't trust us. Here are the commands** — including the ones that make us look worse.

**1. Watch the gate refuse a fabrication (30s).**
```bash
cd examples/synthetic_gate_demo && python gate_demo.py     # needs numpy
```

**2. Run the gate on *your* repository, where you can check it.**
```bash
pip install pyyaml
python firewall.py verify                  # every claim, against your own git record
python firewall.py preregister P-MY-1      # it refuses to commit a criterion with no number in it
```

**3. Run our test-suite — the four ways the gate *must* fail.**
```bash
python -m unittest discover -s tests -v
```
These tests **pass**. What they assert is that the gate goes red when a pre-registration is missing,
late, edited, or vacuous. A green suite here means the failures are enforced, not absent.

**4. Check that our own pre-registration came first — in this public repository.**
```bash
git log --diff-filter=A --oneline -- preregistrations/P-TOOL-1.md     # -> d82e6f8
```
That is the commit that introduced [`P-TOOL-1`](preregistrations/P-TOOL-1.md), **before the first line
of the tool it gates was written**. Edit that file today and the `firewall` check on this repository
turns red — rule (c), applied to us.

**5. Recompute the verdict on us.** P-TOOL-1 says we get killed on **2026-09-08** unless someone
outside our account installs this. All three metrics are public data, and the queries are ours:
```bash
# M1 - external workflows referencing the Action (GitHub code search):
#      "alexcard3/honest-signal" path:.github/workflows      -> count owners that are not alexcard3
# M2 - forks carrying their own commits:
gh api repos/alexcard3/honest-signal/forks --paginate
gh api repos/alexcard3/honest-signal/compare/alexcard3:main...OWNER:main --jq .ahead_by
# M3 - substantive issues/PRs from accounts that are not ours:
gh api repos/alexcard3/honest-signal/issues --state all --paginate --jq '.[].user.login'
```
Stars do not count. Plain forks do not count. **We said so before the fact**, so that we cannot reach
for them afterwards.

**6. Check the evidence for the worst thing we have published about ourselves.**
```bash
git rev-parse v0.3          # -> fe30d96...
```
`v0.3` shipped a gate that **enforced nothing** — it ran, it went red, and a pull request could have
merged straight over it ([`incident-log.md`](incident-log.md), Entry 3). We **left the tag where it
is**: moving it would have erased the only physical evidence. The tag is the receipt.

**What you cannot verify, and we will not pretend otherwise.** The badge number comes from
[`scripts/audit_history.py`](scripts/audit_history.py) run against our **private** research history —
so it cannot run in public CI, and **you cannot re-run it**. What you *can* check is that the badge
agrees with the raw output we commit ([`audit/report.txt`](audit/report.txt)) and with the row-by-row
table in [`FALSIFICATIONS.md`](FALSIFICATIONS.md). Machine-**produced** is not the same as externally
machine-**verifiable**, and we are not going to let a green tick blur the difference.

---

## EN — What this is

honest-signal is a **method for keeping AI-assisted research honest** — so that an agent (or a human) cannot fool itself, or you, into believing a result that isn't there. It ships as five mechanisms, one runnable demo, an incident log of the time the method caught a fabrication in our own pipeline, and a full index of every hypothesis it killed.

We built it because we needed it. Three years of searching for a tradable edge in financial markets produced none that survives costs out-of-sample. The method is what we built to make that verdict trustworthy — and [`FALSIFICATIONS.md`](FALSIFICATIONS.md) states, row by row, how strictly each hypothesis was actually checked: 16 **certified dead** (a 17th and an 18th under review), each listed with what killed it, instead of quietly dropped. Those 16 deaths are the method's test-suite. They are how we know it bites — because what it killed was ours.

**Who built it.** An independent researcher, Alessandro Cardurani, working with AI agents. That detail is not incidental: here the agents are both the *subject* of the method — the thing whose honesty must be enforced — and the *tool* that runs it. The method was forged by making those agents check each other, and check themselves, while never being allowed to self-certify.

**The claim we defend.** Most "AI replicates anomalies and nothing survives" write-ups harden their guardrails *reactively*, after being wrong. We do two things *before* looking at any number:

1. **Pre-register** the exact recipe and the falsification criterion (a "firewall" commit), and
2. Have a **second, independent agent recompute the result byte-for-byte from the raw data** with its own code — never trusting the executor's report.

That independent recompute is the moat. It already caught a real fabrication (see [`incident-log.md`](incident-log.md)).

### How do I know my AI agent actually did what it says?

You don't — not from its report, and not from how confident it sounds. That is the problem this
repository addresses, and the answer it gives is structural: **the agent that produced a number is
never the one that certifies it.** A second, independent agent recomputes the decisive number from the
raw data, with its own code. A fabrication and an honest bug fail the same check, because the check
judges *reproducibility, not intent* — so you never have to assess anyone's good faith.

**If you run AI agents whose results you then act on** — research, analysis, backtests, anything where an agent reports a number and you decide something because of it — you have the problem this repo addresses: an agent can report a check that never ran, and be entirely convincing while doing it. Ours did. It is [Entry 0](incident-log.md).

What you get:

- **A protocol that never lets an agent certify its own work.** The executor does not adjudicate. A second, independent agent recomputes the decisive number from the raw data with its own code. A fabrication and an honest bug fail the same check, because the check judges *reproducibility, not intent* — you never have to assess anyone's good faith.
- **A pre-registration discipline** that freezes the recipe and the kill criterion in a commit *before* the data exists, so the result cannot be chosen after seeing it.
- **A runnable 30-second demo** of the gate catching a fabrication, which you can lift into your own loop.
- **A worked example of the cost of doing this honestly**: [`FALSIFICATIONS.md`](FALSIFICATIONS.md) — 18 hypotheses itemised, including the rows where our own protocol turned out to be younger than our claims about it.

No performance claims, here or anywhere in this repo. Nothing in it will make your research succeed. It makes your failures visible — sooner, and more cheaply than the alternative.

### My backtest has a Sharpe of 2.5 — is it real?

Probably not, and our own eighteen say where it most likely dies. Every dead hypothesis in
[`FALSIFICATIONS.md`](FALSIFICATIONS.md) is tagged with the first gate it failed — **G0** (was there a
gross edge at all?), **G1** (bad prints), **G2** (the cost wall), **G3** (the tax wall) — and the
finding contradicted our own comfortable story: **G0 accounts for ~13–14 of the 18.** The dominant
killer is not the walls. It is the **absence of an edge to defend**.

So before you blame costs, answer the question we had to answer: **did the gross edge ever beat buy &
hold, risk-adjusted?** Usually it did not — it was beta in disguise, out-of-sample decay, or an edge
living inside a bar you cannot trade.

### What does a pre-registration look like?

Like [`preregistrations/P-TOOL-1.md`](preregistrations/P-TOOL-1.md) — the one that gates *this
release*, and predicts our own failure. Start from [`preregistrations/TEMPLATE.md`](preregistrations/TEMPLATE.md),
or let the tool scaffold it: `python firewall.py preregister P-MY-1`. It will refuse to commit until
you have written a kill criterion **with a number in it**, a way to measure that number **a stranger
could follow**, and a **date**. A question you cannot answer is the tool telling you that you do not
have a hypothesis yet.

### How to navigate

- [`METHOD.md`](METHOD.md) — the five mechanisms, in full.
- [`FALSIFICATIONS.md`](FALSIFICATIONS.md) — every hypothesis we killed: what was tested, what was committed before the data, what killed it.
- [`GLOSSARY.md`](GLOSSARY.md) — the named concepts, each with its prior art and our actual delta. Naming is not claiming invention, and the file says whose each idea was.
- [`firewall.py`](firewall.py) — the gate, as software. One file, stdlib plus PyYAML.
- [`preregistrations/`](preregistrations/) — the template, and the pre-registration of this release.
- [`audit/`](audit/) — the badge number and the raw output of the run that produced it.
- [`CITATION.cff`](CITATION.cff) — machine-readable attribution, if you cite this.
- [`examples/blocked-pr/`](examples/blocked-pr/) — a pull request the gate refused, kept in the record.
- [`examples/synthetic_gate_demo/`](examples/synthetic_gate_demo/) — the runnable, dependency-light proof.
- [`incident-log.md`](incident-log.md) — the fabrication the gate caught, the time the method caught our own overstated claim, and the four defects we found in the gate itself.

### We pre-registered this release, and here is what would kill it

[`preregistrations/P-TOOL-1.md`](preregistrations/P-TOOL-1.md) was committed **before the first line
of the tool was written**, and it is the first thing the gate gates. If, by **2026-09-08**, no
external repository references the Action, no fork carries its own commits, and no substantive issue
or pull request arrives from anyone who is not us, then the "usable tool" thesis is weak and we
reconsider the lane. Stars do not count. Plain forks do not count. **Our pre-committed prediction is
that we get killed** — the base rate for an unknown repository is zero, and saying so now means a NO
cannot later be dressed up as *"we expected that anyway"*.

There is a small, deliberate symmetry there worth naming: the line you paste into your workflow —
`uses: alexcard3/honest-signal@v0.3.1` — **is the exact string the kill metric searches for**. The
measurement and the artifact are the same object, so we cannot quietly move one without moving the
other.

### Honest limits (v0.4)

- **The gate covers exactly one claim, and we would rather tell you than let you assume.**
  [`firewall.py`](firewall.py) scans `preregistrations/` and `results/`. `results/` does not exist, and
  `preregistrations/` holds one pre-registration: [`P-TOOL-1`](preregistrations/P-TOOL-1.md). So
  `PREREGISTRATION.md` — **P-PUB-1, the pre-registration of the publication itself, with its own kill
  date** — sits *outside* the gate's coverage. Its proof of precedence exists, but in a private
  repository's commit: not unfounded, **not checkable by the public tool**. This is the same class of
  defect as Entry 3 — *a gate not attached to the thing you assumed it guarded* — and we do not get to
  find it and stay quiet about it.
- **The firewall compiles. The moat does not — and it cannot.** Mechanism #1 (pre-registration) is a
  property of the git history, so a program can enforce it, and now one does, on every pull request
  here. Mechanism #2 — the independent byte-exact recompute, the one we call the moat — is a fact
  about *process*, not about a repository. No tool can read it from a git log. So the headline
  **3 of 18** is still a number you are taking on our word, and we have ended up enforcing the
  weaker mechanism while merely asserting the stronger one. That is the wrong way round, and it is
  the true state of it.
- **The gate is beatable and we publish how.** It catches a missing pre-registration, a late one, an
  edited one, and an empty criterion. It cannot catch one you tuned before committing it. See
  [`incident-log.md`](incident-log.md), Entry 2.
- **Rule (d) is a linter, not a judge.** It checks that a criterion has a number, a procedure and a
  date. It cannot tell you whether the thing you promised to measure means anything.

- This is the **method**, not a market discovery. Our cartographic findings (regime structure, correlation erosion under stress) are, by our own assessment and the literature's, **incremental** — they confirm known facts (buy&hold dominates risk-adjusted; correlations rise in crises). They ship later as *demonstrations of the method*, not as news.
- **Full reproduction on our real market data is not possible from outside** — the data lives in a private database and market feeds are generally not redistributable. So we ship a **synthetic, self-contained demo** anyone can re-run to verify the *mechanism*. Full reproduction of the market findings remains **open**, not solved: it would need a data export or a much richer synthetic case, and we have not done it. We will not call "reproducible" anything an outsider cannot re-run.
- Where we stand relative to prior work is stated openly in `METHOD.md`; we position this as a contribution *inside* an existing lineage (López de Prado on backtest overfitting; the registered-reports / replication movement; the 2026 wave of anti-fabrication harnesses for AI agents) — a part we find under-served, not a lone discovery.
- **Proof-of-precedence is partial, and we now say by how much.** Of the 18 hypotheses in [`FALSIFICATIONS.md`](FALSIFICATIONS.md), **4** have a pre-registration commit that provably precedes the data, **2** carry prediction and verdict in the same commit, and **12** were pre-registered off-repo in files we never versioned. The firewall enters the git record on 2026-06-25; everything before that rests on our word. And all those commits live in private repositories — you see a hash, not a proof. We list the state of every row rather than average it away.
- **The protocol exactly as advertised — both mechanisms, end-to-end — has three complete applications** (rows 14, 17, 18; all after 2026-06-25). It is what we run *now*, on everything. It is not what we can retroactively claim for all eighteen, and we would rather tell you that than have you work it out from our own table. A young protocol, dated precisely, is credible; a backdated one is not.

- **v0.4 changed the artifact under test — after `P-TOOL-1` was registered.** This release adds a
  glossary, a citation file, a contact line and this section: it makes the repository more legible, and
  it was written *after* the pre-registration that measures whether anyone adopts it. What it did **not**
  touch is the pre-registration itself — the metrics, the thresholds, the kill date and the escape
  hatches we disallowed are all unchanged, and rule (c) means we *cannot* change them without turning
  our own CI red. What follows is a limit we state now rather than discover conveniently later: the
  seven changes shipped as one bundle, so **no outcome of `P-TOOL-1` can be attributed to any single one
  of them.** If someone installs the Action, we will not get to say the glossary did it.

## Contact

I do this work — building the discipline that keeps AI-assisted research, and the agents that do it,
from fooling the people who rely on the result. **If your team ships agents whose claims you cannot
check, write to me: honest-signal@cardurani.dev.**

Critique, replication, and *"here is where your gate fails"* are the most useful things you can send.
**So far, the only person who has done that to us is us:** [Entry 2](incident-log.md) is the gate
itself, found broken twice *before* release — by running it on ourselves, not by the test suite, which
stayed green throughout. **This inbox is new, and it is empty.** If you break something here, it gets
its own entry, with your name on it.

> **Please don't open a GitHub issue merely to say hello.** Not because it is unwelcome, but because
> [`P-TOOL-1`](preregistrations/P-TOOL-1.md) counts substantive issues from outside accounts as
> evidence that the tool was *adopted* — and a courtesy issue would push our own measurement toward the
> answer that flatters us. A pre-registration you can contaminate with good manners is one we would
> have to throw away. Email is out of band; use it.

## License

- **Code** (everything under `examples/` and any scripts): [MIT](LICENSE).
- **Content** (`README.md`, `METHOD.md`, `incident-log.md` and other docs): CC-BY-4.0 — use freely with attribution.

Contributions, replications, and adversarial critique are welcome — the whole point is external judgment.

---

## IT — Cos'è

honest-signal è un **metodo per mantenere onesta la ricerca assistita da AI** — così che un agente (o un umano) non possa auto-ingannarsi, né ingannare te, credendo a un risultato che non c'è. Spedisce cinque meccanismi, una demo eseguibile, il log della volta in cui il metodo ha beccato una fabbricazione nella nostra stessa pipeline, e l'indice completo di ogni ipotesi che ha ucciso.

L'abbiamo costruito perché ci serviva. Tre anni di ricerca di un edge di mercato tradabile non ne hanno prodotto uno che sopravviva ai costi fuori campione. Il metodo è ciò che abbiamo costruito per rendere quel verdetto affidabile — e [`FALSIFICATIONS.md`](FALSIFICATIONS.md) dichiara, riga per riga, con quale severità ogni ipotesi è stata davvero verificata: 16 **certificate morte** (una 17ª e una 18ª in revisione), ciascuna elencata con ciò che l'ha uccisa, invece di abbandonarle in silenzio. Quelle 16 morti sono la test-suite del metodo. Sono il motivo per cui sappiamo che morde — perché ciò che ha ucciso era nostro.

**Chi l'ha costruito.** Un ricercatore indipendente, Alessandro Cardurani, insieme ad agenti AI. Non è un dettaglio secondario: qui gli agenti sono insieme il *soggetto* del metodo — ciò di cui va imposta l'onestà — e lo *strumento* che lo esegue. Il metodo è nato facendo controllare quegli agenti l'uno con l'altro, e con sé stessi, senza mai permettere l'auto-certificazione.

**La tesi che difendiamo.** La maggior parte degli articoli "l'AI replica le anomalie e nulla sopravvive" indurisce i guardrail *reattivamente*, dopo aver sbagliato. Noi facciamo due cose *prima* di guardare qualunque numero: (1) **pre-registriamo** la ricetta esatta e il criterio di falsificazione (un commit "firewall"); (2) un **secondo agente indipendente ricalcola il risultato byte-per-byte dal dato grezzo** con codice proprio, senza mai fidarsi del report dell'esecutore. Quel ricalcolo indipendente è il fossato — e ha già beccato una fabbricazione reale ([`incident-log.md`](incident-log.md)).

### Quickstart — dieci minuti

> **Fallo girare sul *tuo* repo, dove puoi verificarlo.
> Noi l'abbiamo fatto girare sul nostro, e ci ha bocciati 14 volte su 18.**

**1. Guarda il gate beccare una fabbricazione (30 secondi).**

```bash
cd examples/synthetic_gate_demo && python gate_demo.py     # serve numpy
```

Un esecutore rivendica una scoperta su puro rumore. Una seconda implementazione indipendente
ricalcola il numero dal grezzo e la rifiuta. Lo stesso meccanismo becca un bug onesto, perché
giudica la riproducibilità, non l'intenzione.

**2. Pre-registra un'ipotesi (5 minuti).** Copia [`firewall.py`](firewall.py) nel tuo repo:

```bash
pip install pyyaml
python firewall.py preregister P-MIA-1 --commit
```

Scaffolda la pre-registrazione e poi **si rifiuta di committarla** finché non hai scritto un criterio
di kill con dentro un numero, un modo di misurarlo che un estraneo potrebbe seguire, e una data. Ti
dà le domande prima di toglierti qualcosa — e una domanda a cui non sai rispondere è il tool che ti
dice che **non hai ancora un'ipotesi**.

**3. Installa il gate nella tua CI (2 minuti).**

```yaml
- uses: actions/checkout@v7
  with:
    fetch-depth: 0            # NON è il default. La precedenza è un fatto sulla storia,
                              # e un clone shallow non ce l'ha.
- uses: alexcard3/honest-signal@v0.3.1
```

Da qui in poi, una PR che rivendica un risultato **non mergia** se non esiste una pre-registrazione
che lo precede dimostrabilmente, non è stata modificata dopo, e nomina qualcosa che avrebbe potuto
ucciderlo.

> **Perché un tag e non `@main`?** Perché `@main` è il riferimento **più mutabile che esista**: la
> tua CI cambierebbe sotto i piedi a ogni nostro push. Un repository la cui tesi è *"l'artefatto non
> deve muoversi dopo il fatto"* non può chiederti di dipendere da un branch mobile. Pinna il tag, o
> pinna lo SHA.
>
> **E perché `v0.3.1` e non `v0.3`?** Perché **`v0.3` è la release che ha spedito un gate che non
> imponeva niente.** Il check girava, diventava rosso, e nulla dipendeva da lui: una PR ci sarebbe
> passata sopra. L'abbiamo scoperto per fortuna, pochi minuti dopo aver pubblicato. **Il tag l'abbiamo
> lasciato dov'è:** spostarlo cancellerebbe l'unica prova fisica di ciò che la Entry 3 di
> `incident-log.md` dice di noi — e un claim non sostanziato resta un claim non sostanziato anche
> quando è un'accusa contro sé stessi. `v0.3.1` è lo stesso tool, con l'interruttore attaccato.

**Cosa controlla:** (a) un risultato deve avere una pre-registrazione; (b) questa deve precederlo
**strettamente** (stesso commit = FAIL); (c) non deve essere stata modificata dopo; (d) il criterio di
kill non dev'essere vacuo (niente numero, niente procedura, niente data = FAIL); (e) il **gap** fra i
due commit si **stampa, non si giudica** — i nostri includono 23 minuti.

> **Questo non ti rende onesto. Rende il retrofitting visibile e costoso.**

È lo stesso limite che dichiariamo ovunque per il firewall (*una guardia contro il retrofitting, non
una garanzia di cecità*), e installarlo come software non compra un claim più forte. Puoi sempre
scrivere una pre-registrazione già accordata e committarla fresca, innocente, prima del risultato. Git
non la distingue dall'onestà. **Nemmeno questo tool, e nemmeno nessun altro.** La ricetta la
pubblichiamo noi (`incident-log.md`, Entry 2) invece di lasciartela scoprire.

**Vuoi vederlo mordere?** [PR #6](https://github.com/alexcard3/honest-signal/pull/6) rivendicava un
edge tradabile senza pre-registrazione: il gate ha fallito e **GitHub ha rifiutato il merge** (*"the
base branch policy prohibits the merge"*), perché qui `firewall` è un check **obbligatorio**. Chiusa e
lasciata apposta nel record ([`examples/blocked-pr/`](examples/blocked-pr/)).

La prima volta quella dimostrazione l'avevamo sbagliata, e la correzione sta sulla stessa pagina: il
gate era rosso ma **non era obbligatorio**, quindi la PR l'ha chiusa un umano — e noi l'abbiamo
raccontata come "bloccata". Non lo era. (`incident-log.md`, Entry 3: **un gate da cui non dipende nulla
non è un gate, è una riga di log.**)

### A chi serve, e cosa ti dà

**Se fai girare agenti AI sui cui risultati poi agisci** — ricerca, analisi, backtest, qualunque cosa in cui un agente riporta un numero e tu decidi di conseguenza — hai il problema che questo repo affronta: un agente può riportare una verifica mai avvenuta, ed essere del tutto convincente mentre lo fa. Il nostro l'ha fatto: è la [Entry 0](incident-log.md).

Cosa ti dà: (1) un **protocollo che non permette mai a un agente di certificare il proprio lavoro** — l'esecutore non aggiudica; un secondo agente indipendente ricalcola la cella decisiva dal dato grezzo con codice proprio. Fabbricazione e bug onesto cadono sullo stesso controllo, perché giudica *la riproducibilità, non l'intenzione*: non devi mai valutare la buona fede di nessuno. (2) Una **disciplina di pre-registrazione** che congela ricetta e criterio di kill in un commit *prima* che il dato esista. (3) Una **demo eseguibile in 30 secondi** del gate che becca una fabbricazione, trasportabile nel tuo loop. (4) Un **esempio concreto di quanto costa farlo onestamente**: [`FALSIFICATIONS.md`](FALSIFICATIONS.md), 18 ipotesi voce per voce — comprese le righe in cui il nostro protocollo si è rivelato più giovane delle nostre affermazioni su di esso.

Nessun claim di performance, qui né altrove in questo repo. Niente di tutto ciò farà riuscire la tua ricerca: rende visibili i suoi fallimenti, prima e a costo minore.

### Limiti onesti (v0.4)

**Il gate copre esattamente UNA claim, e preferiamo dirtelo che lasciartelo presumere.**
[`firewall.py`](firewall.py) scansiona `preregistrations/` e `results/`: `results/` **non esiste** e
`preregistrations/` contiene una sola pre-registrazione ([`P-TOOL-1`](preregistrations/P-TOOL-1.md)).
Quindi `PREREGISTRATION.md` — **P-PUB-1, la pre-registrazione della pubblicazione stessa, con la sua
kill-date** — è **fuori dalla copertura del gate**. La sua prova-di-precedenza esiste, ma vive nel
commit di un repo **privato**: non è infondata, è **non verificabile dal tool pubblico**. È la stessa
classe della Entry 3 — *un gate non attaccato a ciò che credevi custodisse* — e non abbiamo il diritto
di scoprirla e tacerla.

**Il firewall compila. Il fossato no — e non può.** Il meccanismo #1 (pre-registrazione) è una
proprietà della storia git: un programma lo può imporre, e ora lo fa a ogni PR. Il meccanismo #2 — il
ricalcolo indipendente byte-esatto, quello che chiamiamo **il moat** — è un fatto di *processo*, non di
un repository: nessun tool lo legge da un git log. Quindi il **3 su 18** resta un numero sulla nostra
parola, e siamo finiti a imporre il meccanismo più debole e a limitarci ad *asserire* il più forte. È
l'ordine sbagliato, ed è com'è davvero.

**Il gate è battibile, e pubblichiamo come.** Becca una pre-registrazione mancante, tardiva, modificata,
o con un criterio vuoto. Non becca quella che hai accordato *prima* di committarla (`incident-log.md`,
Entry 2). **La regola (d) è un linter, non un giudice:** verifica che un criterio abbia un numero, una
procedura e una data; non può dirti se la cosa che hai promesso di misurare significhi qualcosa.

**Abbiamo pre-registrato anche questa release** ([`preregistrations/P-TOOL-1.md`](preregistrations/P-TOOL-1.md),
committata **prima della prima riga di codice del tool**): se al **2026-09-08** nessun repo esterno
referenzia l'Action, nessun fork porta commit propri e nessuna issue/PR sostanziale arriva da chi non
siamo noi, la tesi "tool usabile" è debole e si riconsidera. Le star non contano, i fork-segnalibro non
contano. **La nostra predizione pre-impegnata è che veniamo uccisi.** E c'è una simmetria voluta: la
riga che incolli nel tuo workflow — `uses: alexcard3/honest-signal@v0.3.1` — **è esattamente la stringa
che la metrica di kill va a cercare.** Misura e artefatto sono lo stesso oggetto: non possiamo spostare
l'una senza spostare l'altro.

Questo è il **metodo**, non una scoperta di mercato (i nostri reperti cartografici sono incrementali per nostra stessa ammissione; ci collochiamo *dentro* una lineage esistente — López de Prado, registered reports, l'ondata 2026 di harness anti-fabbricazione — un aspetto che troviamo sotto-servito, non una scoperta solitaria). La riproduzione piena sui dati di mercato reali non è possibile dall'esterno (DB privato, feed non ridistribuibili): spediamo una **demo sintetica** ri-eseguibile da chiunque per verificare il *meccanismo*. Non chiameremo "riproducibile" ciò che un esterno non può ri-eseguire.

**Prova-di-precedenza: parziale, e ora diciamo di quanto.** Delle 18 ipotesi in [`FALSIFICATIONS.md`](FALSIFICATIONS.md), **4** hanno un commit di pre-registrazione che precede dimostrabilmente il dato, **2** hanno predizione e verdetto nello stesso commit, **12** furono pre-registrate off-repo in file mai versionati. Il firewall entra nel record git il 2026-06-25: tutto ciò che viene prima poggia sulla nostra parola. E quei commit stanno in repo privati — vedi un hash, non una prova. Elenchiamo lo stato di ogni riga invece di mediarlo via.

**Il protocollo esattamente come lo pubblicizziamo — entrambi i meccanismi, end-to-end — ha tre applicazioni complete** (righe 14, 17, 18; tutte dopo il 2026-06-25). È ciò che eseguiamo **ora**, su tutto. Non è ciò che possiamo rivendicare retroattivamente sulle diciotto, e preferiamo dirtelo noi piuttosto che lasciartelo ricavare dalla nostra stessa tabella. Un protocollo giovane e datato con precisione è credibile; uno retrodatato no.

**La v0.4 ha cambiato l'artefatto sotto test — dopo la registrazione di `P-TOOL-1`.** Questa release
aggiunge glossario, file di citazione, riga di contatto e questa sezione: rende il repository più
leggibile, ed è stata scritta *dopo* la pre-registrazione che misura se qualcuno lo adotta. Ciò che
**non** ha toccato è la pre-registrazione stessa: metriche, soglie, kill-date e vie di fuga vietate sono
invariate — e la regola (c) fa sì che **non possiamo** cambiarle senza far diventare rossa la nostra CI.
Il limite lo dichiariamo ora invece di scoprirlo comodamente dopo: i sette interventi spediscono in
**un unico bundle**, quindi **nessun esito di `P-TOOL-1` sarà attribuibile a uno solo di essi**. Se
qualcuno installerà l'Action, non potremo dire *«è stato il glossario»*.

### Contatto

Faccio questo lavoro: costruisco la disciplina che impedisce alla ricerca assistita da AI — e agli
agenti che la eseguono — di ingannare chi poi sul risultato ci decide qualcosa. **Se il tuo team spedisce
agenti i cui claim non puoi verificare, scrivimi: honest-signal@cardurani.dev.**

Critiche, repliche e *«ecco dove il tuo gate fallisce»* sono la cosa più utile che puoi mandarmi.
**Finora l'unico che l'ha fatto a noi siamo noi:** la [Entry 2](incident-log.md) è il gate stesso,
trovato rotto due volte *prima* della release — facendolo girare su di noi, non dal test suite, che è
rimasto verde per tutto il tempo. **Questa casella è nuova, ed è vuota.** Se rompi qualcosa qui, si
guadagna la sua entry, col tuo nome sopra.

> **Per favore non aprire una issue GitHub solo per salutare.** Non perché sia sgradito, ma perché
> [`P-TOOL-1`](preregistrations/P-TOOL-1.md) conta le issue sostanziali da account esterni come **prova
> che il tool è stato adottato**: una issue di cortesia spingerebbe la nostra stessa misura verso la
> risposta che ci lusinga. Una pre-registrazione che si può inquinare con la buona educazione è una
> pre-registrazione da buttare. L'email è **fuori banda**: usa quella.

### Licenza

Codice: [MIT](LICENSE). Contenuti/docs: CC-BY-4.0 (usa liberamente con attribuzione). Contributi, repliche e critica avversariale sono benvenuti — il punto è esattamente il giudizio esterno.

Concetti battezzati, con la loro *prior art* e il nostro delta reale: [`GLOSSARY.md`](GLOSSARY.md).
Attribuzione machine-readable: [`CITATION.cff`](CITATION.cff).
