#!/usr/bin/env python3
"""Print workaround ladder checklists for genealogy roadblocks. Stdlib only.
Usage: workaround_playbook.py <paywall|on-site|no-vital|common-name|illegible|nil-index|language|dna|privacy|list>"""
import sys

PLAYBOOKS = {
    "paywall": ("A Paywall / subscription", ["A1 FamilySearch, free archives, free newspapers", "A2 Same collection elsewhere / index-only", "A3 Free substitutes for same claim", "A4 Finding aid + blocked backlog — then ask user for login/payment only"]),
    "on-site": ("B Not digitised / on-site", ["B1 Digitised copy elsewhere", "B2 Indexes & abstracts online", "B3 Adjacent online record types", "B4 Filled copy-order → deferred — then ask user to order/visit"]),
    "no-vital": ("C No vital record", ["C1 Church/burial/banns", "C2 Census/military/marriage/death ages", "C3 Indirect proof draft", "C4 FAN siblings/children name parents", "C5 DNA plan"]),
    "common-name": ("D Too many same-name hits", ["D1 Second identifier", "D2 FAN cluster filter", "D3 Timeline elimination", "D4 Candidate table P###", "D5 Land/probate tie-break"]),
    "illegible": ("E Bad image / handwriting", ["E1 Inventory + enhance copy", "E2 Partial transcript + [illegible]", "E3 Duplicate record elsewhere", "E4 Same-hand letterform compare", "E5 HTR draft verify — then ask re-capture"]),
    "nil-index": ("F Index/database nil", ["F1 Browse images by date/place", "F2 Search without surname", "F3 Variants + neighbour jurisdiction", "F4 Transcription-error variants", "F5 Second repository"]),
    "language": ("G Language/script barrier", ["G1 Formula + dates/numerals", "G2 Register term dictionary", "G3 Society translation/index", "G4 MT of your transcription (draft) — then ask translator"]),
    "dna": ("H DNA/tool gap", ["H1 Use stated match data only", "H2 Documentary trees for matches", "H3 Targeted testing strategy", "H4 Run dna_file_check/samtools if file present — then ask upload/consent"]),
    "privacy": ("I Privacy / living boundary", ["I1 Research deceased generation only", "I2 Redact living — stop contact/bypass"]),
}

def main():
    if len(sys.argv) != 2:
        print(__doc__); return 2
    key = sys.argv[1].lower()
    if key == "list":
        for k, (title, _) in PLAYBOOKS.items():
            print(f"  {k:12} {title}")
        print("\nSee references/creative-workarounds.md"); return 0
    if key not in PLAYBOOKS:
        print(f"Unknown type: {key}. Valid types:")
        for k, (title, _) in PLAYBOOKS.items(): print(f"  {k:12} {title}")
        return 2
    title, steps = PLAYBOOKS[key]
    print(f"# {title}\nLog each step in 11-backlog.md Roadblock log before blocked/asking user.\n")
    for i, s in enumerate(steps, 1):
        print(f"  [ ] {s}")
    print("\nMinimum 3 steps before user handoff (see proactive-autonomy.md).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
