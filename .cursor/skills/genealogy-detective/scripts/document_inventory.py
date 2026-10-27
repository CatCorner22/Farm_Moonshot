#!/usr/bin/env python3
"""Inventory photos/PDFs of handwritten sources before transcription. Stdlib only.
Reports format, pixel/page dimensions, size, SHA-256. Never modifies files. See references/paleography.md."""
import hashlib, re, struct, sys
from pathlib import Path

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""): h.update(c)
    return h.hexdigest()

def jpeg_size(data):
    i = 2
    while i < len(data) - 9:
        if data[i] != 0xFF: i += 1; continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", data[i + 5:i + 9]); return w, h
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7: i += 2; continue
        i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
    return None

def describe(p: Path):
    data = p.read_bytes(); head = data[:16]
    info = f"{p}  ({len(data):,} bytes)\n  sha256: {sha(p)}"
    if head.startswith(b"\x89PNG"):
        w, h = struct.unpack(">II", data[16:24]); info += f"\n  format: PNG image, {w}x{h}px"
    elif head[:2] == b"\xff\xd8":
        wh = jpeg_size(data); info += f"\n  format: JPEG photo, {wh[0]}x{wh[1]}px" if wh else "\n  format: JPEG photo (dimensions not parsed)"
    elif head.startswith(b"%PDF"):
        pages = len(re.findall(rb"/Type\s*/Page[^s]", data)); count = re.search(rb"/Count\s+(\d+)", data)
        ver = data[5:8].decode(errors="replace")
        info += f"\n  format: PDF {ver}, ~{count.group(1).decode() if count else pages} pages (page-tree count; verify in a viewer)"
        info += "\n  WARNING: any PDF text layer is OCR/transcription (derivative) — verify every relied-upon word against the page image."
    elif head[:4] in (b"II*\x00", b"MM\x00*"):
        info += "\n  format: TIFF image (archive scans often TIFF; check pages/dimensions in an image tool)"
    elif head.startswith((b"GIF8", b"RIFF")):
        info += "\n  format: GIF/WebP image"
    else:
        info += "\n  format: unrecognised — identify before relying on it"
    if any(x in p.suffix.lower() for x in (".png", ".jpg", ".jpeg")):
        info += "\n  check: full page + margins + verso? straight-on, no glare/flash, strokes several px tall? (paleography.md intake)"
    return info

if __name__ == "__main__":
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    for arg in sys.argv[1:]:
        p = Path(arg); print(describe(p) if p.exists() else f"{p}: ERROR no such file")
