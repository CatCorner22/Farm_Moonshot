#!/usr/bin/env python3
"""Pass 91: T626-742 after 0900 + missing 33-8 hunt + header crops."""
from __future__ import annotations

import subprocess
import time
from pathlib import Path

OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass91/estill1930")
PRIOR = Path("/workspace/research/dora-ella-newnam/sources/census/pass90/estill1930")
OUT.mkdir(parents=True, exist_ok=True)
ITEM = "kentuckycensus00reel742"


def fetch(leaf: int, width: int, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 8000:
        print(f"SKIP {dest.name}", flush=True)
        return True
    prior = PRIOR / f"reel742-leaf{leaf:04d}.jpg"
    if width == 800 and prior.exists() and prior.stat().st_size > 8000 and "w" not in dest.name:
        print(f"PRIOR {dest.name}", flush=True)
        return True
    url = f"https://archive.org/download/{ITEM}/page/leaf{leaf:04d}_w{width}.jpg"
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
    jobs: list[tuple[int, int, str]] = []
    # High-res labeled plates for the 33-7/33-10 junction
    for leaf, w in ((819, 1200), (820, 1200), (821, 1600), (747, 1200)):
        jobs.append((leaf, w, f"reel742-leaf{leaf:04d}-w{w}.jpg"))
    # Every leaf 0901–1020 (33-12 tail / 33-13 / possible late 33-8 / Grant start)
    for leaf in range(901, 1021):
        jobs.append((leaf, 800, f"reel742-leaf{leaf:04d}.jpg"))
    # Probe later Grant / reel end
    for leaf in (1050, 1080, 1100, 1120, 1140, 1160, 1164, 1165):
        jobs.append((leaf, 800, f"reel742-leaf{leaf:04d}.jpg"))
    # Dense 33-5/33-6 confirmation samples still unread
    for leaf in (720, 730, 740, 744, 745, 746):
        jobs.append((leaf, 800, f"reel742-leaf{leaf:04d}.jpg"))

    ok = fail = skip = 0
    for leaf, width, name in jobs:
        dest = OUT / name
        prior = PRIOR / f"reel742-leaf{leaf:04d}.jpg"
        if dest.exists() and dest.stat().st_size > 8000:
            skip += 1
            continue
        if width == 800 and prior.exists() and prior.stat().st_size > 8000:
            skip += 1
            continue
        if fetch(leaf, width, dest):
            ok += 1
        else:
            fail += 1
        time.sleep(0.28)
    print(f"DONE ok={ok} skip={skip} fail={fail}", flush=True)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
