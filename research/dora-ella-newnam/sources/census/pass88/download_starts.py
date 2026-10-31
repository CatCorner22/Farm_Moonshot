#!/usr/bin/env python3
"""Pass 88b: official ED starts + Wolfe 237–242 hunt."""
from __future__ import annotations

import subprocess
import time
from pathlib import Path

OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass88")
JOBS = [
    # Official Bell starts
    ("14thcensusofpopu559unit", 609, 1600, "t625-559-leaf0609-w1600.jpg"),
    ("14thcensusofpopu559unit", 643, 1600, "t625-559-leaf0643-w1600.jpg"),
    ("14thcensusofpopu559unit", 610, 1600, "t625-559-leaf0610-w1600.jpg"),
    ("14thcensusofpopu559unit", 644, 1600, "t625-559-leaf0644-w1600.jpg"),
    # Wolfe 236 tail / 237–242 / Whitley junction
    ("14thcensusofpopu602unit", 419, 1600, "wolfe-leaf0419-w1600.jpg"),
    ("14thcensusofpopu602unit", 421, 1600, "wolfe-leaf0421-w1600.jpg"),
    ("14thcensusofpopu602unit", 368, 800, "wolfe-leaf0368.jpg"),
    ("14thcensusofpopu602unit", 372, 800, "wolfe-leaf0372.jpg"),
    ("14thcensusofpopu602unit", 386, 800, "wolfe-leaf0386.jpg"),
    ("14thcensusofpopu602unit", 395, 800, "wolfe-leaf0395.jpg"),
    ("14thcensusofpopu602unit", 405, 800, "wolfe-leaf0405.jpg"),
    ("14thcensusofpopu602unit", 432, 1600, "wolfe-leaf0432-w1600.jpg"),
    ("14thcensusofpopu602unit", 440, 800, "wolfe-leaf0440.jpg"),
]


def fetch(item, leaf, width, dest: Path) -> bool:
    url = f"https://archive.org/download/{item}/page/leaf{leaf:04d}_w{width}.jpg"
    if dest.exists() and dest.stat().st_size > 8000:
        print(f"SKIP {dest.name}", flush=True)
        return True
    for attempt in range(3):
        r = subprocess.run(
            ["curl", "-fsSL", "-A", "Mozilla/5.0 (compatible; genealogy-research/1.0)",
             "--retry", "2", "-o", str(dest), url],
            capture_output=True, text=True,
        )
        if r.returncode == 0 and dest.exists() and dest.stat().st_size > 8000:
            print(f"OK {dest.name} {dest.stat().st_size}", flush=True)
            return True
        print(f"RETRY {dest.name} {r.returncode}", flush=True)
        time.sleep(4 + attempt * 3)
    print(f"FAIL {dest.name}", flush=True)
    return False


def main():
    ok = fail = 0
    for item, leaf, width, name in JOBS:
        if fetch(item, leaf, width, OUT / name):
            ok += 1
        else:
            fail += 1
        time.sleep(1.3)
    print(f"DONE ok={ok} fail={fail}", flush=True)


if __name__ == "__main__":
    main()
