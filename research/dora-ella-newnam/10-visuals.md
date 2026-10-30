# 10 — Visuals register: Dora Ella Newnam Stone

Files live in `visuals/` (data file + generated SVG + alt-text table together).

| Visual ID | File (delivery/working) | One-sentence claim | Claim IDs | Data file + generation command | Uncertainty shown how? | Checklist pass |
|---|---|---|---|---|---|---|
| V001 | visuals/pedigree-dora.svg (delivery) | Dora’s ancestral couple as documented: Elias × Mary; grandparents PROBABLE | C004 | family.json · `make_pedigree.py family.json --root P001 --mode pedigree --generations 3 -o visuals/pedigree-dora.svg` | Dashed links = PROBABLE | ☑ |
| V002 | visuals/descendant-dora.svg (delivery) | Dora’s two unions and seven children (two unnamed dead before 1900) | C010 C014 C020–C025 | family.json · `--mode descendant --generations 2` | Dashed m2; unnamed children labelled Unknown | ☑ |
| V003 | visuals/timeline-dora.svg (delivery) | Lifespans of Dora and the people who locate her | C001 C003 C010 C015 | visuals/life.csv · `make_charts.py timeline …` | Samuel’s bar ends 1910 = “dead by,” not a death date | ☑ |
| V004 | visuals/descendant-elias.svg (delivery) | Elias’s children including Dora, and granddaughter Provie Hoover Burke (FAN, not Dora’s child) | C004 C096 C100 | family.json · `--root P004 --mode descendant --generations 3` | Dashed PROBABLE parentage; Provie on Mary L. × Hoover union | ☑ |
| V005 | [12-image-gallery.md](12-image-gallery.md) (delivery) | Captured NARA JPEGs labelled and ordered by census year | C003 C060 C062 C063 C031 C038 C064 C068 C069 C083 C088 | Hand-assembled markdown; images in `sources/census/` and `sources/soundex/` | Each plate tagged Family hit / Rejected same-name / Negative search / Context | ☑ |
| V006 | book/plates/loc-beattyville-1930.jpg | Beattyville + Kentucky River, 1930 — county seat, not Dora | locality | LOC item 2010651160 | Caption dates the view after her death | ☑ |
| V007 | book/plates/loc-fsa-south-fork-fence-1940.jpg | South Fork fence, Aug 1940 FSA — parent stream, not her farm | locality | LOC item 2017805013 | Caption dates the view 14 years after death | ☑ |
| V008 | book/index.html (delivery) | Illustrated HTML biography: cited life narrative, figures, endnotes 1–91, source appendix, pass 61 chapter | C001–C304 as used | Hand-assembled HTML from case file + `book/plates/` | Confidence labels in prose; dashed chart links; “not merged” plates captioned | ☑ |
| V009 | visuals/pedigree-dora.svg (regenerated 30 Oct 2026) | Same pedigree after pass 61; no new biological links invented | C004 | `make_pedigree.py family.json --root P001 --mode pedigree --generations 3` | Dashed = PROBABLE | ☑ |
| V010 | visuals/timeline-dora.svg (regenerated 30 Oct 2026) | Lifespans; Samuel bar still ends 1910 as a bound | C001 C015 | `make_charts.py timeline visuals/life.csv` | Samuel end-year is “dead by,” not a death date | ☑ |

## Family trees (family-tree-design.md)
- Root person & direction: P001 Dora; pedigree (ancestors) and descendant (children). Cut-off: grandparents and children only (no living great-grandchildren). V004 is a FAN descendant of P004 Elias, three generations, to show Provie on the correct union.
- Legend on chart ☑ (script: solid PROVEN / dashed PROBABLE-POSSIBLE / dotted SPECULATIVE)
- Biological vs documentary lines distinct ☑ · Living redacted ☑ (no post-1926 births; Provie b. 1886) · Person IDs on boxes ☑

## Alt text
- V001: Pedigree chart of Dora Ella Newnam Stone (1871–1926) showing parents Elias T. Newnam (1842–1932) and Mary Ann Smallwood (1842–1918) with dashed probable links, and a further probable generation Henry Harrison Newnam and Millie Tincher.
- V002: Descendant chart of Dora with first husband Samuel P. Newnam (proven) and five named children plus two unnamed children who died before 1900, and a dashed second union with T. A. Stone (probable, no children).
- V003: Horizontal lifespan bars from 1842 to 1980 for Dora, her parents, Samuel (bar ends 1910 as latest bound), probable T. A. Stone, Pearl, and McCoy, with event dots at marriage, 1900 census, and death.
- V004: Descendant chart of Elias T. Newnam showing six children including Dora, a dashed probable union of Mary L. Newnam with James Hoover, and granddaughter Provie Hoover Burke.
- V005: Chronological source-image gallery of NARA microfilm JPEGs (1870–1920), each labelled with record date, role, names on the page, and why the frame was kept.
- V006: Later view of Beattyville and the Kentucky River, 1930 (LOC); not a picture of Dora.
- V007: FSA split-rail fence on the South Fork of the Kentucky River, August 1940; landscape context only.
- V008: Illustrated HTML master book (`book/index.html`) with linked endnotes and a source appendix.
