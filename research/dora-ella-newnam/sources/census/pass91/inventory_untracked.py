#!/usr/bin/env python3
"""Classify untracked pass-90/91 sources; rebuild SOURCE-INVENTORY.tsv."""
from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path

ROOT = Path("/workspace/research/dora-ella-newnam/sources")
INV = ROOT / "SOURCE-INVENTORY.tsv"
SKIP_DIR_PARTS = {".git", "__pycache__"}
JUNK_HINTS = (
    "spa",
    "chrome",
)


def sha12(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def untracked() -> list[str]:
    r = subprocess.run(
        ["git", "-C", "/workspace", "ls-files", "--others", "--exclude-standard", "--", "research/dora-ella-newnam/sources"],
        capture_output=True, text=True, check=True,
    )
    return [ln for ln in r.stdout.splitlines() if ln]


def main() -> None:
    rows = ["path\tbytes\tsha256_12"]
    files: list[Path] = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if any(part in SKIP_DIR_PARTS for part in p.parts):
            continue
        rel = p.relative_to(ROOT)
        files.append(p)
        rows.append(f"{rel.as_posix()}\t{p.stat().st_size}\t{sha12(p)}")
    INV.write_text("\n".join(rows) + "\n")
    u = untracked()
    useful = []
    skip = []
    for rel in u:
        p = Path("/workspace") / rel
        if not p.is_file():
            continue
        size = p.stat().st_size
        name = p.name.lower()
        if size < 200 and name.endswith((".html", ".json")):
            skip.append((rel, size, "tiny"))
        elif "living" in name or "ssn-full" in name:
            skip.append((rel, size, "privacy"))
        else:
            useful.append((rel, size))
    print(f"INVENTORY {len(files)} files -> {INV}")
    print(f"UNTRACKED {len(u)} useful={len(useful)} skip={len(skip)}")
    for rel, size, why in skip[:30]:
        print(f"SKIP {why} {size} {rel}")
    print("--- useful sample ---")
    for rel, size in useful[:40]:
        print(f"KEEP {size} {rel}")


if __name__ == "__main__":
    main()
