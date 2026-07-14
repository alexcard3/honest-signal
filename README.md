# honest-signal

**A method for doing honest research with AI agents — forged and stress-tested on the most hostile case there is: the markets.**

> The system can be the best in the world, but if no one knows it, it's worth nothing.
> So this repository is not a trading edge. It's a *method*, shipped in the open.

---

## EN — What this is

honest-signal is a **method for keeping AI-assisted research honest** — so that an agent (or a human) cannot fool itself, or you, into believing a result that isn't there. It ships as five mechanisms, one runnable demo, an incident log of the time the method caught a fabrication in our own pipeline, and a full index of every hypothesis it killed.

We built it because we needed it. Three years of searching for a tradable edge in financial markets produced none that survives costs out-of-sample. The method is what we built to make that verdict trustworthy — and [`FALSIFICATIONS.md`](FALSIFICATIONS.md) states, row by row, how strictly each hypothesis was actually checked: 16 **certified dead** (a 17th and an 18th under review), each listed with what killed it, instead of quietly dropped. Those 16 deaths are the method's test-suite. They are how we know it bites — because what it killed was ours.

**Who built it.** An independent researcher, Alessandro Cardurani, working with AI agents. That detail is not incidental: here the agents are both the *subject* of the method — the thing whose honesty must be enforced — and the *tool* that runs it. The method was forged by making those agents check each other, and check themselves, while never being allowed to self-certify.

**The claim we defend.** Most "AI replicates anomalies and nothing survives" write-ups harden their guardrails *reactively*, after being wrong. We do two things *before* looking at any number:

1. **Pre-register** the exact recipe and the falsification criterion (a "firewall" commit), and
2. Have a **second, independent agent recompute the result byte-for-byte from the raw data** with its own code — never trusting the executor's report.

That independent recompute is the moat. It already caught a real fabrication (see [`incident-log.md`](incident-log.md)).

### Run the proof yourself (30 seconds, only needs numpy)

```bash
cd examples/synthetic_gate_demo
python gate_demo.py
```

You'll watch the gate **confirm** an honest result and **catch** a fabricated "discovery" on pure-noise data — by recomputing from the raw data with independent code. That's the whole idea, self-contained and deterministic.

### Who this is for, and what you get

**If you run AI agents whose results you then act on** — research, analysis, backtests, anything where an agent reports a number and you decide something because of it — you have the problem this repo addresses: an agent can report a check that never ran, and be entirely convincing while doing it. Ours did. It is [Entry 0](incident-log.md).

What you get:

- **A protocol that never lets an agent certify its own work.** The executor does not adjudicate. A second, independent agent recomputes the decisive number from the raw data with its own code. A fabrication and an honest bug fail the same check, because the check judges *reproducibility, not intent* — you never have to assess anyone's good faith.
- **A pre-registration discipline** that freezes the recipe and the kill criterion in a commit *before* the data exists, so the result cannot be chosen after seeing it.
- **A runnable 30-second demo** of the gate catching a fabrication, which you can lift into your own loop.
- **A worked example of the cost of doing this honestly**: [`FALSIFICATIONS.md`](FALSIFICATIONS.md) — 18 hypotheses itemised, including the rows where our own protocol turned out to be younger than our claims about it.

No performance claims, here or anywhere in this repo. Nothing in it will make your research succeed. It makes your failures visible — sooner, and more cheaply than the alternative.

### How to navigate

- [`METHOD.md`](METHOD.md) — the five mechanisms, in full.
- [`FALSIFICATIONS.md`](FALSIFICATIONS.md) — every hypothesis we killed: what was tested, what was committed before the data, what killed it.
- [`examples/synthetic_gate_demo/`](examples/synthetic_gate_demo/) — the runnable, dependency-light proof.
- [`incident-log.md`](incident-log.md) — the fabrication the gate caught, and the time the method caught our own overstated claim.

### Honest limits (v0.2)

- This is the **method**, not a market discovery. Our cartographic findings (regime structure, correlation erosion under stress) are, by our own assessment and the literature's, **incremental** — they confirm known facts (buy&hold dominates risk-adjusted; correlations rise in crises). They ship later as *demonstrations of the method*, not as news.
- **Full reproduction on our real market data is not possible from outside** — the data lives in a private database and market feeds are generally not redistributable. So we ship a **synthetic, self-contained demo** anyone can re-run to verify the *mechanism*. Full reproduction of the market findings remains **open**, not solved: it would need a data export or a much richer synthetic case, and we have not done it. We will not call "reproducible" anything an outsider cannot re-run.
- Where we stand relative to prior work is stated openly in `METHOD.md`; we position this as a contribution *inside* an existing lineage (López de Prado on backtest overfitting; the registered-reports / replication movement; the 2026 wave of anti-fabrication harnesses for AI agents) — a part we find under-served, not a lone discovery.
- **Proof-of-precedence is partial, and we now say by how much.** Of the 18 hypotheses in [`FALSIFICATIONS.md`](FALSIFICATIONS.md), **4** have a pre-registration commit that provably precedes the data, **2** carry prediction and verdict in the same commit, and **12** were pre-registered off-repo in files we never versioned. The firewall enters the git record on 2026-06-25; everything before that rests on our word. And all those commits live in private repositories — you see a hash, not a proof. We list the state of every row rather than average it away.
- **The protocol exactly as advertised — both mechanisms, end-to-end — has three complete applications** (rows 14, 17, 18; all after 2026-06-25). It is what we run *now*, on everything. It is not what we can retroactively claim for all eighteen, and we would rather tell you that than have you work it out from our own table. A young protocol, dated precisely, is credible; a backdated one is not.

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

