# Fictional example — visuals, statistics, transcription (all names invented)

Shows the three new disciplines at small scale, continuing the invented Venn family from `fictional-mini-case.md`.

## 1. Transcription (photo of a parish register page)

Intake: phone photo, full page, slightly skewed; `document_inventory.py` → JPEG 4032×3024, SHA-256 logged. Deskewed on a copy only. Script: mixed secretary-influenced hand, Latin formula.

Diplomatic (Pass 1 + verification Pass 2):
> `bapt[izavi] Eliam fil[ium] Matthiae Venn et Annae n[atae] Braun [?] / nat[um] 3 Maii, bapt[izatum] 16 Maii 1841 / patrini: Georgius Braun et Maria Braunin`

One `[?]` survives (the mother's surname flourish) → claim C003 (maiden name Braun) would be capped at `POSSIBLE` from this alone; a brother's marriage entry reading `Braun` clearly + burial record corroborate → `PROVEN`, with the uncertainty and its resolution both on file. The Latin is translated in a separate layer; `patrini` extracted as FAN targets (godparents = maternal grandparents, a hypothesis then proven from their own entries).

## 2. Statistics (a family claim, tested honestly)

Family lore: "The Venns lost twice as many babies as everyone else."

Defined *before* computing (`09-statistics.md`): parish cohort = all baptisms in the same parish 1830–1860 with burials linked; family = Venn couples in the same parish/period.

Result via `stats.py risk --a-events 3 --a-n 14 --b-events 61 --b-n 512` (invented counts):
- Family: 3/14 = 214 per 1,000. Parish baseline: 61/512 = 119 per 1,000.
- **Absolute: +95 per 1,000 (+9.5 points), interval wide and crossing zero. Relative: 1.80×, 95% CI includes 1.**
- Delivered sentence: "In this parish and period, about 119 of every 1,000 baptised children died in infancy. In the Venn families, 3 of 14 did (214 per 1,000). That looks like roughly 95 extra deaths per 1,000 — but with only 14 children, the data are consistent with anything from *fewer* deaths than the parish to about three times as many. `POSSIBLE`, not a family curse."

The misleading-but-accurate version — "Venn babies died at nearly double the rate!" (relative only, n hidden) — is in the file as the rejected draft, screened against the catalogue items #1 and #8.

## 3. Visuals (generated, claim-linked, uncertainty visible)

- `visuals/pedigree.svg` via `make_pedigree.py family.json --root P001 --mode pedigree`: the link to the paternal grandfather is `PROBABLE` → drawn dashed automatically from the union confidence in `family.json`; the unknown maternal grandmother is an explicit grey `Unknown` box, not a blank.
- `visuals/timeline.svg` via `make_charts.py timeline life.csv`: lifespan bars for Elias, his siblings, and his FAN (godparents, brother-in-law) — the 1852–1857 gap where Elias vanishes from Cedar County becomes visually obvious and is logged as a research lead (found later in a neighbouring county's tax list).
- Both registered in `10-visuals.md` with claim IDs, data files, generation commands, and the checklist result. Alt-text data tables sit beside the SVGs.

**What "best work" looks like:** the picture, the number, and the reading can each be re-derived by a stranger from the case folder — and none of them claims more than the records support.
