#!/usr/bin/env python3
"""Audit a case folder against this skill's hard rules. Heuristic text checks — flags for human review,
never auto-passes proof. Exit 1 if any FAIL. Usage: audit_dossier.py research/<person>/"""
import re, sys
from pathlib import Path

FAIL, WARN = [], []
def need(cond, msg, bucket=FAIL):
    if not cond: bucket.append(msg)

def main():
    if len(sys.argv) != 2: print(__doc__); return 2
    root = Path(sys.argv[1])
    if not root.is_dir(): print(f"ERROR: not a directory: {root}"); return 2
    txt = {}
    for f in ["00-intake.md","01-plan.md","02-log.md","03-timeline.md","04-evidence.md","05-dna.md","06-dossier.md","07-conflicts.md","08-transcriptions.md","09-statistics.md","10-visuals.md","11-backlog.md"]:
        p = root / f; txt[f] = p.read_text(errors="replace") if p.exists() else ""
        need(bool(txt[f].strip()), f"missing/empty: {f}")
    intake, dossier, evid = txt["00-intake.md"], txt["06-dossier.md"], txt["04-evidence.md"]
    need("Research question" in intake and not re.search(r"Research question.*:\s*$", intake, re.M), "00-intake: research question blank")
    need("deceased" in intake.lower(), "00-intake: deceased confirmation not recorded")
    # Claims: confidence labels present, every PROVEN claim cites sources
    claims = [l for l in evid.splitlines() if re.match(r"\|\s*C\d+", l)]
    need(bool(claims), "04-evidence: no claims (C### rows) registered", WARN)
    for c in claims:
        if "PROVEN" in c:
            need(bool(re.search(r"S\d{3}", c)), f"PROVEN claim without Source ID: {c[:90]}")
            need("SPECULATIVE" not in c, f"PROVEN claim cites speculation: {c[:90]}")
        need(any(x in c for x in ("PROVEN","PROBABLE","POSSIBLE","SPECULATIVE","DISPROVED")), f"claim without confidence label: {c[:90]}", WARN)
    # GPS gates in dossier
    for gate in ("exhaustive", "citations", "analysis", "conflicts resolved", "written conclusion"):
        need(gate in dossier.lower(), f"06-dossier: GPS gate not mentioned: {gate}", WARN)
    need("☐" not in dossier.split("GPS gates")[1].split("\n")[0] if "GPS gates" in dossier else False,
         "06-dossier: GPS gate still unchecked (☐) — cannot claim PROVEN")
    # Negative searches logged?
    log_rows = [l for l in txt["02-log.md"].splitlines() if re.match(r"\|\s*L\d+", l) and "found / nil / n-a" not in l]
    need(any(re.search(r"\bnil\b|nothing found|no record found", l, re.I) for l in log_rows),
         "02-log: no negative (nil) searches logged — exhaustiveness not demonstrated", WARN)
    # Unresolved conflicts?
    conf = [l for l in txt["07-conflicts.md"].splitlines() if l.startswith("|") and "open" in l.lower()]
    if conf: WARN.append(f"07-conflicts: {len(conf)} conflict row(s) marked open — affected claims capped below PROVEN")
    # DNA files: if inventory has files, require checksum-looking entries
    dna_rows = [l for l in txt["05-dna.md"].splitlines() if re.match(r"\|\s*F\d+", l)]
    for r in dna_rows:
        need(bool(re.search(r"\b[0-9a-f]{64}\b", r)), f"05-dna: file row lacks SHA-256: {r[:90]}")
        need(any(b in r for b in ("GRCh37","GRCh38","hg19","hg38")), f"05-dna: file row lacks build (GRCh37/38): {r[:90]}", WARN)
    # Living-person hygiene in dossier
    if re.search(r"\b(born|b\.)\s*(19[5-9]\d|20\d\d)\b", dossier):
        WARN.append("06-dossier: contains post-1950 birth dates — check living-person redaction")
    # Transcription discipline: transcriptions exist but contain no uncertainty notation on difficult docs
    trans = txt["08-transcriptions.md"]
    if "DOC001" in trans.replace("DOC001 — (record type", "") and "[?]" not in trans and "[illegible]" not in trans:
        WARN.append("08-transcriptions: documents transcribed with zero [?]/[illegible] marks — check over-confidence (paleography.md)")
    # Statistics discipline: relative-risk language without absolute values
    if re.search(r"times (as likely|the risk)|double[sd]? the (risk|rate)", dossier, re.I) and "per 1,000" not in dossier and "per 1000" not in dossier:
        FAIL.append("06-dossier: relative-risk language without absolute (per-1,000) values — see statistics.md mandatory format")
    # Visuals registered?
    if "V001" in txt["10-visuals.md"].replace("V001 |", "") and "Claim IDs" not in txt["10-visuals.md"]:
        WARN.append("10-visuals: visuals present but claim-ID column missing")
    backlog = txt.get("11-backlog.md", "")
    open_bl = [l for l in backlog.splitlines() if re.match(r"\|\s*B\d+", l) and re.search(r"\bopen\b|\bin_progress\b", l, re.I)]
    if open_bl: FAIL.append(f"11-backlog: {len(open_bl)} open/in_progress item(s) — exhaustive research incomplete (exhaustive-research.md)")
    print(f"Auditing {root}\nclaims: {len(claims)} | dna files: {len(dna_rows)} | backlog open: {len(open_bl)}")
    for m in FAIL: print(f"FAIL: {m}")
    for m in WARN: print(f"WARN: {m}")
    print("RESULT:", "FAIL — fix or waive in writing before claiming PROVEN" if FAIL else "no FAILs (heuristics only — GPS still requires human judgement)")
    return 1 if FAIL else 0

if __name__ == "__main__":
    sys.exit(main())
