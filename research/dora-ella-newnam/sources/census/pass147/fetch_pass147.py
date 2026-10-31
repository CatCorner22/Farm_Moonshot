#!/usr/bin/env python3
"""Pass 147: B058 one catalog; B071 residual Mercer remaining +
Lincoln Dist 1 remaining + Hopkins remaining (skip Francis J n0238 /
John 59 n0240) + Larue Hamilton remaining + leftover western compiled.
Do not repeat Franklin Dist 1/2, Jeremiah Newman 27, William New 36,
Critcher, NEWLAND n0340, n0149, Gallatin, Hart Dist 1, Henry Dist 1,
Todd 247A, Trigg 314A, TINKER 303A, Kenton 130B compiled Daniel 19,
McCracken 174B, Breckinridge, Graves, Edmonson, Hancock, closed
Laurel/Montgomery/Estill 1840/Clay walks. Do not retest stamp 126.
Do not walk Estill 1930 33-12/33-13. B088 one line. Do not re-ask
phones or R001/R007/R008.
"""
from __future__ import annotations

import ssl
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageOps

ROOT = Path("/workspace/research/dora-ella-newnam")
CAT = ROOT / "sources/catalog"
CENS = ROOT / "sources/census/pass147"
FULL = CENS / "fulls"
KEY = CENS / "keyplates"
NAMES = CENS / "namecols"
SUR = CENS / "surnames"
MON = CENS / "montages"
PRIOR = [
    ROOT / "sources/census" / f"pass{n}"
    for n in range(147, 129, -1)
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
    time.sleep(0.03)
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
    return None


def find_namecol(prefix: str, leaf: int) -> Path | None:
    for d in [CENS] + PRIOR:
        p = d / "namecols" / f"{prefix}-n{leaf:04d}-names.jpg"
        if p.exists() and p.stat().st_size > 2000:
            return p
    return None


def find_full(prefix: str, leaf: int) -> Path | None:
    for d in [CENS] + PRIOR:
        for w in (1600, 1800, 1400, 1100):
            p = d / "fulls" / f"{prefix}-n{leaf:04d}-w{w}.jpg"
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


def ensure_sur(prefix: str, leaf: int) -> Path | None:
    dest = SUR / f"{prefix}-n{leaf:04d}-sur.jpg"
    if dest.exists() and dest.stat().st_size > 2000:
        return dest
    nc = find_namecol(prefix, leaf)
    if nc:
        surname_from_namecol(nc, dest)
    else:
        full = find_full(prefix, leaf)
        if full:
            crop_save(full, (0.14, 0.11, 0.46, 0.99), dest, 1.65)
    if dest.exists() and dest.stat().st_size > 2000:
        return dest
    return None


def stack3(srcs: list[Path], dest: Path, thumb_w: int = 480) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 4000:
        return
    tiles = []
    for p in srcs:
        if p is None or not p.exists():
            continue
        try:
            im = Image.open(p).convert("L")
        except Exception:
            continue
        nh = int(im.height * thumb_w / max(im.width, 1))
        im = im.resize((thumb_w, max(nh, 1)), Image.Resampling.LANCZOS)
        label = Image.new("L", (thumb_w, im.height + 20), 255)
        label.paste(im, (0, 20))
        d = ImageDraw.Draw(label)
        d.text((4, 2), p.name.replace("-sur.jpg", ""), fill=0)
        tiles.append(label)
    if not tiles:
        return
    h = max(t.height for t in tiles)
    canvas = Image.new("L", (thumb_w * len(tiles) + 8, h), 255)
    x = 0
    for t in tiles:
        canvas.paste(t, (x, 0))
        x += thumb_w + 4
    canvas.save(dest, quality=86)


def inventory(prefix: str, lo: int, hi: int) -> tuple[list[int], list[int]]:
    have, miss = [], []
    for leaf in range(lo, hi + 1):
        if have_leaf(prefix, leaf):
            have.append(leaf)
        else:
            miss.append(leaf)
    return have, miss


print("=== B058 / OPEN catalogs ===", flush=True)
for name, url in [
    ("loc-sn89051008-pass147.json",
     "https://www.loc.gov/item/sn89051008/?fo=json"),
    ("ia-solr-postdispatch-1926-pass147.json",
     "https://archive.org/advancedsearch.php?q=title%3A%28Dardanelle%20Post-Dispatch%29%20AND%20year%3A1926&fl[]=identifier&fl[]=title&fl[]=year&output=json&rows=8"),
    ("gt-lee-wwi-pass147.html",
     "https://www.genealogytrails.com/ken/lee/wwi_draft_cards.html"),
    ("fs-1146342-pass147.html",
     "https://www.familysearch.org/search/catalog/1146342"),
    ("usgennet-lee-wills-pass147.html",
     "https://usgennet.org/usa/ky/county/lee/wills/"),
    ("hutchins-faq-9938-pass147.html",
     "https://libraryanswers.berea.edu/faq/9938"),
    ("ia-meta-602-pass147.json",
     "https://archive.org/metadata/14thcensusofpopu0602unit"),
    ("ia-solr-m1509-ky-pass147.json",
     "https://archive.org/advancedsearch.php?q=M1509%20AND%20%28Kentucky%20OR%20KY45%20OR%20KY74%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("fishergenes-estill-marr-pass147.html",
     "https://www.fishergenes.com/estill/estill-marriages.htm"),
]:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=45)
    print(f"  {name} {st} {n}", flush=True)

