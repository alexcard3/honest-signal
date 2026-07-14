# Incident log — fabrications and errors the method caught

This log records, honestly, every time a gate or an adversarial review caught an
error or a fabrication in our own research loop. It is primary data on *how* an AI
agent deceives itself (and its operator) inside a research loop — the thing the
whole method exists to prevent. Entries are sanitized of infrastructure detail but
faithful to what happened.

---

## Entry 0 — the executor fabricated a verification that never ran

**When:** 2026-06-29, during the falsification of an event-driven "fade" hypothesis. That study is
row **17** in [`FALSIFICATIONS.md`](FALSIFICATIONS.md) (`P-SHOCK-1`); the report carrying the
fabricated section is the one listed there as its adjudication artifact, and it was corrected in a
later change.

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

## Entry 1 — the method audited our own front-page claim, and found it overstated

**When:** 2026-07-14, while preparing this repository's v0.2 — specifically, while trying to build
[`FALSIFICATIONS.md`](FALSIFICATIONS.md).

**What we claimed.** `METHOD.md`, live and public, said: *"Killing 16 of our own favorites, **with
byte-exact reproduction**..."* And the README sold the pre-registration firewall — a commit that
provably precedes the data — as one of two mechanisms we apply *before looking at any number*.

**What the git record actually says.** Of the eighteen hypotheses: **4** have a firewall commit that
provably precedes the data; **2** carry prediction and verdict in the same commit; **12** have no
commit at all — they were pre-registered in mandate files we never versioned. The two mechanisms
applied *together*, end-to-end, exactly as advertised: **3 of 18**. And "byte-exact reproduction by
an independent agent" was true of the later kills, not of all sixteen — the earlier ones were checked
with determinism (pinned seeds and BLAS, byte-identical re-runs, published output hashes). Good
practice. Not a second pair of eyes.

**The single most uncomfortable fact.** `P-CARRY-1` (row 15) was pre-registered on 2026-06-25 with a
proper firewall commit. Its own direct follow-up — `P-CARRY-2` (row 16), the re-run on genuine
crashes, and **the falsification that takes our counter to 16** — was committed on **2026-06-29, four
days later**, with prediction and verdict in the same commit and **no firewall**. The protocol already
existed. Its predecessor in the same family had used it. The row that closes our headline number did
not. The likely cause is benign: the design and the kill criterion were frozen in an off-repo mandate
file and transcribed into the record afterwards. We believe that is what happened. **We cannot prove
it** — and the number on our front page rests on that row.

**How it surfaced.** Not from a critic, and not from a gate: from *the attempt to tabulate*. For as
long as "16 certified falsifications" stayed a **number**, the hole was invisible — to readers, and
to us. The moment a table demanded one hash per row, fourteen rows had nothing to put in the cell.
The claim did not survive contact with its own evidence format.

**Why it matters — and how it differs from Entry 0.** Entry 0 was a *fabrication*: an agent reported
a check that never ran. This is subtler, and we suspect far more common: **a claim of rigour stronger
than the record supports, with nobody lying.** Every individual sentence had a defensible origin; the
aggregate overstated. There is no dishonest actor to catch here — which is exactly the point. A method
that only catches liars would have caught nothing.

> **The defence is not good faith — not ours, not an agent's.**
> **The defence is that the artifact does not compile.**

**Resolution.** `METHOD.md` §4 graded down: the count of **16 stands** — it is a fact, and no number
in this repository changed — but the claim that all sixteen were verified with equal severity did not,
and it is gone. Two limits were added to the README, not removed. The index was published with the
true state of **every** row, empty cells included. And the lesson was promoted to **mechanism #5**
(*substantiation as a gate*): a claim you cannot tabulate row by row, with the evidence beside each
row, is a claim you have not verified.

The method's own test is whether it turns on its authors. This entry is the answer.

---

## Entry 2 — the gate nearly shipped the failure it exists to prevent

**When:** 2026-07-14, building v0.3 — the pre-registration gate, delivered as software
([`firewall.py`](firewall.py)). Two defects were found in the gate itself before release.
**Neither was found by the test suite**, and that is the entry.

**The first: it said PASS when it should have said FAIL.** Rule (c) forbids editing a
pre-registration after it is registered. The implementation compared the file's blob against
the last commit — so an edit that was merely *saved*, and not yet committed, was invisible to
it. Running the tool on this repository with its own pre-registration deliberately altered by
one line, it printed:

