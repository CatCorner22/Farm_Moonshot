#!/usr/bin/env python3
"""Pass 90: remaining Bell 25–27 / 31–34 odds + key ED 28/29 w1200 headers."""
from __future__ import annotations

import subprocess
import time
from pathlib import Path

OUT = Path("/workspace/research/dora-ella-newnam/sources/census/pass90")
OUT.mkdir(parents=True, exist_ok=True)
PRIOR = Path("/workspace/research/dora-ella-newnam/sources/census/pass89")

JOBS: list[tuple[str, int, int, str]] = []

# ED 28 official-end + ED 29 start at w1200 for labeled plates
for leaf, w in ((620, 1200), (623, 1200), (628, 1200), (629, 1200), (642, 1200)):
    JOBS.append(("14thcensusofpopu559unit", leaf, w, f"t625-559-leaf{leaf:04d}-w{w}.jpg"))

# Remaining unread odds for Bell 25–27 (after ED 24 ~0450 through 0608)
for leaf in range(451, 609, 2):
    JOBS.append(("14thcensusofpopu559unit", leaf, 800, f"t625-559-leaf{leaf:04d}.jpg"))

# Remaining unread odds for Bell 31–34 (0661–0731)
for leaf in range(661, 732, 2):
    JOBS.append(("14thcensusofpopu559unit", leaf, 800, f"t625-559-leaf{leaf:04d}.jpg"))


def already(dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 8000:
        return True
    p = PRIOR / dest.name
    if p.exists() and p.stat().st_size > 8000 and dest.name.endswith(".jpg") and "w1200" not in dest.name:
        return True
    return False


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
    ok = fail = skip = 0
    for item, leaf, width, name in JOBS:
        dest = OUT / name
        prior = PRIOR / name
        if dest.exists() and dest.stat().st_size > 8000:
            skip += 1
            continue
        if width == 800 and prior.exists() and prior.stat().st_size > 8000:
            skip += 1
            continue
        if fetch(item, leaf, width, dest):
            ok += 1
        else:
            fail += 1
        time.sleep(0.35)
    print(f"DONE ok={ok} skip={skip} fail={fail}", flush=True)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
