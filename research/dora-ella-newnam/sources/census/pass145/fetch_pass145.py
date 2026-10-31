#!/usr/bin/env python3
"""Pass 145: B058 one catalog; B071 Franklin Dist 1+2 remaining
visual close (n0150–n0355). n0148 = Floyd (do not walk).
n0356+ = Gallatin Warsaw (do not walk). Do not repeat NEWLAND n0340.
Then Mercer / Lincoln Dist 1 / Hopkins / Larue if time."""
from __future__ import annotations

import ssl
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageOps

ROOT = Path("/workspace/research/dora-ella-newnam")
CAT = ROOT / "sources/catalog"
CENS = ROOT / "sources/census/pass145"
FULL = CENS / "fulls"
KEY = CENS / "keyplates"
NAMES = CENS / "namecols"
SUR = CENS / "surnames"
MON = CENS / "montages"
PRIOR = [
    ROOT / "sources/census" / f"pass{n}"
    for n in range(145, 129, -1)
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


def contact(srcs: list[Path], dest: Path, cols: int = 4, thumb_w: int = 420) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    tiles = []
    for p in srcs:
        try:
            im = Image.open(p).convert("L")
        except Exception:
            continue
        nh = int(im.height * thumb_w / max(im.width, 1))
        im = im.resize((thumb_w, max(nh, 1)), Image.Resampling.LANCZOS)
        label = Image.new("L", (thumb_w, im.height + 22), 255)
        label.paste(im, (0, 22))
        d = ImageDraw.Draw(label)
        d.text((4, 2), p.name.replace("-sur.jpg", ""), fill=0)
        tiles.append(label)
    if not tiles:
        return
    rows = (len(tiles) + cols - 1) // cols
    row_h = [0] * rows
    for i, t in enumerate(tiles):
        r = i // cols
        row_h[r] = max(row_h[r], t.height)
    canvas = Image.new("L", (thumb_w * cols, sum(row_h)), 255)
    y = 0
    for r in range(rows):
        x = 0
        for c in range(cols):
            i = r * cols + c
            if i < len(tiles):
                canvas.paste(tiles[i], (x, y))
            x += thumb_w
        y += row_h[r]
    canvas.save(dest, quality=86)
    print(f"contact {dest.name} {len(tiles)} {canvas.size}", flush=True)


print("=== B058 / OPEN catalogs ===", flush=True)
for name, url in [
    ("loc-sn89051008-pass145.json",
     "https://www.loc.gov/item/sn89051008/?fo=json"),
    ("ia-solr-postdispatch-1926-pass145.json",
     "https://archive.org/advancedsearch.php?q=title%3A%28Dardanelle%20Post-Dispatch%29%20AND%20year%3A1926&fl[]=identifier&fl[]=title&fl[]=year&output=json&rows=8"),
    ("gt-lee-wwi-pass145.html",
     "https://www.genealogytrails.com/ken/lee/wwi_draft_cards.html"),
    ("fs-1146342-pass145.html",
     "https://www.familysearch.org/search/catalog/1146342"),
    ("usgennet-lee-wills-pass145.html",
     "https://usgennet.org/usa/ky/county/lee/wills/"),
    ("hutchins-faq-9938-pass145.html",
     "https://libraryanswers.berea.edu/faq/9938"),
    ("ia-meta-602-pass145.json",
     "https://archive.org/metadata/14thcensusofpopu0602unit"),
    ("ia-solr-m1509-ky-pass145.json",
     "https://archive.org/advancedsearch.php?q=M1509%20AND%20%28Kentucky%20OR%20KY45%20OR%20KY74%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
]:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=45)
    print(f"  {name} {st} {n}", flush=True)

print("=== leftover western compiled (Franklin + Mercer) ===", flush=True)
for name, url in [
    ("kygenweb-franklin-census-pass145.html",
     "https://kygenweb.net/franklin/census.html"),
    ("us-census-franklin-1850-pass145.html",
     "https://www.us-census.org/pub/usgenweb/census/ky/franklin/1850/"),
    ("gt-franklin-census-pass145.html",
     "https://www.genealogytrails.com/ken/franklin/census.html"),
    ("usgw-franklin-toc-pass145.html",
     "https://www.usgwarchives.net/ky/franklin/toc.html"),
    ("sk-franklin-1850-pass145.html",
     "https://www.skcensus.com/1850-census-index-franklin-county-kentucky/"),
    ("ia-solr-franklin-1850indx-pass145.json",
     "https://archive.org/advancedsearch.php?q=%28franklin%20AND%20kentucky%20AND%20%281850indx%20OR%20%221850%20census%22%29%29&fl[]=identifier&fl[]=title&output=json&rows=10"),
    ("kykinfolk-franklin-pass145.html",
     "https://kykinfolk.com/franklin/census.htm"),
    ("wayback-sk-franklin-pass145.html",
     "https://web.archive.org/web/2024/https://www.skcensus.com/1850-census-index-franklin-county-kentucky/"),
    ("kygenweb-mercer-census-pass145.html",
     "https://kygenweb.net/mercer/census.html"),
    ("us-census-mercer-1850-pass145.html",
     "https://www.us-census.org/pub/usgenweb/census/ky/mercer/1850/"),
    ("gt-mercer-census-pass145.html",
     "https://www.genealogytrails.com/ken/mercer/census.html"),
    ("sk-mercer-1850-pass145.html",
     "https://www.skcensus.com/1850-census-index-mercer-county-kentucky/"),
]:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=35)
    print(f"  {name} {st} {n}", flush=True)

