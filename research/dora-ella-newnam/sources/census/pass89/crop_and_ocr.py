#!/usr/bin/env python3
"""Crop name columns from pass89 sheets and Tesseract-sweep Newman variants."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

SRC = Path("/workspace/research/dora-ella-newnam/sources/census/pass89")
OUT = SRC / "crops"
OUT.mkdir(parents=True, exist_ok=True)
LOG = SRC / "ocr-names.txt"

PAT = re.compile(
    r"newm|newn|noonan|nunan|newan|newnom|mccoy|m coy|cora|dora|posa|dosa",
    re.I,
)


def content_crop(im: Image.Image) -> Image.Image:
    extrema = im.getextrema()
    mean = sum(im.resize((48, 48)).getdata()) / (48 * 48)
    if extrema[0] + extrema[1] < 220 or mean < 90:
        im = ImageOps.invert(im)
    bw = im.point(lambda p: 255 if p > 70 else 0)
    box = bw.getbbox()
    if box:
        w, h = im.size
        x0, y0, x1, y1 = box
        pad = 8
        im = im.crop((max(0, x0 - pad), max(0, y0 - pad), min(w, x1 + pad), min(h, y1 + pad)))
    return ImageOps.autocontrast(im, cutoff=1)


def crop_one(path: Path) -> Path:
    dest = OUT / f"{path.stem}-names.png"
    if dest.exists() and dest.stat().st_size > 2000:
        return dest
    im = Image.open(path).convert("L")
    im = content_crop(im)
    w, h = im.size
    hdr = ImageEnhance.Contrast(im.crop((0, 0, w, int(h * 0.16)))).enhance(2.0)
    hdr.save(OUT / f"{path.stem}-hdr.png")
    hdr.crop((int(w * 0.52), 0, w, hdr.size[1])).save(OUT / f"{path.stem}-ed.png")
    hdr.crop((0, 0, int(w * 0.52), hdr.size[1])).save(OUT / f"{path.stem}-place.png")
    names = im.crop((int(w * 0.06), int(h * 0.14), int(w * 0.34), int(h * 0.97)))
    names = ImageEnhance.Contrast(ImageOps.autocontrast(names)).enhance(1.7)
    names = names.filter(ImageFilter.SHARPEN)
    names.save(dest)
    return dest


def ocr(path: Path) -> str:
    r = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", "6"],
        capture_output=True,
        text=True,
        timeout=60,
    )
    return r.stdout or ""


def main() -> None:
    files = sorted(SRC.glob("*.jpg"))
    hits: list[str] = []
    rows: list[str] = []
    for p in files:
        if p.stat().st_size < 8000:
            continue
        try:
            names = crop_one(p)
            text = ocr(names)
            found = PAT.findall(text)
            line = f"{p.name}\t{len(text)}\thits={found}\n"
            rows.append(line)
            if found:
                hits.append(f"=== {p.name} ===\n{text}\n")
            print(line.strip(), flush=True)
        except Exception as e:
            print(f"ERR {p.name}: {e}", flush=True)
    LOG.write_text("".join(rows) + "\n\n" + "".join(hits))
    print(f"WROTE {LOG} files={len(rows)} token_hits={len(hits)}", flush=True)


if __name__ == "__main__":
    main()
