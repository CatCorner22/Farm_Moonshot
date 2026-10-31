#!/usr/bin/env python3
"""Pass 89: every unread Wolfe 238–241 leaf + remaining Bell 25–34 name sheets."""
from __future__ import annotations

import subprocess
import time
from pathlib import Path

OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass89")
OUT.mkdir(parents=True, exist_ok=True)

# Existing pass88 files we can reuse (do not re-fetch).
EXISTING = Path("/workspace/research/dora-ella-newnam/sources/census/pass88")

JOBS: list[tuple[str, int, int, str]] = []

# Wolfe Torrent 238 / Holly 239 / Stillwater 240 / Clifty 241 — every leaf 0443–0515
for leaf in range(443, 516):
    JOBS.append(("14thcensusofpopu602unit", leaf, 1200, f"wolfe-leaf{leaf:04d}-w1200.jpg"))

# Bell ED 28 remaining (0609–0619) every leaf at w1200
for leaf in range(609, 620):
    JOBS.append(("14thcensusofpopu559unit", leaf, 1200, f"t625-559-leaf{leaf:04d}-w1200.jpg"))

# Bell ED 30 remaining (0643–0669) every leaf
for leaf in range(643, 670):
    JOBS.append(("14thcensusofpopu559unit", leaf, 1200, f"t625-559-leaf{leaf:04d}-w1200.jpg"))

# Bell 25–27, 29, 31–34 densify unread odds/evens not already on disk
for leaf in (
    list(range(450, 609, 2))
    + list(range(620, 643))
    + list(range(670, 732, 2))
):
    JOBS.append(("14thcensusofpopu559unit", leaf, 800, f"t625-559-leaf{leaf:04d}.jpg"))


def already(name: str) -> Path | None:
    for folder in (OUT, EXISTING):
        p = folder / name
        if p.exists() and p.stat().st_size > 8000:
            return p
    # pass88 used different stems for some Wolfe leaves
    stem = Path(name).stem
    for p in EXISTING.glob("*.jpg"):
        if stem in p.stem and p.stat().st_size > 8000:
            return p
    return None


def fetch(item: str, leaf: int, width: int, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 8000:
        print(f"SKIP {dest.name}", flush=True)
        return True
    url = f"https://archive.org/download/{item}/page/leaf{leaf:04d}_w{width}.jpg"
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
        time.sleep(3 + attempt * 2)
    print(f"FAIL {dest.name}", flush=True)
    return False


def main() -> int:
    ok = fail = skip = 0
    for item, leaf, width, name in JOBS:
        dest = OUT / name
        prior = already(name)
        if prior and prior.parent == OUT:
            skip += 1
            continue
        # Still fetch into pass89 even if pass88 has a lower-res copy — we want w1200 names
        if fetch(item, leaf, width, dest):
            ok += 1
        else:
            fail += 1
        time.sleep(0.9)
    print(f"DONE ok={ok} skip={skip} fail={fail}", flush=True)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
