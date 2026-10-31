#!/usr/bin/env python3
"""Pass 94: isolate 1930 Madison Glade 76-18 / 76-19 on T626-769."""
from __future__ import annotations

import subprocess
import time
from pathlib import Path

OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass94")
CAT = Path("/workspace/research/dora-ella-newnam/sources/catalog")
(OUT / "madison1930").mkdir(parents=True, exist_ok=True)
CAT.mkdir(parents=True, exist_ok=True)

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
    # 0394=76-18 1A; 0400=4A; 0410=9A; 0420=14A. Map forward to find 76-18 end + 76-19.
    mapping = sorted(set(
        list(range(425, 521, 5))
        + list(range(430, 521, 10))
        + [422, 424, 426, 428, 432, 434, 436, 438, 442, 444, 446, 448]
    ))
    ok = fail = 0
    for leaf in mapping:
        dest = OUT / "madison1930" / f"t626-769-leaf{leaf:04d}-w800.jpg"
        if ia_leaf(leaf, 800, dest):
            ok += 1
        else:
            fail += 1
        time.sleep(0.12)
    print(f"MAP ok={ok} fail={fail}", flush=True)

    jobs = [
        (CAT / "uscensus-madison-1930-pass94.html",
         "https://www.us-census.org/states/kentucky/teams/Madison1930-T626-769.htm"),
        (CAT / "fs-127913-pass94.html",
         "https://www.familysearch.org/search/catalog/127913"),
        (CAT / "fs-127869-pass94.html",
         "https://www.familysearch.org/search/catalog/127869"),
        (CAT / "fs-1146342-pass94.html",
         "https://www.familysearch.org/search/catalog/1146342"),
        (CAT / "ia-solr-antioch-242-pass94.json",
         "https://archive.org/advancedsearch.php?q=%28antioch+OR+clifty%29+AND+wolfe+AND+kentucky+AND+1920+AND+census&fl[]=identifier&fl[]=title&fl[]=imagecount&output=json&rows=15"),
        (CAT / "ia-solr-t626-742-33-8-pass94.json",
         "https://archive.org/advancedsearch.php?q=%28%22station+camp%22+OR+estill%29+AND+kentucky+AND+1930+AND+census+AND+%28t626+OR+reel%29&fl[]=identifier&fl[]=title&fl[]=imagecount&output=json&rows=20"),
        (CAT / "nara-t626-769-pass94.html",
         "https://catalog.archives.gov/id/40999721"),
    ]
    for dest, url in jobs:
        curl(url, dest, min_size=80)
        time.sleep(0.2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
