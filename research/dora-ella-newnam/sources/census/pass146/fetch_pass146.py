#!/usr/bin/env python3
"""Pass 146: B058 one catalog; B071 Franklin Dist 1 n0203–n0253
+ Dist 2 remaining visual close. Then Mercer / Lincoln Dist 1 /
Hopkins remaining (skip 238/240) / Larue Hamilton / leftover western.
Do not repeat Jeremiah Newman 27 / n0149 / n0355 blank / Gallatin
n0356 / NEWLAND n0340 / Francis J / John 59."""
from __future__ import annotations

import ssl
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageOps

ROOT = Path("/workspace/research/dora-ella-newnam")
CAT = ROOT / "sources/catalog"
CENS = ROOT / "sources/census/pass146"
FULL = CENS / "fulls"
KEY = CENS / "keyplates"
NAMES = CENS / "namecols"
SUR = CENS / "surnames"
MON = CENS / "montages"
PRIOR = [
    ROOT / "sources/census" / f"pass{n}"
    for n in range(146, 129, -1)
]
for p in (CAT, FULL, KEY, NAMES, SUR, MON):
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


def ia_leaf(item: str, leaf: int, w: int = 1600) -> str:
    return f"https://archive.org/download/{item}/page/leaf{leaf:04d}_w{w}.jpg"


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


def grab(item: str, leaf: int, tag: str, w: int = 1600) -> Path:
    dest = FULL / f"{tag}-n{leaf:04d}-w{w}.jpg"
    st, n = fetch(ia_leaf(item, leaf, w), dest)
    print(f"  {tag} n{leaf:04d} {st} {n}", flush=True)
    if dest.exists() and dest.stat().st_size > 80000:
        crop_save(dest, (0.02, 0.00, 0.98, 0.14), KEY / f"{tag}-n{leaf:04d}-header.jpg")
        crop_save(dest, (0.70, 0.00, 1.00, 0.14), KEY / f"{tag}-n{leaf:04d}-stamp.jpg")
        crop_save(dest, (0.07, 0.10, 0.58, 0.99), NAMES / f"{tag}-n{leaf:04d}-names.jpg")
        crop_save(dest, (0.07, 0.10, 0.72, 0.99), KEY / f"{tag}-n{leaf:04d}-nameage.jpg")
        crop_save(dest, (0.14, 0.11, 0.46, 0.99), SUR / f"{tag}-n{leaf:04d}-sur.jpg", 1.65)
    time.sleep(0.04)
    return dest


def find_best(prefix: str, leaf: int, kinds: tuple[str, ...]) -> Path | None:
    pats = [
        f"{prefix}-n{leaf:04d}*",
        f"{prefix}map-n{leaf:04d}*",
    ]
    best = None
    best_n = 0
    for d in [CENS] + PRIOR:
        for folder in kinds:
            p = d / folder
            if not p.exists():
                continue
            for pat in pats:
                for f in p.glob(pat):
                    n = f.stat().st_size
                    if n > best_n and n > 2000:
                        best, best_n = f, n
    return best


def surname_from_namecol(src: Path, dest: Path) -> None:
    if dest.exists() and dest.stat().st_size > 2000:
        return
    if not src.exists() or src.stat().st_size < 2000:
        return
    im = Image.open(src)
    w, h = im.size
    crop = im.crop((int(w * 0.16), int(h * 0.02), int(w * 0.62), int(h * 0.985)))
    crop = ImageOps.autocontrast(crop, cutoff=1)
    crop = ImageEnhance.Contrast(crop).enhance(1.55)
    dest.parent.mkdir(parents=True, exist_ok=True)
    crop.save(dest, quality=88)


def link_or_copy(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 2000:
        return
    try:
        if dest.exists():
            dest.unlink()
        dest.symlink_to(src.resolve())
    except OSError:
        dest.write_bytes(src.read_bytes())


print("=== B058 / OPEN catalogs ===", flush=True)
for name, url in [
    ("loc-sn89051008-pass146.json",
     "https://www.loc.gov/item/sn89051008/?fo=json"),
    ("ia-solr-postdispatch-1926-pass146.json",
     "https://archive.org/advancedsearch.php?q=title%3A%28Dardanelle%20Post-Dispatch%29%20AND%20year%3A1926&fl[]=identifier&fl[]=title&fl[]=year&output=json&rows=8"),
    ("gt-lee-wwi-pass146.html",
     "https://www.genealogytrails.com/ken/lee/wwi_draft_cards.html"),
    ("fs-1146342-pass146.html",
     "https://www.familysearch.org/search/catalog/1146342"),
    ("usgennet-lee-wills-pass146.html",
     "https://usgennet.org/usa/ky/county/lee/wills/"),
    ("hutchins-faq-9938-pass146.html",
     "https://libraryanswers.berea.edu/faq/9938"),
    ("ia-meta-602-pass146.json",
     "https://archive.org/metadata/14thcensusofpopu0602unit"),
    ("ia-solr-m1509-ky-pass146.json",
     "https://archive.org/advancedsearch.php?q=M1509%20AND%20%28Kentucky%20OR%20KY45%20OR%20KY74%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("fishergenes-estill-marr-pass146.html",
     "https://www.fishergenes.com/estill/estill-marriages.htm"),
]:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=45)
    print(f"  {name} {st} {n}", flush=True)

