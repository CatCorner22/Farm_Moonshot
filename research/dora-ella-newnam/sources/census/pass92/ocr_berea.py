#!/usr/bin/env python3
"""Name-column OCR assist for Berea Town 102/103 leaves."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from PIL import Image

DIR = Path("/workspace/research/dora-ella-newnam/sources/census/pass92/madison1920")
OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass92/berea-ocr.txt")
CROP = Path("/tmp/pass92-ocr")
CROP.mkdir(exist_ok=True)

PAT = re.compile(
    r"newm|newn|noonan|nunan|frank|david|mccoy|\bcoy\b",
    re.I,
)


def main() -> None:
    leaves = sorted(DIR.glob("t625-590-leaf03{14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52}*.jpg".replace("{", "").replace("}", "")))
    # explicit range 0314-0352
    leaves = []
    for n in range(314, 353):
        p = DIR / f"t625-590-leaf{n:04d}-w1200.jpg"
        if p.exists():
            leaves.append(p)
    hits: list[str] = []
    scanned = 0
    for img in leaves:
        scanned += 1
        im = Image.open(img)
        w, h = im.size
        box = (int(w * 0.07), int(h * 0.18), int(w * 0.36), int(h * 0.90))
        crop = im.crop(box)
        crop = crop.resize((crop.size[0] * 2, crop.size[1] * 2))
        dest = CROP / (img.stem + "-names.jpg")
        crop.save(dest, quality=90)
        r = subprocess.run(
            ["tesseract", str(dest), "stdout", "--psm", "6"],
            capture_output=True, text=True,
        )
        text = r.stdout or ""
        matched = [ln.strip() for ln in text.splitlines() if PAT.search(ln)]
        if matched:
            hits.append(f"## {img.name}\n" + "\n".join(matched) + "\n")
        print(f"{img.name} hits={len(matched)}", flush=True)
    OUT.write_text(
        f"scanned={scanned} hit_files={len(hits)}\n\n" + "\n".join(hits)
    )
    print(f"WROTE {OUT} hit_files={len(hits)}", flush=True)


if __name__ == "__main__":
    main()
