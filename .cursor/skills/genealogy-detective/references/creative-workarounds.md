# Creative workarounds — solve roadblocks yourself first

Load the moment a search fails, access is denied, a record is missing, handwriting is illegible, a paywall appears, or you are tempted to ask the user to "check Ancestry." **Default:** invent and execute the next independent path — do not transfer the problem upstream until you have run the workaround ladder for that blocker type and logged every attempt in `11-backlog.md` (Roadblock log).

Pair with [proactive-autonomy.md](proactive-autonomy.md): autonomy decides *whether* you can act; this file decides *how* to pivot when the obvious path failed.

## Workaround mindset

1. **Reframe the question.** "Who were his parents?" → "Who witnessed his marriage, who sponsored his child's baptism, who bought land from him, who lived next door in 1860, who filed probate when he died?"
2. **Swap record type before swapping person.** No birth record → baptism, census ages, marriage age, death informant, military enlistment, gravestone, obit, delayed birth, sibling's record.
3. **Swap jurisdiction before giving up.** Wrong county → parent county, neighbouring parish, port of entry, last residence before migration, church diocese, military department, state capital index.
4. **Swap identifier before swapping repository.** Surname failed → first name + place; address-only; occupation; spouse's name; wildcard/OCR forms; Soundex (`scripts/kinship.py soundex`); browse without search.
5. **Use destruction as data.** "Registers burned 1922" → what survived (fragments, transcripts, bishop's copies, newspaper substitutes, census, land that wasn't in the courthouse)?
6. **Use absence as data** only after exhaustive, logged search with realistic coverage — then pivot to FAN who *do* appear in complete sets.

## Blocker → workaround ladders (execute in order; log each step)

### A — Paywall / subscription database

| Step | You do (autonomous) |
|---|---|
| A1 | Search **FamilySearch** (free), **Internet Archive**, state archive portals, **Trove/Papers Past/Chronicling America** (free newspapers), catalog-only even if images aren't online |
| A2 | Find the **same collection** under a different site (e.g. index free + order cert; FamilySearch film number → catalog note for on-site) |
| A3 | Hunt **derivative** substitutes in free sources (census, grave index, probate abstract, directory) that answer the same claim |
| A4 | Locate **finding aid** (ArchiveGrid, WorldCat, FamilySearch Catalog, national archive catalogue) — add `blocked` backlog with exact series/vol/page to retrieve, **only after** A1–A3 logged nil |
| Ask user | Only for: account login you cannot perform, payment/card, or a specific cert they already offered to buy — and give the exact catalog citation + fee + what it should prove |

### B — On-site / not digitised / wrong format

| Step | You do |
|---|---|
| B1 | Check if **digitised elsewhere** (FamilySearch affiliate, commercial site, society publication, Google Books county history with transcript) |
| B2 | Search **indexes & abstracts** (county gen web, PERSI-style periodical index, archive online index without images) |
| B3 | Identify **adjacent online records** (tax, land index, court index) that reference the same event |
| B4 | Draft a **copy order** (repository, collection, call number, years, name variants, research question) → mark `deferred` with form URL if exists |
| Ask user | Physical visit or paid copy order **after** B1–B3; hand them a filled order template, not "can you look?" |

### C — No vital record / civil registration too late

| Step | You do |
|---|---|
| C1 | Church registers (denomination + diocese), burial, marriage banns |
| C2 | Census/substitute ages; military; marriage/death ages; passport/naturalisation |
| C3 | **Indirect proof** argument draft from correlated records (`methods.md`) |
| C4 | FAN: parents named on **sibling** or **child** records |
| C5 | DNA plan if applicable (documentary trees for matches first) |

### D — Common name / too many hits

| Step | You do |
|---|---|
| D1 | Add **second identifier** (age ±2, spouse, occupation, birthplace, parent name fragment) |
| D2 | **Cluster** by FAN: restrict to people appearing with known associates |
| D3 | **Timeline filter**: eliminate candidates born after event or dead before |
| D4 | Build **candidate table** (separate P###); disprove each with negative evidence |
| D5 | Land/probate to tie one candidate to a unique parcel or heir set |

### E — Illegible / bad photo / PDF OCR garbage

| Step | You do |
|---|---|
| E1 | `document_inventory.py`; non-destructive enhance on **copy** (rotate, levels, invert, channel split) — log adjustments |
| E2 | Transcribe **legible portions**; extract partial facts; mark rest `[illegible]` |
| E3 | Seek **duplicate creation** (bishop's transcript, published extract, newspaper notice of same event, certificate copy in another file) |
| E4 | Compare letterforms using **same-hand** words elsewhere on page (`paleography.md`) |
| E5 | Name HTR model/community if regular hand — verify every word against image |
| Ask user | **Re-capture** only with exact instructions (dpi, full page, no flash, flatten page) after E1–E4 |

### F — Index says no / database nil

| Step | You do |
|---|---|
| F1 | **Browse** images around date/place without surname search |
| F2 | Search **without surname** (first name + county; address; witness name) |
| F3 | **Variant storm** + neighbouring jurisdiction (see `genealogy-mastery.md`) |
| F4 | Try **derivative** creator (transcriber error): reversed names, misread letters |
| F5 | Second repository holding **same event type** |

### G — Language / script beyond your skill

| Step | You do |
|---|---|
| G1 | Identify script/period; extract **formula words** and dates/numerals you can read |
| G2 | Free **dictionary** of register terms (baptizavi, geboren, née, hijo legítimo…) |
| G3 | Find **published translation** or bilingual index by genealogical society |
| G4 | Machine translation of **your diplomatic transcription** (label as draft; verify names against other records) |
| Ask user | Professional translator or archive lookup service **after** G1–G3 with specific lines marked |

### H — DNA file/tool missing / match tree empty

| Step | You do |
|---|---|
| H1 | Cluster from **screenshot data** user already gave (cM, segments as stated — never invent) |
| H2 | Build **documentary tree** for matches from public records |
| H3 | Propose **targeted testing** strategy (who to test, why) without pressuring relatives |
| H4 | Install/run `dna_file_check.py`, samtools per `raw-dna-files.md` if file present in workspace |
| Ask user | Upload file, enable consent for specific destination, or test purchase — with one precise ask |

### I — Legal / privacy / living person boundary

| Step | You do |
|---|---|
| I1 | **Shift line** to last deceased generation; redact living |
| I2 | Use records that name deceased only |
| Stop | Contacting living people, bypassing paywalls illegally, scraping behind login, DNA upload without consent |

## Roadblock log (in `11-backlog.md`)

For each blocker, before `blocked` or asking the user:

| Field | Content |
|---|---|
| Blocker ID | R### |
| Type | A–I above |
| What failed | One sentence |
| Steps tried | A1, F2, … with log IDs |
| Next autonomous step | If any remain |
| User only if | Exact single action + citation + what it proves |

**Minimum three workaround steps** from the relevant ladder before status `blocked` or a user message.

## Creative combinations (use often)

- **Sibling + land:** research all siblings; deed from father's estate names heirs.
- **Newspaper + court:** lawsuit over inheritance names non-appearing parent.
- **Directory timeline:** address jump year = migration lead → new county search.
- **Two-country:** emigrant listed in **departure** list and **arrival** list with different spellings.
- **Church transfer letter** when person vanishes from parish.
- **Institutional record** when person "appears" mid-life with no birth.

```bash
python3 scripts/workaround_playbook.py paywall   # prints ladder A1–A4 checklist
python3 scripts/workaround_playbook.py nil-index # prints ladder F1–F5
python3 scripts/workaround_playbook.py list      # all blocker types
```
