#!/usr/bin/env python3
"""Name-column OCR assist for 1930 Berea Town 76-16."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from PIL import Image

DIR = Path("/workspace/research/dora-ella-newnam/sources/census/pass93/madison1930")
OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass93/berea16-ocr.txt")
CROP = Path("/tmp/pass93-ocr")
CROP.mkdir(exist_ok=True)

PAT = re.compile(
    r"newm|newn|noonan|nunan|frank|david|mccoy|\bcoy\b|grant",
    re.I,
)


def main() -> None:
    leaves = []
    for n in range(336, 380):
        p = DIR / f"t626-769-leaf{n:04d}-w1200.jpg"
        if p.exists():
            leaves.append(p)
    hits: list[str] = []
    scanned = 0
    for img in leaves:
        scanned += 1
        im = Image.open(img)
        w, h = im.size
        box = (int(w * 0.07), int(h * 0.16), int(w * 0.38), int(h * 0.92))
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
    OUT.write_text(f"scanned={scanned} hit_files={len(hits)}\n\n" + "\n".join(hits))
    print(f"WROTE {OUT} hit_files={len(hits)}", flush=True)


if __name__ == "__main__":
    main()
