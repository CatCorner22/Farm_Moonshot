#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import time
from pathlib import Path

OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass87")
JOBS = [
    ("14thcensusofpopu559unit", 480, 800, "t625-559-leaf0480.jpg"),
    ("14thcensusofpopu559unit", 500, 800, "t625-559-leaf0500.jpg"),
    ("14thcensusofpopu559unit", 520, 800, "t625-559-leaf0520.jpg"),
    ("14thcensusofpopu559unit", 580, 800, "t625-559-leaf0580.jpg"),
    ("14thcensusofpopu559unit", 600, 800, "t625-559-leaf0600.jpg"),
    ("14thcensusofpopu559unit", 640, 800, "t625-559-leaf0640.jpg"),
    ("14thcensusofpopu559unit", 670, 800, "t625-559-leaf0670.jpg"),
    ("14thcensusofpopu559unit", 685, 800, "t625-559-leaf0685.jpg"),
    ("14thcensusofpopu559unit", 698, 800, "t625-559-leaf0698.jpg"),
    ("14thcensusofpopu602unit", 380, 1600, "wolfe-leaf0380-w1600.jpg"),
    ("14thcensusofpopu602unit", 410, 1600, "wolfe-leaf0410-w1600.jpg"),
    ("14thcensusofpopu602unit", 420, 1600, "wolfe-leaf0420-w1600.jpg"),
]


def fetch(item, leaf, width, dest: Path) -> bool:
    url = f"https://archive.org/download/{item}/page/leaf{leaf:04d}_w{width}.jpg"
    if dest.exists() and dest.stat().st_size > 8000:
        print(f"SKIP {dest.name}", flush=True)
        return True
    for attempt in range(3):
        r = subprocess.run(
            ["curl", "-fsSL", "-A", "Mozilla/5.0", "-o", str(dest), url],
            capture_output=True,
            text=True,
        )
        if r.returncode == 0 and dest.exists() and dest.stat().st_size > 8000:
            print(f"OK {dest.name} {dest.stat().st_size}", flush=True)
            return True
        print(f"RETRY {dest.name} {r.returncode}", flush=True)
        time.sleep(4)
    print(f"FAIL {dest.name}", flush=True)
    return False


def main():
    for item, leaf, width, name in JOBS:
        fetch(item, leaf, width, OUT / name)
        time.sleep(1.3)


if __name__ == "__main__":
    main()
