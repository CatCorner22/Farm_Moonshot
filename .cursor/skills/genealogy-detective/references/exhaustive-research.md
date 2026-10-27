# Exhaustive research — relentless drive without stopping early

Load at case open, before Phase 3, and whenever you feel tempted to summarise, deliver, or declare a brick wall. **Relentless** means pursuing every defensible lead until the completion contract is met or a hard external block is documented — not guessing, not harassing living people, not fabricating access. Stopping because the first database returned nothing, because a plausible story fits, or because the chat is long, is a failure mode this skill forbids.

## Completion contract (what "done" means)

Research is **complete** only when **all** are true:

1. **Matrix closed** — every applicable source-matrix row is `found`, `searched–nil` (with repository, years, variants tried), or `n/a + reason` in `02-log.md`.
2. **Backlog empty or explicitly deferred** — `11-backlog.md` has zero `open` items, OR each remaining item is `deferred` with user-written approval and a retrieval path (paywall, on-site, cost).
3. **FAN swept** — every witness, sponsor, informant, executor, neighbour on a census page, fellow passenger, and co-defendant from *found* records has been identified and either researched or logged `searched–nil` for the question-relevant record sets.
4. **Hypotheses tested** — the null hypothesis and every serious alternative in `01-plan.md` has a written verdict (supported / weakened / disproved / still open + why).
5. **GPS gates honestly assessed** — if any GPS element is incomplete, the answer label is `PROBABLE` or below and the missing element is named; `PROVEN` is never claimed to "be done."

**Paused ≠ done.** Between sessions or context limits, you **pause** with files updated and the next three backlog items written — you do not imply the research question is answered unless the contract is met.

## Operating doctrine — relentless, not reckless

| Do relentlessly | Do not (ever) |
|---|---|
| Run the next backlog item immediately after logging the last | Stop after one "hit" that confirms lore |
| Expand FAN one ring outward when direct records fail | Merge same-name records to force a tidy tree |
| Browse images around every index hit; search without surnames | Trust indexes or OCR as if they were originals |
| Chase footnotes, marginal notes, and "see also" in any source | Declare "no record" before matrix + FAN sweep |
| Re-search under phonetics, initials, address, occupation | Research living people or contact strangers without user direction |
| Log **nil** with the same care as a find | Summarise in chat without writing to the case folder |
| Pivot jurisdiction (parish ↔ county ↔ state ↔ country ↔ neighbouring place) | Skip a matrix row because it "probably doesn't apply" without logging `n/a` |
| Follow land/probate/court chains for every household member | Close when the user might be "satisfied" if GPS isn't met |
| Update backlog when any new name/place/date appears | Invent record contents you could not access |

**Default stance:** the accepted family story is wrong until records prove it. Your job is to *disprove alternatives*, not to decorate the narrative.

## Research backlog (`11-backlog.md`) — the engine that prevents stopping

Maintain a **prioritised queue** of concrete next actions. Each item is one searchable unit:

> `B042 | open | high | PRONI will index 1858–1862 | "Matthias Venn" + variants | test H2 father in Antrim before Ohio`

Statuses: `open` · `in_progress` · `done` (link log ID) · `nil` (link log ID) · `blocked` (exact blocker) · `deferred` (user approved).

**Rules:**
- After **every** find, add backlog items for: (a) corroboration in a second record type, (b) each new person named, (c) each new place, (d) each date that changes the timeline.
- After **every** nil search, add the *next variant* or *next repository* — not "give up on vitals."
- Minimum **three** `open` items before pausing any session.
- Work **top to bottom**; do not skip to easy wins that don't move the research question.
- Run `scripts/research_status.py research/<person>/` before telling the user you are finished — if `open` > 0 and nothing is `deferred`, you are not finished.

## Phase 3 expansion — intensive search passes (run until matrix + FAN gates pass)

Do not treat Phase 3 as "one pass." Cycle these **passes** until gates close or every pass returns only nil with no new FAN names:

1. **Direct identity pass** — target in every applicable matrix row, all name variants from `01-plan.md`.
2. **Household pass** — spouse, children, parents (if named anywhere), siblings; same matrix rows.
3. **FAN pass** — witnesses, sponsors, informants, executors, bondsmen, neighbours (same census page ±2 families), employers, regiment mates, shipmates.
4. **Asset pass** — land (grantor/grantee both directions), tax lists year-by-year, probate of target and each FAN member, mortgages, chancery.
5. **Migration pass** — origin and destination jurisdictions; passenger lists both ports; naturalisation chain; "missing" years in directories.
6. **Institutional pass** — church beyond vitals (membership, transfers, discipline), poor law, prison, asylum, school, orphanage.
7. **Press pass** — newspapers (obit, court, land, accident, social, shipping, "information wanted") for target + FAN surnames in relevant places/years.
8. **Authored-leads pass** — unsourced trees and county histories **only** to harvest names/places/dates as `SPECULATIVE` backlog items — then re-prove from rows 1–7.
9. **DNA pass** (if applicable) — after documentary FAN exists; cluster, build match trees, test hypotheses (see `dna.md`).

**Index-browsing discipline:** for any collection with images, search → open hit → read **±5 entries** on the same page/roll → note neighbours and clerical patterns → browse adjacent pages when dates cluster. Many solutions sit beside the indexed person.

**Brick-wall escalation (never stop at step 1):**
1. Re-verify every "fact" about the target.
2. Research **siblings** and **children** first (they name parents and origins).
3. Full FAN at current ring; then **expand ring** (FAN's FAN).
4. Neighbouring parish/county/state; **both** sides of a border.
5. Name-variant storm + address/occupation-only searches.
6. Land/probate/court deep dive on FAN members.
7. DNA + targeted testing plan (documentary tree required).
8. Written on-site / archivist order list for the user — **then** mark items `blocked`, not "impossible."

## Multi-session continuity (never lose momentum)

**Session open (every time):** read `00-intake.md`, `11-backlog.md`, dossier status block, last 10 log rows → pick highest `open` backlog item → set `in_progress` → execute.

**Session close (every time):** finish current log row → set backlog item `done`/`nil`/`blocked` → add new items from finds → update dossier status (confidence, open count) → write **Next session starts with:** one line naming `B###`.

If the user says **exhaustive**, **don't stop**, **intensive**, or **world-class**: enable **intensive mode** — no pass is skipped; FAN expands two rings; every matrix row gets at least two repositories when one exists; biography context (occupation, religion, migration push factors) is researched to support identity, not as filler.

## When you may pause without guilt

- User explicitly redirects scope ("stop at grandparents").
- Hard block documented: records destroyed (cite destruction source), privacy law, paywall/on-site with `deferred` + exact order form filled for user — **only after** [creative-workarounds.md](creative-workarounds.md) ladders and [proactive-autonomy.md](proactive-autonomy.md) (≥3 logged steps, no homework lists).
- Living-person boundary reached on a line (research deceased generation instead).
- You have met the **completion contract** and passed `audit_dossier.py` + `research_status.py` with zero unjustified `open` items.

Pausing for token limits: **mandatory** file updates first; never end on an unlogged search or an empty backlog.

## Anti-patterns checklist (Phase 7 also screens these)

Stopped after Ancestry/FamilySearch only · Stopped after first confirming record · No nil searches logged · FAN witnesses unnamed · Alternative hypothesis not tested · "Probably" in prose without `PROBABLE` label · Brick wall declared without escalation log · Chat summary replaced case-folder updates · `PROVEN` with open backlog items.
