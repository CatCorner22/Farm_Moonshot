# Dora Ella Newnam Stone — biography books

Two complementary readings of the same case file. Neither invents a portrait of Dora. Living descendants are not named.

## Illustrated HTML book (this PR)

Open **[index.html](index.html)** in any browser. Print to PDF from the browser (File → Print → Save as PDF). Photographs, charts, and endnotes travel with the file.

Every factual sentence carries a numbered endnote (1–74). Endnotes, the source appendix, and the plate list name the creator, repository, whether the *image* or a *transcription* was read, and a link when one exists.

**No portrait of Dora** is in the case file or in the user’s Google Drive as of 28 October 2026 (America/New_York). The plates are public-domain federal census and Soundex images, Library of Congress / HABS / FSA photographs, and Wikimedia Commons place views. Public photographs show her country, not her face. Social Security numbers are omitted.

Plates live in `plates/`. Charts were generated from `../family.json` and `../visuals/life.csv`.

## Markdown / PDF book (from main)

Master narrative (edit this; then rebuild):

- [`Dora-Ella-Newnam-Stone-A-Life.md`](Dora-Ella-Newnam-Stone-A-Life.md)

Compiled PDF with the NARA plate gallery and the four family charts:

- [`Dora-Ella-Newnam-Stone-A-Life.pdf`](Dora-Ella-Newnam-Stone-A-Life.pdf)

Rebuild from the repository root:

```bash
python3 scripts/build_dora_book.py    # PDF + image gallery + Word (.docx)
python3 scripts/build_dora_word.py    # Word only from the same markdown
```

Master Word document (regenerate after editing the markdown):

- [`Dora-Ella-Newnam-Stone-A-Life.docx`](Dora-Ella-Newnam-Stone-A-Life.docx)

The biography builder also rewrites [`../12-image-gallery.md`](../12-image-gallery.md) from `scripts/dora_plates.py`. Chat inventory: [`../13-chat-review.md`](../13-chat-review.md).

## Source and document index (Word)

Complete index of every document used in the investigation — table of contents, class finding aid, full citation for every S-number, every DOC transcription, every plate, every file under `sources/`, and a claim-to-source crosswalk:

- [`Dora-Ella-Newnam-Stone-Source-Index.docx`](Dora-Ella-Newnam-Stone-Source-Index.docx)

Rebuild from the repository root:

```bash
python3 scripts/build_dora_source_index_docx.py
```

Open the file in Microsoft Word and update the table-of-contents field if asked. A reader’s outline with every chapter title is included so the file is usable without Word.