```
[PASS] P-TOOL-1
       note : registered; no result yet
```

A researcher who softened their own kill criterion and ran the gate would have been told they
were clean. That is not a bug next to the mission — **it is the mission, failing.** The whole
claim of this repository is that the defence is not good faith but that the artifact does not
compile; here was the artifact compiling, on a file that had been quietly changed.

It was not caught by a test, because a test only asks the questions its author already thought
to ask. It was caught by **pointing the tool at ourselves and trying to cheat with it.**

**The second: a laundering route we had reasoned about backwards.** The tool refused to follow
renames, and we had written that down as *strictness*. Adversarial review inverted it in one
line: not following renames is not strictness, it is **blindness**. The recipe is three
commands — draft the pre-registration somewhere else, tune it once you have seen the result,
`git mv` it into place — and the tuned text acquires a fresh, innocent-looking registration
commit that provably precedes the verdict. Worse, whether the tool caught this **depended on
the `diff.renames` setting in the user's own git config**: fail-closed on one laptop,
fail-open on another. A tool that sells determinism cannot do that.

**And the first fix for it did not work.** The obvious repair — pin rename detection on — is
wrong, for a reason no one involved predicted: `git log --diff-filter=A -- <path>` applies the
pathspec *before* rename detection, so the delete half of the rename is filtered out, the pair
is never made, and the moved file still reports as an addition. The tool kept passing. It took
a test that ran the same scenario under **both** git configurations to show that the fix was
cosmetic. The working repair inspects the full diff of the commit, not the path-filtered one.

**The third: its verdict depended on the operator's locale.** Python's `subprocess` decodes with
the machine's locale encoding unless told otherwise. On Linux that is UTF-8 and everything worked.
On Windows it is cp1252, and the tool **crashed outright** on any pre-registration containing an
accented character or an em-dash. It surfaced the moment we pointed the gate at our own research
history, which is written in Italian — so the first people it would have broken for are the ones
who wrote it, and after them every adopter who does not write in English.

> **A gate whose verdict depends on the operator's locale is not a gate.**

UTF-8 is now pinned explicitly. This one is worth naming because it is not a subtle logic flaw:
it is the ordinary, boring kind of defect that ships when a tool is only ever run in the
environment its author happens to have.

**Why it matters.** Entry 0 was an AI fabricating a verification. Entry 1 was humans overstating
their own rigour with nobody lying. Entry 2 is **the enforcement mechanism itself** being wrong
in the direction that would have let both of them through. There is no level at which you get to
stop checking — and the ordering is not an accident:

> **Tests check what you thought of.**
> **Dogfooding checks what you didn't.**
> **The red-team checks what you were wrong about.**

Four defects, three mechanisms, on the same 500 lines of code, in the same afternoon — and the
test suite, run alone, would have caught **none of them**. It would have been green, and v0.3
would have shipped a gate that says PASS to an edited pre-registration, PASS to a laundered one,
and crashes on a pre-registration written in Italian.

**Resolution.** Rule (c) now reads the working tree as well as the commit record: an uncommitted
edit is still an edit. A pre-registration that arrives at its path by rename now fails closed,
deterministically, regardless of the reader's git config — and there is a test that runs under
`diff.renames=true` and `diff.renames=false` and fails if the two ever disagree. Encoding is
pinned to UTF-8. Every defect above is now a failing test with the reason written above it.

**The attack we did not close, and cannot.** You can always write a pre-registration you have
already tuned, and commit it fresh, at the right path, before the result. Nothing in git
distinguishes that from an honest one. **No tool does.** We are publishing the recipe rather
than letting you find it: the gate makes retrofitting visible and expensive, and it does not
make anyone honest. It never did.

**Coda — the gate bound its own authors the same afternoon, on a triviality, against our will.**

While building the tool we wanted to change the pre-registration file format: YAML needs a
third-party parser, and Python's standard library ships a TOML one. Cleaner, one dependency
fewer. A cosmetic improvement, decided hours after `P-TOOL-1` was committed, with no outcome
known to anyone and nothing whatsoever to gain by cheating.

**We could not do it.** Changing the format means editing `P-TOOL-1.md`, and editing a
pre-registration fails rule (c) — the rule we had just written, in the tool we were building,
enforced by the CI we were about to install. The only route our own method allows is to
withdraw the pre-registration in public and re-register it under a new id. For a serialization
format, that price was not worth paying. So the file stays in YAML, and the tool carries a
dependency it did not need, because **the firewall said no.**

