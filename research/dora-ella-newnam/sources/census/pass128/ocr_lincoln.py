#!/usr/bin/env python3
"""OCR Lincoln 1850 name columns for Newman/Tincher tokens. Draft only."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path("/workspace/research/dora-ella-newnam/sources/census")
OUT = ROOT / "pass128" / "lincoln-ocr-hits.txt"
OUT.parent.mkdir(parents=True, exist_ok=True)

cols = []
for folder in (ROOT / "pass125" / "namecols", ROOT / "pass126" / "namecols", ROOT / "pass127" / "namecols"):
    if folder.exists():
        cols.extend(sorted(folder.glob("r210-n*-names.jpg")))

# also pass125 fulls cropped? namecols preferred
print(f"namecols {len(cols)}", flush=True)

pat = re.compile(
    r"newm|newn|numan|nunan|tincher|tinch|fincher|tinker|newham|newnan",
    re.I,
)
hits = []
nil = 0
for p in cols:
    try:
        r = subprocess.run(
            ["tesseract", str(p), "stdout", "--psm", "6", "-l", "eng"],
            capture_output=True,
            text=True,
            timeout=25,
        )
        text = r.stdout or ""
        if pat.search(text):
            hits.append(f"HIT {p.name}\n{text}\n---\n")
            print(f"HIT {p.name}", flush=True)
        else:
            nil += 1
    except Exception as e:
        hits.append(f"ERR {p.name} {e}\n")

OUT.write_text(
    f"Lincoln 1850 namecol OCR draft. files={len(cols)} token-hits={len([h for h in hits if h.startswith('HIT')])} nil={nil}\n\n"
    + "".join(hits)
)
print(f"wrote {OUT} hits={len(hits)} nil={nil}", flush=True)
