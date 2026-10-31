#!/usr/bin/env python3
"""Pass 140: B058 one reconfirm; OPEN catalogs; Henry Dist 1 n0440+;
Hart Dist 1 densify; Hopkins remaining; Kenton 130B workarounds;
leftover SK; Larue densify. Do not repeat closed walks."""
from __future__ import annotations

import ssl
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path("/workspace/research/dora-ella-newnam")
CAT = ROOT / "sources/catalog"
CENS = ROOT / "sources/census/pass140"
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


print("=== catalogs B058 / OPEN / leftover SK / Kenton 130B ===", flush=True)
for name, url in [
    ("loc-sn89051008-pass140.json",
     "https://www.loc.gov/item/sn89051008/?fo=json"),
    ("ia-solr-postdispatch-1926-pass140.json",
     "https://archive.org/advancedsearch.php?q=title%3A%28Dardanelle%20Post-Dispatch%29%20AND%20year%3A1926&fl[]=identifier&fl[]=title&fl[]=year&output=json&rows=8"),
    ("gt-lee-wwi-pass140.html",
     "https://www.genealogytrails.com/ken/lee/wwi_draft_cards.html"),
    ("fs-1146342-pass140.html",
     "https://www.familysearch.org/search/catalog/1146342"),
    ("usgennet-lee-wills-pass140.html",
     "https://usgennet.org/usa/ky/county/lee/wills/"),
    ("hutchins-faq-9938-pass140.html",
     "https://libraryanswers.berea.edu/faq/9938"),
    ("ia-meta-602-pass140.json",
     "https://archive.org/metadata/14thcensusofpopu0602unit"),
    ("ia-solr-m1509-ky-pass140.json",
     "https://archive.org/advancedsearch.php?q=M1509%20AND%20%28Kentucky%20OR%20KY45%20OR%20KY74%29&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("sk-kenton-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-kenton-county-kentucky/"),
    ("sk-hart-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-hart-county-kentucky/"),
    ("sk-henry-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-henry-county-kentucky/"),
    ("sk-larue-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-larue-county-kentucky/"),
    ("sk-livingston-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-livingston-county-kentucky/"),
    ("sk-muhlenberg-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-muhlenberg-county-kentucky/"),
    ("sk-mccracken-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-mccracken-county-kentucky/"),
    ("sk-hickman-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-hickman-county-kentucky/"),
    ("sk-fulton-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-fulton-county-kentucky/"),
    ("sk-todd-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-todd-county-kentucky/"),
    ("sk-trigg-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-trigg-county-kentucky/"),
    ("sk-anderson-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-anderson-county-kentucky/"),
    ("sk-caldwell-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-caldwell-county-kentucky/"),
    ("sk-calloway-1850-pass140.html",
     "https://www.skcensus.com/1850-census-index-calloway-county-kentucky/"),
    ("us-census-kenton-1850-dir-pass140.html",
     "https://us-census.org/pub/usgenweb/census/ky/kenton/1850/"),
    ("us-census-henry-1850-dir-pass140.html",
     "https://us-census.org/pub/usgenweb/census/ky/henry/1850/"),
    ("us-census-hart-1850-dir-pass140.html",
     "https://us-census.org/pub/usgenweb/census/ky/hart/1850/"),
    ("us-census-larue-1850-dir-pass140.html",
     "https://us-census.org/pub/usgenweb/census/ky/larue/1850/"),
    ("kygenweb-kenton-records-pass140.html",
     "https://kygenweb.net/kenton/records/"),
    ("rootsweb-kenton-census-pass140.html",
     "https://sites.rootsweb.com/~kykenton/census.htm"),
    ("genky-home-pass140.html",
     "https://genky.kentonlibrary.org/gendb.php"),
    ("genky-n550-pass140.html",
     "https://genky.kentonlibrary.org/gendb.php?s=.SO&t=N550"),
    ("genky-newman-pass140.html",
     "https://genky.kentonlibrary.org/gendb.php?s=.LN&t=Newman"),
    ("ia-solr-gadson-kenton-pass140.json",
     "https://archive.org/advancedsearch.php?q=GADSON%20AND%20Kenton%20AND%201850&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("ia-solr-clustre-kenton-pass140.json",
     "https://archive.org/advancedsearch.php?q=CLUSTRE%20AND%20%28Kenton%20OR%20Kentucky%29%20AND%201850&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("ia-solr-iliff-kenton-pass140.json",
     "https://archive.org/advancedsearch.php?q=ILIFF%20AND%20Kenton%20AND%201850&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("kykinfolk-owsley-marr-pass140.html",
     "https://kykinfolk.com/owsley/marriages.htm"),
    ("fishergenes-estill-marr-pass140.html",
     "https://www.fishergenes.com/estill/estillmarriages.html"),
]:
    dest = CAT / name
    st, n = fetch(url, dest, timeout=45)
    print(f"  {name} {st} {n}", flush=True)

print("=== Henry Dist 1 from n0440 (reel 204, 589 images) ===", flush=True)
# n0440 header IMAGE SEEN = Henry Dist 1 2 Aug. Walk even leaves first.
for leaf in range(440, 590, 2):
    grab("populationschedu0204unix", leaf, "henry")

print("=== Hart Dist 1 densify n0005–n0188 (before Henderson n0200) ===", flush=True)
for leaf in list(range(5, 190, 4)) + [6, 10, 20, 30, 50, 70, 90, 110, 130, 150, 170, 189]:
    grab("populationschedu0204unix", leaf, "hart")

print("=== Hopkins Dist 2 remaining n0262–n0320 ===", flush=True)
for leaf in range(262, 321, 2):
    grab("populationschedu0205unix", leaf, "hopkins2")

print("=== Larue densify n0160–n0240 ===", flush=True)
for leaf in range(160, 241, 4):
    grab("populationschedu0209unix", leaf, "larue")

print("DONE pass140 fetch", flush=True)
