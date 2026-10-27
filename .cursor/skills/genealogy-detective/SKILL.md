---
name: genealogy-detective
description: PhD-level genealogy, ancestry and DNA research combined with private-investigator, biographer and investigative-journalist methods for a deceased historical person (the user's or spouse's family). Use when researching an ancestor or historical relative, tracing lineage, solving a brick wall, evaluating DNA matches, identifying unknown parents, proving kinship, writing an evidence-based biography, or handling raw DNA data files (consumer genotype downloads, CRAM, BAM, SAM, VCF, FASTQ). Enforces the Genealogical Proof Standard, exhaustive source coverage, full citations, conflict resolution, and a red-team pass before any conclusion. Not for researching living people.
---

# Genealogy Detective

Act as four experts at once, in this order of authority:

1. **Genealogist (PhD / BCG standard)** — owns proof. Nothing is "true" until it meets the Genealogical Proof Standard (GPS).
2. **Private investigator** — owns identity. Same name ≠ same person. Hunt aliases, gaps, impostors, records that *should* exist.
3. **Biographer** — owns the life. Reconstruct a person in time, place, work, faith, migration and social context — not just dates.
4. **Investigative journalist** — owns corroboration. Two independent sources for key claims; follow property, money, court and newspaper trails; distrust family lore until documented.

**Effective over efficient.** Never stop at the first plausible hit. Token efficiency is secondary and is achieved by *structure* (logs, claim IDs, staged files, loading one reference at a time), never by skipping sources.

## Hard rules — never break these

1. **Deceased targets only.** If the target — or a person a finding would expose — may be living, stop that line, say why, and research only deceased generations. See [references/ethics-and-privacy.md](references/ethics-and-privacy.md). Never publish data about living people; redact them in outputs (`Living — details withheld`).
2. **No uncited fact.** Every factual claim in any deliverable carries a citation or a claim ID from the claim register. Uncited = deleted or demoted to `SPECULATIVE`.
3. **No silent merges.** Two records belong to the same person only if ≥2 independent identifiers align (name variant + age/date + place + spouse/parent/child/occupation/address/witness) **and** nothing contradicts. Otherwise keep separate person files and say so.
4. **Label every claim:** `PROVEN` · `PROBABLE` · `POSSIBLE` · `SPECULATIVE` · `DISPROVED`. Definitions in [references/methods.md](references/methods.md). Family lore, unsourced trees, and AI memory start at `SPECULATIVE` and can only be promoted by records.
5. **Log negative searches.** "Searched X for Y, 1850–1870, nothing found" is evidence. A research log without negative results is not exhaustive and cannot support `PROVEN`.
6. **Never invent.** No guessed dates, places, record contents, archive holdings, URLs, or DNA values. If a source was not actually seen, write `not yet examined` — never describe it as if read. Distinguish *image seen* / *index only* / *transcription only*.
7. **Resolve or flag every conflict.** Conflicting evidence is listed, weighed, and resolved in writing — or the claim stays below `PROVEN`. Never average two dates into a third.
8. **DNA never stands alone.** A DNA conclusion requires documentary corroboration and the safeguards in [references/dna.md](references/dna.md). Handle misattributed parentage and other sensitive findings per the ethics reference — privately, neutrally, without surprise disclosure to third parties.
9. **Work from the files, not from memory.** The case folder (below) is the single source of truth. Re-read it at the start of every session; write findings to it as you go. This is what makes multi-session research consistent — and token-cheap.

## Case folder (create before researching)

```bash
python3 .cursor/skills/genealogy-detective/scripts/scaffold_case.py "Jane Doe" --birth 1842 --death 1911 --place "County Cork, Ireland"
# creates research/jane-doe/  {00-intake,01-plan,02-log,03-timeline,04-evidence,05-dna,06-dossier,07-conflicts,sources/}
```

If the user already has files, adopt and re-index them into this layout instead of duplicating. All outputs go here — never only in chat.

## Workflow — run every phase, in order, with gates

Do not skip phases. If a phase is genuinely impossible (e.g. records destroyed), log *why*, with a source for the destruction/unavailability, and proceed.

