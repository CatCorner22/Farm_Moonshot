#!/usr/bin/env python3
"""Build a Word source-and-document index for the Dora Ella Newnam Stone case.

Reads the live case folder (evidence register, transcriptions, plates, sources/)
and writes research/dora-ella-newnam/book/Dora-Ella-Newnam-Stone-Source-Index.docx
with Heading styles, a Word TOC field, and a full citation for every S###.
"""

from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement
from docx.oxml.ns import qn, nsmap
from docx.shared import Cm, Inches, Pt, RGBColor, Twips
from docx.enum.style import WD_STYLE_TYPE

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "research" / "dora-ella-newnam"
EVIDENCE = CASE / "04-evidence.md"
TRANSCRIPTS = CASE / "08-transcriptions.md"
SOURCES = CASE / "sources"
INVENTORY = SOURCES / "INVENTORY.txt"
TSV = SOURCES / "SOURCE-INVENTORY.tsv"
BOOK_DIR = CASE / "book"
OUT = BOOK_DIR / "Dora-Ella-Newnam-Stone-Source-Index.docx"

sys.path.insert(0, str(ROOT / "scripts"))
from dora_plates import PLATES  # noqa: E402

INK = RGBColor(0x1C, 0x19, 0x17)
MUTED = RGBColor(0x57, 0x53, 0x4E)
ACCENT = RGBColor(0x7C, 0x2D, 0x12)
RULE = RGBColor(0xA8, 0xA2, 0x9E)
HEADER_BG = "F4EDE4"
ALT_BG = "FAF7F2"
NY = ZoneInfo("America/New_York")

SKIP_FILE_NAMES = {".ds_store", ".gitignore"}
SKIP_SUFFIXES = {".pdf"}  # keep images/text; PDFs if present are listed
ID_RE = re.compile(r"S(\d+)")
RANGE_RE = re.compile(r"^S(\d+)\s*[–\-—]\s*S(\d+)$")
DOC_HEAD_RE = re.compile(r"^##\s+(DOC\d+)\s*[—–-]\s*(.+?)\s*$")
CLAIM_ID_RE = re.compile(r"^C\d+[a-z]?$")
CLAIM_RANGE_RE = re.compile(r"^C(\d+)\s*[–\-—]\s*C(\d+)$")
URL_RE = re.compile(r"https?://[^\s)|>\]]+")
MD_BOLD = re.compile(r"\*\*([^*]+)\*\*")
MD_CODE = re.compile(r"`([^`]+)`")
MD_ITAL = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")


def now() -> str:
    return datetime.now(NY).strftime("%-d %B %Y")


