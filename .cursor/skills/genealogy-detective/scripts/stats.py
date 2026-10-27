#!/usr/bin/env python3
"""Statistics helpers for honest genealogical/demographic/DNA claims. Stdlib only.
Always report counts, absolute AND relative measures, and intervals — see references/statistics.md."""
import argparse, math, sys

Z = 1.959963984540054
def fmt(x, d=4): return f"{x:.{d}f}"

def wilson(k, n):
    if n == 0: return (float("nan"),) * 3
    p = k / n; den = 1 + Z * Z / n; c = p + Z * Z / (2 * n)
    m = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n))
    return p, max(0, (c - m) / den), min(1, (c + m) / den)

def risk(a):
    pa, loa, hia = wilson(a.a_events, a.a_n); pb, lob, hib = wilson(a.b_events, a.b_n)
    rr = pa / pb if pb else float("inf"); ard = pa - pb
    # log-method CI for RR; Wald CI for ARD
    if a.a_events and a.b_events and a.a_n > a.a_events and a.b_n > a.b_events:
        se = math.sqrt(1/a.a_events - 1/a.a_n + 1/a.b_events - 1/a.b_n); rci = (math.exp(math.log(rr) - Z*se), math.exp(math.log(rr) + Z*se))
    else: rci = (float("nan"), float("nan"))
    sea = math.sqrt(pa*(1-pa)/a.a_n + pb*(1-pb)/a.b_n); aci = (ard - Z*sea, ard + Z*sea)
    scale = 1000
    print(f"Group A: {a.a_events}/{a.a_n} = {pa*scale:.1f} per 1,000  (95% CI {loa*scale:.1f}–{hia*scale:.1f})")
    print(f"Baseline B: {a.b_events}/{a.b_n} = {pb*scale:.1f} per 1,000  (95% CI {lob*scale:.1f}–{hib*scale:.1f})")
    print(f"ABSOLUTE difference: {ard*scale:+.1f} per 1,000 ({ard*100:+.2f} percentage points; 95% CI {aci[0]*scale:+.1f} to {aci[1]*scale:+.1f})")
    print(f"RELATIVE risk: {fmt(rr,2)}x (95% CI {fmt(rci[0],2)}–{fmt(rci[1],2)})  |  relative change {(rr-1)*100:+.0f}%")
    if ard: print(f"NNT/NNH: {abs(1/ard):.0f} people for one outcome to differ ({'NNH' if ard>0 else 'NNT'})")
    print("Sentence: \"Baseline {} in 1,000; group {} in 1,000 — {} extra per 1,000 (absolute), {}x relative. Groups, not individual destiny.\"".format(round(pb*scale,1), round(pa*scale,1), round(abs(ard)*scale,1), fmt(rr,2)))

def proportion(a):
    p, lo, hi = wilson(a.k, a.n)
    print(f"{a.k}/{a.n} = {p*100:.1f}%  (Wilson 95% CI {lo*100:.1f}%–{hi*100:.1f}%)  — always cite the counts with the %")

def bayes(a):
    prior = a.prior; odds = prior / (1 - prior)
    print(f"prior P={prior} (odds {fmt(odds,3)})")
    for lr in a.lr:
        odds *= lr; print(f"  x LR {lr} -> posterior P={fmt(odds/(1+odds))}")
    print("Report as a range across defensible priors, name each LR's justification, and include unglamorous hypotheses (see statistics.md).")

def or_to_rr(a):
    rr = a.or_ / (1 - a.baseline + a.baseline * a.or_)
    print(f"OR {a.or_} at baseline risk {a.baseline:.0%} converts to RR {fmt(rr,2)} — quoting the OR as if it were RR overstates the effect when outcomes are common.")

def main():
    ap = argparse.ArgumentParser(description=__doc__); sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("risk"); r.add_argument("--a-events", type=int, required=True); r.add_argument("--a-n", type=int, required=True)
    r.add_argument("--b-events", type=int, required=True); r.add_argument("--b-n", type=int, required=True); r.set_defaults(f=risk)
    p = sub.add_parser("proportion"); p.add_argument("--k", type=int, required=True); p.add_argument("--n", type=int, required=True); p.set_defaults(f=proportion)
    b = sub.add_parser("bayes"); b.add_argument("--prior", type=float, required=True); b.add_argument("--lr", type=float, action="append", required=True); b.set_defaults(f=bayes)
    o = sub.add_parser("or-to-rr"); o.add_argument("--or", dest="or_", type=float, required=True); o.add_argument("--baseline", type=float, required=True); o.set_defaults(f=or_to_rr)
    a = ap.parse_args()
    if hasattr(a, "prior") and not (0 < a.prior < 1): print("prior must be between 0 and 1"); return 2
    a.f(a); return 0

if __name__ == "__main__":
    sys.exit(main())
