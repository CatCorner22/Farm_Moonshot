#!/usr/bin/env python3
"""Build Dora Ella Newnam Stone biography Word (.docx) from the master markdown."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
NARRATIVE = ROOT / "research" / "dora-ella-newnam" / "book" / "Dora-Ella-Newnam-Stone-A-Life.md"
DOCX_PATH = NARRATIVE.with_suffix(".docx")


def add_rich_paragraph(doc: Document, text: str, style: str | None = None) -> None:
    """Paragraph with **bold** segments."""
    p = doc.add_paragraph(style=style)
    parts = re.split(r"(\*\*[^*]+\*\*)", text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = p.add_run(part[2:-2])
            run.bold = True
        else:
            p.add_run(part)


def build_docx() -> None:
    if not NARRATIVE.is_file():
        raise SystemExit(f"missing narrative: {NARRATIVE}")
    text = NARRATIVE.read_text(encoding="utf-8")
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = "Libre Baskerville"
    normal.font.size = Pt(11)

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if line.strip() == "---":
            doc.add_page_break()
            continue
        if line.startswith("# "):
            doc.add_heading(line[2:].strip(), level=0)
        elif line.startswith("## "):
            doc.add_heading(line[3:].strip(), level=1)
        elif line.startswith("### "):
            doc.add_heading(line[4:].strip(), level=2)
        elif line.startswith("- "):
            add_rich_paragraph(doc, line[2:].strip(), style="List Bullet")
        elif line.startswith("*") and line.endswith("*") and not line.startswith("**"):
            p = doc.add_paragraph(line.strip("*"))
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            for run in p.runs:
                run.italic = True
        else:
            add_rich_paragraph(doc, line)

    doc.save(DOCX_PATH)
    print(f"wrote {DOCX_PATH} ({DOCX_PATH.stat().st_size} bytes)")


if __name__ == "__main__":
    build_docx()