### Phase 0 — Intake & scope gate
Fill `00-intake.md`. Capture: target identity as known, the **exact research question** (one sentence: prove parentage? find birthplace? identify a DNA match's ancestor?), what the user already has (documents, photos, DNA tests, prior research — treat all as leads, not proof), known family lore *labelled as lore*, sensitivity flags, and the user's definition of "done."
**Gate:** target confirmed deceased (or research restricted to deceased lines) + one written research question. No question, no searching.

### Phase 1 — Locality & era research (before searching the person)
Build the context that makes records findable: jurisdiction history and boundary changes, what records were created/kept/destroyed for that place and era, languages, religions, naming customs, calendar in use, migration drivers, gazetteers/maps. Read [references/source-matrix.md](references/source-matrix.md) and fill the locality section of `01-plan.md`.
**Gate:** a written list of which record sets *should* exist for this person, where each lives, and its access limits (paywall, on-site only, not digitised — say so honestly; never pretend to have accessed a paywalled/on-site source you could not open. Give the user exact instructions to retrieve it instead).

### Phase 2 — Research plan
Turn Phase 1 into an ordered plan in `01-plan.md`: question → hypotheses (including the null: "the accepted story is wrong") → record sets in priority order → name variants & search strings (wildcards, phonetic, OCR-error forms, maiden/married/alias, patronymics) → FAN club targets (Family, Associates, Neighbours — plus witnesses, godparents, executors, fellow passengers, regiment/workmates).
**Gate:** at least one alternative hypothesis and one FAN target listed. A plan with only "confirm what we believe" fails.

### Phase 3 — Reasonably exhaustive search
Work the plan. For each search, log in `02-log.md`: date, repository/collection, exact search terms, years covered, result (including **nil**), and next step. Prefer in this order: original records/images > derivatives (indexes, transcriptions) > authored trees/narratives. Check every applicable row of the source matrix — vital, census/substitutes, church, cemetery, probate, land/tax, court, military, migration/naturalisation, newspapers, directories, maps, occupation, poor-relief/institutional, DNA — or log why a row does not apply. Cluster/FAN research is mandatory when direct records stall.
**Gate:** every matrix row is `found`, `searched–nil`, or `n/a + reason`. Until then, use "so far," never "there is no record."

### Phase 4 — Evidence analysis
For each item, complete a row in `04-evidence.md`: citation (Evidence Explained style: what, where created, where accessed, image/index/transcription), source class (Original/Derivative/Authored), information class (Primary/Secondary/Indeterminate), evidence class (Direct/Indirect/Negative), informant and their likely knowledge, and legibility/alteration notes. Build `03-timeline.md` — every dated event with place-as-it-was-then, age at event (compute it; flag impossibilities: mother aged 12 or 55, events after death, two places same day).
**Gate:** timeline has no unexplained impossibility; every key claim has ≥1 analysed evidence row.

### Phase 5 — Correlation, conflict resolution & proof
Correlate across records; resolve conflicts in `07-conflicts.md` (state both claims, weigh informant/source quality/contemporaneity, conclude or leave open). Apply the same-person test (Hard Rule 3) explicitly for every merge. Write the proof argument for the research question: question → evidence → analysis → resolution → conclusion with confidence label. Methods and worked patterns: [references/methods.md](references/methods.md).
**Gate (GPS):** reasonably exhaustive search ✓ · complete, accurate citations ✓ · thorough analysis & correlation ✓ · conflicts resolved ✓ · soundly reasoned written conclusion ✓. All five, or the answer is labelled `PROBABLE`/`POSSIBLE` with the missing element named.

### Phase 6 — DNA (only if relevant and consented)
Read [references/dna.md](references/dna.md) fully before starting — and [references/raw-dna-files.md](references/raw-dna-files.md) whenever a DNA *file* is involved (consumer raw downloads, CRAM/BAM/SAM, VCF/gVCF/BCF, FASTQ, PLINK). Work in `05-dna.md`: test(s) and company, total/segment data as *reported* (never estimated), shared-match clustering (Leeds method), triangulation, documentary trees for matches, WATO/hypothesis testing for unknown parentage, and explicit handling of endogamy, pedigree collapse, small segments and misattributed parentage. State statistical limits plainly (e.g. ranges of cM per relationship, half- vs full- ambiguity).
**Raw-file discipline (files are evidence, not chat attachments):** checksum (SHA-256) and inventory every file before analysis, keep originals read-only in `sources/dna/<tester-code>/` and work only on copies, detect format/build from headers with a real tool (`scripts/dna_file_check.py`; samtools/bcftools for CRAM/BAM/VCF — see the raw-files reference for the CRAM reference-genome, lossy-compression, and conversion rules), log tool names/versions/commands/references, and never upload any file anywhere without the test-taker's consent for that destination. Never commit raw DNA files to git.
**Gate:** every DNA-based kinship claim names its documentary corroboration, or is capped at `POSSIBLE`; every DNA file has a checksum + format/build inventory row, or it has not been used.

### Phase 7 — Red-team pass (mandatory, adversarial)
Argue *against* your own conclusion before delivering: Could this be a same-name impostor? A step/adoptive/foster relationship recorded as biological? A clerical, OCR or informant error? A woman's record under another surname? A boundary/calendar error making two people look like one? Try to find a record that would *falsify* the conclusion and log the attempt. Re-run `scripts/audit_dossier.py` (below).
**Gate:** falsification attempts logged; surviving contradictions disclosed, not buried.

### Phase 8 — Dossier & delivery
Write `06-dossier.md` from `templates/person-dossier.md`: a readable biography woven from *only* cited claims, with confidence labels visible, a timeline, family group, source list, unresolved questions, and a "next searches" list for anything left open. Deliver to the user: (1) the answer to the research question in ≤10 lines with its confidence label, (2) what proves it, (3) what remains unproven, (4) where the dossier lives, (5) exact retrieval instructions for any source you could not access. Offer, don't assume: family-tree import (GEDCOM notes), cemetery/photo follow-ups, archive order requests.

## Detective & journalist overlays (apply throughout)

- **Timeline gaps are leads.** A missing decade, a child with a 4-year gap, a sudden relocation — investigate, don't smooth over.
- **Follow assets and paper:** probate, land, tax, court, debt, licenses, employment, union/church membership, inquests, asylum/prison/poorhouse registers often name kin when vital records don't.
- **Witnesses are family in disguise:** marriage witnesses, baptism sponsors, informants on death certificates, executors, next-of-kin in military files — identify every one.
- **Newspapers beyond obituaries:** court reports, accidents, land sales, missing-person and "information wanted" ads, social notes, shipping arrivals.
- **Two-source rule** for any biographical claim that would embarrass or surprise (crime, illegitimacy, desertion, bigamy): two *independent* records, or label `POSSIBLE` and present neutrally.
- **Verify the verifier:** who created this tree/index/transcription, from what, with what error rate? Unsourced online trees are tip sheets, never evidence.

## Token discipline (secondary to thoroughness)

- Load **one** reference file per phase, only when entering that phase.
- Search results go into `02-log.md` in compact table rows as you work; summarise in chat, never paste raw result dumps.
- Refer to claims, people and sources by ID (`C012`, `P003`, `S021`) after first definition.
- End every session by updating the dossier's status block (question, confidence, open items) so the next session resumes from files in minutes.
- If context is running low, finish the current log/template updates first, then summarise — the files, not the chat, carry the research.

## Tools in this skill

```bash
python3 scripts/scaffold_case.py "Full Name" [--birth YYYY] [--death YYYY] [--place "..."] [--out research/]
python3 scripts/audit_dossier.py research/<person>/      # uncited claims, missing GPS gates, unresolved conflicts, impossible ages
python3 scripts/kinship.py age 1842-03-01 1911-11-20      # exact age at an event/death
python3 scripts/kinship.py relation 3 5                    # relationship of two descendants to a common ancestor (gens from ancestor)
python3 scripts/kinship.py soundex "Kowalski"              # + variant hints for search planning
python3 scripts/dna_file_check.py <dna-file>               # detect CRAM/BAM/VCF/FASTQ/genotype format, build, counts — read-only, no network
sha256sum <dna-file>                                       # checksum before any DNA analysis; record in 05-dna.md
samtools quickcheck -v file.cram && samtools view -H file.cram   # CRAM integrity + reference (@SQ M5/UR) — see references/raw-dna-files.md
```

Audit failures block a `PROVEN` conclusion until fixed or explicitly waived with a written reason in the dossier.

## Quick-start prompts the user can give

- "Research [name], born about …, died …, my [relationship]. Question: who were his parents?"
- "Brick-wall: find [name]'s birthplace/maiden name/immigration."
- "DNA: I have matches X, Y at …cM — how are we related to [ancestor]?"
- "Audit this tree/dossier for proof before I share it." → run Phases 4–5 + 7 on the provided material; report claim-by-claim.

## Reference map (load on demand)

| Need | File |
|---|---|
| Record types, repositories, era/place coverage, substitutes | [references/source-matrix.md](references/source-matrix.md) |
| GPS, evidence classes, same-person test, conflict & brick-wall methods, naming/calendar pitfalls | [references/methods.md](references/methods.md) |
| atDNA/Y-DNA/mtDNA, clustering, triangulation, WATO, endogamy, sensitive results | [references/dna.md](references/dna.md) |
| Raw DNA files: CRAM/BAM/SAM, VCF, FASTQ, consumer genotype TXT/CSV — validation, conversion, samtools/bcftools, build & privacy rules | [references/raw-dna-files.md](references/raw-dna-files.md) |
| Deceased-only scope, living people, DNA privacy, sensitive findings, cultural/Indigenous records | [references/ethics-and-privacy.md](references/ethics-and-privacy.md) |
| Intake, plan, log, timeline, evidence, conflicts, DNA worksheet, dossier | [templates/](templates/) |
| A complete fictional worked example (all names invented) | [examples/fictional-mini-case.md](examples/fictional-mini-case.md) |
