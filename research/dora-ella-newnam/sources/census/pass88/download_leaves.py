#!/usr/bin/env python3
"""Pass 88: isolate Bell ED 28/30 + Wolfe Torrent/Clifty/Antioch originals."""
from __future__ import annotations

import subprocess
import time
from pathlib import Path

OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass88")
OUT.mkdir(parents=True, exist_ok=True)

# (item, leaf, width, dest_name)
JOBS = [
    # Bell ED 28 hunt: after ED 27 sh 20B (0600) and before ED 29 Ingram (0620)
    ("14thcensusofpopu559unit", 601, 800, "t625-559-leaf0601.jpg"),
    ("14thcensusofpopu559unit", 602, 800, "t625-559-leaf0602.jpg"),
    ("14thcensusofpopu559unit", 604, 800, "t625-559-leaf0604.jpg"),
    ("14thcensusofpopu559unit", 606, 800, "t625-559-leaf0606.jpg"),
    ("14thcensusofpopu559unit", 608, 800, "t625-559-leaf0608.jpg"),
    ("14thcensusofpopu559unit", 610, 800, "t625-559-leaf0610.jpg"),
    ("14thcensusofpopu559unit", 612, 800, "t625-559-leaf0612.jpg"),
    ("14thcensusofpopu559unit", 614, 800, "t625-559-leaf0614.jpg"),
    ("14thcensusofpopu559unit", 616, 800, "t625-559-leaf0616.jpg"),
    ("14thcensusofpopu559unit", 618, 800, "t625-559-leaf0618.jpg"),
    # Bell ED 30 hunt: after ED 29 sh 6B (0640) and before ED 31 Dorothy sh 3B (0670)
    ("14thcensusofpopu559unit", 642, 800, "t625-559-leaf0642.jpg"),
    ("14thcensusofpopu559unit", 644, 800, "t625-559-leaf0644.jpg"),
    ("14thcensusofpopu559unit", 646, 800, "t625-559-leaf0646.jpg"),
    ("14thcensusofpopu559unit", 648, 800, "t625-559-leaf0648.jpg"),
    ("14thcensusofpopu559unit", 650, 800, "t625-559-leaf0650.jpg"),
    ("14thcensusofpopu559unit", 652, 800, "t625-559-leaf0652.jpg"),
    ("14thcensusofpopu559unit", 654, 800, "t625-559-leaf0654.jpg"),
    ("14thcensusofpopu559unit", 656, 800, "t625-559-leaf0656.jpg"),
    ("14thcensusofpopu559unit", 658, 800, "t625-559-leaf0658.jpg"),
    ("14thcensusofpopu559unit", 662, 800, "t625-559-leaf0662.jpg"),
    ("14thcensusofpopu559unit", 664, 800, "t625-559-leaf0664.jpg"),
    ("14thcensusofpopu559unit", 666, 800, "t625-559-leaf0666.jpg"),
    # Bell 25–34 unread name-column densify
    ("14thcensusofpopu559unit", 485, 800, "t625-559-leaf0485.jpg"),
    ("14thcensusofpopu559unit", 510, 800, "t625-559-leaf0510.jpg"),
    ("14thcensusofpopu559unit", 540, 800, "t625-559-leaf0540.jpg"),
    ("14thcensusofpopu559unit", 570, 800, "t625-559-leaf0570.jpg"),
    ("14thcensusofpopu559unit", 630, 800, "t625-559-leaf0630.jpg"),
    ("14thcensusofpopu559unit", 680, 800, "t625-559-leaf0680.jpg"),
    ("14thcensusofpopu559unit", 695, 800, "t625-559-leaf0695.jpg"),
    ("14thcensusofpopu559unit", 710, 800, "t625-559-leaf0710.jpg"),
    # Wolfe 0412–0424: Torrent 238 / Clifty 241 / Antioch 242 window before Whitley
    ("14thcensusofpopu602unit", 412, 1600, "wolfe-leaf0412-w1600.jpg"),
    ("14thcensusofpopu602unit", 414, 1600, "wolfe-leaf0414-w1600.jpg"),
    ("14thcensusofpopu602unit", 416, 1600, "wolfe-leaf0416-w1600.jpg"),
    ("14thcensusofpopu602unit", 418, 1600, "wolfe-leaf0418-w1600.jpg"),
    ("14thcensusofpopu602unit", 422, 1600, "wolfe-leaf0422-w1600.jpg"),
    ("14thcensusofpopu602unit", 424, 1600, "wolfe-leaf0424-w1600.jpg"),
    ("14thcensusofpopu602unit", 426, 1600, "wolfe-leaf0426-w1600.jpg"),
    ("14thcensusofpopu602unit", 428, 1600, "wolfe-leaf0428-w1600.jpg"),
]


def fetch(item: str, leaf: int, width: int, dest: Path) -> bool:
    url = f"https://archive.org/download/{item}/page/leaf{leaf:04d}_w{width}.jpg"
    if dest.exists() and dest.stat().st_size > 8000:
        print(f"SKIP {dest.name} {dest.stat().st_size}", flush=True)
        return True
    for attempt in range(3):
        r = subprocess.run(
            [
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
            ],
            capture_output=True,
            text=True,
        )
        if r.returncode == 0 and dest.exists() and dest.stat().st_size > 8000:
            print(f"OK {dest.name} {dest.stat().st_size}", flush=True)
            return True
        size = dest.stat().st_size if dest.exists() else 0
        print(f"RETRY {dest.name} rc={r.returncode} size={size}", flush=True)
        time.sleep(4 + attempt * 3)
    print(f"FAIL {dest.name}", flush=True)
    return False


def main() -> int:
    ok = fail = 0
    for item, leaf, width, name in JOBS:
        if fetch(item, leaf, width, OUT / name):
            ok += 1
        else:
            fail += 1
        time.sleep(1.3)
    print(f"DONE ok={ok} fail={fail}", flush=True)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
