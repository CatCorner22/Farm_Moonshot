#!/usr/bin/env python3
"""Pass 128b: remap Scott 399B Dist 1 + 475-476 Newham; crop plates."""
from __future__ import annotations

import ssl
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path("/workspace/research/dora-ella-newnam")
CAT = ROOT / "sources/catalog"
CENS = ROOT / "sources/census/pass128"
FULL = CENS / "fulls"
KEY = CENS / "keyplates"
NAMES = CENS / "namecols"
HDR = CENS / "headers"
for p in (CAT, FULL, KEY, NAMES, HDR):
    p.mkdir(parents=True, exist_ok=True)

CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (compatible; DoraGenealogyResearch/1.0)"


def fetch(url: str, dest: Path, timeout: int = 45) -> tuple[int, int]:
    if dest.exists() and dest.stat().st_size > 800:
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


def ia_leaf(item: str, leaf: int, w: int = 1400) -> str:
    return f"https://archive.org/download/{item}/page/leaf{leaf:04d}_w{w}.jpg"


print("=== catalogs remaining ===", flush=True)
catalogs = [
    ("us-census-kenton-idx-pass128b.html",
     "https://us-census.org/pub/usgenweb/census/ky/kenton/1850/"),
    ("us-census-nelson-idx-pass128b.html",
     "https://us-census.org/pub/usgenweb/census/ky/nelson/1850/"),
    ("us-census-franklin-idx-pass128b.html",
     "https://us-census.org/pub/usgenweb/census/ky/franklin/1850/"),
    ("us-census-mercer-idx-pass128b.html",
     "https://us-census.org/pub/usgenweb/census/ky/mercer/1850/"),
    ("wb-kenton-1850-cdx-pass128b.json",
     "https://web.archive.org/cdx/search/cdx?url=files.usgwarchives.net/ky/kenton/census/1850/*&output=json&limit=30"),
    ("wb-nelson-1850-cdx-pass128b.json",
     "https://web.archive.org/cdx/search/cdx?url=files.usgwarchives.net/ky/nelson/census/1850/*&output=json&limit=30"),
    ("wb-scott-1850-cdx-pass128b.json",
     "https://web.archive.org/cdx/search/cdx?url=files.usgwarchives.net/ky/scott/census/1850/*&output=json&limit=30"),
    ("kygenweb-lincoln-census-pass128b.html",
     "https://kygenweb.net/lincoln/census.htm"),
    ("usgw-lincoln-1850-pass128b.html",
     "https://www.usgwarchives.net/ky/lincoln/census/1850/"),
    ("wb-lincoln-census-cdx-pass128b.json",
     "https://web.archive.org/cdx/search/cdx?url=files.usgwarchives.net/ky/lincoln/census/*&output=json&limit=30"),
    ("kykinfolk-lincoln-marr-pass128b.html",
     "https://www.kykinfolk.com/lincoln/marriages.htm"),
    ("mytrees-william-rhoda-pass128b.html",
     "https://www.mytrees.com/"),
]
for name, url in catalogs:
    st, n = fetch(url, CAT / name, timeout=35)
    print(f"  {name} {st} {n}", flush=True)
    time.sleep(0.1)

print("=== Scott Dist 1 stamp 399 window n0258-n0274 ===", flush=True)
for leaf in range(258, 275):
    dest = HDR / f"r218-n{leaf:04d}-w900.jpg"
    st, n = fetch(ia_leaf("populationschedu0218unix", leaf, 900), dest, timeout=40)
    print(f"  r218 n{leaf:04d} d1 {st} {n}", flush=True)
    time.sleep(0.07)

print("=== Scott Newham 475-476 n0410-n0418 + 480B n0425 ===", flush=True)
for leaf in list(range(410, 419)) + [425, 421, 423]:
    dest = HDR / f"r218-n{leaf:04d}-w900.jpg"
    st, n = fetch(ia_leaf("populationschedu0218unix", leaf, 900), dest, timeout=40)
    print(f"  r218 n{leaf:04d} nh {st} {n}", flush=True)
    time.sleep(0.07)
for leaf in [413, 414, 415, 416, 417, 424, 425, 262, 263, 264, 266]:
    dest = FULL / f"r218-n{leaf:04d}-w1600.jpg"
    st, n = fetch(ia_leaf("populationschedu0218unix", leaf, 1600), dest, timeout=50)
    print(f"  r218 n{leaf:04d} full {st} {n}", flush=True)
    time.sleep(0.1)

print("=== Woodford 462A hi-res if thin ===", flush=True)
for leaf, w in ((254, 2000), (254, 2400), (255, 2000)):
    dest = FULL / f"r222-n{leaf:04d}-w{w}.jpg"
    st, n = fetch(ia_leaf("populationschedu0222unix", leaf, w), dest, timeout=50)
    print(f"  r222 n{leaf:04d} w{w} {st} {n}", flush=True)

print("=== crop keyplates ===", flush=True)


def crop_save(src: Path, box, dest: Path, contrast: float = 1.35) -> None:
    if not src.exists() or src.stat().st_size < 20000:
        print(f"  skip {src.name}", flush=True)
        return
    im = Image.open(src)
    w, h = im.size
    # box is fractions
    l, t, r, b = box
    c = im.crop((int(w * l), int(h * t), int(w * r), int(h * b)))
    c = ImageEnhance.Contrast(c).enhance(contrast)
    dest.parent.mkdir(parents=True, exist_ok=True)
    c.save(dest, quality=85)
    print(f"  wrote {dest.name} {dest.stat().st_size}", flush=True)


src254 = FULL / "r222-n0254-w1600.jpg"
if not src254.exists() or src254.stat().st_size < 800000:
    alt = FULL / "r222-n0254-w2000.jpg"
    if alt.exists() and alt.stat().st_size > src254.stat().st_size if src254.exists() else True:
        src254 = alt if alt.exists() else (HDR / "r222-n0254-w900.jpg")
    else:
        src254 = HDR / "r222-n0254-w900.jpg"
crop_save(src254, (0.04, 0.28, 0.72, 0.48), KEY / "woodford-462a-christopher-newman.jpg")
crop_save(src254, (0.04, 0.06, 0.96, 0.22), KEY / "woodford-462a-header.jpg")

src424 = HDR / "r218-n0424-w900.jpg"
crop_save(src424, (0.04, 0.06, 0.96, 0.22), KEY / "scott-480a-header.jpg")
crop_save(src424, (0.04, 0.18, 0.70, 0.95), KEY / "scott-480a-names.jpg")

print("=== namecols from new fulls ===", flush=True)
for src in sorted(FULL.glob("*.jpg")):
    if src.stat().st_size < 20000:
        continue
    dest = NAMES / f"{src.stem}-names.jpg"
    if dest.exists() and dest.stat().st_size > 4000:
        continue
    try:
        im = Image.open(src)
        w, h = im.size
        crop = im.crop((int(w * 0.05), int(h * 0.08), int(w * 0.55), int(h * 0.98)))
        crop = ImageEnhance.Contrast(crop).enhance(1.3)
        crop.save(dest, quality=82)
    except Exception as e:
        print(f"  crop fail {src.name} {e}", flush=True)
print("  namecols", len(list(NAMES.glob("*.jpg"))), flush=True)
print("DONE fetch_pass128b", flush=True)
