#!/usr/bin/env python3
"""Name-column OCR assist for 1930 Madison Glade 76-18 / 76-19."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from PIL import Image

DIRS = [
    Path("/workspace/research/dora-ella-newnam/sources/census/pass93/madison1930"),
    Path("/workspace/research/dora-ella-newnam/sources/census/pass94/madison1930"),
]
OUT18 = Path("/workspace/research/dora-ella-newnam/sources/census/pass94/glade18-ocr.txt")
OUT19 = Path("/workspace/research/dora-ella-newnam/sources/census/pass94/glade19-ocr.txt")
CROP = Path("/tmp/pass94-ocr")
CROP.mkdir(exist_ok=True)

PAT = re.compile(
    r"newm|newn|noonan|nunan|frank|david|mccoy|\bcoy\b|grant|boyd",
    re.I,
)


def find_leaf(n: int) -> Path | None:
    name = f"t626-769-leaf{n:04d}-w1200.jpg"
    for d in DIRS:
        p = d / name
        if p.exists() and p.stat().st_size >= 8000:
            return p
    return None


def ocr_range(start: int, end: int, out: Path) -> None:
    hits: list[str] = []
    scanned = 0
    missing: list[int] = []
    for n in range(start, end + 1):
        img = find_leaf(n)
        if img is None:
            missing.append(n)
            continue
        scanned += 1
        im = Image.open(img)
        w, h = im.size
        box = (int(w * 0.07), int(h * 0.16), int(w * 0.40), int(h * 0.92))
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
    out.write_text(
        f"scanned={scanned} missing={missing} hit_files={len(hits)}\n\n"
        + "\n".join(hits)
    )
    print(f"WROTE {out} scanned={scanned} hit_files={len(hits)} missing={missing}", flush=True)


def main() -> None:
    ocr_range(394, 429, OUT18)
    ocr_range(430, 465, OUT19)


if __name__ == "__main__":
    main()
