#!/usr/bin/env python3
"""Better name crops: locate the bright schedule, then take the surname band."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageStat

SRC = Path("/workspace/research/dora-ella-newnam/sources/census/pass89")
OUT = SRC / "visual"
OUT.mkdir(exist_ok=True)

WANT = [
    443, 445, 450, 455, 460, 465, 470, 473, 475,
    476, 480, 485, 490, 495, 498,
    500, 505, 510, 512, 513, 514,
    # also a few more Torrent interiors
    447, 452, 458, 462, 468, 472,
]


def bright_box(im: Image.Image):
    bw = im.point(lambda p: 255 if p > 80 else 0)
    box = bw.getbbox()
    return box


def main() -> None:
    for leaf in WANT:
        p = SRC / f"wolfe-leaf{leaf:04d}-w1200.jpg"
        if not p.exists():
            print(f"MISS {leaf}", flush=True)
            continue
        im = Image.open(p).convert("L")
        box = bright_box(im)
        if box:
            im = im.crop(box)
        # if still dark, invert
        mean = ImageStat.Stat(im).mean[0]
        if mean < 100:
            im = ImageOps.invert(im)
        im = ImageOps.autocontrast(im, cutoff=1)
        im = ImageEnhance.Contrast(im).enhance(2.0)
        w, h = im.size
        hdr = im.crop((0, 0, w, int(h * 0.14)))
        hdr.save(OUT / f"w{leaf:04d}-hdr2.png")
        # surname column is left ~8–32% of the bright page
        names = im.crop((int(w * 0.02), int(h * 0.12), int(w * 0.30), h))
        names = ImageEnhance.Brightness(names).enhance(1.25)
        names = names.filter(ImageFilter.SHARPEN)
        names.save(OUT / f"w{leaf:04d}-names2.png")
        print(f"OK {leaf} mean={mean:.0f} {w}x{h}", flush=True)


if __name__ == "__main__":
    main()
