#!/usr/bin/env python3
"""Write Pass 139 case-file rows. IDs start at C1820 (138b used C1815–C1819)."""
from pathlib import Path

ROOT = Path("/workspace/research/dora-ella-newnam")

EXTRACT = """Pass 139 extract — 31 Oct 2026
B058 one catalog reconfirm + B071 Hopkins John 59 IMAGE SEEN
+ Graves compiled close + leftover county-start map
+ Campbell Newport stamp 127 ≠ Kenton 130B
+ OPEN B059/B065/B081/B084 + partials B055/B080/B069/B045/B088 one line

Search-variant-alternatives cats 1–4:
  William/Wm/Jno/John × Newman/Newnam/newnarn/newan/Nureman
  Jane/Rhoda/Louisa/Martha/Eveline/Angeline
  Tincher/Tinker/Tinsher
  Soundex N550 / T526 / S350
  Place: Hopkins reel 205 Dist 2 n0238–n0261; Graves SK; leftover reels 190/194/204/219/220/201/202/209/210/213/214/195/200
  Kenton neighbors: GADSON / CLUSTRE / HERNDON / ILIFF 130B

=== B058 ===
LOC sn89051008 item.digitized: false (pass139 json 34425 B).
IA Solr title:(Dardanelle Post-Dispatch) AND year:1926 numFound 0.
Film unread. Phone 479-968-4368 not re-asked.
C1820

=== B071 Hopkins Dist 2 n0240 ===
n0238 IMAGE SEEN reconfirm: hh 67/67 Francis J. Newman 28 Farmer KY × Mary J 25 + Elizabeth 1. REJECT (already C1776).
n0239 verso 21 July Dist 2: hh 71–74. 74/74 Ash Armstrong 38. John 59 not on this verso.
n0240 IMAGE SEEN:
hh 76/76 Jno Newman 59 M Farmer N. Carolina
         Jane Newman 53 F N. Carolina
         Louisa Newman 28 F Kentucky
         Martha 20 F
         Eveline 16 F
         Elizabeth 13 F
         William P 26 M Farmer   (same household; not a living head)
hh 77/77 Logan Oakley 27 Farmer $257 N. Carolina
REJECT vs William 26 × Jane 22 of Owsley. Jane here is 53 NC. William P 26 is a son. No Francis 4 / Leanner 2. No Rhoda.
C1821 C1822 C1823
Named Hopkins Newman heads Francis J + John 59 both image-seen. County NOT every-line closed.
C1824

=== B071 leftover ===
SK Graves LIVE 124164 B: NEWHOUSE 468A/B; NEWTON 377B/464A/473B/481B. NIL Newman/Newnam/Tincher. County CLOSED compiled couple hunt.
C1825
Reel 204 n0005 = Hart Dist 1 15 July stamp 3 IMAGE SEEN header. n0120 still Hart. County NOT walked.
C1826
Reel 204 n0440 = Henry Dist 1 2 Aug IMAGE SEEN header. County NOT walked. Henderson n0200–n0360 already CLOSED compiled.
C1827 C1828
Larue Hamilton Dist n0160 stamp 398 IMAGE SEEN header. County NOT closed.
C1829
Campbell reel 195 n0130 IMAGE SEEN: City of Newport, Campbell County, stamp 127, 28 Aug, Joseph A. Piner. NOT Kenton Dist 1 130B.
C1830
Kenton reel 208 end n0643 IMAGE SEEN MICROCOPY target. Dist 1 130B is not bound at reel end. kentuckycensus00reel208 metadata empty {}.
SK Kenton LIVE: NEWMAN 130B, 221B, 222A, 226B, 261B, 268A, 270B. 130B neighbors GADSON / CLUSTRE / HERNDON / ILIFF.
C1831 C1832
Leftover starts mapped (NOT closed): Hickman n0005 stamp 3; Livingston n0340 3 Aug; Muhlenberg Dist 2 n0360 stamp 357; Franklin Dist 2 n0300 stamp 163 (reel 200, not yet Fulton); Grayson n0005; Spencer/Trimble/Grant already CLOSED compiled.
C1833
Still no free William × Rhoda or William × Jane license.
C1834
Parents of 1928 Frank still PROBABLE.
1860 Rhoda widow + B.F. 7 PROVEN.
Jane not Rhoda. #28 stands.
1850 living head FOUND remains Owsley hh 311 only.
C1835

=== OPEN / partials ===
GT Lee WWI LIVE 452540. Brandenburg + Underwood only. Cards unread. C1836
FS 1146342 SPA 19655 B (R011-77). USGenNet wills LIVE Jane Steele / Elizabeth / Mary F. — no Samuel P. C1837 C1842
Hutchins FAQ 9938 LIVE cards 228–229. No free June 1958 clip. Phone not re-asked. C1838
IA 602 metadata {}. pass123 still 515. One line. C1839
Grant 21 not merged. B084 POSSIBLE Jr only. Do not print 1966 or 1962. Did not walk 33-12/33-13. C1840
IA Solr M1509 KY 0. C1841

Did not repeat closed N-walks including Breckinridge 100A/100B/108B.
Did not walk Estill 1930 33-12/33-13.
Authored Word SHA 78cdcf44… not overwritten.
"""
(ROOT / "sources/census/pass139-extract-2026-10-31.txt").write_text(EXTRACT)

