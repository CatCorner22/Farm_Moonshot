#!/usr/bin/env python3
"""Honest SVG charts from case-folder CSV. Stdlib only.
 timeline: CSV columns name,birth,death[,events as year:label;year:label]  -> lifespan chart, zero tricks
 bar:      CSV columns label,value[,n] -> bar chart, axis always from zero, values+n labelled"""
import argparse, csv, html, sys
from pathlib import Path

def read(p):
    with open(p, newline="") as f: return list(csv.DictReader(f))

def timeline(rows, out, title):
    rows = [r for r in rows if r.get("birth") and r.get("death")]
    lo = min(int(r["birth"]) for r in rows) // 10 * 10; hi = max(int(r["death"]) for r in rows)
    W, left, rowh = 960, 190, 26; H = 70 + rowh * len(rows) + 40; span = max(hi - lo, 1)
    X = lambda yr: left + (yr - lo) / span * (W - left - 20)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         f'<text x="20" y="24" font-family="sans-serif" font-size="15" font-weight="700">{html.escape(title)}</text>']
    for yr in range(lo, hi + 1, 10):
        s.append(f'<line x1="{X(yr):.0f}" y1="40" x2="{X(yr):.0f}" y2="{H-35}" stroke="#e5e7eb"/><text x="{X(yr):.0f}" y="{H-18}" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#6b7280">{yr}</text>')
    for i, r in enumerate(rows):
        y = 52 + i * rowh; b, d = int(r["birth"]), int(r["death"])
        s.append(f'<text x="{left-8}" y="{y+13}" text-anchor="end" font-family="sans-serif" font-size="11">{html.escape(r["name"])}</text>')
        s.append(f'<rect x="{X(b):.0f}" y="{y}" width="{max(X(d)-X(b),2):.0f}" height="15" rx="3" fill="#2563eb" opacity="0.85"><title>{html.escape(r["name"])} {b}–{d}</title></rect>')
        s.append(f'<text x="{X(d)+5:.0f}" y="{y+12}" font-family="sans-serif" font-size="9" fill="#374151">{b}–{d}</text>')
        for ev in (r.get("events") or "").split(";"):
            if ":" in ev:
                yr, lab = ev.split(":", 1)
                if yr.strip().isdigit(): s.append(f'<circle cx="{X(int(yr)):.0f}" cy="{y+7}" r="3.5" fill="#dc2626"><title>{html.escape(lab.strip())} ({yr.strip()})</title></circle>')
    s.append("</svg>"); Path(out).write_text("\n".join(s)); print(f"wrote {out} ({len(rows)} lifespans, {lo}–{hi})")

def bar(rows, out, title, value, label):
    data = [(r[label], float(r[value]), r.get("n", "")) for r in rows if r.get(value)]
    mx = max(v for _, v, _ in data) or 1; W, left, rowh = 820, 220, 30; H = 70 + rowh * len(data) + 40
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         f'<text x="20" y="24" font-family="sans-serif" font-size="15" font-weight="700">{html.escape(title)}</text>',
         '<text x="20" y="40" font-family="sans-serif" font-size="9" fill="#4b5563">Axis starts at zero. Values labelled; n shown where supplied.</text>']
    for i, (lab, v, n) in enumerate(data):
        y = 55 + i * rowh; w = v / mx * (W - left - 90)
        s.append(f'<text x="{left-8}" y="{y+14}" text-anchor="end" font-family="sans-serif" font-size="11">{html.escape(str(lab))}</text>')
        s.append(f'<rect x="{left}" y="{y}" width="{w:.0f}" height="17" fill="#2563eb" opacity="0.85"/>')
        s.append(f'<text x="{left+w+6:.0f}" y="{y+13}" font-family="sans-serif" font-size="10">{v:g}{("  (n=" + html.escape(str(n)) + ")") if n else ""}</text>')
    s.append("</svg>"); Path(out).write_text("\n".join(s)); print(f"wrote {out} ({len(data)} bars, axis 0–{mx:g})")

def main():
    ap = argparse.ArgumentParser(description=__doc__); sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("timeline", "bar"):
        p = sub.add_parser(name); p.add_argument("csv"); p.add_argument("-o", "--out", default=f"{name}.svg"); p.add_argument("--title", default=name.title())
    p2 = sub.choices["bar"]; p2.add_argument("--value", default="value"); p2.add_argument("--label", default="label")
    a = ap.parse_args(); rows = read(a.csv)
    if a.cmd == "timeline": timeline(rows, a.out, a.title)
    else: bar(rows, a.out, a.title, a.value, a.label)

if __name__ == "__main__":
    main()
