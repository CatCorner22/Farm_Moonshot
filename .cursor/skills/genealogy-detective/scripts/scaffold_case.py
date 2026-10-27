#!/usr/bin/env python3
"""Scaffold a genealogy case folder from this skill's templates. Stdlib only."""
import argparse, re, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
FILES = ["00-intake.md","01-plan.md","02-log.md","03-timeline.md","04-evidence.md","05-dna.md","06-dossier.md","07-conflicts.md","08-transcriptions.md","09-statistics.md","10-visuals.md"]

def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "unknown-person"

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("name"); ap.add_argument("--birth", default=""); ap.add_argument("--death", default="")
    ap.add_argument("--place", default=""); ap.add_argument("--out", default="research")
    ap.add_argument("--force", action="store_true", help="overwrite existing template files")
    a = ap.parse_args()
    root = Path(a.out) / slug(a.name)
    (root / "sources" / "dna").mkdir(parents=True, exist_ok=True)
    (root / "visuals").mkdir(parents=True, exist_ok=True)
    repl = {"{{NAME}}": a.name, "{{BIRTH}}": a.birth or "?", "{{DEATH}}": a.death or "?", "{{PLACE}}": a.place or "?"}
    for f in FILES:
        dest = root / f
        if dest.exists() and not a.force:
            print(f"skip (exists): {dest}"); continue
        text = (SKILL / "templates" / f).read_text()
        for k, v in repl.items(): text = text.replace(k, v)
        dest.write_text(text); print(f"wrote: {dest}")
    gi = root / ".gitignore"
    if not gi.exists():
        gi.write_text("# Raw DNA is biometric data: never commit it.\nsources/dna/\n*.cram *.bam *.sam *.vcf *.vcf.gz *.bcf *.fastq *.fastq.gz *.fq *.fq.gz\n*AncestryDNA*.txt *23andMe*.txt\ngenotype*.txt raw-dna*\n")
        print(f"wrote: {gi}")
    print(f"\nCase folder: {root}\nNext: fill 00-intake.md (Phase 0 gate), then 01-plan.md. See SKILL.md workflow.")

if __name__ == "__main__":
    sys.exit(main())