# --- 04-evidence ---
ev = ROOT / "04-evidence.md"
text = ev.read_text()
if "| C1820 |" not in text:
    ev.write_text(text.rstrip() + """

| C1820 | LOC sn89051008 pass139 `item.digitized: false` (34425 B). IA Solr 1926 **0**. Film unread. Phone not re-asked | PROVEN as catalog | S1487 S1488 L1645 | B058 |
| C1821 | Hopkins Dist 2 n0238 **IMAGE SEEN** reconfirm: hh **67/67 Francis J. Newman 28** Farmer KY × Mary J **25** + Elizabeth **1**. **REJECT** | PROVEN as image + reject | S1489 L1646 | B071 |
| C1822 | Hopkins Dist 2 n0239 verso **IMAGE SEEN**: 21 July; hh **74/74 Ash Armstrong 38**. John **59** not on this verso | PROVEN as image | S1490 L1647 | B071 |
| C1823 | Hopkins Dist 2 n0240 **IMAGE SEEN**: hh **76/76 Jno Newman 59** Farmer **N. Carolina** × Jane **53** NC + Louisa **28** + Martha **20** + Eveline **16** + Elizabeth **13** + **William P 26** Farmer (same household; not a living head). **REJECT** vs William **26** × Jane **22** of Owsley | PROVEN as image + reject | S1491 S1492 L1648 | B071 |
| C1824 | Hopkins named Newman heads Francis J + John **59** both **image-seen**. County **NOT** every-line closed | PROVEN as residual | S1493 L1649 | B071 |
| C1825 | SK Graves **LIVE 124164** B: NEWHOUSE **468A/B**; NEWTON **377B/464A/473B/481B**. NIL Newman/Tincher. County **CLOSED** compiled couple hunt | PROVEN as compiled-index + close | S1494 L1650 | B071 |
| C1826 | Hart Dist 1 n0005 **IMAGE SEEN** header stamp **3** 15 July. n0120 still Hart. County **NOT** walked | PROVEN as mapping + residual | S1495 L1651 | B071 |
| C1827 | Henry Dist 1 n0440 **IMAGE SEEN** header 2 Aug. County **NOT** walked | PROVEN as mapping + residual | S1496 L1652 | B071 |
| C1828 | Henderson n0200–n0360 Dist 1/2 **IMAGE SEEN** headers. Already **CLOSED** compiled | PROVEN as reconfirm | S1497 L1653 | B071 |
| C1829 | Larue Hamilton Dist n0160 stamp **398** **IMAGE SEEN** header. County **NOT** closed | PROVEN as mapping + residual | S1498 L1654 | B071 |
| C1830 | Campbell reel **195** n0130 **IMAGE SEEN**: City of Newport, Campbell Co., stamp **127**, 28 Aug, Joseph A. Piner. **NOT** Kenton Dist 1 **130B** | PROVEN as image + reject-as-place | S1499 L1655 | B071 |
| C1831 | Kenton reel **208** end n0643 **IMAGE SEEN** MICROCOPY. Dist 1 **130B** not bound at reel end. `kentuckycensus00reel208` metadata **{}** | PROVEN as image + catalog | S1500 S1501 L1656 | B071 |
| C1832 | SK Kenton **LIVE**: NEWMAN **130B**/221B/222A/226B/261B/268A/270B. **130B** neighbors GADSON / CLUSTRE / HERNDON / ILIFF. Dist 1 **130B** still a reel-**208** scan gap | PROVEN as compiled-index + residual | S1502 L1657 | B071 |
| C1833 | Leftover starts mapped **NOT** closed: Hickman n0005; Livingston n0340; Muhlenberg Dist 2 n0360; Franklin Dist 2 n0300 stamp **163**; Grayson n0005 | PROVEN as mapping | S1503 L1658 | B071 |
| C1834 | Still **no** free William × Rhoda or William × Jane license | PROVEN as negative | S1504 L1659 | B071 |
| C1835 | Parents of 1928 Frank still **PROBABLE**. 1860 Rhoda widow + B.F. **7** **PROVEN**. Jane **not** Rhoda. #28 stands. 1850 living head **FOUND** remains Owsley hh **311** only | PROBABLE / PROVEN | S1314 S1504 L1660 | B071 |
| C1836 | GT Lee WWI **LIVE 452540**. Brandenburg, Luther + Underwood, Luther only. Cards unread | PROVEN as compiled-index | S1505 L1661 | B059 |
| C1837 | FS **1146342** SPA **19655** B `isLoggedIn false` (R011-**77**) | PROVEN as access | S1506 L1662 | B065 B069 |
| C1838 | Hutchins FAQ **9938** **LIVE** cards **228–229**. No free June **1958** clip | PROVEN as catalog | S1507 L1663 | B055 B080 |
| C1839 | IA **602** pass139 metadata **{}**. pass123 still **515**. One line | PROVEN as catalog | S1508 L1664 | B088 |
| C1840 | Grant 21 **not merged**. B084 POSSIBLE Jr only. Do not print 1966 or 1962. Did not walk **33-12 / 33-13**. Phones / R001/R007/R008 not re-asked | PROVEN as process | S1504 L1665 | B081 B084 B082 |
| C1841 | IA Solr M1509 KY **0**. Cards unread | PROVEN as catalog | S1509 L1666 | B069 |
| C1842 | USGenNet wills **LIVE** — Jane Steele / Elizabeth / Mary F. — **no** Samuel P. | PROVEN as compiled | S1510 L1667 | B045 B065 |
""")
    print("evidence appended")
