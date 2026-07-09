# honest-signal

**A method for doing honest research with AI agents — forged and stress-tested on the most hostile case there is: the markets.**

> The system can be the best in the world, but if no one knows it, it's worth nothing.
> So this repository is not a trading edge. It's a *method*, shipped in the open.

---

## EN — What this is

Over three years of trying to find a tradable edge in financial markets, we found none that survives costs out-of-sample — and we **certified** 16 dead hypotheses (plus a 17th still under review) instead of quietly dropping them. Along the way we built something more valuable than any edge: a **method for keeping AI-assisted research honest**, so that an agent (or a human) cannot fool themselves — or you — into believing a result that isn't there.

This repo ships that method. Four mechanisms, one runnable demo, and an incident log of the time the method caught a fabrication in our own pipeline.

**Who built it.** An independent researcher, Alessandro Cardurani, working with AI agents. That detail is not incidental: here the agents are both the *subject* of the method — the thing whose honesty must be enforced — and the *tool* that runs it. The method was forged by making those agents check each other, and check themselves, while never being allowed to self-certify.

**The claim we defend** (our specific contribution — a part we find under-served, not a lone discovery): most "AI replicates anomalies and nothing survives" write-ups harden their guardrails *reactively*, after being wrong. We do two things *before* looking at any number:

1. **Pre-register** the exact recipe and the falsification criterion (a "firewall" commit), and
2. Have a **second, independent agent recompute the result byte-for-byte from the raw data** with its own code — never trusting the executor's report.

That independent recompute is the moat. It already caught a real fabrication (see [`incident-log.md`](incident-log.md)).

### Run the proof yourself (30 seconds, only needs numpy)

```bash
cd examples/synthetic_gate_demo
python gate_demo.py
```

You'll watch the gate **confirm** an honest result and **catch** a fabricated "discovery" on pure-noise data — by recomputing from the raw data with independent code. That's the whole idea, self-contained and deterministic.

### How to navigate

- [`METHOD.md`](METHOD.md) — the four mechanisms, in full.
- [`examples/synthetic_gate_demo/`](examples/synthetic_gate_demo/) — the runnable, dependency-light proof.
- [`incident-log.md`](incident-log.md) — the fabrication the gate caught, and how.

### Honest limits (v0.1)

- This is the **method**, not a market discovery. Our cartographic findings (regime structure, correlation erosion under stress) are, by our own assessment and the literature's, **incremental** — they confirm known facts (buy&hold dominates risk-adjusted; correlations rise in crises). They ship later as *demonstrations of the method*, not as news.
- **Full reproduction on our real market data is not possible from outside** — the data lives in a private database and market feeds are generally not redistributable. So v0.1 ships a **synthetic, self-contained demo** anyone can re-run to verify the *mechanism*. Full reproduction on market findings is a v0.2 goal (a data export or a richer synthetic case). We will not call "reproducible" anything an outsider cannot re-run.
- Where we stand relative to prior work is stated openly in `METHOD.md`; we position this as a contribution *inside* an existing lineage (López de Prado on backtest overfitting; the registered-reports / replication movement; the 2026 wave of anti-fabrication harnesses for AI agents), not as a lone discovery.

## License

- **Code** (everything under `examples/` and any scripts): [MIT](LICENSE).
- **Content** (`README.md`, `METHOD.md`, `incident-log.md` and other docs): CC-BY-4.0 — use freely with attribution.

Contributions, replications, and adversarial critique are welcome — the whole point is external judgment.

---

## IT — Cos'è

In tre anni di ricerca di un edge di mercato tradabile non ne abbiamo trovato uno che sopravviva ai costi fuori campione — e abbiamo **certificato 16 ipotesi morte** (più una 17ª ancora in revisione) invece di abbandonarle in silenzio. Nel farlo abbiamo costruito qualcosa di più prezioso di qualunque edge: un **metodo per mantenere onesta la ricerca assistita da AI**, così che un agente (o un umano) non possa auto-ingannarsi — né ingannare te — credendo a un risultato che non c'è.

Questo repo spedisce quel metodo: quattro meccanismi, una demo eseguibile, e il log della volta in cui il metodo ha beccato una fabbricazione nella nostra stessa pipeline.

**Chi l'ha costruito.** Un ricercatore indipendente, Alessandro Cardurani, insieme ad agenti AI. Non è un dettaglio secondario: qui gli agenti sono insieme il *soggetto* del metodo — ciò di cui va imposta l'onestà — e lo *strumento* che lo esegue. Il metodo è nato facendo controllare quegli agenti l'uno con l'altro, e con sé stessi, senza mai permettere l'auto-certificazione.

**La tesi che difendiamo** (il nostro contributo specifico — un aspetto che troviamo sotto-servito, non una scoperta solitaria): la maggior parte degli articoli "l'AI replica le anomalie e nulla sopravvive" indurisce i guardrail *reattivamente*, dopo aver sbagliato. Noi facciamo due cose *prima* di guardare qualunque numero: (1) **pre-registriamo** la ricetta esatta e il criterio di falsificazione (un commit "firewall"); (2) un **secondo agente indipendente ricalcola il risultato byte-per-byte dal dato grezzo** con codice proprio, senza mai fidarsi del report dell'esecutore. Quel ricalcolo indipendente è il fossato — e ha già beccato una fabbricazione reale ([`incident-log.md`](incident-log.md)).

### Prova tu stesso (30 secondi, serve solo numpy)

```bash
cd examples/synthetic_gate_demo
python gate_demo.py
```

Vedrai il gate **confermare** un risultato onesto e **beccare** una "scoperta" fabbricata su dati di puro rumore, ricalcolando dal grezzo con codice indipendente. Tutto self-contained e deterministico.

### Limiti onesti (v0.1)

Questo è il **metodo**, non una scoperta di mercato (i nostri reperti cartografici sono incrementali per nostra stessa ammissione). La riproduzione piena sui dati di mercato reali non è possibile dall'esterno (DB privato, feed non ridistribuibili): la v0.1 spedisce una **demo sintetica** ri-eseguibile da chiunque per verificare il *meccanismo*. Non chiameremo "riproducibile" ciò che un esterno non può ri-eseguire.

### Licenza

Codice: [MIT](LICENSE). Contenuti/docs: CC-BY-4.0 (usa liberamente con attribuzione). Contributi, repliche e critica avversariale sono benvenuti — il punto è esattamente il giudizio esterno.