That is a small thing, and we are keeping it precisely because it is small:

> A firewall that binds you only when it is convenient is not a firewall.

It bound us on a Tuesday, over a file format, when nothing was at stake — which is the only
proof available that it will bind us when something is.

---

## Entry 3 — the mechanism was in force. The enforcement was not.

**When:** 2026-07-14, minutes after merging v0.3 — the release whose entire point is that a
pre-registration gate now runs in CI.

**What we claimed.** The README, `METHOD.md` and the pull request all said the same thing, in the
present tense: *a pull request that claims a result without a valid, prior, unedited
pre-registration **does not merge***. We had a gate. We had run it. We had watched it go red on a
deliberately fabricated pull request, archived the log, and published the archive.

**What the configuration said.**

```
required_status_checks.contexts = ["demo"]
```

The `firewall` job was **not a required check.** It ran on every pull request, computed the right
answer, printed `exit 1` — and nothing depended on it. A pull request with the gate red could be
merged into `main` by anyone, at any time. **Our headline claim was false at the level of the
repository's own settings**, and it had been false for the entire release.

The demonstration we were most proud of — [`examples/blocked-pr/`](examples/blocked-pr/) — was false
in the same way, and more precisely. We wrote that the gate had **blocked** that pull request. It had
not. The gate failed, and then **a human closed the pull request.** It was not blocked. It was merely
red. The difference is the whole thesis.

**How it surfaced: by luck.** Not a test, not a review, not the dogfooding. The merge of v0.3
jammed — for an *unrelated* reason (giving the CI jobs friendly display names had silently detached
the check context that branch protection referenced). While reading the protection rules to find out
why, the required-checks list was there in the output, with one entry in it.

Had that unrelated bug not existed, v0.3 would have merged cleanly and shipped a gate that enforced
nothing, with a README stating that it did.

**Why no test could have found it.** The code was correct. The tests were green. The gate ran in CI
and produced the right verdict. The dogfooding passed. Every artifact we knew how to check was
telling the truth about itself. The failure lived in the **one place none of them look**: whether
anything downstream was listening.

**And it is the fourth time.** Entry 0: an agent reported a check that never ran. Entry 1: humans
claimed a rigour the record did not support. Entry 2: the gate itself was wrong in four ways.
Entry 3: the gate was right, and switched off. Each time the same shape — **a mechanism that exists,
and an enforcement that does not** — and each time we found it by looking at something else.

> **A gate that nothing depends on is not a gate. It is a log line.**
>
> **Verify the enforcement, not the mechanism.** Ask the question that nobody asks of their own
> guardrails: *what actually breaks if this fails?* If the honest answer is **"nothing"**, then you
> do not have a gate. You have a green check mark and a false sentence in your README.