else:
    print("evidence already has C1820")

# --- 02-log ---
log = ROOT / "02-log.md"
lt = log.read_text()
if "| L1645 |" not in lt:
    # insert before first Access honesty block
    marker = "**Access honesty (pass 138):**"
    rows = """| L1645 | 2026-10-31 | LOC sn89051008 + IA Solr 1926 (**B058**) | Dora/posa × Stone | `digitized: false` 34425 B. Solr **0**. Phone not re-asked (**C1820**) | S1487 S1488 | B058 |
| L1646 | 2026-10-31 | Hopkins n0238 (**B071**) | Francis J 28 | **IMAGE SEEN** reconfirm hh **67/67** × Mary J **25**. **REJECT** (**C1821**) | S1489 | B071 |
| L1647 | 2026-10-31 | Hopkins n0239 verso (**B071**) | Ash Armstrong 38 | John **59** not on verso (**C1822**) | S1490 | B071 |
| L1648 | 2026-10-31 | Hopkins n0240 (**B071**) | Jno Newman 59 / William P 26 | **IMAGE SEEN** hh **76/76** Jane **53** NC + son William P **26**. **REJECT** vs Owsley (**C1823**) | S1491 S1492 | B071 |
| L1649 | 2026-10-31 | Hopkins named heads (**B071**) | Francis J + John 59 | both image-seen. County **NOT** every-line (**C1824**) | S1493 | B071 |
| L1650 | 2026-10-31 | SK Graves (**B071**) | Newman/Tincher | NEWHOUSE/NEWTON only. County **CLOSED** compiled (**C1825**) | S1494 | B071 |
| L1651 | 2026-10-31 | Hart Dist 1 n0005 (**B071**) | header | stamp **3** 15 July. **NOT** walked (**C1826**) | S1495 | B071 |
| L1652 | 2026-10-31 | Henry Dist 1 n0440 (**B071**) | header | 2 Aug. **NOT** walked (**C1827**) | S1496 | B071 |
| L1653 | 2026-10-31 | Henderson n0200–n0360 (**B071**) | headers | already **CLOSED** compiled (**C1828**) | S1497 | B071 |
| L1654 | 2026-10-31 | Larue n0160 (**B071**) | Hamilton Dist | stamp **398**. **NOT** closed (**C1829**) | S1498 | B071 |
| L1655 | 2026-10-31 | Campbell n0130 (**B071**) | Newport stamp 127 | **IMAGE SEEN**. **NOT** Kenton **130B** (**C1830**) | S1499 | B071 |
| L1656 | 2026-10-31 | Kenton reel-208 end n0643 (**B071**) | MICROCOPY | **130B** not at reel end. alt item meta **{}** (**C1831**) | S1500 S1501 | B071 |
| L1657 | 2026-10-31 | SK Kenton 130B neighbors (**B071**) | GADSON/CLUSTRE/HERNDON/ILIFF | NEWMAN **130B** still a scan gap (**C1832**) | S1502 | B071 |
| L1658 | 2026-10-31 | Leftover starts (**B071**) | Hickman/Livingston/Muhlenberg/Franklin/Grayson | mapped **NOT** closed (**C1833**) | S1503 | B071 |
| L1659 | 2026-10-31 | Free marriage (**B071**) | William × Rhoda / Jane | Still **no** free license (**C1834**) | S1504 | B071 |
| L1660 | 2026-10-31 | Same-person / #28 (**B071**) | William × Rhoda / Jane | Parents **PROBABLE**. Jane **not** Rhoda. #28 stands. Living head remains Owsley hh **311** (**C1835**) | S1314 S1504 | B071 |
| L1661 | 2026-10-31 | GT Lee WWI (**B059**) | Luther / John H. / McCoy | LIVE **452540**. Brandenburg + Underwood only (**C1836**) | S1505 | B059 |
| L1662 | 2026-10-31 | FS **1146342** (**B065**) | catalog | SPA **19655** B (R011-**77**) (**C1837**) | S1506 | B065 B069 |
| L1663 | 2026-10-31 | Hutchins FAQ **9938** (**B055/B080**) | *Citizen* cards | **LIVE** rooms **228–229**. No free June **1958** clip (**C1838**) | S1507 | B055 B080 |
| L1664 | 2026-10-31 | IA **602** metadata (**B088**) | imagecount | pass139 **{}**. pass123 still **515**. One line (**C1839**) | S1508 | B088 |
| L1665 | 2026-10-31 | Grant 21 / Jr / process (**B081/B084**) | deceased-only | **not merged**. POSSIBLE Jr only. No 1966/1962. No **33-12/33-13** (**C1840**) | S1504 | B081 B084 B082 |
| L1666 | 2026-10-31 | IA Solr M1509 KY (**B069**) | cards | **0** (**C1841**) | S1509 | B069 |
| L1667 | 2026-10-31 | USGenNet wills (**B045/B065**) | Samuel P. | Jane Steele / Elizabeth / Mary F. — **no** Samuel P. (**C1842**) | S1510 | B045 B065 |
| L1668 | 2026-10-31 | Search-variant-alternatives cats **1–4** | Jno/William/Jane/Rhoda | Soundex **N550** / **T526** / **S350**. Exact strings this extract | S1504 | B071 |

**Access honesty (pass 139):** LOC sn89051008 JSON **seen** (`digitized: false`). IA Solr Post-Dispatch 1926 **0**. IA Solr M1509 KY **0**. IA **602** metadata **{}** (pass123 still **515**). Hopkins n0238/n0239/n0240 **image seen**. SK Graves **HTML seen** (NEWHOUSE/NEWTON only). Hart Dist 1 / Henry Dist 1 / Larue Hamilton / Campbell Newport **127** / Kenton reel-end MICROCOPY **image seen**. SK Kenton **HTML seen** (NEWMAN **130B** residual). FS **1146342** SPA **19655** B. USGenNet wills **HTML seen**. GT Lee WWI **LIVE**. FAQ **9938** **LIVE**. fishergenes / kykinfolk **404**. SK leftover handshake except Graves. Kenton **130B** still a reel-**208** scan gap. Henry / Hart / Larue / Hopkins remaining. *Dardanelle Post-Dispatch* film **unread**. M1509 **cards unread**. Certs **unread**. Authored `latest.docx` SHA **78cdcf44…** not overwritten.

"""
    if marker in lt:
        log.write_text(lt.replace(marker, rows + marker, 1))
        print("log inserted")
    else:
        log.write_text(lt.rstrip() + "\n" + rows)
        print("log appended")
