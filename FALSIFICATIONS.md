# FALSIFICATIONS — every hypothesis the method killed

**16 certified dead, plus a 17th and an 18th under review.** Until now that was a number we
asserted. This file is the number, itemised: what was tested, what was committed *before* the
data, who checked it, and what killed it.

## Why the commit hashes matter — and where they stop mattering

A pre-registration is only worth something if it provably came **first**. A commit that contains
the prediction, made before the data exists, is that proof: git timestamps it, and a later commit
carrying the verdict cannot retroactively rewrite it. That is the "firewall" in mechanism #1 of
[`METHOD.md`](METHOD.md).

Two honest limits, stated up front rather than buried:

1. **The commits live in private repositories** (our research monorepo and mission-control). You
   can see a hash here; you cannot verify it from outside. We will not call "verifiable" something
   an outsider cannot check. Treat the hashes as an internal audit trail we are exposing, not as
   proof we can hand you.
2. **The firewall only enters the git record on 2026-06-25.** Everything before that date was
   pre-registered *off-repo*, in mandate and design files we never versioned. The discipline was
   real — bars were frozen before runs — but the **precedence is not provable**, and we will not
   backdate it into an implied rigour we did not have.

Of the 18 hypotheses below: **4** have a firewall commit that provably precedes the data, **2**
carry prediction and verdict in the same commit, **12** have no commit at all. That ratio is the
uncomfortable fact this index exists to expose. See *Honest limits of this index*, below.

## How to read the "Pre-registration" column

| State | Meaning |
|---|---|
| `firewall <hash>` | A commit containing the prediction and the kill criterion, **made before the data**. Precedence provable (internally). |
| `same commit as verdict` | Prediction and outcome landed together. The pre-registration may well have existed off-repo first — but **the git record cannot prove it**. |
| `off-repo` | Pre-registered in an unversioned mandate/design file. **No commit exists.** Our word, nothing more. |

## The index

Repositories: `mc` = mission-control, `apps` = research monorepo. Both private.

