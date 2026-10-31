#!/usr/bin/env python3
"""Pass 93: map T626-769 to isolate 1930 Berea Town ED 76-16 + Glade 76-17/18."""
from __future__ import annotations

import subprocess
import time
from pathlib import Path

OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass93")
CAT = Path("/workspace/research/dora-ella-newnam/sources/catalog")
PRESS = Path("/workspace/research/dora-ella-newnam/sources/press")
VITAL = Path("/workspace/research/dora-ella-newnam/sources/vital")
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "madison1930").mkdir(exist_ok=True)
CAT.mkdir(parents=True, exist_ok=True)
PRESS.mkdir(parents=True, exist_ok=True)
VITAL.mkdir(parents=True, exist_ok=True)

ITEM = "kentuckycensus00reel769"
UA = "Mozilla/5.0 (compatible; genealogy-research/1.0)"


def curl(url: str, dest: Path, min_size: int = 200) -> bool:
    if dest.exists() and dest.stat().st_size >= min_size:
        print(f"SKIP {dest.name} {dest.stat().st_size}", flush=True)
        return True
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        ["curl", "-fsSL", "-A", UA, "--retry", "3", "--retry-delay", "2",
         "--max-time", "60", "-o", str(dest), url],
        capture_output=True, text=True,
    )
    ok = r.returncode == 0 and dest.exists() and dest.stat().st_size >= min_size
    print(f"{'OK' if ok else 'FAIL'} {dest.name} rc={r.returncode} "
          f"size={dest.stat().st_size if dest.exists() else 0}", flush=True)
    if not ok and dest.exists() and dest.stat().st_size < min_size:
        dest.unlink(missing_ok=True)
    return ok


def ia_leaf(leaf: int, width: int, dest: Path) -> bool:
    url = f"https://archive.org/download/{ITEM}/page/leaf{leaf:04d}_w{width}.jpg"
    return curl(url, dest, min_size=8000)


def main() -> int:
    # Mapping band: leaf 400 = 76-18 sh 4A; Berea 76-16 is earlier.
    mapping = (
        list(range(200, 421, 20))
        + list(range(300, 411, 10))
        + [250, 270, 285, 295, 305, 315, 325, 335, 345, 355, 365, 375,
           385, 390, 392, 394, 396, 398, 399, 401, 405]
    )
    mapping = sorted(set(mapping))
    ok = fail = 0
    for leaf in mapping:
        dest = OUT / "madison1930" / f"t626-769-leaf{leaf:04d}-w800.jpg"
        if ia_leaf(leaf, 800, dest):
            ok += 1
        else:
            fail += 1
        time.sleep(0.15)
    print(f"MAP ok={ok} fail={fail}", flush=True)

    jobs = [
        (CAT / "uscensus-madison-1930-pass93.html",
         "https://www.us-census.org/states/kentucky/teams/Madison1930-T626-769.htm"),
        (CAT / "ahgp-ky-census-pass93.html",
         "https://ahgp.org/ky/free-kentucky-census-images.html"),
        (CAT / "fs-127913-pass93.html",
         "https://www.familysearch.org/search/catalog/127913"),
        (CAT / "fs-127869-pass93.html",
         "https://www.familysearch.org/search/catalog/127869"),
        (CAT / "fs-1146342-pass93.html",
         "https://www.familysearch.org/search/catalog/1146342"),
        (CAT / "ia-solr-t626-742-missing-pass93.json",
         "https://archive.org/advancedsearch.php?q=estill+county+kentucky+1930+census+station+camp&fl[]=identifier&fl[]=title&fl[]=imagecount&output=json&rows=20"),
        (CAT / "ia-solr-antioch-242-pass93.json",
         "https://archive.org/advancedsearch.php?q=%28antioch+OR+clifty%29+AND+wolfe+AND+kentucky+AND+1920+AND+census&fl[]=identifier&fl[]=title&fl[]=imagecount&output=json&rows=15"),
        (CAT / "nara-t626-769-pass93.html",
         "https://catalog.archives.gov/search?q=T626%20769%20Kentucky%201930%20Madison"),
        (PRESS / "ca-frank-newman-berea-1930-pass93.json",
         "https://chroniclingamerica.loc.gov/search/pages/results/?andtext=Frank+Newman+Berea&date1=1930&date2=1940&format=json&rows=5"),
        (VITAL / "kygenweb-madison-deaths-pass93.html",
         "https://kygenweb.net/madison/"),
    ]
    for dest, url in jobs:
        curl(url, dest, min_size=80)
        time.sleep(0.25)

    print("CATALOG done", flush=True)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
