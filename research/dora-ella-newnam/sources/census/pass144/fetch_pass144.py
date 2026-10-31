#!/usr/bin/env python3
"""Pass 144: B058 one catalog reconfirm; B071 Hart Dist 1 remaining
evens n0006–n0190 visual close + Lincoln Dist 1 remaining + Larue
Hamilton remaining + Franklin/Mercer/Hopkins remaining densify.
Do not repeat closed walks, remaining-odds, BOMAN/NANCE/AMOS/NEWLAND,
Henry Dist 1 / Jesse NORMAN, Todd 247A, Trigg 314A, TINKER 303A,
Kenton 130B compiled Daniel 19, McCracken 174B, Breckinridge,
Graves, Edmonson, Hancock, Hopkins n0238/n0240, stamp 126,
Estill 1930 33-12/33-13. Do not re-ask phones."""
from __future__ import annotations

import ssl
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageOps

ROOT = Path("/workspace/research/dora-ella-newnam")
CAT = ROOT / "sources/catalog"
CENS = ROOT / "sources/census/pass144"
FULL = CENS / "fulls"
KEY = CENS / "keyplates"
NAMES = CENS / "namecols"
SUR = CENS / "surnames"
MON = CENS / "montages"
PRIOR = [
    ROOT / "sources/census/pass140",
    ROOT / "sources/census/pass141",
    ROOT / "sources/census/pass142",
    ROOT / "sources/census/pass143",
    ROOT / "sources/census/pass138",
    ROOT / "sources/census/pass139",
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


def have_leaf(prefix: str, leaf: int) -> Path | None:
    for d in PRIOR + [CENS]:
        for folder in ("namecols", "fulls", "surnames"):
            p = d / folder
            if not p.exists():
                continue
            for f in p.glob(f"{prefix}-n{leaf:04d}*"):
                if f.stat().st_size > 2000:
                    return f
            for f in p.glob(f"{prefix}map-n{leaf:04d}*"):
                if f.stat().st_size > 2000:
                    return f
    return None


def find_namecol(prefix: str, leaf: int) -> Path | None:
    for d in [CENS] + PRIOR:
        p = d / "namecols" / f"{prefix}-n{leaf:04d}-names.jpg"
        if p.exists() and p.stat().st_size > 2000:
            return p
        p = d / "namecols" / f"{prefix}map-n{leaf:04d}-names.jpg"
        if p.exists() and p.stat().st_size > 2000:
            return p
    return None


def find_full(prefix: str, leaf: int) -> Path | None:
    for d in [CENS] + PRIOR:
        for w in (1600, 1800, 1400, 1100):
            for tag in (prefix, f"{prefix}map"):
                p = d / "fulls" / f"{tag}-n{leaf:04d}-w{w}.jpg"
                if p.exists() and p.stat().st_size > 80000:
                    return p
    return None


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


def stack(srcs: list[Path], dest: Path, thumb_w: int = 640) -> None:
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
        d.text((4, 2), p.name.replace("-sur.jpg", "").replace("-names.jpg", ""), fill=0)
        tiles.append(label)
    if not tiles:
        return
    canvas = Image.new("L", (thumb_w, sum(t.height for t in tiles)), 255)
    y = 0
    for t in tiles:
        canvas.paste(t, (0, y))
        y += t.height
    canvas.save(dest, quality=86)
    print(f"stack {dest.name} {len(tiles)} {canvas.size}", flush=True)


print("=== B058 / OPEN catalogs ===", flush=True)
for name, url in [
    ("loc-sn89051008-pass144.json",
     "https://www.loc.gov/item/sn89051008/?fo=json"),
    ("ia-solr-postdispatch-1926-pass144.json",
     "https://archive.org/advancedsearch.php?q=title%3A%28Dardanelle%20Post-Dispatch%29%20AND%20year%3A1926&fl[]=identifier&fl[]=title&fl[]=year&output=json&rows=8"),
    ("gt-lee-wwi-pass144.html",
     "https://www.genealogytrails.com/ken/lee/wwi_draft_cards.html"),
    ("fs-1146342-pass144.html",
     "https://www.familysearch.org/search/catalog/1146342"),
    ("usgennet-lee-wills-pass144.html",
     "https://usgennet.org/usa/ky/county/lee/wills/"),
    ("hutchins-faq-9938-pass144.html",
     "https://libraryanswers.berea.edu/faq/9938"),
    ("ia-meta-602-pass144.json",
     "https://archive.org/metadata/14thcensusofpopu0602unit"),
    ("ia-solr-m1509-ky-pass144.json",
     "https://archive.org/advancedsearch.php?q=M1509%20AND%20%28Kentucky%20OR%20KY45%20OR%20KY74%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("gt-hart-1850-pass144.html",
     "https://www.genealogytrails.com/ken/hart/1850Census.html"),
    ("reeves-hart-1850-pass144.html",
     "https://thereevesproject.org/data/tiki-index.php?page=US_Federal_Census_1850_KY_Hart"),
]:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=45)
    print(f"  {name} {st} {n}", flush=True)

