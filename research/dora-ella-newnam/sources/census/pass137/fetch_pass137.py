#!/usr/bin/env python3
"""Pass 137: isolate Edmonson 11B William 30 + Hancock 295A William 26;
B058/OPEN catalog reconfirm; leftover compiled; residual namecol densify."""
from __future__ import annotations

import json
import ssl
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path("/workspace/research/dora-ella-newnam")
CAT = ROOT / "sources/catalog"
CENS = ROOT / "sources/census/pass137"
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


def ia_leaf(item: str, leaf: int, w: int = 1600) -> str:
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


def grab(item: str, leaf: int, tag: str, w: int = 1600) -> Path:
    dest = FULL / f"{tag}-n{leaf:04d}-w{w}.jpg"
    st, n = fetch(ia_leaf(item, leaf, w), dest)
    print(f"  {tag} n{leaf:04d} {st} {n}", flush=True)
    if dest.exists() and dest.stat().st_size > 80000:
        crop_save(dest, (0.02, 0.00, 0.98, 0.14), KEY / f"{tag}-n{leaf:04d}-header.jpg")
        crop_save(dest, (0.70, 0.00, 1.00, 0.14), KEY / f"{tag}-n{leaf:04d}-stamp.jpg")
        crop_save(dest, (0.07, 0.10, 0.58, 0.99), NAMES / f"{tag}-n{leaf:04d}-names.jpg")
    time.sleep(0.04)
    return dest


print("=== catalogs B058 / OPEN / indexes ===", flush=True)
for name, url in [
    ("loc-sn89051008-pass137.json",
     "https://www.loc.gov/item/sn89051008/?fo=json"),
    ("ia-solr-postdispatch-1926-pass137.json",
     "https://archive.org/advancedsearch.php?q=title%3A%28Dardanelle%20Post-Dispatch%29%20AND%20year%3A1926&fl[]=identifier&fl[]=title&fl[]=year&output=json&rows=8"),
    ("gt-lee-wwi-pass137.html",
     "https://www.genealogytrails.com/ken/lee/wwi_draft_cards.html"),
    ("fs-1146342-pass137.html",
     "https://www.familysearch.org/search/catalog/1146342"),
    ("usgennet-lee-wills-pass137.html",
     "https://usgennet.org/usa/ky/county/lee/wills/"),
    ("hutchins-faq-9938-pass137.html",
     "https://libraryanswers.berea.edu/faq/9938"),
    ("ia-meta-602-pass137.json",
     "https://archive.org/metadata/14thcensusofpopu0602unit"),
    ("ia-meta-198-pass137.json",
     "https://archive.org/metadata/populationschedu0198unix"),
    ("ia-meta-202-pass137.json",
     "https://archive.org/metadata/populationschedu0202unix"),
    ("ia-solr-m1509-ky-pass137.json",
     "https://archive.org/advancedsearch.php?q=M1509%20AND%20%28Kentucky%20OR%20KY45%20OR%20KY74%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("fishergenes-estill-marr-pass137.html",
     "https://www.fishergenes.com/estill/estillmarriages.html"),
    ("kykinfolk-estill-marr-pass137.html",
     "https://kykinfolk.com/estill/marriages.htm"),
    ("wchs-books-pass137.html",
     "https://www.woodfordheritage.org/research/books/"),
    ("us-census-edmonson-1850-dir-pass137.html",
     "https://us-census.org/pub/usgenweb/census/ky/edmonson/1850/"),
    ("us-census-hancock-1850-dir-pass137.html",
     "https://us-census.org/pub/usgenweb/census/ky/hancock/1850/"),
    ("us-census-anderson-1850-dir-pass137.html",
     "https://us-census.org/pub/usgenweb/census/ky/anderson/1850/"),
    ("us-census-henry-1850-dir-pass137.html",
     "https://us-census.org/pub/usgenweb/census/ky/henry/1850/"),
    ("us-census-meade-1850-dir-pass137.html",
     "https://us-census.org/pub/usgenweb/census/ky/meade/1850/"),
    ("us-census-hart-1850-dir-pass137.html",
     "https://us-census.org/pub/usgenweb/census/ky/hart/1850/"),
    ("us-census-grayson-1850-dir-pass137.html",
     "https://us-census.org/pub/usgenweb/census/ky/grayson/1850/"),
    ("us-census-campbell-1850-dir-pass137.html",
     "https://us-census.org/pub/usgenweb/census/ky/campbell/1850/"),
    ("us-census-ky-listing-pass137.html",
     "https://us-census.org/pub/usgenweb/census/ky/"),
]:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=45)
    print(f"  {name} {st} {n}", flush=True)

