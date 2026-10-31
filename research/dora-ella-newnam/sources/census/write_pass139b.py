#!/usr/bin/env python3
"""Pass 139 remaining case-file patches: backlog, dossier, conflicts, gallery,
transcriptions, plan, timeline, biography MD, HTML."""
from pathlib import Path
import re

ROOT = Path("/workspace/research/dora-ella-newnam")

NOTE = (
    " Pass **139:** Hopkins n0240 hh **76/76 Jno Newman 59** Farmer NC × Jane **53** NC "
    "+ **William P 26** son **IMAGE SEEN REJECT** (**C1823**). SK Graves **CLOSED** compiled "
    "(**C1825**). Hart Dist 1 / Henry Dist 1 / Larue Hamilton mapped **NOT** walked "
    "(**C1826 C1827 C1829**). Campbell Newport stamp **127 ≠** Kenton **130B** (**C1830**). "
    "Reel **208** end = MICROCOPY (**C1831**)."
)

OPEN_NOTES = {
    "B058": " Pass **139:** LOC `digitized: false` 34425 B; IA Solr 1926 **0** (**C1820**). Phone not re-asked.",
    "B059": " Pass **139:** GT live **452540**; Brandenburg + Underwood only (**C1836**). Cards unread.",
    "B065": " Pass **139:** FS **1146342** SPA **19655** B (R011-**77**) (**C1837**). Wills no Samuel P. (**C1842**).",
    "B045": " Pass **139:** USGenNet wills **LIVE** — no Samuel P. (**C1842**).",
    "B069": " Pass **139:** FS SPA R011-**77** (**C1837**). IA Solr M1509 KY **0** (**C1841**).",
    "B055": " Pass **139:** FAQ **9938** **LIVE** cards **228–229**. No free June **1958** clip (**C1838**).",
    "B080": " Pass **139:** FAQ **9938** **LIVE**. No free June **1958** clip (**C1838**).",
    "B081": " Pass **139:** still **not merged** (**C1840**).",
    "B084": " Pass **139:** still **POSSIBLE** Jr only (**C1840**).",
    "B082": " Pass **139:** no new Woodford. Do not print 1966 (**C1840**).",
    "B088": " Pass **139:** still **515** (**C1839**) — one line.",
    "B071": NOTE,
}

bl = ROOT / "11-backlog.md"
bt = bl.read_text()
if "Pass **139:** Hopkins n0240" not in bt:
    def patch_row(text, bid, note):
        # append note to the last cell of the matching table row
        lines = text.splitlines(keepends=True)
        out = []
        for line in lines:
            if line.startswith(f"| {bid} |") and note not in line:
                line = line.rstrip("\n")
                if line.endswith("|"):
                    line = line[:-1] + note + " |\n"
                else:
                    line = line + note + "\n"
            out.append(line)
        return "".join(out)
    for bid, note in OPEN_NOTES.items():
        bt = patch_row(bt, bid, note)
    bl.write_text(bt)
    print("backlog rows patched")
else:
    print("backlog already has pass 139 notes")

# handoff
bt = bl.read_text()
old_closed = re.search(r"- \*\*Last closed:\*\*.+", bt)
if old_closed and "Stopped after:** Pass **139" not in bt:
    new_closed = (
        "- **Last closed:** 31 Oct 2026 (America/New_York) · **Stopped after:** Pass **139** "
        "(**L1645–L1668**, **C1820–C1842**) after Pass **138** (**C1797–C1819**). "
        "B058 still film-only (`item.digitized: false`; IA Solr 1926 **0**). "
        "**B071** 1850 living head **FOUND** = Owsley **299B** hh **311** William **26** × Jane **22** **$325**. "
        "Jane **not** Rhoda. Hopkins hh **76/76 Jno Newman 59** × Jane **53** NC + William P **26** son "
        "**IMAGE SEEN REJECT**. Graves **CLOSED** compiled. Breckinridge / Edmonson / Hancock / Boone / Barren "
        "remain **CLOSED**. Kenton Dist 1 **130B** still a reel-**208** scan gap (Campbell Newport **127** is "
        "another county; reel end is MICROCOPY). Hart Dist 1 / Henry Dist 1 / Larue Hamilton mapped **NOT** walked. "
        "No free license. Parents still **PROBABLE**. 1928 Frank = Benjamin F. **PROVEN**. "
        "1860 Rhoda widow + B.F. **7** **PROVEN**. Did **not** walk Estill **1930 33-12 / 33-13**. "
        "FAQ **9938** **LIVE**. Phones and clerk Tyler Phillips **606-464-8400** already recorded — do not re-ask. "
        "#28 stands. #26 open on death date only — do not print 1966 or 1976 as proven deaths. "
        "Do not print Floyd as Boyd. Do not print Hendrix Newnam as Boyd. Do not print Nennian as Boyd. "
        "Do not print 1962 as McCoy’s death. Do not print the 1942 Combs charge as fact. #20 still open. #27 open."
    )
    bt = bt.replace(old_closed.group(0), new_closed, 1)
    new_next = (
        "- **Next session starts with:** **B058** *Dardanelle Post-Dispatch* **Aug–Sep 1926** on Pope **Roll 5** "
        "(phone **479-968-4368**) / UArk **F419.D37 D3** — one catalog reconfirm only; "
        "**B071** residual Kenton Dist 1 **130B** (not on reel **208** labeled sequence; Campbell Newport **127** "
        "is another county) + Henry Dist 1 from n0440 + Hart Dist 1 n0005–n0188 + Mercer remaining + Franklin remaining "
        "+ Lincoln Dist 1 remaining + Hopkins remaining (do **not** repeat Francis J n0238 / John **59** n0240) "
        "+ Larue Hamilton remaining + leftover western SK workarounds (do **not** repeat closed walks including "
        "Breckinridge Dist 1 **100A/100B/108B** / Edmonson / Hancock / Graves compiled / Boone SK Newman / "
        "Barren SK Newman / Hardin **366A** / Logan SK Newman / Christian SK Newman / Ohio compiled / "
        "Kenton **221B/222A** / Henderson compiled / Spencer compiled / Trimble compiled / Grant compiled); "
        "**B055/B080** Hutchins cards **228–229** (FAQ **9938** **LIVE**); "
        "**B069/B047/B059** FS **1146342** + M1509 **KY45**; "
        "**B045/B061/B065** FS sign-in (do not re-ask); "
        "**B082** Duell-Clark / cert **17762** (do not print 1966); "
        "**B081/B084** Grant 21 vs David F. / POSSIBLE Jr only; "
        "**B088** one line max. Do **not** start Estill **1930 33-12 / 33-13**. "
        "User handoffs **R001/R007/R008** (do not re-ask)."
    )
    bt = re.sub(r"- \*\*Next session starts with:\*\*.+", new_next, bt, count=1)
    bl.write_text(bt)
    print("handoff rewritten")
