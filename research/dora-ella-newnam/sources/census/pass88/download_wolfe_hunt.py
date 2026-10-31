#!/usr/bin/env python3
"""Hunt Wolfe 237-242 on T625-602 (Wayne/Wolfe/Whitley)."""
from __future__ import annotations

import time
import urllib.request
from pathlib import Path

OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass88")
OUT.mkdir(parents=True, exist_ok=True)
ITEM = "14thcensusofpopu602unit"

# Sample the reel: early Wayne, Wayne/Wolfe junction, post-Whitley start, later leaves.
LEAVES = [
    (3, 800),
    (10, 800),
    (50, 800),
    (100, 800),
    (200, 800),
    (300, 800),
    (330, 800),
    (350, 800),
    (360, 800),
    (370, 1600),
    (373, 1600),
    (368, 1600),
    (372, 1600),
    (450, 800),
    (500, 800),
    (600, 800),
    (700, 800),
    (800, 800),
    (900, 800),
    (1000, 800),
    (1100, 800),
    (1200, 800),
    (1300, 800),
    (1400, 800),
]


def url(leaf: int, w: int) -> str:
    return f"https://archive.org/download/{ITEM}/page/leaf{leaf:04d}_w{w}.jpg"


def main() -> None:
    for leaf, w in LEAVES:
        dest = OUT / f"wolfe-hunt-{leaf:04d}-w{w}.jpg"
        if dest.exists() and dest.stat().st_size > 20000:
            print(f"HAVE {dest.name} {dest.stat().st_size}", flush=True)
            continue
        req = urllib.request.Request(
            url(leaf, w),
            headers={"User-Agent": "FarmMoonshotGenealogy/1.0 (research; archive.org)"},
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            dest.write_bytes(data)
            print(f"OK {dest.name} {len(data)}", flush=True)
        except Exception as e:
            print(f"ERR leaf {leaf}: {e}", flush=True)
        time.sleep(0.4)


if __name__ == "__main__":
    main()
