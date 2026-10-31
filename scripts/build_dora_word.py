#!/usr/bin/env python3
"""Build Dora Ella Newnam Stone biography Word (.docx) from the master markdown."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
NARRATIVE = ROOT / "research" / "dora-ella-newnam" / "book" / "Dora-Ella-Newnam-Stone-A-Life.md"
DOCX_PATH = NARRATIVE.with_suffix(".docx")

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_RE = re.compile(r"(\*\*[^*]+\*\*)")
CODE_RE = re.compile(r"`([^`]+)`")


def visible_text(text: str) -> str:
    """Markdown links → 'text (url)'; leave bold markers for the run splitter."""
    return LINK_RE.sub(r"\1 (\2)", text)


def add_runs(paragraph, text: str) -> None:
    """Write **bold** and `code` segments into an existing paragraph."""
    text = visible_text(text)
    parts = re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) >= 4:
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("`") and part.endswith("`") and len(part) >= 2:
            run = paragraph.add_run(part[1:-1])
            run.italic = True
            run.font.name = "Liberation Mono"
        else:
            paragraph.add_run(part)


def add_rich_paragraph(doc: Document, text: str, style: str | None = None) -> None:
    p = doc.add_paragraph(style=style)
    add_runs(p, text)


def set_cell_shading(cell, hex_color: str) -> None:
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")
    tcPr.append(shd)


def add_table(doc: Document, rows: list[list[str]]) -> None:
    if not rows:
        return
    cols = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=cols)
    table.style = "Table Grid"
    table.autofit = True
    for i, row in enumerate(rows):
        for j in range(cols):
            cell = table.cell(i, j)
            cell.text = ""
            p = cell.paragraphs[0]
            add_runs(p, row[j] if j < len(row) else "")
            for run in p.runs:
                run.font.size = Pt(9)
                run.font.name = "Liberation Serif"
            if i == 0:
                set_cell_shading(cell, "EDE6D6")
                for run in p.runs:
                    run.bold = True
            # Keep label column readable
            if j == 2 and i > 0:
                for run in p.runs:
                    run.bold = True


def is_table_separator(line: str) -> bool:
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c or "") for c in cells)


def parse_table_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def configure_styles(doc: Document) -> None:
    normal = doc.styles["Normal"]
    normal.font.name = "Liberation Serif"
    normal.font.size = Pt(11)
    normal.font.color.rgb = RGBColor(0x1C, 0x19, 0x17)
    rpr = normal.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    rfonts.set(qn("w:ascii"), "Liberation Serif")
    rfonts.set(qn("w:hAnsi"), "Liberation Serif")
    rfonts.set(qn("w:cs"), "Liberation Serif")

    for level, size in ((0, 22), (1, 16), (2, 13)):
        try:
            style = doc.styles[f"Heading {level}"]
        except KeyError:
            continue
        style.font.name = "Liberation Serif"
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor(0x7C, 0x2D, 0x12)
        style.font.bold = True


def build_docx() -> None:
    if not NARRATIVE.is_file():
        raise SystemExit(f"missing narrative: {NARRATIVE}")
    text = NARRATIVE.read_text(encoding="utf-8")
    doc = Document()
    configure_styles(doc)
    section = doc.sections[0]
    section.top_margin = Inches(0.9)
    section.bottom_margin = Inches(0.9)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

    core = doc.core_properties
    core.title = "Dora Ella Newnam Stone: A Documented Life, 1871–1926"
    core.subject = "Family reading, 31 October 2026. Deceased only. GPS-labelled."
    core.comments = (
        "Generated from research/dora-ella-newnam/book/Dora-Ella-Newnam-Stone-A-Life.md "
        "by scripts/build_dora_word.py. Living descendants are not named."
    )

    table_buf: list[list[str]] = []

    def flush_table() -> None:
        nonlocal table_buf
        if table_buf:
            add_table(doc, table_buf)
            table_buf = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if stripped.startswith("|"):
            if is_table_separator(stripped):
                continue
            table_buf.append(parse_table_row(stripped))
            continue
        flush_table()

        if not stripped:
            continue
        if stripped == "---":
            doc.add_page_break()
            continue
        if line.startswith("# "):
            doc.add_heading(visible_text(line[2:].strip()).replace("**", ""), level=0)
        elif line.startswith("## "):
            doc.add_heading(visible_text(line[3:].strip()).replace("**", ""), level=1)
        elif line.startswith("### "):
            doc.add_heading(visible_text(line[4:].strip()).replace("**", ""), level=2)
        elif re.match(r"^\d+\.\s", stripped):
            add_rich_paragraph(doc, re.sub(r"^\d+\.\s+", "", stripped), style="List Number")
        elif stripped.startswith("- "):
            add_rich_paragraph(doc, stripped[2:], style="List Bullet")
        elif stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**"):
            p = doc.add_paragraph()
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            run = p.add_run(stripped.strip("*"))
            run.italic = True
            run.font.size = Pt(11)
        else:
            add_rich_paragraph(doc, stripped)

    flush_table()
    doc.save(DOCX_PATH)
    print(f"wrote {DOCX_PATH} ({DOCX_PATH.stat().st_size} bytes)")


if __name__ == "__main__":
    build_docx()
