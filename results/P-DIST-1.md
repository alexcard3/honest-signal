# P-DIST-1 — VOID

## EN

**Verdict: VOID. The push was not performed. This is not a reprieve.**

Adjudicated 2026-08-23, sixteen days before the verification date, because the precondition
was time-bound at 2026-08-11 and is already decidable. We are not waiting for 2026-09-08 to
say something we can say now.

### The precondition, and what actually happened

P-prime required three act-classes, each evidenced by a URL or a sent-record, all by 2026-08-11:

| Act | Required | Performed |
|---|---|---|
| Five individually-written emails to the named recipients | yes | **yes** — sent 2026-07-15 |
| One share in the US-RSE Slack #general | yes | **no** |
| One public post (Show HN, an awesome-list PR, a Marketplace listing) | yes | **no** |

The pre-registration says: *"Silence, or only a subset, is not the push."* We performed a subset:
one act-class out of three.

### How to re-check this

- Slack workspace search, `from:@alexcard33`, whole workspace, paid plan with full history:
  **no results**. The membership is real (joined 2026-07-15); the message was never written.
- `gh api users/alexcard3/events/public` — no pull request to any repository other than this
  one, and no external submission, between registration and 2026-08-23. Retention is 90 days;
  the window is covered.
- No Marketplace listing, no awesome-list entry.
- Sent-mail record: five emails, five recipients, 2026-07-15.

### The escape hatch we are refusing

This repository's About description and its nine topics are public, indexed, and have URLs a
third party can point to. They were set on 2026-07-09. It would be easy to call that "one
public post" and mark the precondition satisfied.

We are not doing that, and the reason is in P-DIST-1 itself: the file exists because *"a single
low-effort post would let us say we distributed"*. Repository metadata is not a distribution
act. A gate you route around is not a gate — the same finding, in the same repository, as the
v0.3 release tagged *the release that shipped a gate that enforced nothing*.

### When the gap opened, precisely

The record should be accurate about this, and it is not flattering in the way an excuse would be.

The author was demonstrably at the machine and working through 2026-07-22: thirteen emails sent
on 07-17, six follow-up drafts written 07-22 06:13, two replies sent 07-22 17:49. The scheduled
public acts fell inside that same week — an awesome-list PR on 07-20, a Marketplace listing on
07-21, a Show HN on 07-23 — and did not happen while other work in the same inbox did.

From 2026-07-23 to 2026-08-11 the author was away with no access to the machine. That period is
genuinely explained. **The first week is not.** "Prevented" and "not prioritised" are different
diagnoses and only the second one repeats. We record the second.

A design fault worth naming, because it is correctable: the deadline was set inside a month the
author already knew he would be away, and every act in the lane depended on one machine.

#### Correction, 2026-08-23 — same day, before any external reader

**The paragraph above is wrong.** It is left standing, unedited, so the correction can be read
against it.

Checked at source afterwards: on **2026-08-05**, inside the window, the author worked from
**11:43 to 17:35** in the MetaNet repositories — four pull requests merged, pushes, CI runs — and
again on 2026-08-06. He was on a laptop; the main machine was indeed unavailable. That detail
does not rescue the claim. Connectivity and the ability to perform public online acts existed
**six days before the deadline**: a Show HN post or an awesome-list pull request needs a browser,
not that machine.

The correct diagnosis is therefore **wider** than the one written above — not prioritised, over
more of the window than we first said. One machine being unreachable explains the absence of
some work; it does not explain the absence of the acts.

How the error got in, since that is the part worth keeping: it was written from a verbal account
and never checked against the commit record of a **second git identity**
(`alexcard33@hotmail.com`), which the checks that were run — mail, and the public events of
`alexcard3` — do not cover. **The gate did not catch this**, and could not: nothing in it reads
other repositories. It was caught by routine work forty minutes after the merge. A gate bounds
what it was built to bound, and the space outside those bounds is not smaller for having a gate
inside them.

### Consequence

Per `outcome_if_void`: **the lane is de-prioritised anyway.** A VOID records that we built
instead of shipping — the more embarrassing finding about this lane, not a lesser one. We do not
extend the window and we do not re-run the push to convert a VOID into a NO.

The M1/M3 reading will still be taken on 2026-09-08 and published, labelled for what a zero
would then measure: **our silence, not the audience's indifference.** It counts for nothing.

The repository stays public. De-prioritising a lane is not deleting the artifact: the method,
the falsifications and this file remain readable by anyone who finds them. What ends is the
effort to make them found.

## IT

**Verdetto: VOID. La spinta non è stata eseguita. Non è una grazia.**

Aggiudicato il 2026-08-23, sedici giorni prima della data di verifica, perché la precondizione
scadeva il 2026-08-11 ed è già decidibile. Non aspettiamo il 2026-09-08 per dire una cosa che
possiamo dire adesso.

### La precondizione, e cosa è successo davvero

P′ richiedeva tre classi di atto, ciascuna evidenziabile con un URL o una ricevuta di invio,
tutte entro il 2026-08-11:

| Atto | Richiesto | Eseguito |
|---|---|---|
| Cinque email scritte singolarmente ai destinatari nominati | sì | **sì** — inviate il 2026-07-15 |
| Un messaggio in US-RSE Slack #general | sì | **no** |
| Un post pubblico (Show HN, PR a awesome-list, listing Marketplace) | sì | **no** |

