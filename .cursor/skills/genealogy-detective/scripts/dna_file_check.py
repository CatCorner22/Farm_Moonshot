#!/usr/bin/env python3
"""Read-only DNA file inspector. Detects format (CRAM/BAM/SAM/VCF/BCF/FASTQ/consumer genotype/PLINK),
reports headers, build clues, and record counts. Never modifies, uploads, or interprets health data.
For CRAM/BAM/VCF deep inspection use samtools/bcftools — this tool says so when it sees those formats.
Usage: dna_file_check.py <file> [--sha256]"""
import gzip, hashlib, struct, sys
from pathlib import Path

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""): h.update(chunk)
    return h.hexdigest()

def sniff(p: Path):
    raw = p.read_bytes()[:8192]
    if raw[:4] == b"CRAM": return "CRAM", f"magic CRAM, spec version {raw[4]}.{raw[5]}, file_id={raw[6:26].hex()}"
    if raw[:2] == b"\x1f\x8b":
        try:
            inner = gzip.open(p, "rb").read(8192)
            if inner[:4] == b"BAM\x01": return "BAM (gzipped BGZF)", "binary SAM alignments"
            if inner[:4] == b"CRAM": return "CRAM (gzipped?)", "check with samtools"
            raw = inner
        except Exception as e: return "gzip (unknown inner)", str(e)
    if raw[:4] == b"BAM\x01": return "BAM", "binary SAM alignments"
    if raw[:3] == b"BCF": return "BCF", "binary VCF"
    return None, raw

def lines(p, gz=False, n=400000):
    op = gzip.open(p, "rt", errors="replace") if gz else open(p, errors="replace")
    with op:
        for i, line in enumerate(op):
            if i >= n: break
            yield line.rstrip("\n")

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args: print(__doc__); return 2
    p = Path(args[0])
    if not p.exists(): print(f"ERROR: no such file: {p}"); return 1
    print(f"file: {p}  ({p.stat().st_size:,} bytes)")
    if "--sha256" in sys.argv or True: print(f"sha256: {sha256(p)}")
    fmt, detail = sniff(p)
    gz = p.suffix in (".gz", ".bgz") or (len(p.suffixes) > 1 and p.suffixes[-1] == ".gz")
    if fmt in ("CRAM",) or (fmt and "CRAM" in fmt):
        print(f"format: CRAM — {detail}\nnext: samtools quickcheck -v {p} && samtools view -H {p}  # @SQ M5/UR identifies the reference; CRAM cannot be fully decoded without it. See references/raw-dna-files.md."); return 0
    if fmt and ("BAM" in fmt or fmt == "BCF"):
        tool = "samtools view -H / flagstat" if "BAM" in fmt else "bcftools view -h / stats"
        print(f"format: {fmt} — {detail}\nnext: {tool} {p}. See references/raw-dna-files.md."); return 0
    try: text_lines = list(lines(p, gz=gz))
    except Exception as e: print(f"format: unknown/binary ({e})\nDo not guess — identify with `file` and format tools; see references/raw-dna-files.md."); return 0
    head = text_lines[:40]
    joined = "\n".join(head)
    if joined.startswith("##fileformat=VCF") or any(l.startswith("#CHROM") for l in head):
        ref = [l for l in head if l.startswith("##reference")]; src = [l for l in head if l.startswith(("##source", "##GATKCommandLine"))]
        print(f"format: VCF/gVCF\n{ref[0] if ref else 'reference: NOT STATED in header — do not assume build'}")
        [print(s[:160]) for s in src[:2]]
        print(f"header lines: {sum(1 for l in text_lines if l.startswith('#'))}; records (first 400k lines): {sum(1 for l in text_lines if l and not l.startswith('#'))}")
        print("gVCF note: non-PASS/block records are not variants. Record caller + filters before any use."); return 0
    if head and head[0].startswith("@") and any(l.startswith(("@HD", "@SQ")) for l in head):
        sq = [l for l in head if l.startswith("@SQ")]
        print(f"format: SAM (text alignments)\n@SQ reference contigs: {len(sq)}; first: {sq[0][:160] if sq else 'none'}")
        print("next: samtools flagstat / view; note reference from @SQ before converting."); return 0
    if p.suffix.lower() in (".fastq", ".fq") or (head and head[0].startswith("@") and len(text_lines) > 3):
        print("format: FASTQ (raw reads — not variants; needs alignment + calling). Check: paired _R1/_R2 mates, read count/length, Phred encoding (FastQC/seqkit stats)."); 
        print(f"first record: {head[0][:120] if head else ''}"); return 0
    # Consumer genotype: comment headers + tabular rows
    comments = [l for l in head if l.startswith("#")]
    vendor = "unknown"
    for v in ("AncestryDNA", "23andMe", "MyHeritage", "FamilyTreeDNA", "Living DNA"):
        if v.lower() in joined.lower(): vendor = v
    rows = [l for l in text_lines if l and not l.startswith("#")]
    delim = "\t" if rows and "\t" in rows[0] else ("," if rows and "," in rows[0] else None)
    if rows and delim:
        ncol = len(rows[0].strip('"').split(delim))
        chroms, nocall = set(), 0
        rows = [r for r in rows if not r.strip('"').lower().startswith(("rsid", "rs_id", "#rsid", "chromosome", "snp"))]
        for r in rows:
            parts = [x.strip('"') for x in r.split(delim)]
            if len(parts) >= 3: chroms.add(parts[1])
            if parts and parts[-1] in ("--", "00", "", "0"): nocall += 1
        build = [c for c in comments if "build" in c.lower() or "GRCh" in c or "hg" in c.lower()]
        print(f"format: consumer/research genotype table (vendor header: {vendor})")
        print(f"columns: {ncol} (delimiter {'TAB' if delim == chr(9) else 'comma'}); data rows in first 400k lines: {len(rows):,}; chromosomes seen: {sorted(chroms)[:30]}")
        print(f"no-call-ish rows: {nocall:,}; build from header: {build[0][:140] if build else 'NOT STATED — do not assume (most legacy exports are GRCh37, verify)'}")
        print(f"header: {comments[0][:160] if comments else '(no comment header)'}")
        print("Count is a sanity check only, not a SNP total for matching. One file per tester; log uploads + consent in 05-dna.md."); return 0
    print("format: unrecognised text file. Do not guess — inspect the first lines manually and see references/raw-dna-files.md format map.")
    print(f"first line: {head[0][:160] if head else '(empty)'}"); return 0

if __name__ == "__main__":
    sys.exit(main())
