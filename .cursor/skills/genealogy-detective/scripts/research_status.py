#!/usr/bin/env python3
"""Report whether a case meets the exhaustive-research completion contract.
Exit 1 if open backlog items block 'finished' status. Usage: research_status.py research/<person>/"""
import re, sys
from pathlib import Path

def main():
    if len(sys.argv) != 2: print(__doc__); return 2
    root = Path(sys.argv[1])
    if not root.is_dir(): print(f"ERROR: {root}"); return 2
    backlog = (root / "11-backlog.md").read_text(errors="replace") if (root / "11-backlog.md").exists() else ""
    log = (root / "02-log.md").read_text(errors="replace") if (root / "02-log.md").exists() else ""
    open_items = [l for l in backlog.splitlines() if re.search(r"\|\s*B\d+", l) and re.search(r"\bopen\b|\bin_progress\b", l, re.I)]
    deferred = [l for l in backlog.splitlines() if re.search(r"\|\s*B\d+", l) and "deferred" in l.lower()]
    log_rows = [l for l in log.splitlines() if re.match(r"\|\s*L\d+", l) and not re.search(r"found / nil / n-a", l)]
    nil_logged = any(re.search(r"\bnil\b|nothing found|no record", l, re.I) for l in log_rows)
    print(f"Case: {root}")
    print(f"Backlog: {len(open_items)} open/in_progress, {len(deferred)} deferred")
    if open_items:
        print("OPEN (research not complete):")
        for l in open_items[:15]: print(" ", l[:120])
        if len(open_items) > 15: print(f"  ... +{len(open_items)-15} more")
    print(f"Negative searches in log: {'yes' if nil_logged else 'NO — add nil results'}")
    if open_items:
        print("RESULT: INCOMPLETE — work backlog before claiming exhaustive research or PROVEN GPS #1")
        return 1
    print("RESULT: backlog clear (matrix/FAN/GPS still require human judgement — run audit_dossier.py)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
