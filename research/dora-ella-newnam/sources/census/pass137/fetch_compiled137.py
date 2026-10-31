#!/usr/bin/env python3
"""Pass 137 leftover compiled: SK/USGW/us-census for remaining unclosed KY 1850 counties."""
from __future__ import annotations

import ssl
import urllib.request
from pathlib import Path

ROOT = Path("/workspace/research/dora-ella-newnam")
CAT = ROOT / "sources/catalog"
CAT.mkdir(parents=True, exist_ok=True)
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (compatible; DoraGenealogyResearch/1.0)"


def fetch(url: str, dest: Path, timeout: int = 40) -> tuple[int, int]:
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


counties = [
    "butler", "caldwell", "calloway", "clinton", "cumberland",
    "fulton", "graves", "hart", "hickman", "mccracken",
    "muhlenberg", "todd", "trigg", "union", "warren",
    "livingston", "webster", "lyon", "mclean",
]

print("=== leftover compiled SK / USGW / us-census ===", flush=True)
for co in counties:
    pairs = [
        (f"sk-{co}-1850-pass137.html",
         f"https://www.usgwarchives.net/ky/{co}/census/1850/1850indx.txt"),
        (f"wb-{co}-1850indx-pass137.txt",
         f"https://web.archive.org/web/id_/http://files.usgwarchives.net/ky/{co}/census/1850/1850indx.txt"),
        (f"us-census-{co}-1850-dir-pass137.html",
         f"https://us-census.org/pub/usgenweb/census/ky/{co}/1850/"),
        (f"us-census-{co}-indx-nz-pass137.txt",
         f"https://us-census.org/pub/usgenweb/census/ky/{co}/1850/_indx-n-z.txt"),
        (f"us-census-{co}-indx-mz-pass137.txt",
         f"https://us-census.org/pub/usgenweb/census/ky/{co}/1850/_indx-m-z.txt"),
        (f"us-census-{co}-1850indx-pass137.txt",
         f"https://us-census.org/pub/usgenweb/census/ky/{co}/1850/1850indx.txt"),
    ]
    for name, url in pairs:
        dest = CAT / name
        st, n = fetch(url, dest)
        print(f"  {name} {st} {n}", flush=True)

print("done compiled137", flush=True)
