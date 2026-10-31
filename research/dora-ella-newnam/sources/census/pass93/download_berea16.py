#!/usr/bin/env python3
"""Download 1930 Berea Town ED 76-16 (T626-769) at w1200 + edges."""
from __future__ import annotations

import subprocess
import time
from pathlib import Path

OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass93/madison1930")
OUT.mkdir(parents=True, exist_ok=True)
ITEM = "kentuckycensus00reel769"
UA = "Mozilla/5.0 (compatible; genealogy-research/1.0)"


def ia_leaf(leaf: int, width: int) -> bool:
    dest = OUT / f"t626-769-leaf{leaf:04d}-w{width}.jpg"
    if dest.exists() and dest.stat().st_size >= 8000:
        print(f"SKIP {dest.name} {dest.stat().st_size}", flush=True)
        return True
    url = f"https://archive.org/download/{ITEM}/page/leaf{leaf:04d}_w{width}.jpg"
    r = subprocess.run(
        ["curl", "-fsSL", "-A", UA, "--retry", "3", "--retry-delay", "2",
         "--max-time", "60", "-o", str(dest), url],
        capture_output=True, text=True,
    )
    ok = r.returncode == 0 and dest.exists() and dest.stat().st_size >= 8000
    print(f"{'OK' if ok else 'FAIL'} {dest.name} rc={r.returncode} "
          f"size={dest.stat().st_size if dest.exists() else 0}", flush=True)
    if not ok and dest.exists() and dest.stat().st_size < 8000:
        dest.unlink(missing_ok=True)
    return ok


def main() -> int:
    # 335 = 76-15 sh 7B; 340 = 76-16 sh 1A; 375 = 76-16 college 18B; 380 = 76-17 sh 2A
    leaves = list(range(336, 380))
    ok = fail = 0
    for leaf in leaves:
        if ia_leaf(leaf, 1200):
            ok += 1
        else:
            fail += 1
        time.sleep(0.12)
    print(f"BEREA16 ok={ok} fail={fail}", flush=True)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