print("=== leftover western compiled workarounds ===", flush=True)
for name, url in [
    ("kygenweb-hart-census-pass144.html",
     "https://kygenweb.net/hart/census.html"),
    ("us-census-hart-1850-pass144.html",
     "https://www.us-census.org/pub/usgenweb/census/ky/hart/1850/"),
    ("ia-solr-hart-1850-pass144.json",
     "https://archive.org/advancedsearch.php?q=%28hart%20AND%20kentucky%20AND%201850%20AND%20%28census%20OR%201850indx%20OR%20transcript%29%29&fl[]=identifier&fl[]=title&output=json&rows=12"),
    ("ia-solr-franklin-1850indx-pass144.json",
     "https://archive.org/advancedsearch.php?q=%28franklin%20AND%20kentucky%20AND%201850indx%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("ia-solr-mercer-1850indx-pass144.json",
     "https://archive.org/advancedsearch.php?q=%28mercer%20AND%20kentucky%20AND%201850indx%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("ia-solr-lincoln-1850indx-pass144.json",
     "https://archive.org/advancedsearch.php?q=%28lincoln%20AND%20kentucky%20AND%201850indx%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("ia-solr-hopkins-1850indx-pass144.json",
     "https://archive.org/advancedsearch.php?q=%28hopkins%20AND%20kentucky%20AND%201850indx%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("ia-solr-larue-1850indx-pass144.json",
     "https://archive.org/advancedsearch.php?q=%28larue%20AND%20kentucky%20AND%201850indx%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("usgw-hart-toc-pass144.html",
     "https://www.usgwarchives.net/ky/hart/toc.html"),
    ("usgw-franklin-toc-pass144.html",
     "https://www.usgwarchives.net/ky/franklin/toc.html"),
    ("usgw-mercer-toc-pass144.html",
     "https://www.usgwarchives.net/ky/mercer/toc.html"),
    ("usgw-lincoln-toc-pass144.html",
     "https://www.usgwarchives.net/ky/lincoln/toc.html"),
    ("usgw-hopkins-toc-pass144.html",
     "https://www.usgwarchives.net/ky/hopkins/toc.html"),
    ("usgw-larue-toc-pass144.html",
     "https://www.usgwarchives.net/ky/larue/toc.html"),
    ("sk-hart-1850-pass144.html",
     "https://www.skcensus.com/1850-census-index-hart-county-kentucky/"),
    ("sk-franklin-1850-pass144.html",
     "https://www.skcensus.com/1850-census-index-franklin-county-kentucky/"),
    ("sk-mercer-1850-pass144.html",
     "https://www.skcensus.com/1850-census-index-mercer-county-kentucky/"),
    ("sk-lincoln-1850-pass144.html",
     "https://www.skcensus.com/1850-census-index-lincoln-county-kentucky/"),
    ("sk-hopkins-1850-pass144.html",
     "https://www.skcensus.com/1850-census-index-hopkins-county-kentucky/"),
    ("sk-larue-1850-pass144.html",
     "https://www.skcensus.com/1850-census-index-larue-county-kentucky/"),
]:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=35)
    print(f"  {name} {st} {n}", flush=True)

print("=== Hart Dist 1 remaining evens n0006–n0190 ===", flush=True)
hart_evens = list(range(6, 191, 2))
need = [n for n in hart_evens if not have_leaf("hart", n)]
print(f"  have {len(hart_evens) - len(need)} missing {len(need)}", flush=True)
for leaf in need:
    grab("populationschedu0204unix", leaf, "hart")

