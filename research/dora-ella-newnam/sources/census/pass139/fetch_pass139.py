#!/usr/bin/env python3
"""Pass 139: isolate Hopkins John 59; leftover western county starts;
Kenton 130B alternate items; B058 one reconfirm; OPEN catalogs."""
from __future__ import annotations

import json
import ssl
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path("/workspace/research/dora-ella-newnam")
CAT = ROOT / "sources/catalog"
CENS = ROOT / "sources/census/pass139"
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
    time.sleep(0.03)
    return dest


print("=== catalogs B058 / OPEN / leftover ===", flush=True)
for name, url in [
    ("loc-sn89051008-pass139.json",
     "https://www.loc.gov/item/sn89051008/?fo=json"),
    ("ia-solr-postdispatch-1926-pass139.json",
     "https://archive.org/advancedsearch.php?q=title%3A%28Dardanelle%20Post-Dispatch%29%20AND%20year%3A1926&fl[]=identifier&fl[]=title&fl[]=year&output=json&rows=8"),
    ("gt-lee-wwi-pass139.html",
     "https://www.genealogytrails.com/ken/lee/wwi_draft_cards.html"),
    ("fs-1146342-pass139.html",
     "https://www.familysearch.org/search/catalog/1146342"),
    ("usgennet-lee-wills-pass139.html",
     "https://usgennet.org/usa/ky/county/lee/wills/"),
    ("hutchins-faq-9938-pass139.html",
     "https://libraryanswers.berea.edu/faq/9938"),
    ("ia-meta-602-pass139.json",
     "https://archive.org/metadata/14thcensusofpopu0602unit"),
    ("ia-solr-m1509-ky-pass139.json",
     "https://archive.org/advancedsearch.php?q=M1509%20AND%20%28Kentucky%20OR%20KY45%20OR%20KY74%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("ia-solr-kenton-dist1-pass139.json",
     "https://archive.org/advancedsearch.php?q=%28kenton%20OR%20%22kenton%20county%22%29%20AND%201850%20AND%20%28census%20OR%20population%29&fl[]=identifier&fl[]=title&output=json&rows=20"),
    ("ia-solr-kentuckycensus-208-pass139.json",
     "https://archive.org/advancedsearch.php?q=kentuckycensus%20AND%20%28208%20OR%20reel208%20OR%20kenton%29&fl[]=identifier&fl[]=title&output=json&rows=12"),
    ("sk-kenton-1850-pass139.html",
     "https://www.skcensus.com/1850-census-index-kenton-county-kentucky/"),
    ("sk-butler-1850-pass139.html",
     "https://www.skcensus.com/1850-census-index-butler-county-kentucky/"),
    ("sk-allen-1850-pass139.html",
     "https://www.skcensus.com/1850-census-index-allen-county-kentucky/"),
    ("sk-warren-1850-pass139.html",
     "https://www.skcensus.com/1850-census-index-warren-county-kentucky/"),
    ("sk-union-1850-pass139.html",
     "https://www.skcensus.com/1850-census-index-union-county-kentucky/"),
    ("sk-graves-1850-pass139.html",
     "https://www.skcensus.com/1850-census-index-graves-county-kentucky/"),
    ("sk-henry-1850-pass139.html",
     "https://www.skcensus.com/1850-census-index-henry-county-kentucky/"),
    ("sk-meade-1850-pass139.html",
     "https://www.skcensus.com/1850-census-index-meade-county-kentucky/"),
    ("fishergenes-estill-marr-pass139.html",
     "https://www.fishergenes.com/estill/estillmarriages.html"),
    ("kykinfolk-owsley-marr-pass139.html",
     "https://kykinfolk.com/owsley/marriages.htm"),
    ("kygenweb-hopkins-d2-pg003-pass139.html",
     "https://kykinfolk.com/hopkins/census/1850/d2-pg003.htm"),
    ("kygenweb-hopkins-d2-pg003b-pass139.html",
     "https://www.kykinfolk.com/hopkins/census/1850/d2-pg003.htm"),
    ("wayback-sk-butler-pass139.html",
     "https://web.archive.org/web/2020/https://www.skcensus.com/1850-census-index-butler-county-kentucky/"),
    ("wayback-sk-warren-pass139.html",
     "https://web.archive.org/web/2020/https://www.skcensus.com/1850-census-index-warren-county-kentucky/"),
    ("cdx-sk-warren-pass139.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-warren-county-kentucky&output=json&limit=8"),
    ("cdx-sk-allen-pass139.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-allen-county-kentucky&output=json&limit=8"),
    ("cdx-sk-union-pass139.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-union-county-kentucky&output=json&limit=8"),
    ("cdx-sk-henry-pass139.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-henry-county-kentucky&output=json&limit=8"),
    ("cdx-sk-meade-pass139.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-meade-county-kentucky&output=json&limit=8"),
    ("ia-meta-190-pass139.json",
     "https://archive.org/metadata/populationschedu0190unix"),
    ("ia-meta-194-pass139.json",
     "https://archive.org/metadata/populationschedu0194unix"),
    ("ia-meta-204-pass139.json",
     "https://archive.org/metadata/populationschedu0204unix"),
    ("ia-meta-219-pass139.json",
     "https://archive.org/metadata/populationschedu0219unix"),
    ("ia-meta-220-pass139.json",
     "https://archive.org/metadata/populationschedu0220unix"),
]:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=45)
    print(f"  {name} {st} {n}", flush=True)

