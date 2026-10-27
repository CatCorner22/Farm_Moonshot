#!/usr/bin/env python3
"""Generate an honest SVG family tree from structured JSON.
Input: {"persons":[{"id","name","birth","death","sex"}],
        "unions":[{"id","partners":[...],"children":[...],"type","confidence"}]}
Modes: pedigree (ancestors of --root) / descendant (descendants of --root).
Solid link=PROVEN, dashed=PROBABLE/POSSIBLE, dotted=SPECULATIVE; blue=non-biological union;
explicit grey box=Unknown. Validates cycles and implausible parent ages before drawing. Stdlib only."""
import argparse, html, json, sys
from pathlib import Path

BW, BH, XGAP, YGAP = 190, 46, 70, 14

def load(path):
    d = json.loads(Path(path).read_text())
    persons = {x["id"]: x for x in d.get("persons", [])}
    unions = d.get("unions", [])
    for u in unions:
        for pid in u.get("partners", []) + u.get("children", []):
            if pid not in persons: sys.exit(f"ERROR: union {u.get('id')} references unknown person {pid}")
    child_union = {}
    for u in unions:
        for c in u.get("children", []):
            if c in child_union: sys.exit(f"ERROR: {c} appears as a child in two unions")
            child_union[c] = u
    def check(pid, seen):
        if pid in seen: sys.exit(f"ERROR: cycle — {pid} is their own ancestor")
        u = child_union.get(pid)
        if u:
            for par in u.get("partners", []): check(par, seen | {pid})
    for pid in persons: check(pid, set())
    for u in unions:
        for c in u.get("children", []):
            cb = str(persons[c].get("birth", ""))[:4]
            for par in u.get("partners", []):
                pb = str(persons[par].get("birth", ""))[:4]
                if cb.isdigit() and pb.isdigit() and not (12 <= int(cb) - int(pb) <= 60):
                    print(f"WARN: {par} (b.{pb}) -> {c} (b.{cb}): implausible parent age {int(cb)-int(pb)}", file=sys.stderr)
    return persons, unions, child_union

def dash(conf):
    return {"PROVEN": "", "PROBABLE": ' stroke-dasharray="7 4"', "POSSIBLE": ' stroke-dasharray="7 4"',
            "SPECULATIVE": ' stroke-dasharray="2 4"'}.get(str(conf).upper(), ' stroke-dasharray="7 4"')

def box(x, y, person, unknown=False):
    name = "Unknown" if unknown else html.escape(str(person.get("name", "?")))
    dates = "" if unknown else html.escape(f"{person.get('birth','?')}–{person.get('death','?')}  {person.get('id','')}")
    style = ' fill="#f3f4f6" stroke="#9ca3af" stroke-dasharray="4 3"' if unknown else ' fill="white" stroke="#374151"'
    return (f'<g><rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="5"{style}/>'
            f'<text x="{x+BW/2}" y="{y+19}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="600" fill="#111827">{name}</text>'
            f'<text x="{x+BW/2}" y="{y+35}" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#4b5563">{dates}</text></g>')

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("data"); ap.add_argument("--root", required=True)
    ap.add_argument("--mode", choices=["pedigree", "descendant"], default="pedigree")
    ap.add_argument("--generations", type=int, default=4); ap.add_argument("-o", "--out", default="tree.svg")
    a = ap.parse_args()
    persons, unions, child_union = load(a.data)
    if a.root not in persons: sys.exit(f"ERROR: root {a.root} not in persons")
    partner_unions = {}
    for u in unions:
        for par in u.get("partners", []): partner_unions.setdefault(par, []).append(u)

    nodes, edges, leaf = [], [], [0]
    def node(pid, gen):
        n = {"pid": pid, "gen": gen, "y": 0.0}; nodes.append(n); return n
    def pedigree(pid, gen):
        me = node(pid, gen)
        if gen < a.generations:
            u = child_union.get(pid) if pid else None
            parents = ((u.get("partners", []) if u else []) + [None, None])[:2]
            kids = [pedigree(par, gen + 1) for par in parents]
            for k in kids: edges.append((me, k, u.get("confidence", "SPECULATIVE") if u else "SPECULATIVE", u.get("type", "biological") if u else "biological"))
            me["y"] = sum(k["y"] for k in kids) / 2
        else:
            me["y"] = leaf[0] * (BH + YGAP); leaf[0] += 1
        if gen == a.generations - 0 and False: pass
        return me
    def descendant(pid, gen):
        me = node(pid, gen)
        pairs = []
        if gen < a.generations:
            for u in partner_unions.get(pid, []):
                for c in u.get("children", []): pairs.append((c, u))
        if not pairs:
            me["y"] = leaf[0] * (BH + YGAP); leaf[0] += 1
        else:
            kids = [descendant(c, gen + 1) for c, u in pairs]
            for (c, u), k in zip(pairs, kids): edges.append((me, k, u.get("confidence", "SPECULATIVE"), u.get("type", "biological")))
            me["y"] = sum(k["y"] for k in kids) / len(kids)
        return me
    # pedigree leaves: parents beyond limit and childless branches need leaf slots;
    # pedigree() above only increments at max generation — fix branches ending early:
    # (they get y from children, which exist until max generation, so all paths reach it)
    pedigree(a.root, 0) if a.mode == "pedigree" else descendant(a.root, 0)

    W = (a.generations + 1) * (BW + XGAP) + 40
    H = max(n["y"] for n in nodes) + BH + 80
    xy = lambda n: (20 + n["gen"] * (BW + XGAP), 40 + n["y"])
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.0f} {H:.0f}">',
           f'<text x="20" y="24" font-family="sans-serif" font-size="14" font-weight="700">{a.mode.title()} of {html.escape(str(persons[a.root].get("name", a.root)))}</text>',
           '<text x="20" y="38" font-family="sans-serif" font-size="9" fill="#4b5563">solid PROVEN · dashed PROBABLE/POSSIBLE · dotted SPECULATIVE · blue non-biological · grey dashed box Unknown</text>']
    for parent, child, conf, typ in edges:
        x1, y1 = xy(parent); x2, y2 = xy(child)
        extra = ' stroke="#2563eb" stroke-width="2"' if typ != "biological" else ""
        if not extra: extra = ' stroke="#374151"'
        out.append(f'<path d="M{x1+BW},{y1+BH/2} C{x1+BW+30},{y1+BH/2} {x2-30},{y2+BH/2} {x2},{y2+BH/2}" fill="none"{extra}{dash(conf)}/>')
    for n in nodes:
        x, y = xy(n); out.append(box(x, y, persons.get(n["pid"], {}), unknown=n["pid"] is None))
    out.append(f'<text x="20" y="{H-8:.0f}" font-family="sans-serif" font-size="9" fill="#6b7280">Generated by make_pedigree.py from {html.escape(a.data)} · root {a.root} · {a.generations} generations · verify every link against claim IDs before sharing</text></svg>')
    Path(a.out).write_text("\n".join(out)); print(f"wrote {a.out} ({len(nodes)} boxes, {len(edges)} links)")

if __name__ == "__main__":
    main()
