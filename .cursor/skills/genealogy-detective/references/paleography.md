# Paleography — reviewing old handwritten primary sources from photos & PDFs

Load whenever a source is a handwritten document supplied or encountered as a photo, scan, or PDF (Phases 3–4, and when the user uploads images). Goal: a defensible transcription — what the document *says*, separated from what you *think it means*.

## Governing rules

1. **Never invent a reading.** Illegible is a finding. Every uncertain character/word is marked (conventions below); a transcription with no uncertainty marks on a difficult hand is presumed over-confident and re-done.
2. **Transcribe first, interpret second, translate third** — three separate layers, kept separate in `08-transcriptions.md`. Never silently modernise, expand, or "correct" inside the transcription layer.
3. **Work from the best image obtainable.** If the supplied photo can't support a reading (blur, glare, cropped margin, low resolution), say exactly what re-capture is needed (below) rather than guessing. Record image provenance: who photographed/scanned it, when, repository/original location, and the file's SHA-256.
4. **The PDF's text layer is not the document.** Embedded OCR/transcription in a PDF is a derivative — verify every relied-upon word against the page image. Treat AI handwriting recognition (HTR) output the same way: a draft to correct, never a source.
5. **Cite the image you read:** file + page/folio + line/entry, image adjustments applied, and whether you saw the original, a scan, or a photo of a screen.

## Intake & image quality control (before reading a word)

Inventory each file with `scripts/document_inventory.py <photo-or-pdf>...` (format, dimensions/pages, resolution clues, SHA-256) and log in `08-transcriptions.md`:

- **Completeness:** whole page including margins, edges, verso, endorsements/dockets, seals, neighbouring entries (context disambiguates hands and formulas). A cropped single-entry photo is a lead; request the full page.
- **Legibility:** focus, contrast, glare over ink, show-through/bleed-through, watermarks vs text, folded/occluded corners. Minimum practical target: handwriting strokes span several pixels — if a letter is 3 pixels tall, request a re-scan (300–600 dpi TIFF/PNG at the archive, or a straight-on, evenly lit phone capture, no flash, page flattened, scale/colour target if allowed).
- **Non-destructive enhancement only, on copies:** rotate/deskew, crop, levels/contrast, invert (helps faded ink/pencil), channel splits for show-through, magnification tiling. Log every enhancement per image; the untouched original stays in `sources/` and any quoted image in the dossier is labelled `enhanced for legibility`.
- **PDF specifics:** extract page images at native resolution rather than screenshotting a viewer (screenshots destroy resolution); note scanned-image vs born-digital, page count vs stated foliation, missing/duplicate pages, and mixed hands across pages. Password/DRM limits: stop and ask the user for a lawfully obtained copy — never circumvent repository restrictions.

## Reading method (two passes minimum)

**Pass 0 — Document before text.** Identify: document type & formulary (registers, deeds, wills follow templates — find the formula and the variable parts become predictable), creating office/parish, date range, language(s), script (below), number of hands, ink/pencil, abbreviations system. Build the locality context from `01-plan.md` first: the expected names/places of this parish are your reading lexicon.

**Pass 1 — Diplomatic transcription.** Line-by-line, preserving spelling, capitalisation, punctuation (or its absence), line/page breaks (`/` and `//`), insertions and deletions noted, money/numerals as written. Expand nothing. Compare letterforms against *the same hand's known words* (the scribe's own alphabet from clear contexts — dates, formula words, the target surname elsewhere on the page) before deciding doubtful letters.

**Pass 2 — Verification.** Re-read against the image at high magnification, ideally after a break; check every name, number, and negative (a missed `not`, `formerly`, `widow of`, or a minim stroke changes genealogy). Where possible, a second independent reading (user, another researcher, or a fresh session re-reading blind from the image, not from your draft) is reconciled difference-by-difference. HTR tools (e.g. Transkribus models, archive-provided AI transcriptions) may *seed* Pass 1 for regular hands — every word still verified against the image, tool + model named in the log.

**Then:** normalised reading (expansions in brackets, modernised punctuation) → translation if needed (translator/tool named; ambiguous terms kept in original with options) → extraction into claims (`04-evidence.md`) quoting the diplomatic text.

## Transcription conventions (use exactly these, state them in the file)

