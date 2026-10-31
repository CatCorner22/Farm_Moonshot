#!/usr/bin/env python3
"""OCR name columns on remaining Bell 25–27 / 28 remainder / 29 / 31–34 sheets."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from PIL import Image, ImageOps

P89 = Path("/workspace/research/dora-ella-newnam/sources/census/pass89")
P90 = Path("/workspace/research/dora-ella-newnam/sources/census/pass90")
CROP = P90 / "crops"
CROP.mkdir(parents=True, exist_ok=True)
OUT = P90 / "bell-ocr.txt"

PAT = re.compile(
    r"newman|newnam|newnarn|newan|newnom|noonan|nunan|mccoy|mc coy",
    re.I,
)


def leaves() -> list[Path]:
    files: dict[int, Path] = {}
    for folder in (P90, P89):
        for p in folder.glob("t625-559-leaf*.jpg"):
            m = re.search(r"leaf(\d+)", p.name)
            if not m:
                continue
            n = int(m.group(1))
            if n < 450 or n > 731:
                continue
            # prefer w1200 / later folder
            if n not in files or "w1200" in p.name:
                files[n] = p
    return [files[k] for k in sorted(files)]


def crop_names(src: Path, dest: Path) -> None:
    im = Image.open(src)
    w, h = im.size
    # name column is left-center of the schedule
    box = (int(w * 0.10), int(h * 0.18), int(w * 0.38), int(h * 0.96))
    crop = ImageOps.invert(im.crop(box).convert("L"))
    crop.save(dest)


def main() -> None:
    rows = []
    hits = []
    for src in leaves():
        dest = CROP / (src.stem + "-names.png")
        try:
            crop_names(src, dest)
        except Exception as e:
            rows.append(f"{src.name}\tCROPFAIL {e}")
            continue
        r = subprocess.run(
            ["tesseract", str(dest), "stdout", "--psm", "6"],
            capture_output=True,
            text=True,
        )
        text = r.stdout or ""
        found = sorted(set(PAT.findall(text)))
        rows.append(f"{src.name}\t{src.stat().st_size}\t{len(text)}\thits={found}")
        if found:
            hits.append((src.name, found, text[:400]))
    OUT.write_text("\n".join(rows) + "\n")
    print(f"OCR {len(rows)} sheets; token-hits {len(hits)}")
    for name, found, snippet in hits:
        print("HIT", name, found)
        print(snippet)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
