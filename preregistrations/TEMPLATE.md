---
id: <ID>
claim: >
  TBD - one sentence. What are you asserting? Not what you will study: what you
  are claiming is true.
hypothesis: >
  TBD - the falsifiable form. If this is right, what will be observed that would
  not be observed otherwise?
prediction: >
  TBD - optional, and the most useful field on this page. What do you actually
  expect? Write it now, so that afterwards you cannot claim you knew all along.
kill_criterion: >
  TBD - the number that kills this. Not "if results are disappointing": a threshold,
  a comparison, a count. If you cannot write one, you do not have a hypothesis yet -
  and that, not the tool, is the thing that just failed.
survive_criterion: >
  TBD - the complementary region. What outcome means this is NOT dead? Stating both
  is what stops you from choosing the boundary afterwards.
verification_date: TBD
outcome_if_kill: >
  TBD - what you will DO if it dies. "Reconsider" is honest. "Try a variant" usually
  means the criterion was decoration.
measured_by:
  - id: M1
    what: TBD - the quantity, named precisely enough that someone else could find it.
    how: >
      TBD - the procedure. A query, a command, a script, a source. Written so that a
      stranger who dislikes you could run it and get the same number. If only you can
      measure it, it is not a measurement.
known_blind_spots:
  - >
    TBD - what your measurement cannot see. Every measurement has a blind spot;
    naming it now is the difference between a limit and an excuse.
status: open
---

# <ID> — <one line: the question this settles>

## The claim

What you are asserting, and why it matters. Keep it short. This section is prose for a
human; the machine reads the block above.

## What would kill it

Restate the kill criterion in plain language, and — this is the part people skip —
**name the escape hatches you are disallowing**. Which favourable-looking outcomes will
you refuse to count as a survival? Write them here, now, while they still cost you
nothing. Afterwards, they will look like exactly the reasonable exception you deserve.

## What this pre-registration cannot prove

It cannot prove you had not already glanced at the data. **No commit can.** It proves
that the criterion could not be edited once the outcome was known. That is a guard
against retrofitting, not a guarantee of blindness — and it is worth stating in your own
words rather than inheriting it from this template.

---

*Written with `firewall preregister <ID>`. Once committed, editing this file fails rule
(c) — visibly, in the git record, where anyone can see it.*
