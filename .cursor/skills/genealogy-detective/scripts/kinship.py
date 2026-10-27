#!/usr/bin/env python3
"""Deterministic helpers: exact age, relationship from generations to a common ancestor, Soundex + search variants."""
import sys
from datetime import date

def parse(d):
    y, m, dd = (int(x) for x in d.split("-")); return date(y, m, dd)

def age(a, b):
    d1, d2 = parse(a), parse(b); years = d2.year - d1.year - ((d2.month, d2.day) < (d1.month, d1.day))
    print(f"{years} years (born {a}, event {b})")
    if years < 0: print("WARNING: event before birth"); return 1
    return 0

ORD = {1:"1st",2:"2nd",3:"3rd",4:"4th",5:"5th",6:"6th",7:"7th",8:"8th",9:"9th",10:"10th"}
def relation(g1, g2):
    """gN = generations from common ancestor (child=1)."""
    if g1 == 0 and g2 == 0: print("same person / self"); return
    if g1 == 0 or g2 == 0:
        n = max(g1, g2)
        label = {1:"parent/child",2:"grandparent/grandchild",3:"great-grandparent/great-grandchild"}.get(n, f"{n-2}x great-grandparent/grandchild")
        print(f"direct line: {label}"); return
    if g1 == g2: print(f"{ORD.get(g1-1, str(g1-1)+'th')} cousins" if g1 > 1 else "siblings (or half-siblings)"); return
    c, r = min(g1, g2) - 1, abs(g1 - g2)
    if c == 0: print(f"aunt/uncle–niece/nephew, {r-1} removal(s) beyond" if r > 1 else "aunt/uncle – niece/nephew"); return
    print(f"{ORD.get(c, str(c)+'th')} cousins {r}x removed")

CODES = {**dict.fromkeys("bfpv","1"), **dict.fromkeys("cgjkqsxz","2"), **dict.fromkeys("dt","3"), "l":"4", **dict.fromkeys("mn","5"), "r":"6"}
def soundex(name):
    letters = [c for c in name.lower() if c.isalpha()]
    if not letters: return "????"
    first, prev, out = letters[0], CODES.get(letters[0], ""), []
    for c in letters[1:]:
        code = CODES.get(c, "")
        if code and code != prev: out.append(code)
        if c not in "hw": prev = code
    return (first.upper() + "".join(out) + "000")[:4]

def main(argv):
    if len(argv) < 2: print(__doc__); return 2
    cmd = argv[1]
    if cmd == "age" and len(argv) == 4: return age(argv[2], argv[3])
    if cmd == "relation" and len(argv) == 4: relation(int(argv[2]), int(argv[3])); return 0
    if cmd == "soundex" and len(argv) == 3:
        n = argv[2]; print(f"{n}: Soundex {soundex(n)}")
        print("Search also: swap c/k, ph/f, i/y, single/double consonants, -son/-sen, Mc/Mac, O' prefix, first+last initials with wildcards, and browse by first name + place.")
        return 0
    print(__doc__); return 2

if __name__ == "__main__":
    sys.exit(main(sys.argv))