print("=== leftover western compiled + Mercer/Lincoln/Hopkins/Larue ===", flush=True)
for name, url in [
    ("sk-mercer-1850-pass147.html",
     "https://www.skcensus.com/1850-census-index-mercer-county-kentucky/"),
    ("sk-lincoln-1850-pass147.html",
     "https://www.skcensus.com/1850-census-index-lincoln-county-kentucky/"),
    ("sk-hopkins-1850-pass147.html",
     "https://www.skcensus.com/1850-census-index-hopkins-county-kentucky/"),
    ("sk-larue-1850-pass147.html",
     "https://www.skcensus.com/1850-census-index-larue-county-kentucky/"),
    ("sk-meade-1850-pass147.html",
     "https://www.skcensus.com/1850-census-index-meade-county-kentucky/"),
    ("gt-mercer-census-pass147.html",
     "https://www.genealogytrails.com/ken/mercer/census.html"),
    ("gt-lincoln-census-pass147.html",
     "https://www.genealogytrails.com/ken/lincoln/census.html"),
    ("gt-hopkins-census-pass147.html",
     "https://www.genealogytrails.com/ken/hopkins/census.html"),
    ("gt-larue-census-pass147.html",
     "https://www.genealogytrails.com/ken/larue/census.html"),
    ("kygenweb-mercer-census-pass147.html",
     "https://kygenweb.net/mercer/census.html"),
    ("kygenweb-lincoln-census-pass147.html",
     "https://kygenweb.net/lincoln/census.html"),
    ("kygenweb-hopkins-census-pass147.html",
     "https://kygenweb.net/hopkins/census.html"),
    ("kygenweb-larue-census-pass147.html",
     "https://kygenweb.net/larue/census.html"),
    ("us-census-mercer-1850-pass147.html",
     "https://www.us-census.org/pub/usgenweb/census/ky/mercer/1850/"),
    ("us-census-lincoln-1850-pass147.html",
     "https://www.us-census.org/pub/usgenweb/census/ky/lincoln/1850/"),
    ("us-census-hopkins-1850-pass147.html",
     "https://www.us-census.org/pub/usgenweb/census/ky/hopkins/1850/"),
    ("us-census-larue-1850-pass147.html",
     "https://www.us-census.org/pub/usgenweb/census/ky/larue/1850/"),
    ("usgw-mercer-toc-pass147.html",
     "https://www.usgwarchives.net/ky/mercer/toc.html"),
    ("usgw-lincoln-toc-pass147.html",
     "https://www.usgwarchives.net/ky/lincoln/toc.html"),
    ("usgw-hopkins-toc-pass147.html",
     "https://www.usgwarchives.net/ky/hopkins/toc.html"),
    ("usgw-larue-toc-pass147.html",
     "https://www.usgwarchives.net/ky/larue/toc.html"),
    ("ia-solr-mercer-1850indx-pass147.json",
     "https://archive.org/advancedsearch.php?q=%28mercer%20AND%20kentucky%20AND%20%281850indx%20OR%20%221850%20census%22%29%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("ia-solr-lincoln-1850indx-pass147.json",
     "https://archive.org/advancedsearch.php?q=%28lincoln%20AND%20kentucky%20AND%20%281850indx%20OR%20%221850%20census%22%29%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("ia-solr-hopkins-1850indx-pass147.json",
     "https://archive.org/advancedsearch.php?q=%28hopkins%20AND%20kentucky%20AND%20%281850indx%20OR%20%221850%20census%22%29%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("ia-solr-larue-1850indx-pass147.json",
     "https://archive.org/advancedsearch.php?q=%28larue%20AND%20kentucky%20AND%20%281850indx%20OR%20%221850%20census%22%29%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("cdx-sk-mercer-pass147.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-mercer-county-kentucky/&output=json&limit=8"),
    ("cdx-sk-lincoln-pass147.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-lincoln-county-kentucky/&output=json&limit=8"),
    ("cdx-sk-hopkins-pass147.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-hopkins-county-kentucky/&output=json&limit=8"),
    ("cdx-sk-larue-pass147.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-larue-county-kentucky/&output=json&limit=8"),
    ("cdx-sk-meade-pass147.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-meade-county-kentucky/&output=json&limit=8"),
    ("files-usgw-kenton-1850-pass147.html",
     "https://www.usgwarchives.net/ky/kenton/census/1850/"),
]:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=28)
    print(f"  {name} {st} {n}", flush=True)