| # | Hypothesis | What was tested | Pre-registration | Independent check | Adjudication | Verdict — why it died |
|---|---|---|---|---|---|---|
| 1 | AutoCM clustering (1st species) | Does an auto-associative net see market structure that Pearson does not? | `off-repo` | n/a | n/a — no committed run artifact | **NO** — ARI ≈ 0 vs Pearson 0.51. No structure beyond baseline. *(G0)* |
| 2 | Lead-lag intra-crypto | Is there a rideable propagation wave between major crypto? | `off-repo` | n/a | n/a — no committed run artifact | **NO** — BTC→ETH corr 0.689 @0m collapses to 0.004 @5m. The lead is sub-bar; it is arbitraged inside the candle. *(G0 — latency)* |
| 3 | Shock-response cross-class | Do cross-class shocks propagate tradeably (crypto shock → MSTR/COIN)? | `off-repo` | Determinism (seed 42) | apps `0dc0cbb` | **NO** — realizable gross 0.5–2.5 bps « 10; net −17/−20 bps. The edge lives in the bar you cannot trade. *(G0 — latency; G2 borderline)* |
| 4 | Momentum walk-forward | Does slow trend-following survive out-of-sample? | `off-repo` | Determinism (seed 42, BLAS pinned); byte-identical re-run | apps `0dc0cbb` | **NO** — 7/10 folds negative Sharpe **even at zero cost**; 90% of the return came from one quarter. *(G0 — decay)* |
| 5 | Signal-horizon | Does the bots' slow gross skill clear the cost wall? | `off-repo` | Determinism; byte-identical re-run | apps `0dc0cbb` | **NO** — gross 16–45 bps « 72 bps round-trip. A real slow signal, killed by the wall. *(G2 — cost)* |
| 6 | Dispersion-regime | Does cross-sectional momentum pay more when dispersion is high? | `off-repo` | Determinism (seed 42, BLAS pinned) | apps `609821a` | **NO — hypothesis inverted.** XS_LS in HIGH dispersion −96 bps vs LOW −40. It does *worse*. *(G0)* |
| 7 | Long-only unconditional | Does top-k momentum selection beat simply holding BTC? | `off-repo` | Determinism (seed 42, BLAS pinned) | apps `609821a` | **NO** — 0/18 configs beat BTC risk-adjusted; 100% of the compounded return came from the 2023-24 bull. *(G0 — beta in disguise)* |
| 8 | Arc-closer (crypto) | Synthesis across the arc: does anything beat buy & hold? | `off-repo` | n/a — synthesis of the rows above | n/a | **NO** — 9/9 patterns: nothing beats B&H risk-adjusted. Whoever wins on return pays for it in drawdown. *(G0 — beta)* |
| 9 | Raw equity momentum | Does the same edge clear the wall on equity, where costs are ~7× lower? | `off-repo` | Determinism; output SHA-256 `1d7e6c50…` | apps `609821a` | **NO** — 59/144 holdout survivors, but **0 beat SPY risk-adjusted**; the true market-neutral form is dead. *(G0 — beta)* |
| 10 | Defense overlay | If we cannot pick, can we defend? (drawdown control beats B&H) | `off-repo` | Determinism; output SHA-256 `2c2f35b8…` | apps `609821a` | **NO** — cuts drawdown but gives up 37% of the upside; beats vol-targeting, not buy & hold. *(G0 — insufficient)* |
| 11 | Regime-axis | Is bot skill conditional on market state, exploitably? | `off-repo` | Determinism (seed 42) | apps `2d3d2eb` | **NO** — 0 GO / 8 cells. The shuffled control retains the performance → it was long-bias, not regime information. *(G0)* |
| 12 | Gap-test weekend | Does crypto trading while equity sleeps predict the equity gap? | `off-repo` | Determinism (no RNG); SHA-256 dumps | apps `3832bd8` | **NO** — pass-through is enormous (r = 0.52) but **already priced at the open**; intraday OOS +0.4…+7.1 bps « the 10 bps bar. *(G0 — already priced)* |
| 13 | L2 reversal@1d (`P-FASE2-1` / `P-VAL-1`) | Is our best bot's reversal signal alpha, or downside-beta? | ⚠ `same commit as verdict` (mc `6f10173`) — *pre-epoch* | Determinism; walk-forward 5-fold + PBO (CSCV) | mc `6f10173` | **NO** — +44%/+192% at 0 bps → **−100% net at 72 bps** (turnover × cost); the low-turnover escapees then showed 0/9 significant OOS alpha. *(G2 — cost)* |

> **—— Protocol epoch: 2026-06-25 (`fe78196`) ——**
> From this commit the pre-registration firewall enters the git record. Above the line: pre-registered
> off-repo, precedence **not provable**. Below: provable. This is a dated maturation, not an excuse —
> and row 16 sits *below* the line without a firewall, which no epoch explains. See below.