print("=== leftover western compiled (Mercer/Lincoln/Hopkins/Larue) ===", flush=True)
for name, url in [
    ("kygenweb-mercer-census-pass146.html",
     "https://kygenweb.net/mercer/census.html"),
    ("us-census-mercer-1850-pass146.html",
     "https://www.us-census.org/pub/usgenweb/census/ky/mercer/1850/"),
    ("gt-mercer-census-pass146.html",
     "https://www.genealogytrails.com/ken/mercer/census.html"),
    ("sk-mercer-1850-pass146.html",
     "https://www.skcensus.com/1850-census-index-mercer-county-kentucky/"),
    ("usgw-mercer-toc-pass146.html",
     "https://www.usgwarchives.net/ky/mercer/toc.html"),
    ("kykinfolk-mercer-pass146.html",
     "https://kykinfolk.com/mercer/census.htm"),
    ("ia-solr-mercer-1850indx-pass146.json",
     "https://archive.org/advancedsearch.php?q=%28mercer%20AND%20kentucky%20AND%20%281850indx%20OR%20%221850%20census%22%29%29&fl[]=identifier&fl[]=title&output=json&rows=10"),
    ("kygenweb-lincoln-census-pass146.html",
     "https://kygenweb.net/lincoln/census.html"),
    ("us-census-lincoln-1850-pass146.html",
     "https://www.us-census.org/pub/usgenweb/census/ky/lincoln/1850/"),
    ("gt-lincoln-census-pass146.html",
     "https://www.genealogytrails.com/ken/lincoln/census.html"),
    ("sk-lincoln-1850-pass146.html",
     "https://www.skcensus.com/1850-census-index-lincoln-county-kentucky/"),
    ("usgw-lincoln-toc-pass146.html",
     "https://www.usgwarchives.net/ky/lincoln/toc.html"),
    ("kygenweb-hopkins-census-pass146.html",
     "https://kygenweb.net/hopkins/census.html"),
    ("us-census-hopkins-1850-pass146.html",
     "https://www.us-census.org/pub/usgenweb/census/ky/hopkins/1850/"),
    ("gt-hopkins-census-pass146.html",
     "https://www.genealogytrails.com/ken/hopkins/census.html"),
    ("sk-hopkins-1850-pass146.html",
     "https://www.skcensus.com/1850-census-index-hopkins-county-kentucky/"),
    ("kykinfolk-hopkins-pass146.html",
     "https://kykinfolk.com/hopkins/census.htm"),
    ("usgw-hopkins-toc-pass146.html",
     "https://www.usgwarchives.net/ky/hopkins/toc.html"),
    ("kygenweb-larue-census-pass146.html",
     "https://kygenweb.net/larue/census.html"),
    ("us-census-larue-1850-pass146.html",
     "https://www.us-census.org/pub/usgenweb/census/ky/larue/1850/"),
    ("gt-larue-census-pass146.html",
     "https://www.genealogytrails.com/ken/larue/census.html"),
    ("sk-larue-1850-pass146.html",
     "https://www.skcensus.com/1850-census-index-larue-county-kentucky/"),
    ("usgw-larue-toc-pass146.html",
     "https://www.usgwarchives.net/ky/larue/toc.html"),
    ("files-usgw-kenton-1850-pass146.html",
     "https://www.usgwarchives.net/ky/kenton/census/1850/"),
    ("cdx-sk-hart-pass146.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-hart-county-kentucky/&output=json&limit=8"),
    ("cdx-sk-henry-pass146.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-henry-county-kentucky/&output=json&limit=8"),
]:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=28)
    print(f"  {name} {st} {n}", flush=True)

print("=== link Franklin Dist 1 remaining + Dist 2 surnames ===", flush=True)
for leaf in list(range(203, 254)) + list(range(256, 355)):
    src = find_best("franklin", leaf, ("surnames",))
    dest = SUR / f"franklin-n{leaf:04d}-sur.jpg"
    if src:
        link_or_copy(src, dest)
    elif dest.exists() and dest.stat().st_size > 2000:
        pass
    else:
        print(f"  MISS franklin n{leaf:04d}", flush=True)

print("=== 2-up stacks Dist 1 remaining + Dist 2 ===", flush=True)


def stack2(a: Path, b: Path | None, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 4000:
        return
    tiles = []
    for p in (a, b):
        if p is None or not p.exists():
            continue
        im = Image.open(p).convert("L")
        # keep readable width
        tw = 520
        nh = int(im.height * tw / max(im.width, 1))
        im = im.resize((tw, max(nh, 1)), Image.Resampling.LANCZOS)
        tiles.append(im)
    if not tiles:
        return
    h = max(t.height for t in tiles)
    canvas = Image.new("L", (520 * len(tiles) + 8, h), 255)
    x = 0
    for t in tiles:
        canvas.paste(t, (x, 0))
        x += 520 + 4
    canvas.save(dest, quality=86)


d1 = sorted(SUR.glob("franklin-n02*.jpg")) + sorted(SUR.glob("franklin-n0253-sur.jpg"))
# Dist 1 remaining only
d1 = [p for p in sorted(SUR.glob("franklin-n*-sur.jpg")) if 203 <= int(p.name.split("-n")[1][:4]) <= 253]
d2 = [p for p in sorted(SUR.glob("franklin-n*-sur.jpg")) if 256 <= int(p.name.split("-n")[1][:4]) <= 354]
print(f"  d1 {len(d1)} d2 {len(d2)}", flush=True)
for i in range(0, len(d1), 2):
    a = d1[i]
    b = d1[i + 1] if i + 1 < len(d1) else None
    lo = a.name.split("-n")[1][:4]
    hi = (b.name.split("-n")[1][:4] if b else lo)
    stack2(a, b, MON / f"d1stack-{lo}-{hi}.jpg")
for i in range(0, len(d2), 2):
    a = d2[i]
    b = d2[i + 1] if i + 1 < len(d2) else None
    lo = a.name.split("-n")[1][:4]
    hi = (b.name.split("-n")[1][:4] if b else lo)
    stack2(a, b, MON / f"d2stack-{lo}-{hi}.jpg")

print("DONE catalogs + franklin stacks", flush=True)