print("=== inventory existing leftover crops ===", flush=True)
for prefix, lo, hi in [
    ("lincoln", 173, 270),
    ("mercer", 120, 470),
    ("hopkins", 140, 360),
    ("larue", 160, 390),
]:
    have, miss = inventory(prefix, lo, hi)
    print(f"  {prefix} {lo}-{hi} have {len(have)} miss {len(miss)} first_miss={miss[:8]}", flush=True)

print("=== bound probes ===", flush=True)
# Lincoln Dist 2 start (n0265 already Dist 2). Probe Dist 1 last leaves.
for leaf in [255, 258, 260, 262, 263, 264, 265]:
    if not have_leaf("lincoln", leaf):
        grab("populationschedu0210unix", leaf, "lincoln")
    else:
        print(f"  lincoln n{leaf:04d} have", flush=True)

# Hopkins start (after Hickman) + Dist 2 end (before Jefferson n0355)
for leaf in [160, 165, 170, 175, 178, 179, 180, 348, 350, 352, 353, 354, 355]:
    if not have_leaf("hopkins", leaf):
        grab("populationschedu0205unix", leaf, "hopkins")
    else:
        print(f"  hopkins n{leaf:04d} have", flush=True)

# Mercer start (Meade→Mercer) + end after n0449
for leaf in [130, 135, 140, 142, 144, 145, 148, 149, 449, 450, 452, 455, 460, 465, 470]:
    if not have_leaf("mercer", leaf):
        grab("populationschedu0213unix", leaf, "mercer")
    else:
        print(f"  mercer n{leaf:04d} have", flush=True)

# Larue Hamilton end after n0280 (Lawrence at n0382 on this reel is later county)
for leaf in [280, 285, 290, 300, 310, 320, 330, 340, 350, 360, 370, 375, 380, 381]:
    if not have_leaf("larue", leaf):
        grab("populationschedu0209unix", leaf, "larue")
    else:
        print(f"  larue n{leaf:04d} have", flush=True)

print("=== Lincoln Dist 1 remaining every missing leaf ===", flush=True)
# Dist 1 n0173 → Dist 2 start (~n0265). Do not re-walk Dist 2.
lincoln_lo, lincoln_hi = 173, 264
have, miss = inventory("lincoln", lincoln_lo, lincoln_hi)
print(f"  lincoln Dist1 {lincoln_lo}-{lincoln_hi} have {len(have)} miss {len(miss)}", flush=True)
for leaf in miss:
    grab("populationschedu0210unix", leaf, "lincoln")

print("=== Hopkins remaining every missing leaf (skip 238/240) ===", flush=True)
skip_h = {238, 239, 240}
hopkins_lo, hopkins_hi = 180, 354
have, miss = inventory("hopkins", hopkins_lo, hopkins_hi)
miss = [n for n in miss if n not in skip_h]
print(f"  hopkins {hopkins_lo}-{hopkins_hi} miss {len(miss)} (skip 238/240)", flush=True)
for leaf in miss:
    grab("populationschedu0205unix", leaf, "hopkins")

print("=== Mercer remaining every missing leaf ===", flush=True)
mercer_lo, mercer_hi = 145, 460
have, miss = inventory("mercer", mercer_lo, mercer_hi)
print(f"  mercer {mercer_lo}-{mercer_hi} have {len(have)} miss {len(miss)}", flush=True)
for leaf in miss:
    grab("populationschedu0213unix", leaf, "mercer")

print("=== Larue Hamilton remaining every missing leaf ===", flush=True)
larue_lo, larue_hi = 160, 381
have, miss = inventory("larue", larue_lo, larue_hi)
print(f"  larue {larue_lo}-{larue_hi} have {len(have)} miss {len(miss)}", flush=True)
for leaf in miss:
    grab("populationschedu0209unix", leaf, "larue")

print("=== crop surnames + 3-up stacks ===", flush=True)
for prefix, lo, hi in [
    ("lincoln", 173, 264),
    ("hopkins", 180, 354),
    ("mercer", 145, 460),
    ("larue", 160, 381),
]:
    surs = []
    for leaf in range(lo, hi + 1):
        if prefix == "hopkins" and leaf in (238, 239, 240):
            continue
        dest = ensure_sur(prefix, leaf)
        if dest:
            surs.append(dest)
    print(f"  {prefix} surname crops {len(surs)}", flush=True)
    for i in range(0, len(surs), 3):
        chunk = surs[i : i + 3]
        lo_n = chunk[0].name.split("-n")[1][:4]
        hi_n = chunk[-1].name.split("-n")[1][:4]
        stack3(chunk, MON / f"{prefix}-row-{lo_n}-{hi_n}.jpg")

print("DONE pass147 fetch", flush=True)