| # | Hypothesis | What was tested | Pre-registration | Independent check | Adjudication | Verdict — why it died |
|---|---|---|---|---|---|---|
| 14 | `P-WPROBE-1` | Temporal W(t) probe: is there a tradeable lead-lag in the coupling structure? | ✅ `firewall` mc `fe78196` | **Companion gate** — second agent recomputed independently from the raw DB | mc `8dc72a3` / apps `5dedc54` | **NO** — R² to direction 0.024; net Sharpe −211…−653; **86/86 pairs peak at lag 0** → common factor, not propagation. *(G0)* |
| 15 | `P-CARRY-1` | Carry/premium sleeve + W(t) tail control: is the premium harvestable? | ✅ `firewall` mc `c3f4cee` | Determinism (no second-agent recompute) | mc `9307c84` / apps `4d6236a` | **NO GO** — +0.89%/yr, genuinely positive, **but Sharpe 0.15 « SPY 1.02**. A real rent, dominated by doing nothing. *(G0 — does not beat B&H)* |
| 16 | `P-CARRY-2` — **the 16th, the one that closes the counter** | Same thesis, re-tested on genuine crashes (2018 / 2020 / 2022) once the data existed | ⚠ **`same commit as verdict`** (mc `635bf18`, 2026-06-29) — **four days *after* the epoch** | Companion cross-check of the raw crash windows (pre-run) + byte-identical re-run | mc `635bf18` / apps `e143a4a` | **NO GO** — tail CVaR improves by **+2.46% rel** vs the +15% bar; bootstrap CI straddles 0. *(G0 — dominated)* |
| 17 | `P-SHOCK-1` — *candidate 17th, under review* | Fade of sharp shocks + point-in-time breadth classifier | ✅ `firewall` mc `cbdebd6` | **Companion gate** — and **this is the run where the executor fabricated the gate section**. See [`incident-log.md`](incident-log.md), Entry 0. The real gate was then run independently; it confirmed the hypothesis was dead. | mc `1c73543` / apps `2416fa4` (the report that carried the fabricated section; corrected later) | **NO** — net ≈ +8 bps « the 57 bps wall; and **13 of 14 apparent survivors were bad prints** (a flat 45400 BTC bar reads as a +40% move). *(G1 + G2)* |
| 18 | `P-CTSM-1` — *candidate 18th, under review* | Weekly crypto time-series momentum (the last momentum corridor) | ✅ `firewall` mc `2b1a5f7` | **Companion gate** — second agent recomputed the decisive cell from the raw data | mc `4558fd3` / apps `c7c8436` | **NO** — gross BTC +100% is **real**, and it still dies: Sharpe 0.547 < 0.627 buy & hold, and net-net ≈ 0% vs B&H +33% after costs **and 33% crypto tax**. *(G2 + G3)* |

The 17th and 18th are marked **under review**: they are adjudicated internally but not yet ratified,
and we do not move the counter until they are. It stays at **16**.

### The number you would otherwise have to compute yourself

