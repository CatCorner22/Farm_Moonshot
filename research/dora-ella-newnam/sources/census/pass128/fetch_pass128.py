#!/usr/bin/env python3
"""Pass 128: isolate Woodford 462A, Scott 399/475/480, Lincoln OCR, catalogs."""
from __future__ import annotations

import json
import ssl
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path("/workspace/research/dora-ella-newnam")
CAT = ROOT / "sources/catalog"
CENS = ROOT / "sources/census/pass128"
P125 = ROOT / "sources/census/pass125"
P126 = ROOT / "sources/census/pass126"
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


print("=== B058 / open-item catalogs ===", flush=True)
catalogs = [
    ("loc-sn89051008-pass128.json",
     "https://www.loc.gov/item/sn89051008/?fo=json"),
    ("ia-solr-postdispatch-1926-pass128.json",
     "https://archive.org/advancedsearch.php?q=title%3A%28Dardanelle%20Post-Dispatch%29%20AND%20year%3A1926&fl[]=identifier&fl[]=title&fl[]=year&output=json&rows=10"),
    ("ia-solr-m1509-ky-pass128.json",
     "https://archive.org/advancedsearch.php?q=collection%3Awwi_draft%20AND%20subject%3AKentucky&fl[]=identifier&fl[]=title&output=json&rows=5"),
    ("ia-meta-602-pass128.json",
     "https://archive.org/metadata/14thcensusofpopu0602unit"),
    ("ia-meta-218-pass128.json",
     "https://archive.org/metadata/populationschedu0218unix"),
    ("ia-meta-219-pass128.json",
     "https://archive.org/metadata/populationschedu0219unix"),
    ("ia-meta-222-pass128.json",
     "https://archive.org/metadata/populationschedu0222unix"),
    ("ia-meta-213-pass128.json",
     "https://archive.org/metadata/populationschedu0213unix"),
    ("ia-meta-215-pass128.json",
     "https://archive.org/metadata/populationschedu0215unix"),
    ("gt-lee-wwi-pass128.html",
     "https://www.genealogytrails.com/ken/lee/wwi_draft_cards.html"),
    ("fs-1146342-pass128.html",
     "https://www.familysearch.org/search/catalog/1146342"),
    ("fs-127913-pass128.html",
     "https://www.familysearch.org/search/catalog/127913"),
    ("fs-156057-pass128.html",
     "https://www.familysearch.org/search/catalog/156057"),
    ("usgennet-lee-wills-pass128.html",
     "https://usgennet.org/usa/ky/county/lee/wills/"),
    ("hutchins-faq-9938-pass128.html",
     "https://libraryanswers.berea.edu/faq/9938"),
    ("us-census-woodford-1850-pass128.html",
     "https://us-census.org/pub/usgenweb/census/ky/woodford/1850/"),
    ("us-census-scott-1850-pass128.html",
     "https://us-census.org/pub/usgenweb/census/ky/scott/1850/"),
    ("us-census-lincoln-1850-pass128.html",
     "https://us-census.org/pub/usgenweb/census/ky/lincoln/1850/"),
    ("us-census-spencer-1850-pass128.html",
     "https://us-census.org/pub/usgenweb/census/ky/spencer/1850/"),
    ("us-census-nelson-1850-pass128.html",
     "https://us-census.org/pub/usgenweb/census/ky/nelson/1850/"),
    ("us-census-shelby-1850-pass128.html",
     "https://us-census.org/pub/usgenweb/census/ky/shelby/1850/"),
    ("us-census-kenton-1850-pass128.html",
     "https://us-census.org/pub/usgenweb/census/ky/kenton/1850/"),
    ("kygenweb-lincoln-pass128.html",
     "https://kygenweb.net/lincoln/"),
    ("kygenweb-woodford-census-pass128.html",
     "https://kygenweb.net/woodford/census.htm"),
    ("kygenweb-scott-census-pass128.html",
     "https://kygenweb.net/scott/census.htm"),
    ("kykinfolk-lincoln-marr-pass128.html",
     "https://www.kykinfolk.com/lincoln/marriages.htm"),
    ("kykinfolk-owsley-marr-pass128.html",
     "https://www.kykinfolk.com/owsley/marriages.htm"),
    ("kykinfolk-estill-grooms-pass128.html",
     "https://www.kykinfolk.com/estill/marriages/grooms-to-1850.htm"),
    ("usgw-lincoln-census-pass128.html",
     "https://www.usgwarchives.net/ky/lincoln/census.html"),
    ("wb-lincoln-1850-cdx-pass128.json",
     "https://web.archive.org/cdx/search/cdx?url=files.usgwarchives.net/ky/lincoln/census/1850/*&output=json&limit=20"),
    ("wb-woodford-pg462-cdx-pass128.json",
     "https://web.archive.org/cdx/search/cdx?url=files.usgwarchives.net/ky/woodford/census/1850/*&output=json&limit=20"),
    ("sk-lincoln-1850-pass128.html",
     "https://www.skcensus.com/1850-census-index-lincoln-county-kentucky/"),
    ("wchs-books-pass128.html",
     "https://www.woodfordcountyhistory.org/research/books"),
]
for name, url in catalogs:
    st, n = fetch(url, CAT / name, timeout=40)
    print(f"  {name} {st} {n}", flush=True)
    time.sleep(0.1)

