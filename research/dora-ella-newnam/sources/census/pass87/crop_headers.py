#!/usr/bin/env python3
"""Crop ED box / place / name-column bands from pass-87 leaves."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps

SRC = Path("/workspace/research/dora-ella-newnam/sources/census/pass87")
OUT = SRC / "crops"
OUT.mkdir(parents=True, exist_ok=True)


def crop_bands(path: Path) -> None:
    im = Image.open(path).convert("L")
    # invert if mostly dark (BookReader sometimes serves inverted)
    extrema = im.getextrema()
    if extrema[0] + extrema[1] < 200 or (sum(im.resize((40, 40)).getdata()) / 1600) < 80:
        im = ImageOps.invert(im)
    w, h = im.size
    # skip large black margins: find content bbox
    bw = im.point(lambda p: 255 if p > 40 else 0)
    box = bw.getbbox()
    if box:
        im = im.crop(box)
        w, h = im.size
    # header band (top ~18%)
    hdr = im.crop((0, 0, w, int(h * 0.18)))
    hdr = ImageEnhance.Contrast(hdr).enhance(1.8)
    hdr.save(OUT / f"{path.stem}-hdr.png")
    # ED box is upper-right of header
    ed = hdr.crop((int(w * 0.55), 0, w, hdr.size[1]))
    ed.save(OUT / f"{path.stem}-ed.png")
    # place / county left of header
    place = hdr.crop((0, 0, int(w * 0.55), hdr.size[1]))
    place.save(OUT / f"{path.stem}-place.png")
    # name column roughly 8–28% width, below header
    names = im.crop((int(w * 0.07), int(h * 0.16), int(w * 0.32), int(h * 0.96)))
    names = ImageEnhance.Contrast(ImageOps.autocontrast(names)).enhance(1.6)
    names.save(OUT / f"{path.stem}-names.png")
    print(f"cropped {path.name} {w}x{h}")


def main() -> None:
    files = sorted(SRC.glob("*.jpg"))
    for p in files:
        try:
            crop_bands(p)
        except Exception as e:
            print(f"ERR {p.name}: {e}")


if __name__ == "__main__":
    main()
