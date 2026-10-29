#!/usr/bin/env python3
"""Generate search variant lists for proactive index/archive/code search.

Usage:
  search_variants.py person GIVEN SURNAME [--also ALT ...]
  search_variants.py ocr-given NAME
  search_variants.py ocr-surname NAME
  search_variants.py cert NUMBER [--rd RD]
  search_variants.py soundex SURNAME   # delegates hint to kinship if present
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

OCR_GIVEN = {
    "dora": ["posa", "dosa", "rosa", "dona", "dara", "dore", "dori", "dola"],
    "mary": ["mayr", "mam", "marv"],
    "ella": ["alla", "elia"],
    "louisa": ["eliza", "luisa", "loisa", "louiza"],
    "eliza": ["louisa", "louiza", "elisa"],
    "coy": ["mccoy", "m coy", "mc coy", "mccay"],
    "thomas": ["thos", "tom", "t a", "t. a."],
}

OCR_SURNAME_SUBS = [
    ("newnam", ["newman", "newnarn", "newan", "newnom"]),
    ("newman", ["newnam", "newnarn", "newan"]),
    ("smallwood", ["smalwood", "smallood"]),
    ("stone", ["storie", "stona", "stome"]),
    ("brandenburg", ["brandenburgh", "brandenburi", "branenburg"]),
    ("pendergrass", ["pendergass", "pendergras", "pendergraas"]),
]

SUFFIX_SWAPS = [("son", "sen"), ("burg", "burgh"), ("burgh", "brough")]


def _unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for x in items:
        k = x.lower().strip()
        if not k or k in seen:
            continue
        seen.add(k)
        out.append(x.strip())
    return out


def ocr_given(name: str) -> list[str]:
    key = name.lower().strip()
    base = [name, name.title(), name.upper()]
    extra = list(OCR_GIVEN.get(key, []))
    # First-letter OCR bucket D/P/R
    if key and key[0] in "d":
        for alt in "pr":
            extra.append(alt + key[1:])
    return _unique(base + extra)


def ocr_surname(name: str) -> list[str]:
    key = name.lower().strip()
    out = [name, name.title(), name.upper()]
    for stem, alts in OCR_SURNAME_SUBS:
        if stem in key or key in stem:
            out.extend(alts)
    low = key
    for a, b in SUFFIX_SWAPS:
        if low.endswith(a):
            out.append(low[: -len(a)] + b)
        if low.endswith(b):
            out.append(low[: -len(b)] + a)
    if "mc" in low and not low.startswith("mc"):
        out.append(re.sub(r"\bmc", "mc", low, flags=re.I))
    if low.startswith("mc"):
        out.append("mac" + low[2:])
    return _unique(out)


def person_variants(given: str, surname: str, also: list[str]) -> None:
    g_vars = ocr_given(given)
    s_vars = ocr_surname(surname)
    s_vars = _unique(s_vars + also)
    print(f"# Person: {given} {surname}")
    print("## Given-name queries")
    for g in g_vars:
        print(f"  - {g}")
    print("## Surname queries")
    for s in s_vars:
        print(f"  - {s}")
    print("## Combined (sample — expand in plan)")
    for s in s_vars[:6]:
        for g in g_vars[:6]:
            print(f"  - \"{g} {s}\" | \"{s}, {g}\" | {s} + filter {g}*")
    kinship = Path(__file__).resolve().parents[2] / "genealogy-detective" / "scripts" / "kinship.py"
    if kinship.is_file():
        print("## Soundex")
        subprocess.run([sys.executable, str(kinship), "soundex", surname], check=False)

def cert_variants(number: str, rd: str | None) -> None:
    print(f"# Certificate {number}" + (f" RD {rd}" if rd else ""))
    print("## Queries without relying on name spelling")
    print(f"  - cert {number}")
    print(f"  - certificate {number}")
    if rd:
        print(f"  - RD {rd} / district {rd} + date + county")
    print("  - volume + cert fields from index help screens")
    print("  - date-only + county + surname wildcards")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    pp = sub.add_parser("person", help="Given + surname variant table")
    pp.add_argument("given")
    pp.add_argument("surname")
    pp.add_argument("--also", action="append", default=[])

    og = sub.add_parser("ocr-given")
    og.add_argument("name")

    os_ = sub.add_parser("ocr-surname")
    os_.add_argument("name")

    pc = sub.add_parser("cert")
    pc.add_argument("number")
    pc.add_argument("--rd", default=None)

    ps = sub.add_parser("soundex")
    ps.add_argument("surname")

    args = p.parse_args()
    if args.cmd == "person":
        person_variants(args.given, args.surname, args.also)
    elif args.cmd == "ocr-given":
        for v in ocr_given(args.name):
            print(v)
    elif args.cmd == "ocr-surname":
        for v in ocr_surname(args.name):
            print(v)
    elif args.cmd == "cert":
        cert_variants(args.number, args.rd)
    elif args.cmd == "soundex":
        kinship = Path(__file__).resolve().parents[2] / "genealogy-detective" / "scripts" / "kinship.py"
        if not kinship.is_file():
            print("kinship.py not found", file=sys.stderr)
            return 1
        return subprocess.call([sys.executable, str(kinship), "soundex", args.surname])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
