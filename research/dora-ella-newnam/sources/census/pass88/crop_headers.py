#!/usr/bin/env python3
"""Crop ED / place / name bands. Find the bright schedule first (Wolfe is dark-margin)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

SRC = Path("/workspace/research/dora-ella-newnam/sources/census/pass88")
# also re-crop pass87 Wolfe w1600 that were margin-dark
ALSO = [
    Path("/workspace/research/dora-ella-newnam/sources/census/pass87/wolfe-leaf0420-w1600.jpg"),
    Path("/workspace/research/dora-ella-newnam/sources/census/pass87/wolfe-leaf0425.jpg"),
    Path("/workspace/research/dora-ella-newnam/sources/census/pass87/wolfe-leaf0430.jpg"),
    Path("/workspace/research/dora-ella-newnam/sources/census/pass87/wolfe-leaf0410-w1600.jpg"),
]
OUT = SRC / "crops"
OUT.mkdir(parents=True, exist_ok=True)


def content_crop(im: Image.Image) -> Image.Image:
    extrema = im.getextrema()
    mean = sum(im.resize((48, 48)).getdata()) / (48 * 48)
    if extrema[0] + extrema[1] < 220 or mean < 90:
        im = ImageOps.invert(im)
    # bright-page detector
    bw = im.point(lambda p: 255 if p > 70 else 0)
    box = bw.getbbox()
    if box:
        # pad slightly
        w, h = im.size
        x0, y0, x1, y1 = box
        pad = 8
        im = im.crop((max(0, x0 - pad), max(0, y0 - pad), min(w, x1 + pad), min(h, y1 + pad)))
    return ImageOps.autocontrast(im, cutoff=1)


def crop_bands(path: Path) -> None:
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
    names.save(OUT / f"{path.stem}-names.png")
    print(f"cropped {path.name} {w}x{h}", flush=True)


def main() -> None:
    files = sorted(SRC.glob("*.jpg")) + ALSO
    for p in files:
        if not p.exists():
            continue
        try:
            crop_bands(p)
        except Exception as e:
            print(f"ERR {p.name}: {e}", flush=True)


if __name__ == "__main__":
    main()
