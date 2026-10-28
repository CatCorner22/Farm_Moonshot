#!/usr/bin/env python3
"""Build the Dora Ella Newnam Stone biography PDF and refresh the image gallery."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib.colors import Color, HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents
from svglib.svglib import svg2rlg
from reportlab.graphics.shapes import Drawing

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from dora_plates import PLATES, SRC, missing_plates, plate_path, uncatalogued_jpegs  # noqa: E402

CASE = ROOT / "research" / "dora-ella-newnam"
BOOK_DIR = CASE / "book"
NARRATIVE = BOOK_DIR / "Dora-Ella-Newnam-Stone-A-Life.md"
PDF_PATH = BOOK_DIR / "Dora-Ella-Newnam-Stone-A-Life.pdf"
GALLERY_MD = CASE / "12-image-gallery.md"
VISUALS = CASE / "visuals"
CHARTS = [
    ("pedigree-dora.svg", "Pedigree — Dora Ella Newnam Stone",
     "Ancestors as documented. Dashed links are probable. Grandparents beyond Elias and Mary stay probable."),
    ("descendant-dora.svg", "Descendants — Dora’s two unions",
     "Samuel P. Newnam (proved) and five named children plus two unnamed children who died before 1900. The second union with T. A. Stone is dashed (probable, no children in this file)."),
    ("descendant-elias.svg", "Descendants — Elias T. Newnam",
     "Six children including Dora, and granddaughter Provie Hoover Burke on Mary L.’s union — FAN, not Dora’s child."),
    ("timeline-dora.svg", "Lifespan bars, 1842–1980",
     "Samuel’s bar ends at 1910 as a latest bound, not a death date. T. A. Stone is labelled probable."),
]

INK = HexColor("#1c1917")
MUTED = HexColor("#57534e")
RULE = HexColor("#a8a29e")
ACCENT = HexColor("#7c2d12")
PAPER = HexColor("#faf7f2")
PLATE_BG = HexColor("#e7e5e4")

ROLE_LABEL = {
    "family": "Family hit",
    "rejected": "Rejected same-name",
    "negative": "Negative search",
    "context": "Context",
}


def register_fonts() -> None:
    serif = Path("/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf")
    serif_b = Path("/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf")
    serif_i = Path("/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf")
    serif_bi = Path("/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf")
    sans = Path("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf")
    sans_b = Path("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf")
    pdfmetrics.registerFont(TTFont("LibSerif", str(serif)))
    pdfmetrics.registerFont(TTFont("LibSerif-Bold", str(serif_b)))
    pdfmetrics.registerFont(TTFont("LibSerif-Italic", str(serif_i)))
    pdfmetrics.registerFont(TTFont("LibSerif-BoldItalic", str(serif_bi)))
    pdfmetrics.registerFont(TTFont("LibSans", str(sans)))
    pdfmetrics.registerFont(TTFont("LibSans-Bold", str(sans_b)))
    pdfmetrics.registerFontFamily(
        "LibSerif",
        normal="LibSerif",
        bold="LibSerif-Bold",
        italic="LibSerif-Italic",
        boldItalic="LibSerif-BoldItalic",
    )


def styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    s: dict[str, ParagraphStyle] = {}
    s["cover_kicker"] = ParagraphStyle(
        "cover_kicker", parent=base["Normal"], fontName="LibSans", fontSize=9,
        textColor=ACCENT, tracking=2, alignment=TA_CENTER, spaceAfter=10,
    )
    s["cover_title"] = ParagraphStyle(
        "cover_title", parent=base["Normal"], fontName="LibSerif-Bold", fontSize=28,
        leading=34, textColor=INK, alignment=TA_CENTER, spaceAfter=8,
    )
    s["cover_sub"] = ParagraphStyle(
        "cover_sub", parent=base["Normal"], fontName="LibSerif-Italic", fontSize=14,
        leading=20, textColor=MUTED, alignment=TA_CENTER, spaceAfter=18,
    )
    s["cover_meta"] = ParagraphStyle(
        "cover_meta", parent=base["Normal"], fontName="LibSans", fontSize=9,
        leading=13, textColor=MUTED, alignment=TA_CENTER,
    )
    s["h1"] = ParagraphStyle(
        "h1", parent=base["Heading1"], fontName="LibSerif-Bold", fontSize=16,
        leading=20, textColor=INK, spaceBefore=16, spaceAfter=10,
        borderPadding=0,
    )
    s["h2"] = ParagraphStyle(
        "h2", parent=base["Heading2"], fontName="LibSerif-Bold", fontSize=13,
        leading=17, textColor=ACCENT, spaceBefore=14, spaceAfter=8,
    )
    s["h3"] = ParagraphStyle(
        "h3", parent=base["Heading3"], fontName="LibSans-Bold", fontSize=10,
        leading=13, textColor=INK, spaceBefore=10, spaceAfter=6,
    )
    s["body"] = ParagraphStyle(
        "body", parent=base["Normal"], fontName="LibSerif", fontSize=10.5,
        leading=15.2, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=9,
        firstLineIndent=14,
    )
    s["body_first"] = ParagraphStyle(
        "body_first", parent=s["body"], firstLineIndent=0,
    )
    s["epigraph"] = ParagraphStyle(
        "epigraph", parent=base["Normal"], fontName="LibSerif-Italic", fontSize=10,
        leading=14, textColor=MUTED, alignment=TA_LEFT, spaceAfter=12,
        leftIndent=18, rightIndent=18,
    )
    s["caption"] = ParagraphStyle(
        "caption", parent=base["Normal"], fontName="LibSans", fontSize=8.5,
        leading=11.5, textColor=INK, alignment=TA_LEFT, spaceBefore=6, spaceAfter=2,
    )
    s["caption_meta"] = ParagraphStyle(
        "caption_meta", parent=base["Normal"], fontName="LibSans", fontSize=7.5,
        leading=10, textColor=MUTED, spaceAfter=10,
    )
    s["toc"] = ParagraphStyle(
        "toc", parent=base["Normal"], fontName="LibSerif", fontSize=11,
        leading=16, textColor=INK,
    )
    s["footer"] = ParagraphStyle(
        "footer", parent=base["Normal"], fontName="LibSans", fontSize=8,
        textColor=MUTED, alignment=TA_CENTER,
    )
    s["index"] = ParagraphStyle(
        "index", parent=base["Normal"], fontName="LibSans", fontSize=8.5,
        leading=11.5, textColor=INK, spaceAfter=4,
    )
    s["part"] = ParagraphStyle(
        "part", parent=base["Normal"], fontName="LibSerif-Bold", fontSize=20,
        leading=24, textColor=INK, alignment=TA_CENTER, spaceBefore=80, spaceAfter=12,
    )
    s["bullet"] = ParagraphStyle(
        "bullet", parent=s["body"], firstLineIndent=0, leftIndent=12, bulletIndent=0,
    )
    return s


def md_inline(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`([^`]+)`", r"<font face='LibSans' size='8'>\1</font>", text)
    text = re.sub(r"\[(C[0-9]+[–\-]?[C0-9]*)\]", r"<font size='7' color='#7c2d12'>[\1]</font>", text)
    text = re.sub(r"\[(S[0-9]+)\]", r"<font size='7' color='#57534e'>[\1]</font>", text)
    return text


class NumberedDoc(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name in ("h1", "part"):
            text = flowable.getPlainText()
            level = 0 if flowable.style.name == "part" else 1
            self.notify("TOCEntry", (level, text, self.page))


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PAPER)
    canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
    if doc.page > 1:
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.4)
        canvas.line(0.75 * inch, letter[1] - 0.55 * inch, letter[0] - 0.75 * inch, letter[1] - 0.55 * inch)
        canvas.setFont("LibSans", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(0.75 * inch, letter[1] - 0.45 * inch, "DORA ELLA NEWNAM STONE")
        canvas.drawRightString(letter[0] - 0.75 * inch, letter[1] - 0.45 * inch, "A DOCUMENTED LIFE")
        canvas.line(0.75 * inch, 0.55 * inch, letter[0] - 0.75 * inch, 0.55 * inch)
        canvas.drawCentredString(letter[0] / 2, 0.38 * inch, str(doc.page))
    canvas.restoreState()


def jpeg_flowable(path: Path, max_w: float, max_h: float) -> Image:
    with PILImage.open(path) as im:
        im = im.convert("RGB")
        w, h = im.size
        scale = min(max_w / w, max_h / h, 1.0)
        # Downsample large microfilm frames so the PDF stays readable and lean.
        target = (max(1, int(w * min(scale, 1600 / max(w, 1)))), max(1, int(h * min(scale, 1600 / max(h, 1)))))
        if target[0] < w or target[1] < h:
            im = im.resize(target, PILImage.Resampling.LANCZOS)
        tmp = Path("/tmp") / f"dora-plate-{path.stem}.jpg"
        im.save(tmp, "JPEG", quality=82, optimize=True)
        iw, ih = im.size
    display_scale = min(max_w / iw, max_h / ih)
    return Image(str(tmp), width=iw * display_scale, height=ih * display_scale)


def svg_flowable(path: Path, max_w: float, max_h: float):
    drawing = svg2rlg(str(path))
    if drawing is None:
        return Paragraph(f"[Could not render {path.name}]", styles()["caption"])
    w, h = drawing.width, drawing.height
    if w == 0 or h == 0:
        return Paragraph(f"[Empty SVG {path.name}]", styles()["caption"])
    scale = min(max_w / w, max_h / h)
    drawing.width = w * scale
    drawing.height = h * scale
    drawing.scale(scale, scale)
    return drawing


def parse_narrative(st: dict) -> list:
    text = NARRATIVE.read_text(encoding="utf-8")
    lines = text.splitlines()
    story = []
    para_buf: list[str] = []
    first_in_section = True

    def flush():
        nonlocal para_buf, first_in_section
        if not para_buf:
            return
        raw = " ".join(para_buf).strip()
        para_buf = []
        if not raw:
            return
        style = st["body_first"] if first_in_section else st["body"]
        first_in_section = False
        if raw.startswith("*") and raw.endswith("*") and raw.count("*") == 2:
            story.append(Paragraph(md_inline(raw), st["epigraph"]))
        else:
            story.append(Paragraph(md_inline(raw), style))

    for line in lines:
        if line.startswith("# ") and not story:
            # Cover uses the title; skip the markdown H1 inside the body.
            continue
        if line.startswith("## "):
            flush()
            first_in_section = True
            title = line[3:].strip()
            story.append(Paragraph(md_inline(title), st["h1"]))
            continue
        if line.startswith("### "):
            flush()
            first_in_section = True
            title = line[4:].strip()
            story.append(Paragraph(md_inline(title), st["h2"]))
            continue
        if line.strip() == "---":
            flush()
            first_in_section = True
            story.append(Spacer(1, 8))
            continue
        if line.startswith("- "):
            flush()
            first_in_section = False
            story.append(Paragraph("• " + md_inline(line[2:].strip()), st["bullet"]))
            continue
        if not line.strip():
            flush()
            continue
        para_buf.append(line.strip())
    flush()
    return story


def plate_block(plate: dict, st: dict, max_w: float, max_h: float) -> list:
    path = plate_path(plate)
    img = jpeg_flowable(path, max_w, max_h)
    head = Paragraph(
        md_inline(f"**Plate {plate['n']:02d}.** {plate['title']}"),
        st["caption"],
    )
    meta = Paragraph(
        f"{plate['date']}  ·  {ROLE_LABEL[plate['role']]}  ·  {plate['path']}  ·  {plate['source']}",
        st["caption_meta"],
    )
    cap = Paragraph(md_inline(plate["caption"]), st["caption"])
    return [Spacer(1, 6), img, head, cap, meta]


def build_gallery_markdown() -> None:
    lines = [
        "# Source-image gallery: Dora Ella Newnam Stone",
        "",
        f"Sixty-one JPEG images captured from NARA microfilm (via Internet Archive) during this case. "
        f"They are ordered by **the date of the census they record or index**, not by the date the film was scanned.",
        "",
        "Soundex and Miracode cards sit with the census year they index, immediately after any original population schedules for that year.",
        "",
        "| Role | Meaning |",
        "|---|---|",
        "| **Family hit** | Names Dora or a documented relative |",
        "| **Rejected same-name** | A Dora, Samuel, Thomas, or similar who fails the same-person test |",
        "| **Negative search** | The alphabetical or dwelling slot where our person would appear — they are not there |",
        "| **Context** | Adjacent page or divider, kept so the search window can be verified |",
        "",
        "Diplomatic transcriptions: [`08-transcriptions.md`](08-transcriptions.md). "
        "Citations: [`04-evidence.md`](04-evidence.md). "
        "Checksums: [`sources/INVENTORY.txt`](sources/INVENTORY.txt). "
        "Master biography: [`book/Dora-Ella-Newnam-Stone-A-Life.md`](book/Dora-Ella-Newnam-Stone-A-Life.md).",
        "",
        "---",
        "",
        "## Contents",
        "",
        "| # | Record date | Role | Image |",
        "|---|---|---|---|",
    ]
    for p in PLATES:
        lines.append(
            f"| {p['n']} | {p['date']} | {ROLE_LABEL[p['role']]} | [{p['title']}](sources/{p['path']}) |"
        )
    lines += ["", "---", ""]
    current_year = None
    for p in PLATES:
        if p["year"] != current_year:
            current_year = p["year"]
            heading = {
                1870: "1870 — original population schedules",
                1880: "1880 — schedules and Soundex",
                1900: "1900 — Missouri Stone search (Tom A. candidates)",
                1910: "1910 — Soundex, Peebles test, and Sturgeon ED 99",
                1920: "1920 — Kentucky Newman index and Beattyville original",
            }[current_year]
            lines += [f"## {heading}", ""]
        lines += [
            f"### {p['n']} · {p['date']} · {p['title']}",
            "",
            f"**Role:** {ROLE_LABEL[p['role']]}  ",
            f"**File:** [`sources/{p['path']}`](sources/{p['path']})  ",
            f"**Source:** {p['source']}",
            "",
            p["caption"],
            "",
            f"![{p['title']}](sources/{p['path']})",
            "",
        ]
    GALLERY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_pdf() -> None:
    register_fonts()
    st = styles()
    BOOK_DIR.mkdir(parents=True, exist_ok=True)

    missing = missing_plates()
    extra = uncatalogued_jpegs()
    if missing:
        names = ", ".join(p["path"] for p in missing)
        raise SystemExit(f"Missing plate files: {names}")
    if extra:
        names = ", ".join(str(p.relative_to(SRC)) for p in extra)
        print(f"warning: uncatalogued JPEGs (not in PDF): {names}", file=sys.stderr)

    doc = NumberedDoc(
        str(PDF_PATH),
        pagesize=letter,
        leftMargin=0.85 * inch,
        rightMargin=0.85 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        title="Dora Ella Newnam Stone: A Documented Life",
        author="Farm Moonshot genealogy case file",
        subject="GPS biography of Dora Ella Newnam (later Stone), 1871–1926",
    )

    story = []
    # Cover
    story.append(Spacer(1, 1.6 * inch))
    story.append(Paragraph("A GENEALOGICAL BIOGRAPHY", st["cover_kicker"]))
    story.append(Paragraph("Dora Ella Newnam Stone", st["cover_title"]))
    story.append(Paragraph("A documented life, 1871–1926", st["cover_sub"]))
    story.append(Spacer(1, 0.35 * inch))
    story.append(Paragraph(
        "Lee County, Kentucky · Yell County, Arkansas<br/>"
        "Two documented marriages · Sixty-one archival plates<br/>"
        "Compiled 28 October 2026 from every research chat in this project",
        st["cover_meta"],
    ))
    story.append(PageBreak())

    story.append(Paragraph("Contents", st["h1"]))
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("toc0", fontName="LibSerif-Bold", fontSize=11, leading=16, textColor=INK),
        ParagraphStyle("toc1", fontName="LibSerif", fontSize=10, leading=14, textColor=INK, leftIndent=14),
    ]
    story.append(toc)
    story.append(PageBreak())

    story.append(Paragraph("Part I — The life", st["part"]))
    story.append(Paragraph(
        "Written in Standard English and active voice from cited records only. "
        "Confidence below proved is stated in the sentence, not hidden in a footnote.",
        st["epigraph"],
    ))
    story.append(PageBreak())
    story.extend(parse_narrative(st))
    story.append(PageBreak())

    story.append(Paragraph("Part II — The plates", st["part"]))
    story.append(Paragraph(
        "Every JPEG preserved in the case file, in chronological order of the record. "
        "Negatives are evidence: they show where Dora was not.",
        st["epigraph"],
    ))
    story.append(PageBreak())

    max_w = letter[0] - 1.7 * inch
    max_h = 6.3 * inch
    for p in PLATES:
        block = plate_block(p, st, max_w, max_h)
        story.extend(block)
        story.append(PageBreak())

    story.append(Paragraph("Part III — Charts", st["part"]))
    story.append(Paragraph(
        "Generated from family.json. Dashed links mean probable. Living people born after 1926 are omitted.",
        st["epigraph"],
    ))
    story.append(PageBreak())
    for fname, title, cap in CHARTS:
        path = VISUALS / fname
        story.append(Paragraph(md_inline(title), st["h1"]))
        story.append(Paragraph(md_inline(cap), st["caption"]))
        if path.is_file():
            story.append(Spacer(1, 8))
            story.append(svg_flowable(path, max_w, 8.2 * inch))
        story.append(PageBreak())

    story.append(Paragraph("Picture index", st["h1"]))
    story.append(Paragraph(
        "All sixty-one plates, with role and source tags. Each plate occupies its own page in Part II "
        "(Plate 1 begins on the page after the Part II divider).",
        st["body_first"],
    ))
    rows = [[
        Paragraph("<b>#</b>", st["index"]),
        Paragraph("<b>Date</b>", st["index"]),
        Paragraph("<b>Role</b>", st["index"]),
        Paragraph("<b>Title</b>", st["index"]),
        Paragraph("<b>File</b>", st["index"]),
    ]]
    for p in PLATES:
        rows.append([
            Paragraph(str(p["n"]), st["index"]),
            Paragraph(p["date"], st["index"]),
            Paragraph(ROLE_LABEL[p["role"]], st["index"]),
            Paragraph(p["title"], st["index"]),
            Paragraph(p["path"].split("/")[-1], st["index"]),
        ])
    table = Table(rows, colWidths=[0.4 * inch, 1.05 * inch, 1.15 * inch, 2.6 * inch, 2.0 * inch])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, 0), 0.6, ACCENT),
        ("LINEBELOW", (0, 1), (-1, -1), 0.2, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#f5f0eb")),
    ]))
    story.append(table)

    doc.multiBuild(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"wrote {PDF_PATH} ({PDF_PATH.stat().st_size} bytes)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gallery-only", action="store_true")
    args = parser.parse_args()
    build_gallery_markdown()
    print(f"wrote {GALLERY_MD}")
    if not args.gallery_only:
        build_pdf()


if __name__ == "__main__":
    main()
