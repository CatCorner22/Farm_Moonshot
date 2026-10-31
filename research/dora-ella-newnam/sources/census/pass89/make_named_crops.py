#!/usr/bin/env python3
"""Make high-contrast name + header crops for visual reading."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

SRC = Path("/workspace/research/dora-ella-newnam/sources/census/pass89")
OUT = SRC / "visual"
OUT.mkdir(exist_ok=True)

# Key leaves: Torrent start/mid/end, Holly start/mid, Stillwater, Clifty, Bell 28/30
WANT = [
    443, 445, 450, 455, 460, 465, 470, 473, 475,
    476, 480, 485, 490, 495,
    498, 500, 505, 510, 512, 513, 514, 515,
]


def enhance(im: Image.Image) -> Image.Image:
    extrema = im.getextrema()
    mean = sum(im.resize((32, 32)).getdata()) / (32 * 32)
    if mean < 95:
        im = ImageOps.invert(im)
    im = ImageOps.autocontrast(im, cutoff=2)
    return ImageEnhance.Contrast(im).enhance(1.8).filter(ImageFilter.SHARPEN)


def main() -> None:
    for leaf in WANT:
        p = SRC / f"wolfe-leaf{leaf:04d}-w1200.jpg"
        if not p.exists():
            print(f"MISS {leaf}", flush=True)
            continue
        im = Image.open(p).convert("L")
        im = enhance(im)
        w, h = im.size
        im.crop((0, 0, w, int(h * 0.18))).save(OUT / f"wolfe-{leaf:04d}-hdr.png")
        im.crop((int(w * 0.05), int(h * 0.13), int(w * 0.36), int(h * 0.98))).save(
            OUT / f"wolfe-{leaf:04d}-names.png"
        )
        print(f"OK {leaf} {w}x{h}", flush=True)


if __name__ == "__main__":
    main()