| Mark | Meaning |
|---|---|
| `[?]` after a word/letter | uncertain reading (give alternative in a note if plausible) |
| `[illegible]`, `[illegible — 3 words]` | cannot be read from this image |
| `[—]` | blank/gap left in the original |
| `⟨word⟩` or `[word]` (pick one, state it) | editor-supplied expansion/completion, e.g. `W[illia]m`, `p[ar]ish` |
| `word` struck through in original | render with strikethrough and note `deleted in original` |
| `^word^` | interlineated insertion in original |
| `{word}` | editorial comment only — never original text |
| `[torn]`, `[fold]`, `[ink blot]` | physical cause of loss |
| `...` | **never** used for illegibility (it means trailing off in prose) — use the marks above |

Numbers are double-checked digit-by-digit (minims: i/m/n/u confusion; long-s vs f; secretary-hand e/o; Kurrent e/n/m). Ages, years, and sums of money get an independent second read — they are the highest-impact characters on the page.

## Scripts & languages — know which hand you're in

| Context | Script / features | Starter moves |
|---|---|---|
| England/US pre-1700 | Secretary hand, then mixed italic; Latin in court/church records | Letterform charts for e, h, r, s (long ſ), thorn/abbreviations (`ye` = *the*), per/contractions, £sd money |
| Germany/Austria, to ~1940s | Kurrent, then Sütterlin (from 1915); Fraktur is print, not handwriting | Kurrent letter charts (e/h/m/n traps), umlaut strokes, *geb./gest./unehelich* vocabulary |
| France | Cursive with heavy abbreviation; Republican-calendar dates in 1793–1805 records | Formula of actes (birth/marriage/death templates), *né/décédé*, marginal mentions on birth acts (later marriage/death notes — read margins!) |
| Spain/Latin America | Procesal/cortesana hands, double surnames, *hijo legítimo/natural* distinctions | Act templates, godparent (padrinos) fields, margin notes |
| Scandinavia | Gothic cursive; patronymics, farm names, moving/household-examination columns | Column headings first; clerical survey structure |
| Latin (Catholic/European) | Formulaic registers: *baptizavi, in matrimonium conjunxi, sepultus est* | Learn the 50-word register vocabulary; names Latinised (Gulielmus = William) — record as written, normalise in brackets |
| Cyrillic / Greek / Hebrew / Arabic-script records | Pre-reform orthographies (e.g. Russian pre-1918 letters ѣ/ъ), Hebrew cursive & Yiddish, Ottoman Turkish | Script-specialist letter charts; transliteration standard named; community-archive help sought rather than guessed |
| Anywhere | Personal names Latinised/translated, occupations abbreviated, dit/patronymic systems | Keep original form in transcription; normalisation is a separate, labelled step |

For any script you cannot demonstrably read: produce the image inventory, identify script/language/period, give the user a translation/transcription route (archive service, society, named HTR model or specialist), and mark the claim dependent on it `not yet examined`. A confident wrong reading is worse than none.

## Common traps

- **Formula blindness:** reading the variable name with the certainty of the printed-like formula around it — names get *more* scrutiny, not less.
- **Expectation capture:** "finding" the surname you came for in a minim-scramble. Test the reading against the hand's alphabet and the parish name-stock.
- **Numerals & dates:** regnal years, feast-day dating ("the Monday after Michælmas"), double-dating, fiscal vs calendar years — convert in the interpretation layer with the original preserved.
- **Negatives & qualifiers:** *non, relict(a)* (widow/er), *formerly, late of, alias/dictus, natural child, reputed father* — hunt them deliberately on the second pass.
- **Marginalia & later hands:** endorsements, clerks' later notes, pencil additions by archivists/descendants — different hand = different date/authority; transcribe and attribute separately.
- **Photo artefacts:** page curvature distorting line starts, fingers/book spines occluding margins, auto-"enhancement" filters on phones inventing contrast (request unfiltered originals), mirrored images from camera apps.

## Deliverable per document (in `08-transcriptions.md`)

File inventory + checksum → document identification (type/office/date/language/script/hands) → image-quality verdict (sufficient / re-capture requested: specifics) → diplomatic transcription with conventions → normalised/translation layer if any → extracted facts as claim IDs with the exact quoted words → uncertainties carried forward (a claim resting on a `[?]` reading inherits at most `POSSIBLE` until corroborated).
