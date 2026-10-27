# Visualisation — charts, graphs, timelines, maps

Load when any information will be *shown*, not just written (Phase 8, or earlier for working charts). Family trees have their own reference: [family-tree-design.md](family-tree-design.md). Statistics behind a chart: [statistics.md](statistics.md).

## First principle: a chart is an argument

Every visual asserts something. Before drawing, write its one-sentence claim, its source claim IDs (`C###`), and its confidence. If the claim is `POSSIBLE`/`SPECULATIVE`, the uncertainty must be *in the picture* (hatching, dashed lines, grey, `?`), not in a footnote nobody reads. A beautiful chart of unproven data is the fastest way to launder speculation into "fact" — the opposite of this skill.

## Chart selection — match form to question

| Question | Use | Avoid |
|---|---|---|
| When did events happen / what overlaps? | Timeline, lifespan (Gantt-style) chart | Prose lists, pie charts |
| Where / migration path? | Map with dated waypoints, small-multiple maps per generation | A single cluttered map of everyone |
| How many / how does it change? | Line (time), bar (categories), dot plot | Pie (>3 slices), 3D anything |
| Distribution (ages at death/marriage, family size)? | Histogram, box/violin-style summary, dot strip | Mean-only bar ("average age 41" hiding infant deaths) |
| Composition (origins, religions, occupations)? | Stacked bar with counts labelled, waffle/icon array | Pie with tiny slices, percentages without n |
| Relationship / kinship? | Pedigree, descendant, hourglass, fan chart → [family-tree-design.md](family-tree-design.md) | Network hairball for >30 people |
| DNA sharing / clusters? | Shared-cM dot/strip plot by relationship, cluster matrix (matches × matches), chromosome segment map | Ethnicity pie treated as ancestry proof |
| Risk / probability? | Natural-frequency icon array (x per 1,000), risk ladder → [statistics.md](statistics.md) | Relative-risk-only bar charts, truncated axes |
| Comparing places/cohorts? | Small multiples, same scales; slope chart for two time points | Dual axes implying a relationship |

Working charts (for your own analysis) may be rough; delivery charts must pass the checklist below. Label each file `working` or `delivery` in its filename/caption.

## Honesty rules — non-negotiable (see also misleading-presentations in statistics.md)

1. **Axes start at zero** for bar/length encodings; any exception is flagged on the chart itself with a visible break mark and a written reason. Line charts may truncate only with the break stated.
2. **No dual y-axes** to imply correlation; no 3D, no exploded pie, no pictogram area distortion (scale by area, never by height/radius alone).
3. **Show n and denominators.** Every percentage carries `n=…`; every rate carries its population and period. Small-n charts show the counts, not just smooth lines.
4. **Show uncertainty:** ranges/intervals as bands or whiskers; estimated dates as ranges (`c.1841–1843`) drawn as spans, never fake single points; missing data shown as gaps, not interpolated silently.
5. **No cherry-picked windows:** time ranges chosen before looking at the effect, or the choice is disclosed on the chart. Endpoints that flatter the story are a red-flag in the Phase-7 review of any chart.
6. **Scales consistent** across panels being compared (small multiples share axes); map projections and any boundary vintage stated ("county boundaries as of 1850").
7. **Colour means one thing** per document, is colour-blind safe (e.g. Okabe–Ito / viridis-type palettes), works in greyscale print, and never encodes the *only* copy of critical information (add labels/patterns).
8. **Direct labelling over legends** where possible; every axis has name + unit; every chart has title (the claim, not "Chart 1"), subtitle (population/place/period), source line (claim/source IDs, repository, access date), and a note of exclusions.

## Design craft (delivery standard)

- **Data-ink discipline (Tufte):** remove gridlines/borders/backgrounds that carry no information; light reference lines only; whitespace separates groups before boxes do.
- **Hierarchy:** the one key comparison is darkest/largest; context is grey; annotations state the *so-what* next to the data (" leaves Cork after the 1847 eviction cluster — see C041").
- **Typography:** one sans family, ≤3 sizes, names `Surname, Given (dates)` consistently; dates in ISO or "3 May 1841" — never ambiguous `03/05/41`.
- **Accessibility:** minimum readable size at intended output (print A4/Letter vs screen), contrast-checked text, alt text / data table supplied for every delivery chart (the table doubles as the citation trail).
- **Reproducibility:** delivery charts are generated from a data file in the case folder (CSV/JSON of claim IDs + values) by a script or named tool, logged in `06-dossier.md` — never hand-moved pixels that can't be regenerated when a date is corrected.

## Genealogy-specific visuals

- **Timeline chart:** one row per person (target + FAN), life spans as bars, events as points, shaded bands for wars/epidemics/census years/record availability — gaps become visible research leads.
- **Migration map:** numbered dated waypoints per household, transport mode if known, historical boundaries, `?` on inferred legs (dashed). One household per map.
- **Fan/pedigree wall charts:** see family-tree-design.md for layout, collapse handling, and print tiling.
- **DNA visuals:** shared-cM strip plot against relationship ranges (ranges, not point predictions); segment maps labelled with build (GRCh37/38) and tester codes only.
- **Photo/document figures:** cropped evidence images are labelled `detail, enhanced for legibility — original: <file/checksum>`; never present an enhanced image as the untouched record (see [paleography.md](paleography.md)).

## Tools in this skill

```bash
python3 scripts/make_pedigree.py family.json --root P001 --mode pedigree   -o tree.svg     # ancestor chart
python3 scripts/make_pedigree.py family.json --root P001 --mode descendant -o descendants.svg
python3 scripts/make_charts.py timeline events.csv -o timeline.svg   # lifespan/event timeline from claim-linked CSV
python3 scripts/make_charts.py bar data.csv --value n --label place -o chart.svg  # honest bar (zero axis, n labelled)
```

Generated SVG is text: diffable, regenerable, print-safe. For interactive exploration recommend (don't require) GEDCOM viewers / charting tools, and record tool + version; the case-folder SVG + its data file remain the archival deliverable.

## Pre-delivery checklist (log pass/fail in the dossier)

Claim sentence written · claim IDs cited · uncertainty visible · zero/baseline honest · n + denominator shown · scales consistent · colour-blind + greyscale safe · alt-text data table attached · data file + generation command logged · a hostile reader could not take away a stronger claim than the evidence supports.
