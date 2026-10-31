#!/usr/bin/env python3
"""Sequential IA BookReader leaf download (avoid parallel 0-byte rate-limit)."""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass87")
OUT.mkdir(parents=True, exist_ok=True)

# (item, leaf, width, dest_name)
JOBS = [
    # Confirm 0720 ED number at w1600
    ("14thcensusofpopu559unit", 720, 1600, "t625-559-leaf0720-w1600.jpg"),
    ("14thcensusofpopu559unit", 700, 1600, "t625-559-leaf0700-w1600.jpg"),
    # Bell 24 tail / 25-34 hunt
    ("14thcensusofpopu559unit", 690, 800, "t625-559-leaf0690.jpg"),
    ("14thcensusofpopu559unit", 721, 800, "t625-559-leaf0721.jpg"),
    ("14thcensusofpopu559unit", 722, 800, "t625-559-leaf0722.jpg"),
    ("14thcensusofpopu559unit", 724, 800, "t625-559-leaf0724.jpg"),
    ("14thcensusofpopu559unit", 726, 800, "t625-559-leaf0726.jpg"),
    ("14thcensusofpopu559unit", 728, 800, "t625-559-leaf0728.jpg"),
    ("14thcensusofpopu559unit", 730, 800, "t625-559-leaf0730.jpg"),
    ("14thcensusofpopu559unit", 731, 800, "t625-559-leaf0731.jpg"),
    # Bell ED map samples
    ("14thcensusofpopu559unit", 50, 800, "t625-559-leaf0050.jpg"),
    ("14thcensusofpopu559unit", 150, 800, "t625-559-leaf0150.jpg"),
    ("14thcensusofpopu559unit", 250, 800, "t625-559-leaf0250.jpg"),
    ("14thcensusofpopu559unit", 350, 800, "t625-559-leaf0350.jpg"),
    ("14thcensusofpopu559unit", 450, 800, "t625-559-leaf0450.jpg"),
    ("14thcensusofpopu559unit", 550, 800, "t625-559-leaf0550.jpg"),
    ("14thcensusofpopu559unit", 620, 800, "t625-559-leaf0620.jpg"),
    ("14thcensusofpopu559unit", 660, 800, "t625-559-leaf0660.jpg"),
    # ED 40 unread full sheets
    ("14thcensusofpopu559unit", 771, 800, "t625-559-leaf0771.jpg"),
    ("14thcensusofpopu559unit", 772, 800, "t625-559-leaf0772.jpg"),
    ("14thcensusofpopu559unit", 773, 800, "t625-559-leaf0773.jpg"),
    ("14thcensusofpopu559unit", 774, 800, "t625-559-leaf0774.jpg"),
    ("14thcensusofpopu559unit", 775, 800, "t625-559-leaf0775.jpg"),
    ("14thcensusofpopu559unit", 777, 800, "t625-559-leaf0777.jpg"),
    ("14thcensusofpopu559unit", 778, 800, "t625-559-leaf0778.jpg"),
    ("14thcensusofpopu559unit", 779, 800, "t625-559-leaf0779.jpg"),
    ("14thcensusofpopu559unit", 781, 800, "t625-559-leaf0781.jpg"),
    ("14thcensusofpopu559unit", 783, 800, "t625-559-leaf0783.jpg"),
    ("14thcensusofpopu559unit", 785, 800, "t625-559-leaf0785.jpg"),
    ("14thcensusofpopu559unit", 787, 800, "t625-559-leaf0787.jpg"),
    # Wolfe ED map (235 Hazel Green, 238 Torrent, 241 Clifty, 242 Antioch)
    ("14thcensusofpopu602unit", 380, 800, "wolfe-leaf0380.jpg"),
    ("14thcensusofpopu602unit", 385, 800, "wolfe-leaf0385.jpg"),
    ("14thcensusofpopu602unit", 390, 800, "wolfe-leaf0390.jpg"),
    ("14thcensusofpopu602unit", 400, 800, "wolfe-leaf0400.jpg"),
    ("14thcensusofpopu602unit", 410, 800, "wolfe-leaf0410.jpg"),
    ("14thcensusofpopu602unit", 420, 800, "wolfe-leaf0420.jpg"),
    ("14thcensusofpopu602unit", 425, 800, "wolfe-leaf0425.jpg"),
    ("14thcensusofpopu602unit", 430, 800, "wolfe-leaf0430.jpg"),
    ("14thcensusofpopu602unit", 435, 800, "wolfe-leaf0435.jpg"),
]


def fetch(item: str, leaf: int, width: int, dest: Path) -> bool:
    url = f"https://archive.org/download/{item}/page/leaf{leaf:04d}_w{width}.jpg"
    dest.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(3):
        cmd = [
            "curl",
            "-fsSL",
            "-A",
            "Mozilla/5.0 (compatible; genealogy-research/1.0)",
            "--retry",
            "2",
            "--retry-delay",
            "3",
            "-o",
            str(dest),
            url,
        ]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0 and dest.exists() and dest.stat().st_size > 8000:
            print(f"OK {dest.name} {dest.stat().st_size}", flush=True)
            return True
        size = dest.stat().st_size if dest.exists() else 0
        print(f"RETRY {dest.name} rc={r.returncode} size={size} {r.stderr[-120:]}", flush=True)
        time.sleep(4 + attempt * 3)
    print(f"FAIL {dest.name}", flush=True)
    return False


def main() -> int:
    ok = 0
    fail = 0
    for item, leaf, width, name in JOBS:
        dest = OUT / name
        if dest.exists() and dest.stat().st_size > 8000:
            print(f"SKIP {name} already {dest.stat().st_size}", flush=True)
            ok += 1
            continue
        if fetch(item, leaf, width, dest):
            ok += 1
        else:
            fail += 1
        time.sleep(1.4)
    print(f"DONE ok={ok} fail={fail}", flush=True)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
