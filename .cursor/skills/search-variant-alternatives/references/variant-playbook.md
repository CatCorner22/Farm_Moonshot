# Variant playbook — reference

Load when the SKILL checklist is not enough (unusual language, heavy OCR, or repeated nils).

## OCR / HTR: common given-name confusions (Latin script)

Often seen on death indexes and cursive certificates:

| Intended | Try also |
|---|---|
| Dora | Posa, Dosa, Rosa, Dona, Dara, Dore, Dori, Dola |
| Mary | Mayr, Mam, Marv, Mercy (context) |
| Ella | Alla, Elia, Emma (context) |
| Coy / McCoy | McCay, Coy, McKay, M Coy |
| Thomas | Thos, Tom, T A, T. A. |
| Elizabeth | Eliza, Bettie, Betsy, Lizie |
| Louisa | Eliza, Luisa, Loisa, Louiza |

Rule: **one-stroke differences** in D/P/R and o/a/e loops — generate all in `ocr-given` mode.

## OCR / HTR: surname confusions

| Pattern | Try |
|---|---|
| rn ↔ m | Newnam ↔ Newman (also Newnarn) |
| nn ↔ n | Newnam ↔ Newan |
| cl ↔ d | McClure ↔ McDure (context) |
| ie ↔ e | Smallwood ↔ Smalwood |
| trailing syllable | -son/-sen/-sson; -burg/-burgh/-brough |

## Index-specific (vital records)

- Search **certificate number** and **registration district** without name.
- Search **year ±1** (delayed registration).
- Search **county of death** vs **county of residence** separately.
- Ancestry/FS: try **Last name only** + filter; **First name** wildcards `D*` + place.
- Misfiled given name on **wrong letter tab** (Posa under P not D) — browse letter bucket.

## Soundex / Miracode

- Same Soundex ≠ same person — use as **discovery**, not merge.
- Card may use **married name** while certificate uses **maiden**.
- Miracode **volume/ED/family** beats index spelling for identity.

## Place variants

- Post office vs railroad name vs colloquial ("Mammoth" vs nearest real PO).
- **Township, precinct, ward, magisterial district** — all may appear on census without the name you expect.
- Cross **county and state lines** within 10 miles when nil persists.

## Non-genealogy (code / docs / web)

- American vs British spelling; hyphenation; `_` vs `-` vs space.
- Acronyms expanded and collapsed; product rename; deprecated API names.
- Git: search commit messages and old paths when filename search fails.

## Anti-patterns

- Do **not** treat one Ancestry hint as the only spelling.
- Do **not** merge on variant match alone (genealogy GPS still applies).
- Do **not** invent variants — only plausible orthographic/OCR/cultural forms + user-supplied aliases.
