# Dora Ella Newnam Stone — Master Biography Book

Open **[index.html](index.html)** in any browser. Print to PDF from the browser (File → Print → Save as PDF) for a paper copy. Photographs, charts, and endnotes travel with the file.

This book is the Phase 8 biography for the case folder `research/dora-ella-newnam/`. Every factual sentence carries a numbered endnote. Confidence labels follow the Genealogical Proof Standard used in the case files. Endnotes, the source appendix, and the plate list name the creator, repository, whether the *image* or a *transcription* was read, and a link when one exists.

**No portrait of Dora** is in the case file or in the user’s Google Drive as of 28 October 2026 (America/New_York). The plates are public-domain federal census and Soundex images, Library of Congress / HABS / FSA photographs, and Wikimedia Commons place views. Public photographs show her country, not her face.

Living people are redacted. Descendants born after about 1926 are not named. Social Security numbers are omitted.

## Contents

Preface · The country of Three Forks · childhood (1880) · marriage (1885) · children (1900) · the lost decade · Arkansas and T. A. Stone · death (1926) · after she was gone · what the records will not say · family group · timeline · charts · documentary plates · conflicts · unread sources · endnotes 1–67 · source appendix · plate credits.

## How this file was built

`index.html` is the book. Plates live in `plates/`. Charts were generated from `../family.json` and `../visuals/life.csv`. Census crops come from `../sources/census/` and `../sources/soundex/`.
# Biography book

Master narrative (edit this; then rebuild):

- [`Dora-Ella-Newnam-Stone-A-Life.md`](Dora-Ella-Newnam-Stone-A-Life.md)

Compiled PDF with all 61 plates and the four family charts:

- [`Dora-Ella-Newnam-Stone-A-Life.pdf`](Dora-Ella-Newnam-Stone-A-Life.pdf)

Rebuild from the repository root:

```bash
python3 scripts/build_dora_book.py
```

The builder also rewrites [`../12-image-gallery.md`](../12-image-gallery.md) from `scripts/dora_plates.py`. Chat inventory: [`../13-chat-review.md`](../13-chat-review.md).