print("=== map n0149 (Floyd/Franklin bound) ===", flush=True)
grab("populationschedu0200unix", 149, "franklin")

print("=== crop Franklin Dist 1+2 surnames n0150–n0355 ===", flush=True)
need = []
surs = []
for leaf in range(150, 356):
    dest = SUR / f"franklin-n{leaf:04d}-sur.jpg"
    if dest.exists() and dest.stat().st_size > 2000:
        surs.append(dest)
        continue
    existing = find_best("franklin", leaf, ("surnames",))
    if existing and existing.stat().st_size > 2000:
        dest.write_bytes(existing.read_bytes())
        surs.append(dest)
        continue
    nc = find_best("franklin", leaf, ("namecols",))
    if nc:
        surname_from_namecol(nc, dest)
    else:
        full = find_best("franklin", leaf, ("fulls",))
        if full:
            crop_save(full, (0.14, 0.11, 0.46, 0.99), dest, 1.65)
    if dest.exists() and dest.stat().st_size > 2000:
        surs.append(dest)
    else:
        need.append(leaf)
print(f"  have {len(surs)} need {len(need)} {need[:40]}", flush=True)
for leaf in need:
    grab("populationschedu0200unix", leaf, "franklin")
    dest = SUR / f"franklin-n{leaf:04d}-sur.jpg"
    if dest.exists() and dest.stat().st_size > 2000:
        surs.append(dest)

# refresh list
surs = sorted(SUR.glob("franklin-n*-sur.jpg"), key=lambda p: p.name)
surs = [p for p in surs if 150 <= int(p.name.split("-n")[1][:4]) <= 355 and p.stat().st_size > 2000]
print(f"  franklin Dist1+2 surname crops {len(surs)}/206", flush=True)

print("=== Dist 1 / Dist 2 / Gallatin bound headers ===", flush=True)
for leaf in (148, 149, 150, 255, 256, 355, 356):
    hdr = find_best("franklin", leaf, ("keyplates",))
    print(f"  header n{leaf:04d} {hdr}", flush=True)

print("=== contact sheets Dist 1 n0150–n0255 / Dist 2 n0256–n0355 ===", flush=True)
d1 = [p for p in surs if 150 <= int(p.name.split("-n")[1][:4]) <= 255]
d2 = [p for p in surs if 256 <= int(p.name.split("-n")[1][:4]) <= 355]
for label, chunk in (("d1", d1), ("d2", d2)):
    for i in range(0, len(chunk), 8):
        part = chunk[i : i + 8]
        lo = part[0].name.split("-n")[1][:4]
        hi = part[-1].name.split("-n")[1][:4]
        contact(part, MON / f"franklin-{label}-{lo}-{hi}.jpg", cols=4, thumb_w=400)

print("DONE pass145 fetch", flush=True)