def strip_md(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = MD_BOLD.sub(r"\1", text)
    text = MD_CODE.sub(r"\1", text)
    text = MD_ITAL.sub(r"\1", text)
    text = text.replace("**", "")
    return re.sub(r"\s+", " ", text).strip()


def short_title(citation: str, limit: int = 96) -> str:
    clean = strip_md(citation)
    cut = clean.split(". ")[0].split(";")[0]
    if len(cut) > limit:
        cut = cut[: limit - 1].rstrip() + "…"
    return cut


def classify_source(citation: str, source_class: str) -> str:
    t = citation.lower()
    sc = source_class.lower()
    if "soundex" in t or "miracode" in t:
        return "Soundex / Miracode"
    if "numident" in t or "social security" in t:
        return "Social Security / NUMIDENT"
    if any(k in t for k in ("death certificate", "death index", "vital statistics death", "deaths 1", "obituar")):
        if "obituar" in t or "enterprise" in t or "newspaper" in t:
            return "Newspapers / obituaries"
        return "Vital records (death)"
    if any(k in t for k in ("marriage book", "married", "m. ", "bride", "groom", "license")) and "census" not in t:
        return "Vital records (marriage)"
    if "birth" in t and "census" not in t:
        return "Vital records (birth)"
    if "cemetery" in t or "find a grave" in t or "findagrave" in t or "memorial" in t:
        return "Cemetery / memorial"
    if any(k in t for k in ("newspaper", "enterprise", "chronicling", "obits", "press", "journal")):
        return "Newspapers / obituaries"
    if any(k in t for k in ("will of", "probate", "deed", "land", "tax")):
        return "Probate / land / court"
    if "wwi" in t or "draft" in t or "military" in t:
        return "Military"
    if "census" in t or "population" in t or "enumerator" in t:
        return "Census population schedules"
    if sc.startswith("a") or "wikitree" in t or "compiled" in t or "family history" in t:
        return "Authored / compiled"
    if "catalog" in t or "inventory of county" in t:
        return "Catalog / finding aid"
    return "Other / method"


def access_label(citation: str) -> str:
    t = citation.lower()
    if "image seen" in t or "card images seen" in t or "original image" in t or "images seen" in t:
        return "Image seen"
    if "transcription only" in t:
        return "Transcription only"
    if "index only" in t:
        return "Index only"
    if "ocr" in t:
        return "OCR / derivative scan"
    if "catalog" in t:
        return "Catalog only"
    if "prior session" in t or "not re-opened" in t or "not re-fetched" in t:
        return "Prior session"
    return "Cited"


def parse_table_rows(md_path: Path, header_marker: str) -> list[list[str]]:
    """Parse GitHub-style tables that follow a `## heading` until the next `##`."""
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == header_marker or line.strip().startswith(header_marker + " "):
            start = i + 1
            break
    if start is None:
        raise SystemExit(f"heading not found: {header_marker} in {md_path}")
    rows: list[list[str]] = []
    in_table = False
    for raw in lines[start:]:
        line = raw.strip()
        if line.startswith("## ") and in_table:
            break
        if not line:
            continue
        if not line.startswith("|"):
            if in_table:
                break
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells or all(not c for c in cells):
            continue
        if cells and set(cells[0].replace(":", "")) <= {"-"}:
            in_table = True
            continue
        if not in_table and cells and cells[0].lower() in {"id", "claim id"}:
            in_table = True
            continue
        if in_table:
            rows.append(cells)
    return rows


def expand_source_ids(raw: str) -> list[str]:
    raw = raw.strip()
    m = RANGE_RE.match(raw)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        return [f"S{n:03d}" for n in range(a, b + 1)]
    if re.fullmatch(r"S\d+", raw):
        return [f"S{int(raw[1:]):03d}"]
    return [raw]


def parse_sources() -> list[dict]:
    rows = parse_table_rows(EVIDENCE, "## Sources")
    out: list[dict] = []
    seen: set[str] = set()
    for cells in rows:
        if len(cells) < 3:
            continue
        raw_id, citation, source_class = cells[0], cells[1], cells[2]
        informant = cells[3] if len(cells) > 3 else ""
        ids = expand_source_ids(raw_id)
        for sid in ids:
            if sid in seen:
                # later duplicate row (out-of-order re-entry): keep first, note extra
                continue
            seen.add(sid)
            urls = URL_RE.findall(citation)
            files = re.findall(r"`(sources/[^`]+)`", citation)
            files += re.findall(r"(?<!`)sources/[A-Za-z0-9_./-]+\.(?:jpg|jpeg|png|txt|html|md|json)", citation)
            sha = re.findall(r"`([0-9a-f]{64})`", citation)
            sha += re.findall(r"(?<!`)([0-9a-f]{64})", citation)
            out.append(
                {
                    "id": sid,
                    "n": int(sid[1:]),
                    "citation": strip_md(citation),
                    "citation_md": citation,
                    "source_class": source_class,
                    "informant": strip_md(informant),
                    "category": classify_source(citation, source_class),
                    "access": access_label(citation),
                    "title": short_title(citation),
                    "urls": urls,
                    "files": list(dict.fromkeys(files)),
                    "sha": list(dict.fromkeys(sha)),
                }
            )
    out.sort(key=lambda r: r["n"])
    return out


def parse_claims() -> list[dict]:
    rows = parse_table_rows(EVIDENCE, "## Claims")
    out = []
    seen: set[str] = set()
    for cells in rows:
        if len(cells) < 5:
            continue
        raw_id = cells[0].strip()
        ids: list[str] = []
        rm = CLAIM_RANGE_RE.match(raw_id)
        if rm:
            width = max(len(rm.group(1)), 3)
            ids = [f"C{n:0{width}d}" for n in range(int(rm.group(1)), int(rm.group(2)) + 1)]
        elif CLAIM_ID_RE.match(raw_id):
            ids = [raw_id]
        else:
            continue
        source_field = cells[4] if len(cells) > 4 else ""
        source_ids = [f"S{int(m):03d}" for m in ID_RE.findall(source_field)]
        claim_text = strip_md(cells[1]) if len(cells) > 1 else ""
        confidence = strip_md(cells[2]) if len(cells) > 2 else ""
        for cid in ids:
            if cid in seen:
                continue
            seen.add(cid)
            num = int(re.match(r"C(\d+)", cid).group(1))
            suffix = cid[len(f"C{num}") :]
            out.append(
                {
                    "id": cid,
                    "n": num,
                    "suffix": suffix,
                    "claim": claim_text,
                    "confidence": confidence,
                    "sources": source_ids,
                    "source_field": strip_md(source_field),
                }
            )
    out.sort(key=lambda r: (r["n"], r.get("suffix", "")))
    return out


def parse_docs() -> list[dict]:
    text = TRANSCRIPTS.read_text(encoding="utf-8")
    out: list[dict] = []
    seen: Counter[str] = Counter()
    current = None
    for line in text.splitlines():
        m = DOC_HEAD_RE.match(line)
        if m:
            if current:
                out.append(current)
            did, title = m.group(1), m.group(2).strip()
            seen[did] += 1
            suffix = f" ({seen[did]})" if seen[did] > 1 else ""
            current = {
                "id": did,
                "n": int(did[3:]),
                "title": strip_md(title) + suffix,
                "source": "",
                "image": "",
                "sha": "",
                "claims": [],
                "lines": [],
            }
            continue
        if current is None:
            continue
        if line.startswith("## ") and not line.startswith("## DOC"):
            out.append(current)
            current = None
            continue
        src = re.search(r"\*\*S(\d+)\*\*|→\s*\*\*S(\d+)\*\*|Source:.*?(S\d+)", line)
        if line.startswith("- Source:") or line.startswith("- Image:") or line.startswith("- Page:") or line.startswith("- Reel:") or line.startswith("- Provenance:"):
            current["lines"].append(strip_md(line[2:]))
            if "Source:" in line:
                current["source"] = strip_md(line.split(":", 1)[-1])
            if "Image:" in line or "image:" in line:
                current["image"] = strip_md(line.split(":", 1)[-1])
            sm = re.search(r"`([0-9a-f]{64})`", line)
            if sm:
                current["sha"] = sm.group(1)
        for cm in re.findall(r"C\d+", line):
            if cm not in current["claims"]:
                current["claims"].append(cm)
        for sm in ID_RE.findall(line):
            sid = f"S{int(sm):03d}"
            if sid not in current["source"]:
                if current["source"]:
                    if sid not in current["source"]:
                        current["source"] = (current["source"] + " " + sid).strip()
                else:
                    current["source"] = sid
    if current:
        out.append(current)
    # stable order by first appearance, then id
    return out


def parse_inventory_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    if INVENTORY.is_file():
        current = None
        for line in INVENTORY.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("/workspace/"):
                path = line.split("  (")[0].strip()
                try:
                    rel = str(Path(path).relative_to(SOURCES))
                except ValueError:
                    rel = path
                current = rel
            elif current and "sha256:" in line:
                h = line.split("sha256:", 1)[1].strip().split()[0]
                hashes[current] = h
                current = None
    if TSV.is_file():
        for i, line in enumerate(TSV.read_text(encoding="utf-8").splitlines()):
            if i == 0 or not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) >= 3:
                hashes.setdefault(parts[0], parts[2])
    return hashes