print("=== Woodford 462A window reel 222 n0248-n0266 ===", flush=True)
for leaf in range(248, 267):
    dest = HDR / f"r222-n{leaf:04d}-w900.jpg"
    st, n = fetch(ia_leaf("populationschedu0222unix", leaf, 900), dest, timeout=40)
    print(f"  r222 n{leaf:04d} hdr {st} {n}", flush=True)
    time.sleep(0.07)

print("=== Woodford hi-res candidates n0252-n0260 ===", flush=True)
for leaf in range(252, 261):
    dest = FULL / f"r222-n{leaf:04d}-w1600.jpg"
    st, n = fetch(ia_leaf("populationschedu0222unix", leaf, 1600), dest, timeout=50)
    print(f"  r222 n{leaf:04d} full {st} {n}", flush=True)
    time.sleep(0.1)

print("=== Scott 399 window reel 218 n0460-n0472 ===", flush=True)
for leaf in range(460, 473):
    dest = HDR / f"r218-n{leaf:04d}-w900.jpg"
    st, n = fetch(ia_leaf("populationschedu0218unix", leaf, 900), dest, timeout=40)
    print(f"  r218 n{leaf:04d} 399hdr {st} {n}", flush=True)
    time.sleep(0.07)
for leaf in range(462, 470):
    dest = FULL / f"r218-n{leaf:04d}-w1600.jpg"
    st, n = fetch(ia_leaf("populationschedu0218unix", leaf, 1600), dest, timeout=50)
    print(f"  r218 n{leaf:04d} 399full {st} {n}", flush=True)
    time.sleep(0.1)

print("=== Scott 475-480 window reel 218 n0608-n0630 ===", flush=True)
for leaf in list(range(608, 631, 2)) + [614, 615, 616, 617, 618, 623, 624, 625, 626]:
    dest = HDR / f"r218-n{leaf:04d}-w900.jpg"
    st, n = fetch(ia_leaf("populationschedu0218unix", leaf, 900), dest, timeout=40)
    print(f"  r218 n{leaf:04d} 475hdr {st} {n}", flush=True)
    time.sleep(0.07)

print("=== Scott 475-480 hi-res once stamps lock ===", flush=True)
for leaf in [614, 615, 616, 617, 618, 623, 624, 625, 626]:
    dest = FULL / f"r218-n{leaf:04d}-w1600.jpg"
    st, n = fetch(ia_leaf("populationschedu0218unix", leaf, 1600), dest, timeout=50)
    print(f"  r218 n{leaf:04d} 475full {st} {n}", flush=True)
    time.sleep(0.1)

print("=== Shelby Newman 361/380/385 window ===", flush=True)
for leaf in [386, 387, 422, 423, 424, 425, 432, 433, 434, 435]:
    dest = HDR / f"r218-n{leaf:04d}-w900.jpg"
    st, n = fetch(ia_leaf("populationschedu0218unix", leaf, 900), dest, timeout=40)
    print(f"  r218 n{leaf:04d} shelby {st} {n}", flush=True)
    time.sleep(0.07)

print("=== Spencer reel 219 start + p.72-98 ===", flush=True)
for leaf in [5, 20, 40, 60, 80, 100, 120, 140, 160]:
    dest = HDR / f"r219-n{leaf:04d}-w800.jpg"
    st, n = fetch(ia_leaf("populationschedu0219unix", leaf, 800), dest, timeout=40)
    print(f"  r219 n{leaf:04d} {st} {n}", flush=True)
    time.sleep(0.08)

print("=== Nelson reel 213/215 probe ===", flush=True)
for item, tag in (("populationschedu0213unix", "213"), ("populationschedu0215unix", "215")):
    dest = HDR / f"r{tag}-n0005-w800.jpg"
    st, n = fetch(ia_leaf(item, 5, 800), dest, timeout=40)
    print(f"  r{tag} n0005 {st} {n}", flush=True)
    dest = HDR / f"r{tag}-n0200-w800.jpg"
    st, n = fetch(ia_leaf(item, 200, 800), dest, timeout=40)
    print(f"  r{tag} n0200 {st} {n}", flush=True)

print("=== crop namecols from new fulls ===", flush=True)
for src in sorted(FULL.glob("*.jpg")):
    if src.stat().st_size < 20000:
        continue
    dest = NAMES / f"{src.stem}-names.jpg"
    if dest.exists() and dest.stat().st_size > 4000:
        continue
    try:
        im = Image.open(src)
        w, h = im.size
        crop = im.crop((int(w * 0.05), int(h * 0.08), int(w * 0.52), int(h * 0.98)))
        crop = ImageEnhance.Contrast(crop).enhance(1.3)
        crop.save(dest, quality=82)
    except Exception as e:
        print(f"  crop fail {src.name} {e}", flush=True)
print("  namecols", len(list(NAMES.glob("*.jpg"))), flush=True)

print("DONE fetch_pass128", flush=True)