# metadata summaries
for meta in ("ia-meta-198-pass137.json", "ia-meta-202-pass137.json", "ia-meta-602-pass137.json"):
    p = CAT / meta
    try:
        j = json.loads(p.read_text())
        md = j.get("metadata") or j
        print(f"  META {meta} imagecount={md.get('imagecount')} desc={str(md.get('description'))[:180]}", flush=True)
    except Exception as e:
        print(f"  META {meta} parse {e}", flush=True)

print("=== Edmonson reel 198 map + isolate (Estill 85A=n0403 => Edmonson 4A~n0241 11B~n0256) ===", flush=True)
for leaf in [5, 220, 230, 235, 238, 240, 241, 242, 250, 254, 255, 256, 257, 260, 270, 320, 326, 328]:
    grab("populationschedu0198unix", leaf, "edmonson")

print("=== Hancock reel 202 map + isolate (Greenup 261B=n0526 => Hancock 266A~n0535 295A~n0593) ===", flush=True)
for leaf in [526, 530, 534, 535, 536, 548, 550, 552, 580, 582, 586, 590, 592, 593, 594, 600, 610]:
    grab("populationschedu0202unix", leaf, "hancock")

print("=== compiled leftover N/T indexes ===", flush=True)
compiled = [
    ("us-census-anderson-indx-pass137.txt",
     "https://us-census.org/pub/usgenweb/census/ky/anderson/1850/_indx-a-z.txt"),
    ("us-census-anderson-indx-nz-pass137.txt",
     "https://us-census.org/pub/usgenweb/census/ky/anderson/1850/_indx-n-z.txt"),
    ("us-census-henry-indx-nz-pass137.txt",
     "https://us-census.org/pub/usgenweb/census/ky/henry/1850/_indx-n-z.txt"),
    ("us-census-meade-indx-nz-pass137.txt",
     "https://us-census.org/pub/usgenweb/census/ky/meade/1850/_indx-n-z.txt"),
    ("us-census-hart-indx-nz-pass137.txt",
     "https://us-census.org/pub/usgenweb/census/ky/hart/1850/_indx-n-z.txt"),
    ("us-census-grayson-indx-nz-pass137.txt",
     "https://us-census.org/pub/usgenweb/census/ky/grayson/1850/_indx-n-z.txt"),
    ("us-census-campbell-indx-pass137.txt",
     "https://us-census.org/pub/usgenweb/census/ky/campbell/1850/_indx-a-z.txt"),
    ("us-census-edmonson-indx-i-o-pass137.txt",
     "https://us-census.org/pub/usgenweb/census/ky/edmonson/1850/_indx-i-o.txt"),
    ("us-census-hancock-indx-mz-pass137.txt",
     "https://us-census.org/pub/usgenweb/census/ky/hancock/1850/_indx-m-z.txt"),
    ("us-census-hancock-pg0294b-pass137.txt",
     "https://us-census.org/pub/usgenweb/census/ky/hancock/1850/pg0294b.txt"),
    ("us-census-edmonson-pg0001b-pass137.txt",
     "https://us-census.org/pub/usgenweb/census/ky/edmonson/1850/pg0001b.txt"),
    ("sk-kenton-1850-pass137.html",
     "https://www.usgwarchives.net/ky/kenton/census/1850/1850indx.txt"),
    ("sk-kenton-1850-alt-pass137.html",
     "http://www.skpub.com/genie/census/ky/kenton/1850indx.html"),
]
for name, url in compiled:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=40)
    print(f"  {name} {st} {n}", flush=True)

print("done pass137 fetch", flush=True)