def list_local_files(hashes: dict[str, str]) -> list[dict]:
    files = []
    for p in sorted(SOURCES.rglob("*")):
        if not p.is_file():
            continue
        if p.name.lower() in SKIP_FILE_NAMES:
            continue
        rel = str(p.relative_to(SOURCES))
        kind = p.suffix.lower().lstrip(".") or "file"
        folder = rel.split("/", 1)[0] if "/" in rel else "(root)"
        files.append(
            {
                "rel": rel,
                "folder": folder,
                "bytes": p.stat().st_size,
                "kind": kind,
                "sha": hashes.get(rel, ""),
            }
        )
    return files


def list_case_papers() -> list[dict]:
    papers = []
    names = [
        "00-intake.md",
        "01-plan.md",
        "02-log.md",
        "03-timeline.md",
        "04-evidence.md",
        "05-dna.md",
        "06-dossier.md",
        "07-conflicts.md",
        "08-transcriptions.md",
        "09-statistics.md",
        "10-visuals.md",
        "11-backlog.md",
        "12-image-gallery.md",
        "13-chat-review.md",
        "SOURCE-INDEX.md",
        "family.json",
        "book/Dora-Ella-Newnam-Stone-A-Life.md",
        "book/Dora-Ella-Newnam-Stone-A-Life.docx",
        "book/Dora-Ella-Newnam-Stone-A-Life.pdf",
        "book/README.md",
        "sources/authored/PROVENANCE.md",
        "sources/INVENTORY.txt",
        "sources/SOURCE-INVENTORY.tsv",
    ]
    for name in names:
        p = CASE / name
        papers.append(
            {
                "name": name,
                "exists": p.is_file(),
                "bytes": p.stat().st_size if p.is_file() else 0,
            }
        )
    return papers


def set_run_font(run, name: str = "Times New Roman", size: int | None = None, bold=None, italic=None, color=None):
    run.font.name = name
    r = run._element
    rPr = r.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    rFonts.set(qn("w:ascii"), name)
    rFonts.set(qn("w:hAnsi"), name)
    rFonts.set(qn("w:cs"), name)
    rFonts.set(qn("w:eastAsia"), name)
    if size is not None:
        run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    if color is not None:
        run.font.color.rgb = color


def shade_cell(cell, hex_color: str) -> None:
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")
    tcPr.append(shd)


def set_cell_border(cell) -> None:
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "D6D3D1")
        tcBorders.append(el)
    tcPr.append(tcBorders)


def set_cell_text(cell, text: str, *, bold=False, size=9, color=INK, align=None) -> None:
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.line_spacing = 1.05
    if align:
        p.alignment = align
    run = p.add_run(text)
    set_run_font(run, size=size, bold=bold, color=color)
    set_cell_border(cell)


def prevent_row_split(row) -> None:
    tr = row._tr
    trPr = tr.get_or_add_trPr()
    cant = OxmlElement("w:cantSplit")
    trPr.append(cant)


def set_col_widths(table, widths_in: list[float]) -> None:
    table.autofit = False
    table.allow_autofit = False
    for row in table.rows:
        for i, w in enumerate(widths_in):
            row.cells[i].width = Inches(w)


def add_page_number_footer(section) -> None:
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Dora Ella Newnam Stone — Source & document index  ·  ")
    set_run_font(run, size=9, color=MUTED, italic=True)
    # PAGE field
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    fld_sep = OxmlElement("w:fldChar")
    fld_sep.set(qn("w:fldCharType"), "separate")
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    r1 = p.add_run()
    set_run_font(r1, size=9, color=MUTED)
    r1._r.append(fld_begin)
    r1._r.append(instr)
    r1._r.append(fld_sep)
    r2 = p.add_run("1")
    set_run_font(r2, size=9, color=MUTED)
    r2._r.append(fld_end)
    run3 = p.add_run("  ·  compiled ")
    set_run_font(run3, size=9, color=MUTED, italic=True)
    run4 = p.add_run(now())
    set_run_font(run4, size=9, color=MUTED, italic=True)


def enable_update_fields(doc: Document) -> None:
    settings = doc.settings.element
    update = settings.find(qn("w:updateFields"))
    if update is None:
        update = OxmlElement("w:updateFields")
        settings.append(update)
    update.set(qn("w:val"), "true")


def add_toc_field(doc: Document) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run()
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = r' TOC \o "1-2" \h \z \u '
    fld_sep = OxmlElement("w:fldChar")
    fld_sep.set(qn("w:fldCharType"), "separate")
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    r = run._r
    r.append(fld_begin)
    r.append(instr)
    r.append(fld_sep)
    placeholder = p.add_run(
        "Microsoft Word will fill this table of contents when the file is opened "
        "(enable “Update fields” if asked). A reader’s outline with every section "
        "title follows immediately below, so the document is usable without Word."
    )
    set_run_font(placeholder, size=10, italic=True, color=MUTED)
    end_run = p.add_run()
    end_run._r.append(fld_end)


