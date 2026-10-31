#!/usr/bin/env python3
"""Pass 92: remaining Berea Town 102/103 leaves + catalog workarounds."""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass92")
CAT = Path("/workspace/research/dora-ella-newnam/sources/catalog")
PRESS = Path("/workspace/research/dora-ella-newnam/sources/press")
VITAL = Path("/workspace/research/dora-ella-newnam/sources/vital")
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "madison1920").mkdir(exist_ok=True)
CAT.mkdir(parents=True, exist_ok=True)
PRESS.mkdir(parents=True, exist_ok=True)
VITAL.mkdir(parents=True, exist_ok=True)

MAD = "14thcensusofpopu590unit"
UA = "Mozilla/5.0 (compatible; genealogy-research/1.0)"


def curl(url: str, dest: Path, min_size: int = 200) -> bool:
    if dest.exists() and dest.stat().st_size >= min_size:
        print(f"SKIP {dest.name} {dest.stat().st_size}", flush=True)
        return True
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        ["curl", "-fsSL", "-A", UA, "--retry", "2", "--retry-delay", "2",
         "-o", str(dest), url],
        capture_output=True, text=True,
    )
    ok = r.returncode == 0 and dest.exists() and dest.stat().st_size >= min_size
    print(f"{'OK' if ok else 'FAIL'} {dest.name} rc={r.returncode} "
          f"size={dest.stat().st_size if dest.exists() else 0}", flush=True)
    return ok


def ia_leaf(item: str, leaf: int, width: int, dest: Path) -> bool:
    url = f"https://archive.org/download/{item}/page/leaf{leaf:04d}_w{width}.jpg"
    return curl(url, dest, min_size=8000)


def main() -> int:
    # Berea Town ED 103: 0320=2B => start ~0317; 0348=16B short end.
    # ED 102 college: 0350=17B. Pull 0314-0356 every leaf + a few later.
    leaves_w1200 = list(range(314, 357)) + [360, 365, 370]
    ok = fail = 0
    for leaf in leaves_w1200:
        dest = OUT / "madison1920" / f"t625-590-leaf{leaf:04d}-w1200.jpg"
        if ia_leaf(MAD, leaf, 1200, dest):
            ok += 1
        else:
            fail += 1
        time.sleep(0.2)
    print(f"LEAVES ok={ok} fail={fail}", flush=True)

    # Catalog / index workarounds (B088 Antioch, B089 33-8, B045 FS, B049, B016, B082, B055)
    jobs = [
        (CAT / "fs-127913-pass92.html",
         "https://www.familysearch.org/search/catalog/127913"),
        (CAT / "fs-127869-pass92.html",
         "https://www.familysearch.org/search/catalog/127869"),
        (CAT / "fs-1146342-pass92.html",
         "https://www.familysearch.org/search/catalog/1146342"),
        (CAT / "uscensus-madison-1920-pass92.html",
         "https://www.us-census.org/pub/usgenweb/census/ky/madison/1920/"),
        (CAT / "uscensus-wolfe-1920-pass92.html",
         "https://www.us-census.org/pub/usgenweb/census/ky/wolfe/1920/"),
        (CAT / "uscensus-estill-1930-pass92.html",
         "https://www.us-census.org/pub/usgenweb/census/ky/estill/1930/"),
        (CAT / "kygenweb-wolfe-census-pass92.html",
         "https://kygenweb.net/wolfe/census1.htm"),
        (CAT / "kygenweb-madison-pass92.html",
         "https://kygenweb.net/madison/"),
        (CAT / "nara-t626-catalog-pass92.html",
         "https://catalog.archives.gov/search?q=T626%20742%20Kentucky%201930"),
        (PRESS / "ca-frank-newman-berea-pass92.json",
         "https://chroniclingamerica.loc.gov/search/pages/results/?andtext=Frank+Newnam+Berea&format=json&rows=5"),
        (PRESS / "ca-dora-stone-1926-pass92.json",
         "https://chroniclingamerica.loc.gov/search/pages/results/?andtext=Dora+Stone+Ola&date1=1926&date2=1926&format=json&rows=5"),
        (VITAL / "gt-madison-obits-pass92.html",
         "https://genealogytrails.com/ken/madison/obits.html"),
        (CAT / "ia-solr-antioch-242-pass92.json",
         "https://archive.org/advancedsearch.php?q=wolfe+county+kentucky+1920+census+antioch&fl[]=identifier&fl[]=title&fl[]=imagecount&output=json&rows=20"),
        (CAT / "ia-solr-madison-1930-pass92.json",
         "https://archive.org/advancedsearch.php?q=identifier%3A%28kentuckycensus00reel780+OR+15thcensusofpopu780unit+OR+kentuckycensus00reel781%29&fl[]=identifier&fl[]=title&fl[]=imagecount&output=json&rows=10"),
    ]
    for dest, url in jobs:
        curl(url, dest, min_size=80)
        time.sleep(0.3)

    # NARA 1950 Madison Frank / David
    for name, dest in (
        ("Newman", CAT / "nara-1950-madison-newman-pass92.json"),
        ("Newnam", CAT / "nara-1950-madison-newnam-pass92.json"),
        ("Frank", CAT / "nara-1950-madison-frank-newman-pass92.json"),
    ):
        url = (
            "https://1950census.archives.gov/api/search"
            f"?name={name}&state=KY&county=Madison"
        )
        if name == "Frank":
            url = "https://1950census.archives.gov/api/search?name=Frank%20Newman&state=KY&county=Madison"
        curl(url, dest, min_size=20)
        time.sleep(0.3)

    print("CATALOG done", flush=True)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