print("=== Hopkins Dist 2: isolate John 59 after Francis J n0238 ===", flush=True)
for leaf in range(238, 262):
    grab("populationschedu0205unix", leaf, "hopkins")

print("=== leftover county starts (do not repeat closed) ===", flush=True)
# reel 190 Adair/Allen/Anderson/Ballard — Adair+Ballard closed; find Allen/Anderson
for leaf in [80, 120, 160, 200, 240, 280, 320]:
    grab("populationschedu0190unix", leaf, "r190")
# reel 194 Butler/Caldwell/Calloway
for leaf in [5, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480]:
    grab("populationschedu0194unix", leaf, "r194")
# reel 204 Hart/Henderson/Henry — Henderson closed
for leaf in [5, 40, 80, 120, 200, 280, 360, 440]:
    grab("populationschedu0204unix", leaf, "r204")
# reel 219 Spencer/Taylor/Todd/Trigg — Spencer+Taylor closed
for leaf in [80, 160, 240, 320, 400, 480]:
    grab("populationschedu0219unix", leaf, "r219")
# reel 220 Trimble/Union/Warren — Trimble closed
for leaf in [40, 80, 160, 240, 320, 400, 480]:
    grab("populationschedu0220unix", leaf, "r220")
# reel 201 Graves after Grant
for leaf in [200, 280, 360, 440]:
    grab("populationschedu0201unix", leaf, "r201")
# reel 202 Grayson start (Greenup/Hancock closed later)
for leaf in [5, 40, 80]:
    grab("populationschedu0202unix", leaf, "r202gray")
# reel 209 Larue after Knox n0160
for leaf in [160, 180, 200, 220]:
    grab("populationschedu0209unix", leaf, "larue")
# reel 210 Livingston after Lincoln
for leaf in [340, 380, 420]:
    grab("populationschedu0210unix", leaf, "livingston")
# reel 213 Meade before Mercer
for leaf in [5, 40, 80, 120]:
    grab("populationschedu0213unix", leaf, "meade")
# reel 214 Muhlenberg after Morgan
for leaf in [360, 400, 440, 480]:
    grab("populationschedu0214unix", leaf, "muhlenberg")
# reel 211 McCracken after Logan
for leaf in [280, 320, 360]:
    grab("populationschedu0211unix", leaf, "mccracken")
# reel 212 Marshall after Marion
for leaf in [200, 260, 320]:
    grab("populationschedu0212unix", leaf, "marshall")
# reel 195 Campbell Dist 1 stamp ~130 (not Kenton)
for leaf in [5, 40, 80, 120, 128, 130, 132, 160]:
    grab("populationschedu0195unix", leaf, "campbell")
# reel 200 Fulton after Franklin
for leaf in [300, 360, 420]:
    grab("populationschedu0200unix", leaf, "fulton")
# reel 205 Hickman before Hopkins
for leaf in [5, 40, 80, 120]:
    grab("populationschedu0205unix", leaf, "hickman")

print("=== Kenton Dist 1 130B alternate items ===", flush=True)
for item in [
    "kentuckycensus00reel208",
    "populationschedu0208unix",
]:
    dest = CAT / f"ia-meta-{item}-pass139.json"
    fetch(f"https://archive.org/metadata/{item}", dest, timeout=30)
    print(f"  meta {item} {dest.stat().st_size}", flush=True)
# late reel 208 leaves after Dist 2 / Covington (maybe Dist 1 bound at end)
for leaf in [620, 624, 628, 632, 636, 640, 643]:
    grab("populationschedu0208unix", leaf, "kentonend")

print("DONE pass139 fetch", flush=True)
