#!/usr/bin/env python3
"""Isolate Breckinridge Dist 1 100A/100B and 108A/108B."""
from __future__ import annotations

import ssl
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path("/workspace/research/dora-ella-newnam")
CENS = ROOT / "sources/census/pass138"
FULL = CENS / "fulls"
KEY = CENS / "keyplates"
NAMES = CENS / "namecols"
for p in (FULL, KEY, NAMES):
    p.mkdir(parents=True, exist_ok=True)

CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (compatible; DoraGenealogyResearch/1.0)"
ITEM = "populationschedu0193unix"


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


def crop_save(src: Path, box, dest: Path, contrast: float = 1.55) -> None:
    if not src.exists() or src.stat().st_size < 80000:
        return
    im = Image.open(src)
    w, h = im.size
    l, t, r, b = box
    crop = im.crop((int(w * l), int(h * t), int(w * r), int(h * b)))
    crop = ImageEnhance.Contrast(crop).enhance(contrast)
    dest.parent.mkdir(parents=True, exist_ok=True)
    crop.save(dest, quality=92)


def grab(leaf: int, tag: str, w: int = 1800) -> Path:
    dest = FULL / f"{tag}-n{leaf:04d}-w{w}.jpg"
    url = f"https://archive.org/download/{ITEM}/page/leaf{leaf:04d}_w{w}.jpg"
    st, n = fetch(url, dest)
    print(f"  {tag} n{leaf:04d} {st} {n}", flush=True)
    if dest.exists() and dest.stat().st_size > 80000:
        crop_save(dest, (0.02, 0.00, 0.98, 0.16), KEY / f"{tag}-n{leaf:04d}-header.jpg")
        crop_save(dest, (0.68, 0.00, 1.00, 0.16), KEY / f"{tag}-n{leaf:04d}-stamp.jpg")
        crop_save(dest, (0.06, 0.10, 0.62, 0.99), NAMES / f"{tag}-n{leaf:04d}-names.jpg")
    time.sleep(0.05)
    return dest


print("=== Breckinridge Dist 1 100 / 108 ===", flush=True)
for leaf, tag in [
    (398, "breck100"),
    (399, "breck100"),
    (400, "breck101"),
    (413, "breck108"),
    (414, "breck108"),
    (415, "breck108"),
    (416, "breck108"),
]:
    grab(leaf, tag)

print("ISOLATE DONE", flush=True)
