#!/usr/bin/env python3
"""Pass 138b: leftover western compiled dirs; Kenton 130B workarounds;
reel 194 Butler/Caldwell map; Hopkins correct leaves; marriage reconfirm."""
from __future__ import annotations

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


def fetch(url: str, dest: Path, timeout: int = 45) -> tuple[int, int]:
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


print("=== leftover western + Kenton 130B compiled workarounds ===", flush=True)
pairs = [
    ("us-census-ky-inventory-pass138.html",
     "https://www.us-census.org/inventory/kentucky.htm"),
    ("us-census-ky-b-pass138.html",
     "https://www.us-census.org/states/kentucky/b-ky.htm"),
    ("us-census-ky-c-pass138.html",
     "https://www.us-census.org/states/kentucky/c-ky.htm"),
    ("us-census-ky-f-pass138.html",
     "https://www.us-census.org/states/kentucky/f-ky.htm"),
    ("us-census-ky-g-pass138.html",
     "https://www.us-census.org/states/kentucky/g-ky.htm"),
    ("us-census-ky-h-pass138.html",
     "https://www.us-census.org/states/kentucky/h-ky.htm"),
    ("us-census-butler-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/butler/1850/"),
    ("us-census-caldwell-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/caldwell/1850/"),
    ("us-census-calloway-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/calloway/1850/"),
    ("us-census-clinton-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/clinton/1850/"),
    ("us-census-cumberland-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/cumberland/1850/"),
    ("us-census-fulton-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/fulton/1850/"),
    ("us-census-graves-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/graves/1850/"),
    ("us-census-hart-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/hart/1850/"),
    ("us-census-hickman-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/hickman/1850/"),
    ("us-census-allen-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/allen/1850/"),
    ("us-census-warren-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/warren/1850/"),
    ("us-census-union-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/union/1850/"),
    ("us-census-muhlenberg-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/muhlenberg/1850/"),
    ("us-census-grayson-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/grayson/1850/"),
    ("us-census-marshall-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/marshall/1850/"),
    ("us-census-kenton-1850-dir-pass138.html",
     "https://us-census.org/pub/usgenweb/census/ky/kenton/1850/"),
    ("usgw-kenton-1850-pg0130b-pass138.txt",
     "https://www.usgwarchives.net/ky/kenton/census/1850/pg0130b.txt"),
    ("files-usgw-kenton-1850-dir-pass138.html",
     "http://files.usgwarchives.net/ky/kenton/census/1850/"),
    ("files-usgw-kenton-1850indx-pass138.txt",
     "http://files.usgwarchives.net/ky/kenton/census/1850/1850indx.txt"),
    ("gt-kenton-census-pass138.html",
     "https://www.genealogytrails.com/ken/kenton/census.html"),
    ("kygenweb-kenton-census-pass138.html",
     "https://kykinfolk.com/kenton/census.htm"),
    ("kygenweb-kenton-1850-pass138.html",
     "https://www.kykinfolk.com/kenton/census/1850/"),
    ("ia-meta-208-pass138.json",
     "https://archive.org/metadata/populationschedu0208unix"),
    ("ia-meta-194-pass138.json",
     "https://archive.org/metadata/populationschedu0194unix"),
    ("ia-solr-butler-1850-pass138.json",
     "https://archive.org/advancedsearch.php?q=butler%20AND%201850%20AND%20census%20AND%20kentucky&fl[]=identifier&fl[]=title&output=json&rows=8"),
    ("wayback-kenton-1850indx-pass138.txt",
     "https://web.archive.org/web/2015/http://www.usgwarchives.net/ky/kenton/census/1850/1850indx.txt"),
    ("cdx-kenton-1850indx-pass138.json",
     "https://web.archive.org/cdx/search/cdx?url=usgwarchives.net/ky/kenton/census/1850/1850indx.txt&output=json&limit=8"),
    ("cdx-sk-butler-pass138.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-butler-county-kentucky&output=json&limit=8"),
    ("cdx-sk-caldwell-pass138.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-caldwell-county-kentucky&output=json&limit=8"),
    ("cdx-sk-calloway-pass138.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-calloway-county-kentucky&output=json&limit=8"),
    ("cdx-sk-graves-pass138.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-graves-county-kentucky&output=json&limit=8"),
    ("cdx-sk-hart-pass138.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-hart-county-kentucky&output=json&limit=8"),
    ("cdx-sk-hickman-pass138.json",
     "https://web.archive.org/cdx/search/cdx?url=skcensus.com/1850-census-index-hickman-county-kentucky&output=json&limit=8"),
    ("fishergenes-estill-grooms-pass138.html",
     "https://www.fishergenes.com/estill/estillgrooms.html"),
    ("gt-lee-wwi-pass138b.html",
     "https://www.genealogytrails.com/ken/lee/wwi_draft_cards.html"),
]
for name, url in pairs:
    dest = CAT / name
    st, n = fetch(url, dest)
    print(f"  {name} {st} {n}", flush=True)

print("=== reel 194 map (Butler/Caldwell leftover) ===", flush=True)
for leaf in [5, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]:
    grab("populationschedu0194unix", leaf, "r194map")

print("=== Hopkins Dist 2 correct leaves after Francis J n0238 ===", flush=True)
for leaf in [239, 241, 243, 245, 247, 249, 251, 253, 255, 260, 270, 280, 290]:
    grab("populationschedu0205unix", leaf, "hopkins")

print("=== Kenton Dist 1 130B residual samples (not 221B/Dist2) ===", flush=True)
for leaf in [350, 360, 370, 380, 390, 400, 410, 420, 448, 460, 470, 480, 500, 520, 540, 560, 580, 600]:
    grab("populationschedu0208unix", leaf, "kenton130")

print("DONE pass138b", flush=True)