[`METHOD.md`](METHOD.md) claims two mechanisms applied **together**, *before* any number is computed:
pre-registration (#1) **and** an independent byte-exact recompute by a second agent (#2). Cross the two
columns above and you get the honest count:

> **Firewall commit:** rows 14, 15, 17, 18. **Companion gate:** rows 14, 16, 17, 18.
> **Both, end-to-end — the protocol exactly as we advertise it: rows 14, 17, 18 → 3 of 18.**
> All three are after 2026-06-25.

So: **the protocol as published has three complete end-to-end applications.** It is what we run *now*,
on everything; it is not what we can retroactively claim for the eighteen. We would rather hand you
that number than have you derive it from our own table and conclude we were hiding it. A young
protocol, dated precisely, is credible. A backdated one is not.

### Why some firewalls are minutes old, and what a commit can actually prove

Three of the four firewalled rows were pre-registered and adjudicated **on the same day**:

| Row | Firewall | Adjudication | Gap |
|---|---|---|---|
| 14 `P-WPROBE-1` | 2026-06-25 00:51 | 2026-06-25 01:52 | 61 min |
| 15 `P-CARRY-1` | 2026-06-25 08:46 | 2026-06-25 09:09 | **23 min** |
| 17 `P-SHOCK-1` | 2026-06-29 21:45 | 2026-06-29 22:56 | 71 min |
| 18 `P-CTSM-1` | 2026-07-07 | 2026-07-13 | 6 days |

Twenty-three minutes is the number a sceptic will find, so here it is from us. **Precedence rests on
commit order, not on the calendar date**: git orders the two commits, and the probes are scripted runs
over an existing harness and already-loaded data — writing the recipe takes longer than executing it.

But we should be exact about what that buys, because it is less than it looks:

> A firewall commit proves the prediction and the kill criterion **could not be edited after the outcome
> was known**. It does **not** prove that nobody had already glanced at the data before writing the
> firewall. **No commit can prove that.** It is a guard against retrofitting, not a guarantee of
> blindness.

The mechanism that does *not* depend on our restraint is the other one — the independent recompute
(#2) — because it does not care what the executor knew, saw, or intended. That is why we treat the
companion gate, not the firewall, as the moat.

### A note on this file's format

The table is **English only**, and the Italian section below is a summary rather than a second table.
This is a methodological choice, not a shortcut: the table is the *evidence*, and duplicated evidence
is evidence that can diverge. Two tables would become two truths the first time someone edits one and
forgets the other — in a repository whose only asset is that its numbers can be trusted, that is a risk
with no upside. The facts that matter, including every uncomfortable one, are in the Italian summary.

## Honest limits of this index

- **Proof-of-precedence is 4 out of 18.** Rows 14, 15, 17, 18 have a firewall commit that provably
  precedes the data. Rows 13 and 16 carry prediction and verdict in one commit. Rows 1–12 have no
  commit at all. We are publishing the ratio rather than the average.
- **Row 16 is the uncomfortable one, and it is the one that closes the counter.** The 16th
  falsification — the one that takes the number to 16 — was committed on 2026-06-29, **four days
  after the firewall protocol was already in the git record**, with prediction and verdict in the
  same commit. Its immediate predecessor in the same family, `P-CARRY-1` (row 15, 2026-06-25),
  *has* a proper firewall commit; the re-run does not. The likely cause is benign — the design and
  the kill criterion for the re-run were frozen in an off-repo mandate file, and the section was
  transcribed into the record afterwards. We think that is what happened. **But we cannot prove
  it, and the epistemic fact does not care what we think:** our headline number rests on a row whose
  precedence is not demonstrable, registered after we already knew how to demonstrate it. That is
  the most inconvenient sentence in this repository, which is exactly why it is not in a footnote.
- **"Byte-exact reproduction" does not apply to all 16.** The independent second-agent recompute
  became protocol partway through. The earlier kills were checked with determinism (pinned seeds and
  BLAS, byte-identical re-runs, published output hashes) — good practice, but not a second pair of
  eyes. The `Independent check` column says which is which, row by row. We corrected the claim in
  [`METHOD.md`](METHOD.md) that said otherwise; see [`incident-log.md`](incident-log.md), Entry 1.
- **The full protocol — both mechanisms, end-to-end — has been applied to 3 of the 18.** Rows 14, 17
  and 18, all after 2026-06-25. That is the true age of the thing we are publishing. We state it here
  rather than let you infer it from the table.
- **The underlying data is not redistributable.** Market data lives in a private database under feed
  terms that forbid redistribution. You cannot re-run these studies from this repo. What you *can*
  re-run is the mechanism: [`examples/synthetic_gate_demo/`](examples/synthetic_gate_demo/).

## What actually killed them — the G0–G3 scale

Every death above is tagged with the **first gate it failed**. The gates are ordered, and a death at
a wall only counts if the hypothesis had a real gross edge to begin with — i.e. if it cleared G0.

- **G0 — Does the edge exist at all?** Is there a real *gross* edge (positive before costs, alpha and
  not beta, stable out-of-sample, actionable at your latency)? A death here is **not a wall**: it is
  the absence of raw material.
- **G1 — The bad-print wall.** Is the gross edge real, or an artifact of the feed (single-bar glitches)?
- **G2 — The cost wall.** Does the real gross edge survive net costs (~57–93 bps round-trip crypto,
  ~10–20 bps equity; magnitude = per-trade cost × turnover)?
- **G3 — The tax wall.** Does the net-of-cost result survive tax (33% on crypto realisations, stamp
  duty, basket mismatch)?

**This scale was itself firewalled — and that matters here more than anywhere.** A sceptic reading the
definition of G0 will notice that it is broad (it absorbs beta-in-disguise, out-of-sample decay, and
edges that live inside an untradeable bar) and will reasonably ask whether we defined the gates *after*
counting, in the shape that flattered our thesis. We did not, and it is checkable in the same way
everything else here is:

| | Commit | |
|---|---|---|
| **Firewall** (gate definitions + the predictions, **before** the tabulation) | mission-control `2b72e3e` | 2026-07-13 16:42 |
| **Delivered** (the count) | mission-control `b2c5355` | 2026-07-13 16:52 |

The firewall commit is an ancestor of the delivery commit; the same caveat as above applies (precedence
rests on commit order, and no commit can prove nobody peeked). And the prediction that was frozen in
`2b72e3e` **was an argument against ourselves**: our own comfortable framing was *"the walls killed us"*,
and the pre-registered prediction said the opposite — that the walls would turn out to be a **minority**,
and the dominant killer would be upstream. Four of four pre-committed predictions held, that one included.
**We bet against our own story and lost the bet.**

Note what that means for the weakest part of this document. This file's exposed flank is *"only 4
firewalls out of 18"* — and the taxonomy you are reading right now is a **properly firewalled result**.
It is counter-neutral (a method deliverable, not an edge claim), which is why it is not a nineteenth row
in the table above. But it is the part of this index that was produced under the full protocol.

**The finding, and it is not the one we expected.** We had framed our own defeats as *"the walls got
us — costs, tax, bad prints"*. We pre-registered the opposite prediction and tabulated it. The
opposite held:

> **G0 ≈ 13–14 of 18.** Pure cost-wall deaths: **2** (rows 5, 13). Bad-print + cost: **1** (row 17).
> Cost + tax: **1** (row 18).

**The dominant killer is not the walls — it is the absence of an edge.** Roughly three quarters of
the time, the room was empty before we walked in. The walls are downstream filters, relevant only to
the handful of strategies that had a genuine gross edge to defend.

**A transferable corollary.** Anyone who searches for alpha tends to blame the walls, because blaming
the walls is comfortable: it implies you *had* something, and the world took it. Before you blame the
walls, answer one question honestly: **did the gross edge ever beat buy & hold risk-adjusted?**
Usually it did not — it was beta in disguise, or out-of-sample decay, or an edge living inside a bar
you cannot trade.

Each wall has a **context** signature, not a frequency one (a further correction to our own framing —
only cost scales with frequency):

- **Cost (G2) — universal.** It bites at every frequency. It kills when `gross_edge_per_trade <
  round_trip_cost × turnover`.
- **Tax (G3) — crypto/realisation only.** 33% on every flip's realisation, with losses not fully
  offsettable.
- **Bad print (G1) — event/tail studies only.** Feed glitches manufacture false survivors in any study
  that anchors on extreme bars.

**The scale as a rule you can use in three minutes:** *(any frequency)* does the gross edge beat buy &
hold risk-adjusted? **[G0]** → *(high turnover)* does it survive the cost wall? **[G2]** → *(crypto /
realisation)* does it survive tax? **[G3]** → *(event / tail study)* is it real, or a bad print? **[G1]**

---

## IT — sintesi

**16 ipotesi certificate morte, più una 17ª e una 18ª in revisione.** Fin qui era un numero
*asserito*. Questo file è quel numero, voce per voce: cosa è stato testato, cosa è stato committato
*prima* del dato, chi ha verificato, e cosa l'ha uccisa. La tabella è sopra, in inglese (una riga per
ipotesi, non tradotta per non creare due versioni divergenti dello stesso fatto).

**Perché gli hash contano.** Una pre-registrazione vale qualcosa solo se è provabile che venga
**prima**. Un commit che contiene la predizione e il criterio di kill, fatto prima che il dato
esista, è quella prova. Due limiti onesti, detti subito:

1. **I commit stanno in repo privati.** Vedi un hash, non puoi verificarlo dall'esterno. Non
   chiamiamo "verificabile" ciò che un esterno non può controllare.
2. **Il firewall entra nel record git solo dal 2026-06-25.** Prima era pre-registrazione *off-repo*,
   in file mandate/design mai versionati. La disciplina c'era davvero — le barre erano congelate
   prima delle run — ma **la precedenza non è dimostrabile**, e non la retrodatiamo.

**Prova-di-precedenza: 4 su 18.** Righe 14, 15, 17, 18 hanno un firewall che precede il dato. Righe
13 e 16 hanno predizione e verdetto nello stesso commit. Righe 1–12 non hanno alcun commit.

**La riga 16 è quella scomoda — ed è quella che chiude il contatore.** La 16ª falsificazione, quella
che porta il numero a 16, è stata committata il 2026-06-29, **quattro giorni dopo** che il protocollo
firewall era già nel record git, con predizione e verdetto nello stesso commit. Il suo predecessore
nella stessa famiglia, `P-CARRY-1` (2026-06-25), il firewall **ce l'ha**; il re-run no. La causa
probabile è benigna (design e criterio di kill congelati in un mandate off-repo, sezione trascritta
dopo). **Ma non possiamo dimostrarlo, e il fatto epistemico non si cura di cosa pensiamo:** il numero
di testa poggia su una riga la cui precedenza non è dimostrabile, registrata dopo che sapevamo già
come dimostrarla. È la frase più scomoda del repository — motivo per cui non sta in una nota a piè
di pagina.

**Il protocollo come lo pubblicizziamo — i due meccanismi INSIEME — è stato applicato end-to-end a 3
ipotesi su 18** (righe 14, 17, 18; tutte dopo il 2026-06-25). Incrociando le due colonne della tabella
quel numero si ricava da soli: preferiamo darvelo noi. È il protocollo che eseguiamo **ora**, su tutto;
non è ciò che possiamo rivendicare retroattivamente sulle diciotto. Un protocollo giovane e datato con
precisione è credibile; uno retrodatato no.

**"Riproduzione byte-esatta" non vale per tutte e 16.** Il ricalcolo indipendente da parte di un
secondo agente è diventato protocollo a metà strada. Le morti precedenti sono state verificate con
determinismo (seed e BLAS pinnati, re-run byte-identici, hash pubblicati) — buona pratica, non un
secondo paio d'occhi. La colonna `Independent check` dice riga per riga quale delle due. Abbiamo
corretto il claim in `METHOD.md` che diceva altrimenti (`incident-log.md`, Entry 1).

**Cosa le ha uccise davvero (scala G0–G3).** Ogni morte è taggata col **primo** gradino non superato.
G0 = l'edge lordo esiste? (non è un muro: è assenza di materia prima) · G1 = muro bad-print · G2 =
muro costo · G3 = muro fisco. **La scala stessa è stata firewallata** (definizioni dei gate + predizioni
committate *prima* della tabulazione: mission-control `2b72e3e` → `b2c5355`), e la predizione congelata
era **contro di noi**: diceva che i muri sarebbero risultati una *minoranza*, contro il nostro stesso
framing comodo ("ci hanno ucciso i costi"). 4 predizioni pre-impegnate su 4 hanno tenuto, quella
inclusa: **abbiamo scommesso contro la nostra storia e perso la scommessa.** In un file la cui debolezza
dichiarata è "4 firewall su 18", la tassonomia è un risultato prodotto **sotto il protocollo pieno** (ed
è contatore-neutro — un deliverable di metodo, non un claim d'edge: per questo non è una diciannovesima
riga). **Il reperto, che non è quello che ci aspettavamo:** avevamo inquadrato
le nostre sconfitte come *"ci hanno ucciso i muri"*. Abbiamo pre-registrato la predizione **opposta**
e l'abbiamo tabulata. Ha tenuto: **G0 ≈ 13–14 su 18**. Il killer dominante **non sono i muri — è
l'assenza di edge**. Tre quarti delle volte la stanza era vuota prima che ci entrassimo. Prima di
incolpare i costi, rispondi onestamente a una domanda: **l'edge lordo ha mai battuto buy & hold
risk-adjusted?**