def add_rich(p, text: str, *, size=11, color=INK) -> None:
    """Render **bold** segments into an existing paragraph."""
    parts = re.split(r"(\*\*[^*]+\*\*)", text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = p.add_run(part[2:-2])
            set_run_font(run, size=size, bold=True, color=color)
        else:
            run = p.add_run(part)
            set_run_font(run, size=size, color=color)


def body(doc: Document, text: str, *, size=11, space_after=8, first_line=None) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    if first_line is not None:
        p.paragraph_format.first_line_indent = Inches(first_line)
    add_rich(p, text, size=size)


def hanging_cite(doc: Document, label: str, citation: str, meta: str) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.35)
    p.paragraph_format.first_line_indent = Inches(-0.35)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.line_spacing = 1.12
    run = p.add_run(label + "  ")
    set_run_font(run, size=10.5, bold=True, color=ACCENT)
    run2 = p.add_run(citation)
    set_run_font(run2, size=10.5, color=INK)
    if meta:
        run3 = p.add_run("  " + meta)
        set_run_font(run3, size=9.5, italic=True, color=MUTED)


def style_heading(style, size: int, color=ACCENT, space_before=16, space_after=6, bold=True):
    style.font.name = "Times New Roman"
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.color.rgb = color
    style.paragraph_format.space_before = Pt(space_before)
    style.paragraph_format.space_after = Pt(space_after)
    style.paragraph_format.keep_with_next = True
    rPr = style.element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rFonts.set(qn(attr), "Times New Roman")


def add_table(doc: Document, headers: list[str], rows: list[list[str]], widths: list[float], header=True) -> None:
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        set_cell_text(table.rows[0].cells[i], h, bold=True, size=8.5, color=ACCENT)
        shade_cell(table.rows[0].cells[i], HEADER_BG)
    for r_i, row in enumerate(rows):
        for c_i, val in enumerate(row):
            set_cell_text(table.rows[r_i + 1].cells[c_i], val, size=8)
            if r_i % 2 == 1:
                shade_cell(table.rows[r_i + 1].cells[c_i], ALT_BG)
        prevent_row_split(table.rows[r_i + 1])
    prevent_row_split(table.rows[0])
    set_col_widths(table, widths)
    doc.add_paragraph()


def fmt_bytes(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f} MB"
    if n >= 1_000:
        return f"{n / 1_000:.1f} KB"
    return f"{n} B"


def repository_from_url(url: str) -> str:
    host = re.sub(r"^https?://(www\.)?", "", url).split("/")[0].lower()
    mapping = {
        "archive.org": "Internet Archive (NARA microfilm scans)",
        "usgennet.org": "USGenNet / ALHN (Lee & Owsley transcriptions)",
        "sites.rootsweb.com": "RootsWeb / USGenNet mirrors",
        "www.wikitree.com": "WikiTree",
        "wikitree.com": "WikiTree",
        "www.argenweb.net": "ARGenWeb (Perry County)",
        "argenweb.net": "ARGenWeb",
        "sortedbyname.com": "SortedByName (NUMIDENT / DMF extracts)",
        "www.yellcountyobits.org": "Yell County Obits",
        "yellcountyobits.org": "Yell County Obits",
        "genealogytrails.com": "Genealogy Trails",
        "www.loc.gov": "Library of Congress / Chronicling America",
        "chroniclingamerica.loc.gov": "Library of Congress / Chronicling America",
        "kdla.ky.gov": "Kentucky Department for Libraries and Archives",
        "kygenweb.net": "KYGenWeb",
        "www.slavens.net": "Slavens.net (Soundex method key)",
        "ukmfilms.omeka.net": "University of Kentucky Microfilm Holdings",
        "www.findagrave.com": "Find a Grave",
        "findagrave.com": "Find a Grave",
        "familysearch.org": "FamilySearch",
        "www.familysearch.org": "FamilySearch",
        "www.ancestry.com": "Ancestry (index cited; images not re-opened)",
        "ancestry.com": "Ancestry",
    }
    return mapping.get(host, host)