else:
    print("log already has L1645")

# --- SOURCE-INDEX ---
si = ROOT / "SOURCE-INDEX.md"
st = si.read_text()
if "| S1487 |" not in st:
    marker = "\n## Word biography provenance"
    rows = """| S1487 | `sources/catalog/loc-sn89051008-pass139.json` | 2026-10-31 | LOC | https://www.loc.gov/item/sn89051008/ | `item.digitized: false` 34425 B | **C1820** | catalog only |
| S1488 | `sources/catalog/ia-solr-postdispatch-1926-pass139.json` | 2026-10-31 | IA Solr | https://archive.org/ | 1926 **0** | **C1820** | index only |
| S1489 | `sources/census/pass139/keyplates/hopkins-n0238-francis-band.jpg` | 2026-10-31 | IA reel 205 n0238 | https://archive.org/details/populationschedu0205unix | Francis J 28 reconfirm | **C1821** | image seen |
| S1490 | `sources/census/pass139/namecols/hopkins-n0239-names.jpg` | 2026-10-31 | IA reel 205 n0239 | https://archive.org/details/populationschedu0205unix | Ash Armstrong 38 verso | **C1822** | image seen |
| S1491 | `sources/census/pass139/keyplates/hopkins-n0240-john-59-tight.jpg` | 2026-10-31 | IA reel 205 n0240 | https://archive.org/details/populationschedu0205unix | Jno Newman 59 SHA **4c7f1521…** | **C1823** | image seen |
| S1492 | `sources/census/pass139/keyplates/hopkins-n0240-john-59-william-p.jpg` | 2026-10-31 | IA reel 205 n0240 | https://archive.org/details/populationschedu0205unix | William P 26 same hh SHA **da4158b0…** | **C1823** | image seen |
| S1493 | `sources/census/pass139-extract-2026-10-31.txt` | 2026-10-31 | This session | — | Pass 139 extract | **C1820–C1842** | extract |
| S1494 | `sources/catalog/sk-graves-1850-pass139.html` | 2026-10-31 | S-K Publications | https://www.skcensus.com/1850-census-index-graves-county-kentucky/ | NEWHOUSE/NEWTON only | **C1825** | index only |
| S1495 | `sources/census/pass139/keyplates/r204-n0005-header.jpg` | 2026-10-31 | IA reel 204 n0005 | https://archive.org/details/populationschedu0204unix | Hart Dist 1 stamp **3** | **C1826** | image seen |
| S1496 | `sources/census/pass139/keyplates/r204-n0440-header.jpg` | 2026-10-31 | IA reel 204 n0440 | https://archive.org/details/populationschedu0204unix | Henry Dist 1 2 Aug | **C1827** | image seen |
| S1497 | `sources/census/pass139/keyplates/r204-n0200-header.jpg` | 2026-10-31 | IA reel 204 n0200 | https://archive.org/details/populationschedu0204unix | Henderson Dist 1 | **C1828** | image seen |
| S1498 | `sources/census/pass139/keyplates/larue-n0160-header.jpg` | 2026-10-31 | IA reel 209 n0160 | https://archive.org/details/populationschedu0209unix | Larue Hamilton stamp **398** | **C1829** | image seen |
| S1499 | `sources/census/pass139/keyplates/campbell-n0130-header.jpg` | 2026-10-31 | IA reel 195 n0130 | https://archive.org/details/populationschedu0195unix | Newport Campbell stamp **127** | **C1830** | image seen |
| S1500 | `sources/census/pass139/keyplates/kentonend-n0643-header.jpg` | 2026-10-31 | IA reel 208 n0643 | https://archive.org/details/populationschedu0208unix | MICROCOPY reel end | **C1831** | image seen |
| S1501 | `sources/catalog/ia-meta-kentuckycensus00reel208-pass139.json` | 2026-10-31 | IA | https://archive.org/metadata/kentuckycensus00reel208 | empty **{}** | **C1831** | catalog only |
| S1502 | `sources/catalog/sk-kenton-1850-pass139.html` | 2026-10-31 | S-K Publications | https://www.skcensus.com/1850-census-index-kenton-county-kentucky/ | NEWMAN **130B** + neighbors | **C1832** | index only |
| S1503 | `sources/census/pass139/keyplates/` leftover headers | 2026-10-31 | IA reels 200/202/204/210/214 | https://archive.org/ | Hickman/Livingston/Muhlenberg/Franklin/Grayson map | **C1833** | image seen |
| S1504 | `sources/census/pass139-extract-2026-10-31.txt` | 2026-10-31 | This session | — | no license; process | **C1834 C1835 C1840** | extract |
| S1505 | `sources/catalog/gt-lee-wwi-pass139.html` | 2026-10-31 | Genealogy Trails | https://www.genealogytrails.com/ken/lee/wwi_draft_cards.html | LIVE **452540** | **C1836** | index only |
| S1506 | `sources/catalog/fs-1146342-pass139.html` | 2026-10-31 | FamilySearch | https://www.familysearch.org/search/catalog/1146342 | SPA **19655** B | **C1837** | catalog only |
| S1507 | `sources/catalog/hutchins-faq-9938-pass139.html` | 2026-10-31 | Berea Library Answers | https://libraryanswers.berea.edu/faq/9938 | Cards **228–229** LIVE | **C1838** | catalog only |
| S1508 | `sources/catalog/ia-meta-602-pass139.json` | 2026-10-31 | IA T625-602 | https://archive.org/metadata/14thcensusofpopu0602unit | empty **{}** | **C1839** | catalog only |
| S1509 | `sources/catalog/ia-solr-m1509-ky-pass139.json` | 2026-10-31 | IA Solr | https://archive.org/ | M1509 KY **0** | **C1841** | index only |
| S1510 | `sources/catalog/usgennet-lee-wills-pass139.html` | 2026-10-31 | USGenNet Lee wills | https://usgennet.org/usa/ky/county/lee/wills/ | no Samuel P. | **C1842** | transcription only |

"""
    if marker in st:
        si.write_text(st.replace(marker, "\n" + rows + marker, 1))
        print("source-index inserted")
    else:
        print("SOURCE-INDEX marker missing")
else:
    print("source-index already has S1487")

print("core tables done")