### Prova tu stesso (30 secondi, serve solo numpy)

```bash
cd examples/synthetic_gate_demo
python gate_demo.py
```

Vedrai il gate **confermare** un risultato onesto e **beccare** una "scoperta" fabbricata su dati di puro rumore, ricalcolando dal grezzo con codice indipendente. Tutto self-contained e deterministico.

### A chi serve, e cosa ti dà

**Se fai girare agenti AI sui cui risultati poi agisci** — ricerca, analisi, backtest, qualunque cosa in cui un agente riporta un numero e tu decidi di conseguenza — hai il problema che questo repo affronta: un agente può riportare una verifica mai avvenuta, ed essere del tutto convincente mentre lo fa. Il nostro l'ha fatto: è la [Entry 0](incident-log.md).

Cosa ti dà: (1) un **protocollo che non permette mai a un agente di certificare il proprio lavoro** — l'esecutore non aggiudica; un secondo agente indipendente ricalcola la cella decisiva dal dato grezzo con codice proprio. Fabbricazione e bug onesto cadono sullo stesso controllo, perché giudica *la riproducibilità, non l'intenzione*: non devi mai valutare la buona fede di nessuno. (2) Una **disciplina di pre-registrazione** che congela ricetta e criterio di kill in un commit *prima* che il dato esista. (3) Una **demo eseguibile in 30 secondi** del gate che becca una fabbricazione, trasportabile nel tuo loop. (4) Un **esempio concreto di quanto costa farlo onestamente**: [`FALSIFICATIONS.md`](FALSIFICATIONS.md), 18 ipotesi voce per voce — comprese le righe in cui il nostro protocollo si è rivelato più giovane delle nostre affermazioni su di esso.

Nessun claim di performance, qui né altrove in questo repo. Niente di tutto ciò farà riuscire la tua ricerca: rende visibili i suoi fallimenti, prima e a costo minore.

### Limiti onesti (v0.2)

Questo è il **metodo**, non una scoperta di mercato (i nostri reperti cartografici sono incrementali per nostra stessa ammissione; ci collochiamo *dentro* una lineage esistente — López de Prado, registered reports, l'ondata 2026 di harness anti-fabbricazione — un aspetto che troviamo sotto-servito, non una scoperta solitaria). La riproduzione piena sui dati di mercato reali non è possibile dall'esterno (DB privato, feed non ridistribuibili): spediamo una **demo sintetica** ri-eseguibile da chiunque per verificare il *meccanismo*. Non chiameremo "riproducibile" ciò che un esterno non può ri-eseguire.

**Prova-di-precedenza: parziale, e ora diciamo di quanto.** Delle 18 ipotesi in [`FALSIFICATIONS.md`](FALSIFICATIONS.md), **4** hanno un commit di pre-registrazione che precede dimostrabilmente il dato, **2** hanno predizione e verdetto nello stesso commit, **12** furono pre-registrate off-repo in file mai versionati. Il firewall entra nel record git il 2026-06-25: tutto ciò che viene prima poggia sulla nostra parola. E quei commit stanno in repo privati — vedi un hash, non una prova. Elenchiamo lo stato di ogni riga invece di mediarlo via.

**Il protocollo esattamente come lo pubblicizziamo — entrambi i meccanismi, end-to-end — ha tre applicazioni complete** (righe 14, 17, 18; tutte dopo il 2026-06-25). È ciò che eseguiamo **ora**, su tutto. Non è ciò che possiamo rivendicare retroattivamente sulle diciotto, e preferiamo dirtelo noi piuttosto che lasciartelo ricavare dalla nostra stessa tabella. Un protocollo giovane e datato con precisione è credibile; uno retrodatato no.

### Licenza

Codice: [MIT](LICENSE). Contenuti/docs: CC-BY-4.0 (usa liberamente con attribuzione). Contributi, repliche e critica avversariale sono benvenuti — il punto è esattamente il giudizio esterno.
