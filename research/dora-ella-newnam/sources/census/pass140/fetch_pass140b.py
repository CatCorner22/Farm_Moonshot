#!/usr/bin/env python3
"""Pass 140b: isolate SK-named Newman/Tinker pages —
McCracken 174B, Todd 247A, Trigg 314A + Tinker 303A.
Map reel 211 McCracken and reel 219 Todd/Trigg first."""
from __future__ import annotations

import ssl
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path("/workspace/research/dora-ella-newnam")
CAT = ROOT / "sources/catalog"
CENS = ROOT / "sources/census/pass140"
FULL = CENS / "fulls"
KEY = CENS / "keyplates"
NAMES = CENS / "namecols"
for p in (CAT, FULL, KEY, NAMES):
    p.mkdir(parents=True, exist_ok=True)

CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (compatible; DoraGenealogyResearch/1.0)"


def fetch(url: str, dest: Path, timeout: int = 50) -> tuple[int, int]:
    if dest.exists() and dest.stat().st_size > 200:
        return 200, dest.stat().st_size
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            data = r.read()
            dest.write_bytes(data)
            return getattr(r, "status", 200) or 200, len(data)
    except Exception as e:
        dest.write_text(f"ERR {type(e).__name__}: {e}\n{url}\n")
        return 0, dest.stat().st_size if dest.exists() else 0


def ia_leaf(item: str, leaf: int, w: int = 1800) -> str:
    return f"https://archive.org/download/{item}/page/leaf{leaf:04d}_w{w}.jpg"


def crop_save(src: Path, box, dest: Path, contrast: float = 1.55) -> None:
    if not src.exists() or src.stat().st_size < 80000:
        return
    im = Image.open(src)
    w, h = im.size
    l, t, r, b = box
    crop = im.crop((int(w * l), int(h * t), int(w * r), int(h * b)))
    crop = ImageEnhance.Contrast(crop).enhance(contrast)
    dest.parent.mkdir(parents=True, exist_ok=True)
    crop.save(dest, quality=90)


def grab(item: str, leaf: int, tag: str, w: int = 1800) -> Path:
    dest = FULL / f"{tag}-n{leaf:04d}-w{w}.jpg"
    st, n = fetch(ia_leaf(item, leaf, w), dest)
    print(f"  {tag} n{leaf:04d} {st} {n}", flush=True)
    if dest.exists() and dest.stat().st_size > 80000:
        crop_save(dest, (0.02, 0.00, 0.98, 0.14), KEY / f"{tag}-n{leaf:04d}-header.jpg")
        crop_save(dest, (0.70, 0.00, 1.00, 0.14), KEY / f"{tag}-n{leaf:04d}-stamp.jpg")
        crop_save(dest, (0.07, 0.10, 0.58, 0.99), NAMES / f"{tag}-n{leaf:04d}-names.jpg")
        crop_save(dest, (0.07, 0.10, 0.72, 0.99), KEY / f"{tag}-n{leaf:04d}-nameage.jpg")
    time.sleep(0.03)
    return dest


print("=== reel 211 McCracken map (after Logan) ===", flush=True)
for leaf in [260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500]:
    grab("populationschedu0211unix", leaf, "mccracken")

print("=== reel 219 Todd/Trigg map (after Spencer/Taylor) ===", flush=True)
for leaf in [200, 240, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540]:
    grab("populationschedu0219unix", leaf, "toddtrigg")

print("DONE pass140b map", flush=True)