def build() -> dict:
    sources = parse_sources()
    claims = parse_claims()
    docs = parse_docs()
    hashes = parse_inventory_hashes()
    files = list_local_files(hashes)
    papers = list_case_papers()

    by_cat = defaultdict(list)
    for s in sources:
        by_cat[s["category"]].append(s)

    urls: dict[str, list[str]] = defaultdict(list)
    for s in sources:
        for u in s["urls"]:
            urls[repository_from_url(u)].append(f"{s['id']}: {u}")

    expected = set(range(1, max(s["n"] for s in sources) + 1)) if sources else set()
    present = {s["n"] for s in sources}
    missing_ids = [f"S{n:03d}" for n in sorted(expected - present)]

    doc = Document()
    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.left_margin = Inches(0.9)
    section.right_margin = Inches(0.9)
    section.top_margin = Inches(0.85)
    section.bottom_margin = Inches(0.85)
    add_page_number_footer(section)
    enable_update_fields(doc)

    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(11)
    normal.font.color.rgb = INK
    style_heading(doc.styles["Heading 1"], 16, ACCENT, 18, 8)
    style_heading(doc.styles["Heading 2"], 13, ACCENT, 14, 6)
    style_heading(doc.styles["Heading 3"], 11.5, RGBColor(0x44, 0x40, 0x3C), 10, 4)

    # ----- Title page -----
    for _ in range(3):
        doc.add_paragraph()
    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run("DORA ELLA NEWNAM STONE")
    set_run_font(r, size=26, bold=True, color=ACCENT)
    t2 = doc.add_paragraph()
    t2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t2.add_run("Source and Document Index")
    set_run_font(r, size=20, italic=True, color=INK)
    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = sub.add_run(
        "Every cited source, diplomatic transcription, local image, and working paper\n"
        "used in the genealogical investigation of Dora Ella (Newnam) Stone\n"
        "(1871, Kentucky — 23 August 1926, Ola, Yell County, Arkansas)"
    )
    set_run_font(r, size=12, color=MUTED)
    meta = doc.add_paragraph()
    meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = meta.add_run(
        f"Compiled {now()} (America/New_York)\n"
        f"Case folder  research/dora-ella-newnam/\n"
        f"{len(sources)} source citations  ·  {len(docs)} transcriptions  ·  "
        f"{len(files)} local files  ·  {len(claims)} claims  ·  {len(PLATES)} plates"
    )
    set_run_font(r, size=11, color=INK)
    note = doc.add_paragraph()
    note.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = note.add_run(
        "Citations follow the case register (Evidence Explained elements: creator, title, "
        "type/dates, repository, volume/page/certificate, URL and access date, "
        "and whether the image, an index, or a transcription was read). "
        "Living persons are not named."
    )
    set_run_font(r, size=10, italic=True, color=MUTED)

    doc.add_page_break()

    # ----- TOC -----
    doc.add_heading("Table of contents", level=1)
    body(
        doc,
        "This file uses Word heading styles (Heading 1 and Heading 2) so the "
        "automatic table of contents below can be refreshed in Microsoft Word: "
        "right-click the field and choose Update Field. The reader’s outline "
        "under it lists every chapter and is complete without Word.",
        size=11,
    )
    add_toc_field(doc)

    doc.add_heading("Reader’s outline", level=2)
    outline = [
        ("1.", "How this index was compiled"),
        ("2.", "Summary of holdings"),
        ("3.", "Case-folder working papers"),
        ("4.", "Index of documents by class"),
        ("    4.1", "Census population schedules"),
        ("    4.2", "Soundex / Miracode"),
        ("    4.3", "Vital records (birth, marriage, death)"),
        ("    4.4", "Cemetery / memorial"),
        ("    4.5", "Newspapers / obituaries"),
        ("    4.6", "Probate / land / court"),
        ("    4.7", "Military"),
        ("    4.8", "Social Security / NUMIDENT"),
        ("    4.9", "Authored / compiled / catalog"),
        ("    4.10", "Other / method"),
        ("5.", "Complete source citations (every S-number)"),
        ("6.", "Transcription register (every DOC-number)"),
        ("7.", "Plate catalog"),
        ("8.", "Local file inventory (every file in sources/)"),
        ("9.", "Claim-to-source index (every C-number)"),
        ("10.", "Repositories and URLs"),
        ("11.", "Gaps, paywalled items, and unused classes"),
    ]
    for num, title in outline:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.space_before = Pt(0)
        run = p.add_run(f"{num}  {title}")
        set_run_font(run, size=11, color=INK)

    # ----- 1 How compiled -----
    doc.add_heading("1. How this index was compiled", level=1)
    body(
        doc,
        "This Word document is a finding aid for the Dora Ella Newnam Stone case. "
        "It was generated from the live case folder on the compile date on the title page, "
        "not from memory. The generator reads:",
    )
    for item in [
        "**04-evidence.md** — master evidence register: every S-number citation, source class, informant, and every C-number claim with supporting source IDs.",
        "**08-transcriptions.md** — diplomatic transcriptions DOC001–DOC233 (and any later DOC headings in that file).",
        "**scripts/dora_plates.py** — chronological plate catalog of preserved JPEGs.",
        "**sources/INVENTORY.txt** and **sources/SOURCE-INVENTORY.tsv** — SHA-256 hashes of retained images.",
        "A walk of **sources/** — every file actually present on disk when the index was built.",
        "The numbered case papers **00-intake.md** through **13-chat-review.md**, plus the biography book files.",
    ]:
        p = doc.add_paragraph(style="List Bullet")
        add_rich(p, item, size=11)
    body(
        doc,
        "A “document used” here means a record the investigation opened, transcribed, "
        "hashed, rejected, or cited as a negative search — not only the handful of "
        "records that prove Dora’s identity. Negative Soundex windows and rejected "
        "same-name people are listed because they are part of the proof.",
    )
    body(
        doc,
        "Citation form follows the case register. Elements, when known, are: creator; "
        "title; record type and dates; repository (NARA microfilm publication and reel, "
        "Internet Archive item, USGenNet page, county book); volume, enumeration district, "
        "sheet, line, dwelling, or certificate number; URL and access date; and whether "
        "the **image**, an **index**, or a **transcription** was read. SHA-256 prefixes "
        "are given when the case folder holds a local copy.",
    )

    # ----- 2 Summary -----
    doc.add_heading("2. Summary of holdings", level=1)
    by_access = Counter(s["access"] for s in sources)
    by_class = Counter(s["source_class"] for s in sources)
    file_bytes = sum(f["bytes"] for f in files)
    hashed = sum(1 for f in files if f["sha"])
    add_table(
        doc,
        ["Holding", "Count"],
        [
            ["Source citations in 04-evidence.md (unique S-numbers after expanding ranges)", str(len(sources))],
            ["Highest S-number", f"S{max(s['n'] for s in sources):03d}"],
            ["S-numbers unused in the 001–max series (not a defect; IDs were assigned as work arrived)", str(len(missing_ids))],
            ["Diplomatic transcriptions (DOC headings in 08-transcriptions.md)", str(len(docs))],
            ["Claims in the evidence register", str(len(claims))],
            ["Catalogued plates in scripts/dora_plates.py", str(len(PLATES))],
            ["Local files under sources/ (this compile)", str(len(files))],
            ["Those files with a recorded SHA-256", str(hashed)],
            ["Bytes of local source files", fmt_bytes(file_bytes)],
            ["Distinct repositories (from URLs in citations)", str(len(urls))],
        ],
        [5.6, 1.1],
    )
    add_table(
        doc,
        ["How the source was read", "Sources"],
        [[k, str(by_access[k])] for k in sorted(by_access)],
        [5.6, 1.1],
    )
    add_table(
        doc,
        ["GPS source class (as recorded)", "Sources"],
        [[k, str(by_class[k])] for k in sorted(by_class)],
        [5.6, 1.1],
    )
    add_table(
        doc,
        ["Document class (this index)", "Sources"],
        [[k, str(len(by_cat[k]))] for k in sorted(by_cat)],
        [5.6, 1.1],
    )

    # ----- 3 Working papers -----
    doc.add_heading("3. Case-folder working papers", level=1)
    body(
        doc,
        "These are the investigation’s own documents — research log, evidence register, "
        "diplomatic transcriptions, backlog, and the narrative book. They are not original "
        "historical records. Each is listed so a reviewer can see the complete paper trail.",
    )
    paper_rows = []
    for p in papers:
        paper_rows.append(
            [
                p["name"],
                "present" if p["exists"] else "missing",
                fmt_bytes(p["bytes"]) if p["exists"] else "—",
            ]
        )
    add_table(doc, ["Case paper", "Status", "Size"], paper_rows, [4.6, 1.1, 1.0])

    # ----- 4 Class index -----
    doc.add_heading("4. Index of documents by class", level=1)
    body(
        doc,
        "Finding aid only. Full Evidence Explained citations are in chapter 5, in "
        "S-number order. Classes are assigned from the citation text (Soundex vs "
        "population schedule vs vital record, and so on).",
    )

    class_order = [
        "Census population schedules",
        "Soundex / Miracode",
        "Vital records (birth)",
        "Vital records (marriage)",
        "Vital records (death)",
        "Cemetery / memorial",
        "Newspapers / obituaries",
        "Probate / land / court",
        "Military",
        "Social Security / NUMIDENT",
        "Authored / compiled",
        "Catalog / finding aid",
        "Other / method",
    ]
    # One Heading 2 per outline number; vital-record subclasses use Heading 3.
    emitted_h2 = set()
    h2_for = {
        "Census population schedules": "4.1 Census population schedules",
        "Soundex / Miracode": "4.2 Soundex and Miracode",
        "Vital records (birth)": "4.3 Vital records",
        "Vital records (marriage)": "4.3 Vital records",
        "Vital records (death)": "4.3 Vital records",
        "Cemetery / memorial": "4.4 Cemetery and memorial readings",
        "Newspapers / obituaries": "4.5 Newspapers and obituaries",
        "Probate / land / court": "4.6 Probate, land, and court",
        "Military": "4.7 Military",
        "Social Security / NUMIDENT": "4.8 Social Security and NUMIDENT",
        "Authored / compiled": "4.9 Authored, compiled, and catalog sources",
        "Catalog / finding aid": "4.9 Authored, compiled, and catalog sources",
        "Other / method": "4.10 Other and method notes",
    }
    for cat in class_order:
        items = by_cat.get(cat, [])
        h2 = h2_for[cat]
        if h2 not in emitted_h2:
            doc.add_heading(h2, level=2)
            emitted_h2.add(h2)
        if not items:
            continue
        if cat.startswith("Vital") or cat in {"Authored / compiled", "Catalog / finding aid"}:
            doc.add_heading(cat, level=3)
        rows = [[s["id"], s["access"], s["source_class"], s["title"]] for s in items]
        add_table(doc, ["ID", "Access", "Class", "Short title"], rows, [0.7, 1.4, 1.3, 3.3])

    # ----- 5 Full citations -----
    doc.add_heading("5. Complete source citations", level=1)
    body(
        doc,
        f"Every unique S-number in **04-evidence.md**, {len(sources)} citations, "
        f"S001 through S{max(s['n'] for s in sources):03d}. "
        "Range rows in the register (for example S102–S105) are expanded so each "
        "number has its own entry. Duplicate later rows for the same S-number were "
        "not repeated. Unused numbers in the series are listed at the end of this chapter.",
    )
    body(
        doc,
        "Each entry is: **S-number**, then the full citation (creator; title; type/dates; "
        "repository; volume/page/certificate; URL and access; image/index/transcription "
        "note; SHA-256 when recorded), then source class and informant in italics.",
    )

    # chunk H2 every 50 for TOC navigation (use the first present ID in each bucket)
    last_bucket = None
    max_n = max(x["n"] for x in sources)
    for s in sources:
        bucket = ((s["n"] - 1) // 50) * 50 + 1
        if bucket != last_bucket:
            end = min(bucket + 49, max_n)
            doc.add_heading(f"S{bucket:03d}–S{end:03d}", level=2)
            last_bucket = bucket
        meta = f"[{s['source_class']}; {s['access']}; {s['category']}]"
        if s["informant"]:
            meta += f"  Informant / basis: {s['informant']}."
        if s["files"]:
            meta += "  Local file: " + "; ".join(s["files"][:4])
            if len(s["files"]) > 4:
                meta += f" (+{len(s['files']) - 4} more)"
            meta += "."
        hanging_cite(doc, s["id"], s["citation"], meta)

    if missing_ids:
        doc.add_heading("S-numbers not assigned", level=2)
        body(
            doc,
            "The following numbers in the S001–S"
            + f"{max(s['n'] for s in sources):03d}"
            + " series do not appear as rows in the evidence register. "
            "They were never assigned, or they were reserved and then skipped. "
            "This is not a list of missing historical records.",
        )
        body(doc, ", ".join(missing_ids), size=10)

    # ----- 6 Transcriptions -----
    doc.add_heading("6. Transcription register", level=1)
    body(
        doc,
        f"**08-transcriptions.md** contains {len(docs)} DOC headings. "
        "Early in the file a few DOC numbers were reused (for example DOC002 and DOC003 "
        "appear more than once). Reused numbers are marked “(2)” in the title. "
        "Each row cites the linked S-number when the transcription names one.",
    )
    doc_rows = []
    for d in docs:
        img = d["image"] or d["sha"]
        if len(img) > 70:
            img = img[:69] + "…"
        claims_s = " ".join(d["claims"][:8])
        if len(d["claims"]) > 8:
            claims_s += "…"
        doc_rows.append([d["id"], d["title"][:80], d["source"][:40], claims_s])
    # split into chunks of 40 so Word stays responsive
    for i in range(0, len(doc_rows), 40):
        chunk = doc_rows[i : i + 40]
        first_id = docs[i]["id"]
        last_id = docs[min(i + 39, len(docs) - 1)]["id"]
        doc.add_heading(f"{first_id}–{last_id}", level=2)
        add_table(doc, ["DOC", "Title", "Source", "Claims"], chunk, [0.8, 3.2, 1.5, 1.2])

    doc.add_heading("Transcription citations (diplomatic source lines)", level=2)
    body(
        doc,
        "The lines below repeat the Source / Image / Page / Reel / Provenance bullets "
        "from each DOC entry so a reviewer does not have to open the markdown file.",
    )
    for d in docs:
        bits = [x for x in d["lines"] if x]
        cite = "  ".join(bits) if bits else d["source"] or "(no source line on the heading block)"
        hanging_cite(doc, d["id"], f"{d['title']}. {cite}", "")

    # ----- 7 Plates -----
    doc.add_heading("7. Plate catalog", level=1)
    body(
        doc,
        f"{len(PLATES)} plates are catalogued in **scripts/dora_plates.py**. "
        "Plate numbers follow the date of the record, not the date the scan was made. "
        "Roles: family (Dora or a documented relative), rejected (same-name failure), "
        "negative (the slot where she would appear), context (adjacent page or divider).",
    )
    plate_rows = []
    for p in PLATES:
        plate_rows.append(
            [
                str(p.get("n", "")),
                str(p.get("date", "")),
                str(p.get("role", "")),
                str(p.get("source", "")),
                str(p.get("title", ""))[:70],
            ]
        )
    for i in range(0, len(plate_rows), 50):
        chunk = plate_rows[i : i + 50]
        a = PLATES[i].get("n", i + 1)
        b = PLATES[min(i + 49, len(PLATES) - 1)].get("n", i + 50)
        doc.add_heading(f"Plates {a}–{b}", level=2)
        add_table(doc, ["#", "Date", "Role", "Cite", "Title"], chunk, [0.45, 1.2, 0.9, 1.4, 2.75])

    # ----- 8 File inventory -----
    doc.add_heading("8. Local file inventory", level=1)
    body(
        doc,
        f"Every file under **research/dora-ella-newnam/sources/** at compile time "
        f"({len(files)} files, {fmt_bytes(file_bytes)}). "
        "SHA-256 is the full hash from INVENTORY.txt when present, otherwise the "
        "16-character prefix from SOURCE-INVENTORY.tsv. Files added after those "
        "inventories were last rebuilt may show a blank hash.",
    )
    folder_counts = Counter(f["folder"] for f in files)
    add_table(
        doc,
        ["Folder", "Files", "Bytes"],
        [
            [k, str(folder_counts[k]), fmt_bytes(sum(f["bytes"] for f in files if f["folder"] == k))]
            for k in sorted(folder_counts)
        ],
        [3.4, 1.2, 2.1],
    )

    files_by_folder = defaultdict(list)
    for f in files:
        files_by_folder[f["folder"]].append(f)
    for folder in sorted(files_by_folder):
        group = files_by_folder[folder]
        doc.add_heading(f"sources/{folder}/  ({len(group)} files)", level=2)
        rows = []
        for f in group:
            sha = f["sha"]
            if len(sha) > 16:
                sha = sha[:16]
            rows.append([f["rel"].split("/", 1)[-1][:70], f["kind"], fmt_bytes(f["bytes"]), sha])
        for i in range(0, len(rows), 45):
            add_table(
                doc,
                ["File", "Type", "Size", "SHA-256"],
                rows[i : i + 45],
                [4.0, 0.7, 0.8, 1.2],
            )

    # ----- 9 Claims -----
    doc.add_heading("9. Claim-to-source index", level=1)
    body(
        doc,
        f"{len(claims)} claims from **04-evidence.md**. Each row is one fact, the "
        "GPS confidence label, and the S-numbers that support or contradict it. "
        "Use this chapter to go from a conclusion back to the citations in chapter 5.",
    )
    claim_rows = []
    for c in claims:
        src = " ".join(c["sources"]) if c["sources"] else c["source_field"][:40]
        claim_rows.append(
            [
                c["id"],
                c["confidence"][:36],
                src[:42],
                c["claim"][:90] + ("…" if len(c["claim"]) > 90 else ""),
            ]
        )
    for i in range(0, len(claim_rows), 40):
        a = claims[i]["id"]
        b = claims[min(i + 39, len(claims) - 1)]["id"]
        doc.add_heading(f"{a}–{b}", level=2)
        add_table(doc, ["Claim", "Confidence", "Sources", "Fact"], claim_rows[i : i + 40], [0.7, 1.5, 1.6, 2.9])

    # ----- 10 Repositories -----
    doc.add_heading("10. Repositories and URLs", level=1)
    body(
        doc,
        "Every http(s) URL captured in a source citation, grouped by repository. "
        "Access dates stay on the individual citations in chapter 5. "
        "Internet Archive items are NARA microfilm scans (population schedules and Soundex/Miracode).",
    )
    for repo in sorted(urls):
        doc.add_heading(repo, level=2)
        for line in urls[repo]:
            p = doc.add_paragraph(style="List Bullet")
            run = p.add_run(line)
            set_run_font(run, size=9.5, color=INK)

    nara = [
        ("T9 / 1880 population", "Lee County, Kentucky, ED 59 (S010, S040, S044)"),
        ("M593 / 1870 population", "Lee Co. Sturgeon (S042); Owsley Travellers Rest (S048 / DOC003)"),
        ("T623 / 1900 population", "Lee, Douglas, Dunklin, Greene, Bollinger and related Missouri EDs"),
        ("T624 / 1910 population", "Lee Sturgeon ED 99; Owsley Buck Creek; Bollinger Liberty"),
        ("T625 / 1920 population", "Lee Beattyville ED 111 (S073); Arkansas Perry / Yell (S102–S105)"),
        ("T750 / 1880 Soundex", "Kentucky N-550 (S001, S002)"),
        ("T1055 / 1900 Soundex", "Missouri S-350 Thomas window (S070); S-415 leftover walks (S406–S415)"),
        ("T1266 / 1910 KY Miracode", "N-550 and P-142 (S020, S021, S026, S027, S062)"),
        ("T1270 / 1910 AR & MO Miracode", "N-550 and P-142 (S022, S023, S063)"),
        ("T1272 / 1910 TN Soundex", "N-550 (S025, S028)"),
        ("T1273 / 1910 OK Miracode", "N-550 (S049)"),
        ("T1275 / 1910 KY Soundex PDF", "Newman children scan (S058)"),
        ("T1277 / 1910 TX Soundex", "N-550 (S050)"),
        ("M1560 / M1563 / 1920 KY Soundex", "N-550 and S-350 (S045, S046, S052)"),
        ("M1571 / 1920 MO Soundex", "N-500–N-650 (S056)"),
        ("M1582 / 1920 OK Soundex", "N-400–N-630 (S053)"),
        ("M1588 / 1920 TN Soundex", "N-450–O-165 (S055)"),
    ]
    doc.add_heading("NARA microfilm publications used", level=2)
    add_table(
        doc,
        ["Publication", "Use in this case"],
        [list(row) for row in nara],
        [2.4, 4.3],
    )

    # ----- 11 Gaps -----
    doc.add_heading("11. Gaps, paywalled items, and unused classes", level=1)
    body(
        doc,
        "The following items were identified as relevant and **not** fully opened as images "
        "in this investigation. They are listed so the index is honest about what was used "
        "and what remains on-site or behind a login. Details live in SOURCE-INDEX.md and 11-backlog.md.",
    )
    gaps = [
        ["Arkansas death certificate image (Dora Stone / indexed Posa Stone), Yell Co., 23 Aug 1926, cert. 1524, RD 676", "User-supplied image cited as S003; Ancestry collection 8771 / FamilySearch 1940760 not re-opened"],
        ["Lee County Marriage Book 2 original (FS Q2QD-PZHL)", "S004 is the Kendrick transcription only"],
        ["Thomas / T. A. Stone 1925 Arkansas death certificate", "Cemetery readings used (S078, S282); DC still required"],
        ["Newspapers.com Beattyville Enterprise, especially 1926", "IA beatty holds six issues only; 1926 not among them (S283, S284)"],
        ["Yell County Journal (Ola) 1925–1934", "Not digitised free; AR State Archives / local library"],
        ["NARA M1509 WWI draft cards, rolls KY45, KY24, KY74, AR69", "Genealogy Trails transcript used (S285); card images unread"],
        ["KDLA / KHS Lee County probate 1873–2004", "Samuel P. Newnam administration still a backlog item"],
        ["University of Kentucky film S 90-033 / KUK 18568", "Catalog only (S284)"],
        ["DNA matches and living testers", "05-dna.md; living persons are not named in this index"],
    ]
    add_table(doc, ["Document not fully used", "What stands in its place"], gaps, [3.3, 3.4])

    body(
        doc,
        "Rebuild this file from the repository root after the evidence register changes:",
    )
    p = doc.add_paragraph()
    run = p.add_run("python3 scripts/build_dora_source_index_docx.py")
    set_run_font(run, size=10.5, color=INK)
    p.paragraph_format.left_indent = Inches(0.35)

    end = doc.add_paragraph()
    end.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = end.add_run("— end of source and document index —")
    set_run_font(r, size=10, italic=True, color=MUTED)

    BOOK_DIR.mkdir(parents=True, exist_ok=True)
    doc.save(OUT)
    stats = {
        "path": str(OUT),
        "bytes": OUT.stat().st_size,
        "sources": len(sources),
        "docs": len(docs),
        "claims": len(claims),
        "files": len(files),
        "plates": len(PLATES),
        "missing_s": len(missing_ids),
        "repos": len(urls),
    }
    return stats


if __name__ == "__main__":
    stats = build()
    print("wrote", stats["path"])
    for k, v in stats.items():
        if k != "path":
            print(f"  {k}: {v}")