# crop surnames for every even from any existing namecol/full
hart_surs = []
for leaf in hart_evens:
    dest = SUR / f"hart-n{leaf:04d}-sur.jpg"
    nc = find_namecol("hart", leaf)
    if nc:
        surname_from_namecol(nc, dest)
    else:
        full = find_full("hart", leaf)
        if full:
            crop_save(full, (0.14, 0.11, 0.46, 0.99), dest, 1.65)
    if dest.exists() and dest.stat().st_size > 2000:
        hart_surs.append(dest)
print(f"  hart even surname crops {len(hart_surs)}/{len(hart_evens)}", flush=True)
for i in range(0, len(hart_surs), 2):
    chunk = hart_surs[i : i + 2]
    lo = chunk[0].name.split("-n")[1][:4]
    hi = chunk[-1].name.split("-n")[1][:4]
    stack(chunk, MON / f"hart-evens-sur-{lo}-{hi}.jpg", thumb_w=700)

print("=== Lincoln Dist 1 remaining (reel 210; Dist 2 n0253+ already closed) ===", flush=True)
lincoln_need = [173, 178, 179, 191, 197, 203, 206, 209, 218, 221, 227, 233, 239]
# Dist 1 start remap
for leaf in [168, 169, 170, 172, 174, 176] + lincoln_need:
    if have_leaf("lincoln", leaf):
        continue
    grab("populationschedu0210unix", leaf, "lincoln")

print("=== Larue Hamilton remaining (reel 209 n0160+) ===", flush=True)
larue_have = set()
for d in PRIOR + [CENS]:
    for folder in ("namecols", "fulls", "surnames"):
        p = d / folder
        if not p.exists():
            continue
        for f in p.glob("larue-n*"):
            try:
                larue_have.add(int(f.name.split("-n")[1][:4]))
            except Exception:
                pass
larue_need = [n for n in range(160, 281) if n not in larue_have]
print(f"  larue have {len(larue_have)} need {len(larue_need)}", flush=True)
for leaf in larue_need:
    grab("populationschedu0209unix", leaf, "larue")

print("=== Franklin remaining densify (reel 200; Gallatin by n0380) ===", flush=True)
frank_need = []
for leaf in range(150, 378):
    if have_leaf("franklin", leaf):
        continue
    frank_need.append(leaf)
# every remaining leaf in Dist 1+2 — visual close attempt
print(f"  franklin missing {len(frank_need)}", flush=True)
for leaf in frank_need:
    grab("populationschedu0200unix", leaf, "franklin")

print("=== Mercer remaining densify (reel 213) ===", flush=True)
merc_need = []
for leaf in range(150, 451):
    if have_leaf("mercer", leaf):
        continue
    merc_need.append(leaf)
# every 2nd missing to keep volume sane
merc_need = merc_need[::2]
print(f"  mercer fetch {len(merc_need)}", flush=True)
for leaf in merc_need:
    grab("populationschedu0213unix", leaf, "mercer")

print("=== Hopkins remaining (skip n0238 Francis J / n0240 John 59) ===", flush=True)
skip_h = {238, 239, 240}
hop_need = []
for leaf in list(range(150, 238)) + list(range(242, 360)):
    if leaf in skip_h or have_leaf("hopkins", leaf):
        continue
    hop_need.append(leaf)
hop_need = hop_need[::2]
print(f"  hopkins fetch {len(hop_need)} (skip 238/240)", flush=True)
for leaf in hop_need:
    grab("populationschedu0205unix", leaf, "hopkins")

print("=== crop remaining-county surnames from existing namecols ===", flush=True)
for prefix, lo, hi in [
    ("franklin", 150, 377),
    ("mercer", 150, 450),
    ("lincoln", 168, 252),
    ("hopkins", 150, 359),
    ("larue", 160, 280),
]:
    surs = []
    for leaf in range(lo, hi + 1):
        dest = SUR / f"{prefix}-n{leaf:04d}-sur.jpg"
        nc = find_namecol(prefix, leaf)
        if nc:
            surname_from_namecol(nc, dest)
        else:
            full = find_full(prefix, leaf)
            if full:
                crop_save(full, (0.14, 0.11, 0.46, 0.99), dest, 1.65)
        if dest.exists() and dest.stat().st_size > 2000:
            surs.append(dest)
    print(f"  {prefix} surname crops {len(surs)}", flush=True)

print("DONE pass144 fetch", flush=True)