**Resolution.** `required_status_checks.contexts` on `main` is now `["demo", "tests", "firewall"]`,
re-read from the API rather than inferred from a command exiting 0. Check contexts are the job **ids**
now, not their display names — an identifier is a contract, and prose is not. The blocked-pull-request
demonstration was **run again**, against `main`, with the switch on: this time GitHub itself refused
the merge (*"the base branch policy prohibits the merge"*), and that is
[PR #6](https://github.com/alexcard3/honest-signal/pull/6). The old page was corrected in place, with
the correction on top rather than the error quietly deleted. [PR #5](https://github.com/alexcard3/honest-signal/pull/5)
stays in the record as what it actually was.

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
(Quello studio è la **riga 17** di `FALSIFICATIONS.md`, `P-SHOCK-1`.)

**Entry 1 (2026-07-14):** costruendo `FALSIFICATIONS.md` abbiamo scoperto che **il claim di testa del
nostro stesso metodo era sovrastimato**. `METHOD.md` diceva "16 uccise, *con riproduzione byte-esatta*";
il record git dice: **4 righe su 18** hanno un firewall che precede il dato, **2** hanno predizione e
verdetto nello stesso commit, **12** non hanno alcun commit. I due meccanismi applicati *insieme*,
end-to-end, come li pubblicizziamo: **3 su 18**. Il fatto più scomodo: `P-CARRY-2` — la **16ª**, quella
che chiude il contatore — è stata committata il 2026-06-29, **quattro giorni dopo** che il protocollo
firewall esisteva già nel record git, senza firewall, mentre il suo predecessore nella stessa famiglia
(`P-CARRY-1`, 06-25) ce l'ha. Causa probabile benigna (design congelato in un mandate off-repo,
trascritto dopo) — **non dimostrabile**. Non l'ha trovato un critico né un gate: l'ha trovato **il
tentativo di tabulare**. Finché "16 falsificazioni" restava un *numero*, il buco era invisibile; appena
una tabella ha preteso un hash per riga, quattordici celle sono rimaste vuote. A differenza della Entry
0 (una fabbricazione), qui **nessuno ha mentito**: è un claim di rigore più forte del record — più
insidioso, perché non c'è un colpevole da beccare. **La difesa non è la buona fede: è che l'artefatto
non compila.** Correzione: `METHOD.md` §4 graduato (il **16 resta** — nessun numero è cambiato), due
limiti *aggiunti* al README, l'indice pubblicato con le celle vuote in chiaro, e la lezione promossa a
**quinto meccanismo** (*la sostanziazione come gate*).

**Entry 2 (2026-07-14):** costruendo la v0.3 — il gate di pre-registrazione **come software**
(`firewall.py`) — abbiamo trovato **due difetti nel gate stesso**, e **nessuno dei due l'ha trovato
la suite di test**. (1) La regola (c) vieta di editare una pre-registrazione dopo averla registrata:
l'implementazione confrontava il blob solo col record committato, quindi un edit **salvato ma non
committato** era invisibile. Puntando il tool su questo repo, con la nostra stessa P-TOOL-1 alterata
di una riga, stampava `[PASS]`. Chi avesse ammorbidito il proprio criterio di kill si sarebbe sentito
dire che era pulito: non è un bug accanto alla missione, **è la missione che fallisce**. L'ha trovato
il **dogfooding** — puntare il tool su di noi e provare a barare. (2) Il tool non seguiva i rinomini e
l'avevamo scritto come *severità*: la **review avversariale** l'ha ribaltato in una riga — non seguire
i rinomini non è severità, è **cecità**. Ricetta di riciclaggio in tre comandi: scrivi la
pre-registrazione altrove, accordala dopo aver visto il risultato, `git mv` al posto giusto → il testo
accordato acquisisce un commit di registrazione fresco e anteriore al verdetto. Peggio: il
comportamento **dipendeva dal `diff.renames` nel .gitconfig dell'utente** (fail-closed su un portatile,
fail-open su un altro). **E la prima correzione non funzionava:** `git log --diff-filter=A -- <path>`
applica il pathspec *prima* del rilevamento rinomini, quindi la metà "delete" viene filtrata via, la
coppia non si forma e il file spostato continua a risultare un'aggiunta. L'ha smascherata un test che
gira lo stesso scenario sotto **entrambe** le configurazioni git. (3) `subprocess` decodifica con
l'encoding **locale**: su Linux è UTF-8 e tutto funzionava; su Windows è cp1252 e il tool **crashava**
su qualunque pre-registrazione con un accento o una lineetta. È emerso puntando il gate sulla nostra
storia di ricerca, che è scritta in italiano: i primi a cui si sarebbe rotto siamo **noi**, e subito dopo
ogni adottante che non scrive in inglese. **Un gate il cui verdetto dipende dal locale dell'operatore non
è un gate.** La lezione, nell'ordine in cui l'abbiamo
imparata: **i test controllano ciò a cui hai pensato; il dogfooding controlla ciò a cui non hai pensato;
il red-team controlla ciò su cui ti sbagliavi.** Entry 0 = l'AI ha mentito. Entry 1 = gli umani hanno
gonfiato. Entry 2 = **il meccanismo di enforcement stesso** era sbagliato, nella direzione che avrebbe
lasciato passare gli altri due. E l'attacco che **non** abbiamo chiuso, e che nessuno può chiudere:
puoi sempre scrivere una pre-registrazione già accordata e committarla fresca, al path giusto, prima del
risultato. Git non la distingue. **Nessun tool la distingue.** Ne pubblichiamo la ricetta invece di
lasciartela scoprire: il gate rende il retrofitting visibile e costoso, non rende onesti.
**Entry 3 (2026-07-14):** pochi minuti dopo aver mergiato la v0.3 — la release il cui punto è che il
gate di pre-registrazione **gira in CI** — abbiamo scoperto che il gate **non era obbligatorio**.
README, `METHOD.md` e la PR dicevano, al presente: *una PR che rivendica un risultato senza
pre-registrazione valida, anteriore e non modificata **non mergia***. La configurazione diceva
`required_status_checks.contexts = ["demo"]`: il job `firewall` girava su ogni PR, calcolava la
risposta giusta, stampava `exit 1` — e **nulla dipendeva da lui**. Una PR col gate rosso poteva essere
mergiata su `main` da chiunque. **Il nostro claim di testa era falso al livello delle impostazioni del
repository stesso.** E la dimostrazione di cui andavamo più fieri (`examples/blocked-pr/`) era falsa
allo stesso modo: avevamo scritto che il gate aveva **bloccato** quella PR — non l'aveva bloccata. Il
gate ha fallito, e poi **un umano ha chiuso la PR**. Non bloccata: **soltanto rossa.** La differenza è
l'intera tesi. **Come è emerso: per fortuna.** Non un test, non una review, non il dogfooding: il merge
della v0.3 si è inceppato per una ragione *diversa* (aver dato ai job un `name:` descrittivo aveva
sganciato in silenzio il contesto del check a cui la branch protection si riferiva), e leggendo le
regole di protezione per capire perché, la lista dei check obbligatori era lì, con una sola voce dentro.
Senza quel bug scorrelato, la v0.3 sarebbe passata pulita spedendo un gate che non imponeva niente, con
un README che diceva il contrario. **Perché nessun test poteva trovarlo:** il codice era giusto, i test
verdi, il gate girava in CI col verdetto corretto, il dogfooding passava. Ogni artefatto che sapevamo
controllare diceva la verità su sé stesso. Il fallimento viveva nell'**unico posto in cui nessuno di
essi guarda**: se a valle qualcuno stesse ascoltando. **Ed è la quarta volta**: Entry 0 = un agente ha
riportato una verifica mai avvenuta; Entry 1 = gli umani hanno rivendicato un rigore che il record non
sosteneva; Entry 2 = il gate stesso era sbagliato in quattro modi; Entry 3 = il gate era giusto, e
spento. Ogni volta la stessa forma — **un meccanismo che esiste e un'imposizione che non esiste** — e
ogni volta l'abbiamo trovata guardando altro. **Un gate da cui non dipende nulla non è un gate: è una
riga di log. Verifica l'IMPOSIZIONE, non il meccanismo.** Fatti la domanda che nessuno fa ai propri
guardrail: *cosa si rompe davvero se questo fallisce?* Se la risposta onesta è **"niente"**, non hai un
gate: hai una spunta verde e una frase falsa nel README. **Correzione:** `contexts` su `main` ora è
`["demo","tests","firewall"]`, **riletto dall'API** e non dedotto da un comando uscito 0; i contesti
sono gli **id** dei job, non i loro nomi descrittivi (un identificatore è un contratto, la prosa no); e
la dimostrazione è stata **rifatta** contro `main` con l'interruttore acceso — questa volta è **GitHub**
a rifiutare il merge (*"the base branch policy prohibits the merge"*), ed è la
[PR #6](https://github.com/alexcard3/honest-signal/pull/6). La pagina vecchia è corretta **in loco**,
con la correzione in cima invece dell'errore cancellato in silenzio.

**Coda — lo stesso pomeriggio il gate ha legato i propri autori, su una banalità, contro la loro
volontà.** Volevamo cambiare il formato del frontmatter (YAML richiede un parser di terze parti; la
stdlib di Python ne ha uno per TOML): una dipendenza in meno, un miglioramento cosmetico, deciso poche
ore dopo il commit di `P-TOOL-1`, con nessun esito noto a nessuno e nulla da guadagnare barando.
**Non abbiamo potuto.** Cambiare formato significa editare `P-TOOL-1.md`, ed editare una
pre-registrazione viola la regola (c) — la regola che avevamo appena scritto, nel tool che stavamo
costruendo, imposta dalla CI che stavamo per installare. L'unica strada che il nostro stesso metodo
consente è ritirarla in pubblico e ri-registrarla con un id nuovo: per una serializzazione, quel prezzo
non valeva. Quindi il file resta in YAML e il tool si porta una dipendenza di cui non aveva bisogno,
**perché il firewall ha detto no.** È una cosa piccola, e la teniamo proprio perché è piccola: **un
firewall che ti lega solo quando ti fa comodo non è un firewall.** Ci ha legati di martedì, su un
formato di file, quando non c'era nulla in gioco — che è l'unica prova disponibile del fatto che ci
legherà quando qualcosa in gioco ci sarà.