else:
    print("handoff already pass 139 or pattern miss")

# dossier last-updated
dos = ROOT / "06-dossier.md"
dt = dos.read_text()
dt2 = re.sub(
    r"- \*\*Last updated:\*\*.+",
    "- **Last updated:** 31 Oct 2026 (America/New_York) — Pass **139** (**L1645–L1668**, **C1820–C1842**) after Pass **138** (**C1797–C1819**): B058 still film-only (`item.digitized: false`; IA Solr 1926 **0**). **B071** 1850 living head **FOUND** = Owsley **299B** hh **311** William **26** × Jane **22** **$325**. Jane **not** merged with Rhoda. Hopkins hh **76/76 Jno Newman 59** × Jane **53** NC + William P **26** son **IMAGE SEEN REJECT**. Graves **CLOSED** compiled. Breckinridge / Edmonson / Hancock / Boone / Barren remain **CLOSED**. Kenton Dist 1 **130B** residual (Campbell Newport stamp **127** is another county; reel **208** end = MICROCOPY). Hart Dist 1 / Henry Dist 1 / Larue Hamilton mapped **NOT** walked. No free license. Parents still **PROBABLE**. Did **not** walk Estill **1930 33-12 / 33-13**. FAQ **9938** **LIVE**. Phones and clerk not re-asked. #28 stands. #26 open on death date only. #20 still open. #27 open.",
    dt,
    count=1,
)
dt2 = dt2.replace(
    "Illustrated HTML book:** [`book/index.html`](book/index.html) — plates, endnotes, source appendix through **S1481**",
    "Illustrated HTML book:** [`book/index.html`](book/index.html) — plates, endnotes, source appendix through **S1510**",
)
dos.write_text(dt2)
print("dossier last-updated")

# conflicts #28 — append a short Pass 139 sentence to the last cell
cf = ROOT / "07-conflicts.md"
ct = cf.read_text()
if "Pass **139** Hopkins" not in ct:
    lines = ct.splitlines(keepends=True)
    out = []
    for line in lines:
        if line.startswith("| 28 |") and "Pass **139** Hopkins" not in line:
            line = line.rstrip("\n")
            if line.endswith("|"):
                line = (
                    line[:-1]
                    + " Pass **139** Hopkins n0240 Jno **59** × Jane **53** NC + William P **26** son "
                    "**IMAGE SEEN REJECT** (**C1823**). Graves **CLOSED** compiled. Hart/Henry/Larue mapped. "
                    "Campbell Newport **127 ≠** Kenton **130B**. #28 unchanged. |"
                    + "\n"
                )
        out.append(line)
    cf.write_text("".join(out))
    print("conflicts #28 patched")
else:
    print("conflicts already pass 139")

