#!/usr/bin/env python3
"""Crop + OCR Bell ED 28 (0609–0619) and ED 30 (0643–0669)."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageStat

SRC = Path("/workspace/research/dora-ella-newnam/sources/census/pass89")
OUT = SRC / "bell-crops"
OUT.mkdir(exist_ok=True)
LOG = SRC / "bell-ocr.txt"
PAT = re.compile(r"newm|newn|noonan|nunan|newan|newnom|mccoy|m coy", re.I)


def prep(path: Path) -> Image.Image:
    im = Image.open(path).convert("L")
    bw = im.point(lambda p: 255 if p > 70 else 0)
    box = bw.getbbox()
    if box:
        im = im.crop(box)
    if ImageStat.Stat(im).mean[0] < 100:
        im = ImageOps.invert(im)
    return ImageOps.autocontrast(im, cutoff=1)


def main() -> None:
    files = sorted(SRC.glob("t625-559-leaf06*.jpg"))
    rows = []
    hits = []
    for p in files:
        if p.stat().st_size < 8000:
            continue
        im = prep(p)
        w, h = im.size
        hdr = ImageEnhance.Contrast(im.crop((0, 0, w, int(h * 0.16)))).enhance(2.0)
        hdr.save(OUT / f"{p.stem}-hdr.png")
        names = im.crop((int(w * 0.04), int(h * 0.14), int(w * 0.34), h))
        names = ImageEnhance.Contrast(names).enhance(1.8).filter(ImageFilter.SHARPEN)
        dest = OUT / f"{p.stem}-names.png"
        names.save(dest)
        r = subprocess.run(
            ["tesseract", str(dest), "stdout", "--psm", "6"],
            capture_output=True, text=True, timeout=60,
        )
        text = r.stdout or ""
        found = PAT.findall(text)
        line = f"{p.name}\t{len(text)}\thits={found}"
        print(line, flush=True)
        rows.append(line)
        if found:
            hits.append(f"=== {p.name} ===\n{text}\n")
    LOG.write_text("\n".join(rows) + "\n\n" + "".join(hits))
    print(f"DONE files={len(rows)} token_hits={len(hits)}", flush=True)


if __name__ == "__main__":
    main()
