# Family tree design — pedigree, descendant & relationship charts

Load whenever drawing a family tree (working or delivery). General chart honesty: [visualisation.md](visualisation.md). Proof labels: [methods.md](methods.md).

## Choose the tree for the question

| Tree | Shows | Best for | Watch out for |
|---|---|---|---|
| Pedigree / ancestry chart | One person's ancestors, generation by generation | "Where did I come from?", DNA-match placement | Exponential width (2ⁿ per generation); collapse duplicates |
| Descendant chart | One ancestor/couple → all descendants | Reunions, DNA recruiting, surname studies | Explodes fast; prune by line/time with the cut stated |
| Hourglass | Ancestors + descendants of one person | Single-person dossier centrepiece | Crowding at the waist |
| Bowtie | Paternal left, maternal right of one person | Compact ancestry overview | Hides intermarriage between sides |
| Fan chart | Ancestors in semicircles, colour by line/place | Seeing completeness gaps at a glance | Text legibility beyond ~6 generations |
| A Beziehung / relationship chart | Everyone + all links in a family network | Complex intermarried communities, FAN analysis | Hairball risk — filter by place/date |
| Genogram-style overlay | + occupation, cause of death, migration, religion symbols | Biographical/social-pattern insight | Symbol overload; needs a legend |
| Ahnentafel (numbered list) | Ancestors as text: 1=person, 2=father, 3=mother, 2n/2n+1=parents | Compact, citable, print-proof companion to any chart | Not visual; pair with a chart |

Always state: root person (`P###`), direction, generations included, cut-off rule ("descendants shown to grandchildren"), and date generated. A tree without a root/cut-off statement is uninterpretable in a year.

## Encoding truth in the tree (the core discipline)

- **Every person box:** name (maiden names in full for women, never "Mrs Husband"), birth–death years or `c.`/`?`, and person ID. Unknown = an explicit `Unknown` box — a *blank space silently reads as "no such person"*.
- **Every link carries its confidence:** solid = `PROVEN`, dashed = `PROBABLE/POSSIBLE`, dotted+`?` = `SPECULATIVE`. The legend is on the chart, every time.
- **Line types distinguish biology from law/social life:** solid = biological (as documented/DNA), double line = adoptive, wavy/different colour = step/foster/guardianship, `+DNA` tag where DNA is part of the proof. Never merge a biological and a documentary tree into one silent line set — where they differ, show both, labelled (see ethics reference for private handling).
- **Multiple unions:** each partnership drawn separately, children attached to the correct union, partnerships ordered by date, divorce/end noted. A child under the wrong union line is the commonest tree error.
- **Pedigree collapse / intermarriage:** the same person appearing twice is drawn once with cross-reference arrows (or duplicated with `= P017` markers) — the chosen convention is stated; silently duplicating inflates ancestor counts and hides collapse, which matters for DNA.
- **Disproved links** do not appear on delivery trees; they live in the evidence file with their disproof. Working trees may show them crossed out.
- **Dates on places:** a birthplace on a box is the place *at that date*; modern equivalent in the dossier text.
- **Living people:** box reads `Living` (plus relationship if the user approves), no dates/places/photos. Default for anyone born <100 years ago without a death record.

## Layout & craft

- **Reading order:** generations in aligned columns (pedigree) or rows (descendant), root at left/bottom consistently per document set; partners adjacent, siblings in birth order with order preserved even when dates unknown (`order uncertain` noted).
- **No crossing lines** where avoidable; route partners' joining line to the children drop-line once, not per child. If crossings are unavoidable (intermarriage), use bridge/jump markers.
- **Colour discipline:** one semantic per document (e.g. colour = ancestral line, or = birth country) with legend; never colour = sex *and* line *and* confidence simultaneously. Shape/line-style carries confidence so colour-blind and greyscale readers lose nothing.
- **Scale strategy:** >6 generations or >60 people → split: overview tree (truncated, "continued on Tree B") + per-line detail trees with matching continuation numbers, a person index (name → tree/page, person ID), and consistent box numbering across sheets. Print tiling: state paper size, overlap, and sheet map.
- **Photos/coats of arms/decoration:** optional, subordinate, sourced (a portrait labelled with provenance; arms only if documented entitlement — never decorative "family crests" bought online, which are labelled misattribution risks).
- **Typography/consistency:** same name/date formats as the dossier; surnames not all-caps in one tree and title-case in the next within one deliverable set.

## Data-driven generation (required for delivery trees)

Trees are generated from structured data in the case folder, never hand-drawn-only:

```json
{"persons":[{"id":"P001","name":"Doe, Jane","birth":"1842","death":"1911","sex":"F"}],
 "unions":[{"id":"U001","partners":["P002","P003"],"marriage":"1865","children":["P001"],
             "type":"biological|adoptive|step","confidence":"PROVEN"}]}
```

```bash
python3 scripts/make_pedigree.py family.json --root P001 --mode pedigree --generations 5 -o visuals/pedigree.svg
python3 scripts/make_pedigree.py family.json --root P001 --mode descendant -o visuals/descendants.svg
```

- Validate before drawing: no person is their own ancestor, parents' birth years precede children's by plausible margins, union children link to existing persons — the generator errors on cycles/impossibilities rather than drawing them.
- GEDCOM is the interchange format (import/export through the user's tree software); note GEDCOM loses confidence/line-type nuance — the JSON + chart legend remain authoritative in the case folder.
- Regenerate after every correction; keep the data file and command in the visual's source line. Version delivery trees (`tree-v3.svg`) when shared externally.

## Review checklist (Phase 7 applies to trees too)

Root/cut-off stated · unknowns explicit · confidence in line styles + legend · biological vs adoptive/step distinct · children on correct unions · collapse handled & stated · disproved links absent · living redacted · index + Ahnentafel companion for >4 generations · a stranger could re-derive every link from claim IDs.
