#!/usr/bin/env python3
"""Pass 144 Hart Dist 1 remaining evens only — skip hanging catalogs."""
from __future__ import annotations

import ssl
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps

ROOT = Path("/workspace/research/dora-ella-newnam")
CENS = ROOT / "sources/census/pass144"
FULL = CENS / "fulls"
KEY = CENS / "keyplates"
NAMES = CENS / "namecols"
SUR = CENS / "surnames"
for p in (FULL, KEY, NAMES, SUR):
    p.mkdir(parents=True, exist_ok=True)
PRIOR = [ROOT / f"sources/census/pass{n}" for n in (140, 141, 142, 143, 144)]
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


def have(leaf: int) -> bool:
    for d in PRIOR:
        for folder in ("namecols", "fulls", "surnames"):
            p = d / folder
            if not p.exists():
                continue
            for tag in ("hart", "hartmap"):
                for f in p.glob(f"{tag}-n{leaf:04d}*"):
                    if f.stat().st_size > 80000 if folder == "fulls" else 2000:
                        return True
    return False


def crop_save(src: Path, box, dest: Path, contrast: float = 1.55) -> None:
    if dest.exists() and dest.stat().st_size > 2000:
        return
    if not src.exists() or src.stat().st_size < 80000:
        return
    im = Image.open(src)
    w, h = im.size
    l, t, r, b = box
    crop = im.crop((int(w * l), int(h * t), int(w * r), int(h * b)))
    crop = ImageEnhance.Contrast(crop).enhance(contrast)
    dest.parent.mkdir(parents=True, exist_ok=True)
    crop.save(dest, quality=88)


need = [n for n in range(6, 191, 2) if not have(n)]
print(f"Hart evens need {len(need)}: {need}", flush=True)
for leaf in need:
    dest = FULL / f"hart-n{leaf:04d}-w1600.jpg"
    url = f"https://archive.org/download/populationschedu0204unix/page/leaf{leaf:04d}_w1600.jpg"
    st, n = fetch(url, dest)
    print(f"  hart n{leaf:04d} {st} {n}", flush=True)
    if dest.exists() and dest.stat().st_size > 80000:
        crop_save(dest, (0.02, 0.00, 0.98, 0.14), KEY / f"hart-n{leaf:04d}-header.jpg")
        crop_save(dest, (0.70, 0.00, 1.00, 0.14), KEY / f"hart-n{leaf:04d}-stamp.jpg")
        crop_save(dest, (0.07, 0.10, 0.58, 0.99), NAMES / f"hart-n{leaf:04d}-names.jpg")
        crop_save(dest, (0.07, 0.10, 0.72, 0.99), KEY / f"hart-n{leaf:04d}-nameage.jpg")
        crop_save(dest, (0.14, 0.11, 0.46, 0.99), SUR / f"hart-n{leaf:04d}-sur.jpg", 1.65)
    time.sleep(0.03)
print("DONE hart evens", flush=True)
