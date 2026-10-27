# Methods — proof, identity, conflicts, brick walls

Load when entering Phases 4–5 or 7. Standards follow the Board for Certification of Genealogists (BCG) *Genealogy Standards* and Elizabeth Shown Mills' evidence framework.

## The Genealogical Proof Standard (GPS) — all five, or not proven

1. Reasonably exhaustive research (all applicable rows of the source matrix searched, nil results logged).
2. Complete, accurate source citations (another researcher can re-find every item).
3. Thorough analysis and correlation of evidence.
4. Resolution of conflicting evidence.
5. A soundly reasoned, coherently written conclusion.

## Confidence labels

| Label | Meaning |
|---|---|
| `PROVEN` | Meets GPS; direct evidence or a written indirect-evidence proof argument; conflicts resolved |
| `PROBABLE` | Strong convergent evidence, one GPS element incomplete (name which) |
| `POSSIBLE` | Some supporting evidence, alternatives not excluded |
| `SPECULATIVE` | Lore, unsourced trees, single weak index hit, DNA-only hint. Never presented as fact |
| `DISPROVED` | Contradicted by stronger evidence — keep in the file with its disproof; it prevents re-chasing |

## Evidence analysis (per item, in `04-evidence.md`)

- **Source:** Original (first recording / image of it) · Derivative (index, transcription, abstract) · Authored (tree, biography, compiled history).
- **Information:** Primary (informant with firsthand knowledge, recorded near the event) · Secondary (later / secondhand) · Indeterminate.
- **Evidence:** Direct (states the answer) · Indirect (must be combined) · Negative (absence where a record should exist — only meaningful after an exhaustive, logged search of the right place/years).
- Always name the **informant** and ask: how would they know, how long after, what motive to distort? A death certificate is primary for death, secondary for birth and parents.

## Citation minimum (Evidence Explained style)

Creator/record title; record type & date range; repository/collection & place; volume/page/certificate/entry identifiers; URL/database + access date for online items; `image | index only | transcription only`; informant if stated. A citation that cannot be re-found fails GPS #2.

## Same-person test (identity)

Merge two records only when **≥2 independent identifiers align and zero facts contradict**: full name/variant, age or birth date/place, spouse, parents, children, occupation, address/land parcel, religion, witnesses/sponsors, military unit, signature/mark, neighbours (same census page / FAN). One identifier + a contradiction = two people until the contradiction is explained (e.g. age heaping, remarriage, boundary change). Keep rival candidates as separate `P###` files with a disambiguation note — future research must see why a candidate was rejected.

## Conflict resolution

State both claims verbatim → analyse each informant, contemporaneity, source class, motive → prefer primary information in original records, but explain *why* the loser is wrong (informant error, age rounding, step-parent named as parent, delayed registration, transcription/OCR error) → record the resolution in `07-conflicts.md`. Unresolvable = claim capped at `PROBABLE` and both versions shown in the dossier.

## Indirect-evidence proof argument (template)

Question → items of indirect evidence (each cited) → correlation (how they interlock: time, place, FAN, naming) → why alternatives fail → conclusion + confidence. Used for most pre-vital-registration parentage, maiden names, and origins.

## Brick-wall protocol (in order)

1. Re-verify every "fact" about the target; brick walls are often one wrong assumption.
2. Extend the timeline ±10 years; hunt gaps.
3. Full FAN club: siblings first (a sibling's record often names what the target's doesn't), then witnesses, sponsors, executors, neighbours on every census, fellow migrants/passengers, workmates, co-religionists.
4. Follow land, probate, court, tax and newspaper trails for every FAN member.
5. Change jurisdiction level: town → county → state/province → national; church parish → diocese; check the neighbouring county/parish across a boundary.
6. Name-variant storm: wildcards, initials, phonetics (Soundex/Metaphone via `scripts/kinship.py soundex`), translated names, patronymics, farm names, dit names, maiden↔married swaps, middle-name-as-first-name.
7. Substitute records: no birth record → baptism, census ages, military age, marriage age, death age, gravestone, obituary (all secondary — correlate, don't cherry-pick).
8. DNA (autosomal clustering + targeted testing of documented descendants; Y-DNA for a paternal line, mtDNA for a maternal line) — see `dna.md` and `raw-dna-files.md`.
9. Hire/on-site lookup list: write exact archive, series, years and question for records not online; hand it to the user rather than declaring defeat or guessing contents.

## Common traps

- **Same-name impostors**, cousins named alike, father/son conflation, a widow remarrying (children change surname informally).
- **Ages lie:** census age heaping (rounding to 0/5), lying to enlist/marry/work, vanity on death records. Treat ages as ranges (±2 yrs normal, ±5 not rare).
- **Places lie:** birthplace reported as last residence / port / nearest town; jurisdictions and county boundaries change; record the place as it was *at the event date*, modern equivalent in brackets.
- **Calendars & dating:** Julian→Gregorian (1752 in Britain/colonies; 1582–1923 elsewhere), Old Style year beginning 25 March (Jan–Mar dates may be double-dated 1710/11), French Republican calendar, regnal years, "inst./ult." in newspapers.
- **Naming customs:** patronymics (Scandinavia, Wales, Netherlands), dit names (French Canada), farm names (Norway), Spanish double surnames, Ashkenazi naming after deceased relatives, Irish/Scottish naming patterns (useful as a *hint*, never proof), children named for dead siblings (two same-name children ≠ one child).
- **Women disappear** into married names, initials ("Mrs J Smith"), and husbands' records — search via children, widows' pensions, probate of fathers/brothers naming married daughters.
- **Indexes lie:** OCR and transcription errors, mis-indexed surnames, pages skipped in digitisation. Browse images around a found entry; search by first name + place, or by address/household, not surname alone.
- **Migration:** chain migration, return migration, name changed *by usage* (formal change-of-name records are the exception), naturalisation papers that name origin town vs. those that don't (pre/post-1906 in the US differs sharply).

## Red-team checklist (Phase 7)

Same-name impostor? · step/adoptive/foster/guardianship shown as biological? · informant or clerical error? · two spouses merged into one? · one person split in two by a name change? · a record for a cousin attached by an online tree and copied 500 times (one source, many copies ≠ corroboration)? · Does any record actually *falsify* the conclusion — did you search for it and log the attempt?