# gallery
gal = ROOT / "12-image-gallery.md"
gt = gal.read_text()
if "pass 139" not in gt.lower() and "Hopkins n0240" not in gt[-2000:]:
    gal.write_text(gt.rstrip() + """

## 1850 — Hopkins Dist 2 (pass 139)

1850 U.S. census, Hopkins County, District 2 — household 76/76 **Jno Newman**, 59, farmer, North Carolina, with **Jane**, 53, North Carolina, and **William P.**, 26, farmer, same household (a son, not a living head). Rejected versus William 26 × Jane 22 of Owsley.

![Hopkins n0240 Jno 59](sources/census/pass139/keyplates/hopkins-n0240-john-59-tight.jpg)

**Source:** S1491 · C1823

Same sheet, lines 8–14, with William P. 26 visible.

![Hopkins n0240 William P 26](sources/census/pass139/keyplates/hopkins-n0240-john-59-william-p.jpg)

**Source:** S1492 · C1823
""")
    print("gallery appended")
else:
    print("gallery already has pass 139")

# transcriptions
tr = ROOT / "08-transcriptions.md"
tt = tr.read_text()
if "DOC053" not in tt:
    tr.write_text(tt.rstrip() + """

## DOC053 — 1850 Hopkins Dist 2 n0240 Jno Newman 59 × Jane 53 + William P 26

**Inventory:** `sources/census/pass139/keyplates/hopkins-n0240-john-59-tight.jpg` SHA **4c7f1521…**; wide SHA **da4158b0…** (image seen). Dist 2, n0240.

### Diplomatic
> 76/76  Jno Newman      59  M  Farmer           N. Carolina
>         Jane Newman    53  F                   N. Carolina
>         Louisa Newman  28  F                   Kentucky
>         Martha         20  F
>         Eveline        16  F
>         Elizabeth      13  F
>         William P      26  M  Farmer
> 77/77  Logan Oakley    27  M  Farmer  $257     N. Carolina

Pass 2: Jane is 53 NC, not 22 KY. William P 26 is a son in the same household, not a living head. No Francis 4 / Leanner 2. No Rhoda. **REJECT** vs Owsley hh 311. → **C1823** / **S1491 S1492**.
""")
    print("DOC053 written")
else:
    print("DOC053 exists")

# plan
pl = ROOT / "01-plan.md"
pt = pl.read_text()
if "### Pass 139 variant storm" not in pt:
    pl.write_text(pt.rstrip() + """

### Pass 139 variant storm (31 Oct 2026)

**Dora Stone 1926 (B058)** — Dora/posa/dosa/rosa/dona × Stone/Newman/Newnam. Soundex **S350** / **N550**. One catalog reconfirm (`item.digitized: false`). Phone **479-968-4368** not re-asked.

**William × Jane / Hopkins John 59 (B071)** — William/Wm/Jno/John × Newman/Newnam/newnarn/newan/Nureman. Jane/Rhoda/Louisa/Martha/Eveline/Angeline. Tincher/Tinker/Tinsher. Soundex **N550** / **T526** / **S350**. Place Hopkins reel **205** Dist 2 n0238–n0261; Graves SK; Hart/Henry reel **204**; Larue **209**; Campbell **195** stamp **127**; Kenton neighbors GADSON/CLUSTRE/HERNDON/ILIFF **130B**.

**Marriage** — William × Rhoda / William × Jane. Still no free license.

**Frank / WWI / probate / 602 / Grant** — same strings as pass 138. FAQ **9938** LIVE. FS SPA R011-**77**.

Exact strings logged **L1645–L1668**.
""")
    print("plan appended")
else:
    print("plan already pass 139")

# timeline
tl = ROOT / "03-timeline.md"
tt = tl.read_text()
if "Hopkins Dist 2 n0240" not in tt:
    marker = "\n\n**Impossibility flags:**"
    rows = """
| **21 Jul 1850** | Hopkins Dist 2 n0238 hh **67** | FAN **PROVEN** as image + reject (reconfirm): Francis J. Newman **28** × Mary J **25** + Elizabeth **1** | Hopkins Co., KY | C1821 | S1489 |
| **1850** | Hopkins Dist 2 n0240 hh **76/76** | FAN **PROVEN** as image + reject: **Jno Newman 59** Farmer NC × Jane **53** NC + **William P 26** son (not a living head) | Hopkins Co., KY | C1823 | S1491 S1492 |
| **1850** | Graves | FAN **PROVEN** as compiled-index: NEWHOUSE/NEWTON only. County **CLOSED** compiled couple hunt | Graves Co., KY | C1825 | S1494 |
| **15 Jul 1850** | Hart Dist 1 n0005 stamp **3** | FAN **PROVEN** as mapping: header **IMAGE SEEN**. County **NOT** walked | Hart Co., KY | C1826 | S1495 |
| **2 Aug 1850** | Henry Dist 1 n0440 | FAN **PROVEN** as mapping: header **IMAGE SEEN**. County **NOT** walked | Henry Co., KY | C1827 | S1496 |
| **28 Aug 1850** | Campbell Newport n0130 stamp **127** | FAN **PROVEN** as image + reject-as-place: City of Newport, **not** Kenton Dist 1 **130B** | Campbell Co., KY | C1830 | S1499 |
"""
    if marker in tt:
        tl.write_text(tt.replace(marker, rows + marker, 1))
        print("timeline inserted")
    else:
        tl.write_text(tt.rstrip() + rows)
        print("timeline appended")
else:
    print("timeline already pass 139")

print("pass139b core done")
