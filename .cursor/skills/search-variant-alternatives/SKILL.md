---
name: search-variant-alternatives
description: Proactively expand every person, place, and record search with misspellings, OCR/HTR misreads, phonetic and cultural variants, swapped index order, and repository-specific quirks before the first query — and after every nil result. Use for genealogy, archives, newspapers, death indexes, census, code/repo search when names or labels matter, and any task where "nothing found" might mean wrong spelling not wrong hypothesis.
---

# Search variant alternatives

**Default:** A single spelling is never enough. Treat "no results" as **unsearched** until a documented variant pass runs.

## When to load this skill

- Before the **first** repository query for a person, place, certificate number, or street.
- After **any nil** search (index, grep, web, database).
- When a user reports a **misfile** (e.g. Posa for Dora, Newman for Newnam).
- When merging records across **derivative** sources (indexes, OCR, Soundex, Ancestry hints).

Genealogy cases: also run [genealogy-detective](../genealogy-detective/SKILL.md) and write variants into `01-plan.md` + log exact strings in `02-log.md`.

## Mandatory pre-search gate (do not skip)

For each **target string** (surname, given name, place, cert #), produce a **variant set** before querying:

1. **Canonical** — what the best primary record uses.
2. **User / family variants** — nicknames, maiden vs married, reported misfiles.
3. **Machine variants** — script output below + Soundex (`genealogy-detective/scripts/kinship.py soundex`).
4. **Repository quirks** — index order (`Last, First` vs `First Last`), punctuation stripped, middle initial dropped, Soundex card only.

Run the generator (adjust paths if not in repo root):

```bash
python3 .cursor/skills/search-variant-alternatives/scripts/search_variants.py person "Dora" "Newnam" --also Newman
python3 .cursor/skills/search-variant-alternatives/scripts/search_variants.py ocr-given Dora
python3 .cursor/skills/search-variant-alternatives/scripts/search_variants.py cert 1524 --rd 676
```

5. **Cross-identifier searches** — when name fails, search **cert #**, **RD/volume**, **date + county**, **spouse**, **informant**, **address**, **FAN** neighbour (genealogy).

Only after steps 1–5 may you log `nil` for that repository.

## Variant categories (think in all eight every time)

| Category | Examples | Action |
|---|---|---|
| **Orthographic** | Newnam/Newman, Thomson/Thompson, Gray/Grey | Always search both; add `-son/-sen`, double consonant |
| **Phonetic** | Soundex; Metaphone-style swaps c/k, ph/f, i/y | `kinship.py soundex`; browse same code bucket |
| **OCR / HTR given-name** | Dora→Posa/Dosa/Rosa/Dona; Mary→Mayr | Run `ocr-given` / `ocr-surname` on anchor name |
| **OCR / HTR surname** | rn/m, cl/d, vv/w, li/h | See [references/variant-playbook.md](references/variant-playbook.md) |
| **Handwriting** | looped D/P/R; n/u; s/r | Paleography pass; never trust PDF text layer alone |
| **Cultural / historical** | Mc/Mac, O', St./Saint, Jr., dit names, patronymics | Expand per [genealogy-mastery](../genealogy-detective/references/genealogy-mastery.md) |
| **Index / database** | Wrong field, swapped given/surname, maiden indexed under husband | Search **alias reported by user**; cert #; date range only |
| **Place** | Mammoth vs Nimrod; township vs precinct; old county name | Gazetteer + boundary history before place-only nil |

## After nil — variant storm (minimum 3 new tries)

1. Next **category** not yet tried (e.g. phonetic after orthographic).
2. **Drop surname** — first name + place + year; or address-only.
3. **Adjacent index** — browse ±5 entries, neighbouring pages, neighbouring jurisdictions.
4. **Second repository** with same variant list.

Log each attempt with **exact string**. Never write "searched variants" without listing them.

## Output discipline

- **Plans:** paste the variant table into `01-plan.md` (genealogy) or the task checklist (other work).
- **Logs:** one row per repository × variant batch; nil must name strings tried.
- **Claims:** index-only hits under a variant spelling stay **PROBABLE** until certificate/schedule image agrees.

## Deep reference

Full confusion matrices, workflow diagrams, and repository notes: [references/variant-playbook.md](references/variant-playbook.md).

## Integration

- **Genealogy detective:** Phase 2 plan + Phase 3 every search + nil backlog items.
- **Creative workarounds:** ladder F4 "Transcription-error variants" — use this skill as the F4 checklist.
- **Red-team:** Ask "Could the record exist under a misread name we did not query?"
