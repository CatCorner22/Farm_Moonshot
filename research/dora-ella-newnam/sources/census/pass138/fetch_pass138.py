#!/usr/bin/env python3
"""Pass 138: B058/OPEN catalogs; isolate Hopkins John 59; Mercer N-index;
Franklin/Mercer/Lincoln densify; Kenton 130B + leftover compiled workarounds."""
from __future__ import annotations

import json
import ssl
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path("/workspace/research/dora-ella-newnam")
CAT = ROOT / "sources/catalog"
CENS = ROOT / "sources/census/pass138"
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
    time.sleep(0.03)
    return dest


print("=== catalogs B058 / OPEN / indexes ===", flush=True)
for name, url in [
    ("loc-sn89051008-pass138.json",
     "https://www.loc.gov/item/sn89051008/?fo=json"),
    ("ia-solr-postdispatch-1926-pass138.json",
     "https://archive.org/advancedsearch.php?q=title%3A%28Dardanelle%20Post-Dispatch%29%20AND%20year%3A1926&fl[]=identifier&fl[]=title&fl[]=year&output=json&rows=8"),
    ("gt-lee-wwi-pass138.html",
     "https://www.genealogytrails.com/ken/lee/wwi_draft_cards.html"),
    ("fs-1146342-pass138.html",
     "https://www.familysearch.org/search/catalog/1146342"),
    ("usgennet-lee-wills-pass138.html",
     "https://usgennet.org/usa/ky/county/lee/wills/"),
    ("hutchins-faq-9938-pass138.html",
     "https://libraryanswers.berea.edu/faq/9938"),
    ("ia-meta-602-pass138.json",
     "https://archive.org/metadata/14thcensusofpopu0602unit"),
    ("ia-solr-m1509-ky-pass138.json",
     "https://archive.org/advancedsearch.php?q=M1509%20AND%20%28Kentucky%20OR%20KY45%20OR%20KY74%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("ia-solr-kenton-1850-pass138.json",
     "https://archive.org/advancedsearch.php?q=kenton%20AND%201850%20AND%20%28census%20OR%20population%29%20AND%20kentucky&fl[]=identifier&fl[]=title&output=json&rows=12"),
    ("fishergenes-estill-marr-pass138.html",
     "https://www.fishergenes.com/estill/estillmarriages.html"),
    ("kykinfolk-estill-marr-pass138.html",
     "https://kykinfolk.com/estill/marriages.htm"),
    ("kykinfolk-owsley-marr-pass138.html",
     "https://kykinfolk.com/owsley/marriages.htm"),
    ("wchs-books-pass138.html",
     "https://www.woodfordheritage.org/research/books/"),
    ("sk-kenton-1850-pass138.html",
     "https://www.skcensus.com/1850-census-index-kenton-county-kentucky/"),
    ("sk-mercer-1850-pass138.html",
     "https://www.skcensus.com/1850-census-index-mercer-county-kentucky/"),
    ("sk-franklin-1850-pass138.html",
     "https://www.skcensus.com/1850-census-index-franklin-county-kentucky/"),
    ("sk-hopkins-1850-pass138.html",
     "https://www.skcensus.com/1850-census-index-hopkins-county-kentucky/"),
    ("sk-lincoln-1850-pass138.html",
     "https://www.skcensus.com/1850-census-index-lincoln-county-kentucky/"),
    ("kygenweb-mercer-index-m-pass138.html",
     "https://kykinfolk.com/mercer/census/index/index-m.html"),
    ("kygenweb-mercer-index-m2-pass138.html",
     "https://www.kykinfolk.com/mercer/census/1850/index-m.html"),
    ("kygenweb-mercer-index-m3-pass138.html",
     "https://kykinfolk.com/mercer/census/1850/index-m.html"),
    ("kygenweb-mercer-n-pass138.html",
     "https://kykinfolk.com/mercer/census/index/index-m.html#N"),
    ("us-census-breckinridge-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/breckinridge/1850/"),
    ("us-census-breckinridge-indx-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/breckinridge/"),
    ("usgw-kenton-1850-dir-pass138.html",
     "https://www.usgwarchives.net/ky/kenton/census/1850/"),
    ("usgw-kenton-1850indx-pass138.txt",
     "https://www.usgwarchives.net/ky/kenton/census/1850/1850indx.txt"),
    ("ahgp-ky-census-pass138.html",
     "https://www.ahgp.org/census/ky.html"),
]:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=45)
    print(f"  {name} {st} {n}", flush=True)

print("=== Breckinridge index guesses ===", flush=True)
for name, url in [
    ("us-census-breckinridge-indx-n-z-pass138.txt",
     "https://us-census.org/pub/usgenweb/census/ky/breckinridge/1850/_indx-n-z.txt"),
    ("us-census-breckinridge-indx-m-z-pass138.txt",
     "https://us-census.org/pub/usgenweb/census/ky/breckinridge/1850/indx-m-z.txt"),
    ("us-census-breckinridge-indx-n-s-pass138.txt",
     "https://us-census.org/pub/usgenweb/census/ky/breckinridge/1850/indx-n-s.txt"),
    ("us-census-breckinridge-1850indx-pass138.txt",
     "https://us-census.org/pub/usgenweb/census/ky/breckinridge/1850/1850indx.txt"),
]:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=30)
    print(f"  {name} {st} {n}", flush=True)

print("=== Hopkins Dist 2: isolate John 59 after Francis J n0238 ===", flush=True)
for leaf in range(2236, 2250):
    grab("populationschedu0205unix", leaf, "hopkins")

print("=== Mercer Dist 1 densify n0202-n0410 ===", flush=True)
for leaf in list(range(202, 260, 4)) + list(range(260, 420, 5)) + [215, 219, 223, 227, 231, 235, 239, 243, 247]:
    grab("populationschedu0213unix", leaf, "mercer")

print("=== Franklin Dist 1/2 densify remaining ===", flush=True)
for leaf in list(range(152, 250, 6)) + list(range(250, 450, 8)) + [168, 172, 178, 184, 188, 194, 198, 204, 208, 214, 220, 226, 232, 238, 244]:
    grab("populationschedu0200unix", leaf, "franklin")

print("=== Lincoln Dist 1 remaining ===", flush=True)
for leaf in list(range(172, 286, 4)) + [176, 182, 188, 194, 202, 208, 214, 220, 226, 232, 238, 244, 250, 256, 262, 268, 274]:
    grab("populationschedu0210unix", leaf, "lincoln")

print("=== Kenton Dist 1 130B probes (reel 195 Campbell + 208 edges) ===", flush=True)
for leaf in [1, 5, 10, 20, 50, 100, 120, 125, 128, 130, 132, 135, 140, 250, 252]:
    grab("populationschedu0195unix", leaf, "r195")
for leaf in [252, 253, 1, 2, 3, 4]:
    grab("populationschedu0208unix", leaf, "r208edge")

print("DONE pass138 fetch", flush=True)
