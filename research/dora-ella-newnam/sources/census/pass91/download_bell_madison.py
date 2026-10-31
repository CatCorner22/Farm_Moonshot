#!/usr/bin/env python3
"""Pass 91/92: Bell 31-34 remainder + Madison T625-590 mapping leaves."""
from __future__ import annotations

import subprocess
import time
from pathlib import Path

BELL_OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass91/bell1920")
MAD_OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass91/madison1920")
BELL_OUT.mkdir(parents=True, exist_ok=True)
MAD_OUT.mkdir(parents=True, exist_ok=True)

BELL_ITEM = "14thcensusofpopu559unit"
MAD_ITEM = "14thcensusofpopu590unit"


def fetch(item: str, leaf: int, width: int, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 8000:
        print(f"SKIP {dest.name}", flush=True)
        return True
    url = f"https://archive.org/download/{item}/page/leaf{leaf:04d}_w{width}.jpg"
    for attempt in range(3):
        r = subprocess.run(
            [
                "curl", "-fsSL",
                "-A", "Mozilla/5.0 (compatible; genealogy-research/1.0)",
                "--retry", "2", "--retry-delay", "3",
                "-o", str(dest), url,
            ],
            capture_output=True, text=True,
        )
        if r.returncode == 0 and dest.exists() and dest.stat().st_size > 8000:
            print(f"OK {dest.name} {dest.stat().st_size}", flush=True)
            return True
        size = dest.stat().st_size if dest.exists() else 0
        print(f"RETRY {dest.name} rc={r.returncode} size={size}", flush=True)
        time.sleep(2 + attempt * 2)
    print(f"FAIL {dest.name}", flush=True)
    return False


def main() -> int:
    jobs: list[tuple[str, int, int, Path]] = []
    # Bell 26/27 unused + cards + 31-34 remainder
    for leaf, w in (
        (560, 800), (607, 800), (608, 800),
        (665, 800), (670, 800), (675, 1200), (680, 800),
        (685, 1200), (690, 800), (693, 1200), (695, 1200),
        (696, 1200), (697, 1200), (710, 800), (731, 1200),
        (661, 1200),
    ):
        jobs.append((BELL_ITEM, leaf, w, BELL_OUT / f"t625-559-leaf{leaf:04d}-w{w}.jpg"))
    # Madison T625-590 mapping (Berea hunt)
    for leaf in (1, 2, 5, 10, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250,
                 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 550, 600):
        w = 800 if leaf % 25 else 1200
        jobs.append((MAD_ITEM, leaf, w, MAD_OUT / f"t625-590-leaf{leaf:04d}-w{w}.jpg"))

    ok = fail = skip = 0
    for item, leaf, width, dest in jobs:
        if dest.exists() and dest.stat().st_size > 8000:
            skip += 1
            continue
        if fetch(item, leaf, width, dest):
            ok += 1
        else:
            fail += 1
        time.sleep(0.25)
    print(f"DONE ok={ok} skip={skip} fail={fail}", flush=True)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