La pre-registrazione dice: *"Il silenzio, o solo un sottoinsieme, non è la spinta."* Abbiamo
eseguito un sottoinsieme: una classe di atto su tre.

### Come ricontrollarlo

- Ricerca nel workspace Slack, `from:@alexcard33`, intero workspace, piano a pagamento con
  cronologia completa: **nessun risultato**. L'iscrizione è reale (15-07-2026); il messaggio non
  è mai stato scritto.
- `gh api users/alexcard3/events/public` — nessuna pull request verso repository diversi da
  questo, nessuna submission esterna, tra la registrazione e il 2026-08-23. Retention 90 giorni:
  la finestra è coperta.
- Nessun listing Marketplace, nessuna voce awesome-list.
- Registro invii: cinque email, cinque destinatari, 2026-07-15.

### La scappatoia che rifiutiamo

La descrizione About di questo repository e i suoi nove topics sono pubblici, indicizzati e
hanno URL indicabili da terzi. Furono impostati il 2026-07-09. Sarebbe facile chiamarli "un post
pubblico" e dare la precondizione per soddisfatta.

Non lo facciamo, e la ragione è dentro P-DIST-1: quel file esiste perché *"un singolo post a
basso sforzo ci permetterebbe di dire che abbiamo distribuito"*. I metadati del repo non sono un
atto di distribuzione. Un gate che si aggira non è un gate — lo stesso reperto, nello stesso
repository, della release v0.3 taggata *la release che ha spedito un gate che non imponeva niente*.

### Quando si è aperto il buco, con precisione

Il record dev'essere esatto su questo, e non è lusinghiero come sarebbe una scusa.

L'autore era dimostrabilmente alla macchina e al lavoro fino al 2026-07-22: tredici email
inviate il 17-07, sei bozze di follow-up scritte il 22-07 alle 06:13, due risposte inviate il
22-07 alle 17:49. Gli atti pubblici in calendario cadevano nella stessa settimana — PR
awesome-list il 20-07, listing Marketplace il 21-07, Show HN il 23-07 — e non sono avvenuti,
mentre nella stessa casella si faceva altro lavoro.

Dal 2026-07-23 al 2026-08-11 l'autore era via, senza accesso alla macchina. Quel periodo è
spiegato davvero. **La prima settimana no.** "Impedito" e "non prioritizzato" sono diagnosi
diverse, e solo la seconda si ripete. Registriamo la seconda.

Un difetto di disegno che vale la pena nominare, perché è correggibile: la scadenza è stata
fissata dentro un mese in cui l'autore sapeva già che sarebbe stato via, e ogni atto della lane
dipendeva da una sola macchina.

#### Correzione, 2026-08-23 — stesso giorno, prima di qualunque lettore esterno

**Il paragrafo qui sopra è sbagliato.** Resta in piedi, non modificato, perché la correzione si
possa leggere contro di lui.

Verificato dopo, alla fonte: il **2026-08-05**, dentro la finestra, l'autore ha lavorato dalle
**11:43 alle 17:35** nei repository MetaNet — quattro pull request mergiate, push, run di CI — e
di nuovo il 2026-08-06. Era su un portatile; la macchina principale era davvero irraggiungibile.
Quel dettaglio non salva l'affermazione. Connettività e capacità di compiere atti pubblici online
c'erano **sei giorni prima della scadenza**: un post su Show HN o una pull request a una
awesome-list richiedono un browser, non quella macchina.

La diagnosi corretta è quindi **più ampia** di quella scritta sopra — non prioritizzato, su una
porzione maggiore della finestra di quanto avessimo detto. Una macchina irraggiungibile spiega
l'assenza di parte del lavoro; non spiega l'assenza degli atti.

Come si è infilato l'errore, che è la parte che vale la pena conservare: è stato scritto da un
racconto verbale e mai verificato contro il registro dei commit di una **seconda identità git**
(`alexcard33@hotmail.com`), che i controlli eseguiti — la posta, e gli eventi pubblici di
`alexcard3` — non coprono. **Il gate non l'ha catturato**, e non poteva: niente in lui legge
altri repository. L'ha catturato il lavoro ordinario quaranta minuti dopo il merge. Un gate
delimita ciò per cui è stato costruito, e lo spazio fuori da quei confini non è più piccolo per
il fatto che dentro ci sia un gate.

### Conseguenza

Come da `outcome_if_void`: **la lane si de-prioritizza comunque.** Un VOID registra che abbiamo
costruito invece di spedire — il reperto più imbarazzante su questa lane, non uno minore. Non
allunghiamo la finestra e non rieseguiamo la spinta per convertire un VOID in un NO.

La lettura M1/M3 verrà comunque presa il 2026-09-08 e pubblicata, etichettata per ciò che uno
zero misurerebbe a quel punto: **il nostro silenzio, non l'indifferenza del pubblico.** Non conta
nulla.

Il repository resta pubblico. De-prioritizzare una lane non è cancellare l'artefatto: il metodo,
le falsificazioni e questo file restano leggibili da chiunque li trovi. Finisce lo sforzo per
farli trovare.
