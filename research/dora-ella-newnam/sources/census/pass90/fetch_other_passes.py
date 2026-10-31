#!/usr/bin/env python3
"""Pass 90: NARA/FS Antioch remainder + probate/press/WWI/Woodford/Rissie/1926/FAN."""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

OUT = Path("/workspace/research/dora-ella-newnam/sources")
CAT = OUT / "catalog"
PRESS = OUT / "press"
VITAL = OUT / "vital"
MIL = OUT / "military"
CENSUS = OUT / "census" / "pass90"
for p in (CAT, PRESS, VITAL, MIL, CENSUS):
    p.mkdir(parents=True, exist_ok=True)

UA = "Mozilla/5.0 (compatible; genealogy-research/1.0)"


def curl(url: str, dest: Path, extra: list[str] | None = None, timeout: int = 45) -> tuple[int, int]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "curl", "-sS", "-L", "--max-time", str(timeout),
        "-A", UA, "-o", str(dest), "-w", "%{http_code}",
    ]
    if extra:
        cmd[1:1] = extra
    cmd.append(url)
    r = subprocess.run(cmd, capture_output=True, text=True)
    code = (r.stdout or "").strip()[-3:] if r.returncode == 0 else f"rc{r.returncode}"
    size = dest.stat().st_size if dest.exists() else 0
    print(f"{code:4} {size:8} {dest.name}  {url}", flush=True)
    return (int(code) if code.isdigit() else 0, size)


JOBS: list[tuple[str, Path]] = [
    # B088 Antioch/Clifty remainder — NARA / FS / IA / ED descriptions
    ("https://catalog.archives.gov/api/v1/?q=T625%20602%20Kentucky%201920&resultTypes=item,file,recordGroup&rows=20",
     CAT / "nara-t625-602-pass90.json"),
    ("https://catalog.archives.gov/api/v1/?q=%2214th%20census%20of%20population%201920%22%20Wolfe%20Kentucky&rows=10",
     CAT / "nara-1920-wolfe-pass90.json"),
    ("https://www.familysearch.org/search/catalog/127913",
     CAT / "fs-127913-pass90.html"),
    ("https://www.familysearch.org/search/catalog/127869",
     CAT / "fs-127869-pass90.html"),
    ("https://www.familysearch.org/search/catalog/1146342",
     CAT / "fs-1146342-pass90.html"),
    ("https://www.familysearch.org/search/catalog/546788",
     CAT / "fs-1920-ky-census-pass90.html"),
    ("https://archive.org/metadata/14thcensusofpopu602unit",
     CAT / "ia-14thcensusofpopu602unit-pass90.json"),
    ("https://archive.org/metadata/14thcensusofpopu0602unit",
     CAT / "ia-14thcensusofpopu0602unit-pass90.json"),
    ("https://archive.org/advancedsearch.php?q=title%3A%28T625%20OR%20%2214th%20census%22%29%20AND%20%28wolfe%20OR%20602%29%20AND%20kentucky&fl[]=identifier,title,volume&output=json&rows=20",
     CAT / "ia-solr-t625-602-pass90.json"),
    ("https://archive.org/advancedsearch.php?q=%221920%20census%20enumeration%20district%22%20kentucky%20wolfe&fl[]=identifier,title&output=json&rows=15",
     CAT / "ia-solr-1920-ed-desc-pass90.json"),
    ("https://www.us-census.org/pub/usgenweb/census/ky/wolfe/1920/",
     CAT / "uscensus-wolfe-1920-pass90.html"),
    ("https://stevemorse.org/census/ed1920.html",
     CAT / "stevemorse-ed1920-pass90.html"),
    ("https://kygenweb.net/wolfe/census1.htm",
     CENSUS / "wolfe-census1-pass90.html"),
    ("https://kygenweb.net/wolfe/txt/1920i.txt",
     CENSUS / "1920i-clifty-pass90.txt"),
    ("https://kygenweb.net/wolfe/txt/1920k.txt",
     CENSUS / "1920k-antioch-pass90.txt"),

    # B045 / B061 probate substitutes
    ("https://chroniclingamerica.loc.gov/search/pages/results/?andtext=Newnam&date1=1900&date2=1911&state=Kentucky&format=json&rows=20",
     PRESS / "ca-newnam-ky-1900-1911-pass90.json"),
    ("https://chroniclingamerica.loc.gov/search/pages/results/?andtext=%22Samuel+Newman%22&date1=1900&date2=1912&state=Kentucky&format=json&rows=15",
     PRESS / "ca-samuel-newman-ky-1900-1912-pass90.json"),
    ("https://chroniclingamerica.loc.gov/search/pages/results/?andtext=%22Samuel+Newnam%22&date1=1900&date2=1912&format=json&rows=15",
     PRESS / "ca-samuel-newnam-1900-1912-pass90.json"),
    ("https://archive.org/advancedsearch.php?q=%28%22Samuel+Newnam%22+OR+%22Samuel+Newman%22%29+AND+%28Lee+OR+Owsley+OR+Beattyville%29+AND+%28will+OR+estate+OR+administrator+OR+probate%29&fl[]=identifier,title&output=json&rows=20",
     CAT / "ia-solr-samuel-estate-pass90.json"),
    ("https://www.courtlistener.com/?type=o&q=%22Newnam%22+Kentucky&order_by=score+desc",
     CAT / "courtlistener-newnam-pass90.html"),
    ("https://www.courtlistener.com/api/rest/v3/search/?q=Newnam%20Kentucky&type=o",
     CAT / "courtlistener-newnam-api-pass90.json"),
    ("https://usgennet.org/usa/ky/county/lee/court/court.html",
     CAT / "usgennet-lee-court-pass90.html"),
    ("https://usgennet.org/usa/ky/county/lee/wills/wills.html",
     CAT / "usgennet-lee-wills-pass90.html"),
    ("https://www.kygenweb.net/lee/",
     CAT / "kygenweb-lee-pass90.html"),
    ("https://sites.rootsweb.com/~kylee/",
     CAT / "rootsweb-lee-pass90.html"),
    ("https://www.genealogytrails.com/ken/lee/",
     CAT / "gt-lee-pass90.html"),
    ("https://archive.org/advancedsearch.php?q=title%3A%28%22Lee+County%22%29+AND+kentucky+AND+%28history+OR+will+OR+probate%29&fl[]=identifier,title&output=json&rows=15",
     CAT / "ia-solr-lee-history-pass90.json"),

    # B089 Boyd / Allie / certs
    ("https://usgennet.org/usa/ky/county/lee/marriage/marrbook6.html",
     VITAL / "lee-marr-book6-pass90.html"),
    ("http://www.scgs-ky.org/delbrth/lee-ok.pdf",
     VITAL / "scgs-lee-delayed-pass90.pdf"),
    ("https://kygenweb.net/estill/site/records/death/pages/1976.htm",
     VITAL / "estill-deaths-1976-pass90.html"),
    ("https://kygenweb.net/estill/site/records/death/pages/1978.htm",
     VITAL / "estill-deaths-1978-pass90.html"),
    ("https://kygenweb.net/fayette/",
     VITAL / "kygenweb-fayette-pass90.html"),
    ("https://www.findagrave.com/cemetery/search?cemetery-name=Lexington+Cemetery&cemetery-loc=Lexington%2C+Fayette+County%2C+Kentucky",
     VITAL / "fag-lexington-cemetery-search-pass90.html"),
    ("https://usgennet.org/usa/ky/county/lee/births/birthsn.html",
     VITAL / "lee-births-n-pass90.html"),
    ("https://archive.org/advancedsearch.php?q=identifier%3A%28t626*+OR+15thcensus*%29+estill+kentucky+1930&fl[]=identifier,title&output=json&rows=10",
     CAT / "ia-solr-1930-estill-pass90.json"),
    ("https://archive.org/advancedsearch.php?q=14thcensusofpopu+madison+kentucky+1920&fl[]=identifier,title&output=json&rows=10",
     CAT / "ia-solr-1920-madison-pass90.json"),
    ("https://archive.org/advancedsearch.php?q=14thcensusofpopu+clark+kentucky+1920&fl[]=identifier,title&output=json&rows=10",
     CAT / "ia-solr-1920-clark-pass90.json"),

    # B087 1942 Combs
    ("https://chroniclingamerica.loc.gov/search/pages/results/?andtext=Combs+Owsley&date1=1942&date2=1942&format=json&rows=15",
     PRESS / "ca-combs-owsley-1942-pass90.json"),
    ("https://chroniclingamerica.loc.gov/search/pages/results/?andtext=%22George+Combs%22+Kentucky&date1=1942&date2=1942&format=json&rows=15",
     PRESS / "ca-george-combs-1942-pass90.json"),
    ("https://usgennet.org/usa/ky/county/owsley/obit/gcombs.htm",
     PRESS / "owsley-courier-1942-gcombs-pass90.html"),
    ("https://kygenweb.net/owsley/",
     PRESS / "kygenweb-owsley-pass90.html"),

    # B069 / B047 WWI
    ("https://catalog.archives.gov/api/v1/?q=M1509%20Kentucky%20Lee&rows=15",
     CAT / "nara-m1509-lee-pass90.json"),
    ("https://archive.org/advancedsearch.php?q=M1509+kentucky+draft&fl[]=identifier,title&output=json&rows=15",
     CAT / "ia-solr-m1509-ky-pass90.json"),
    ("https://www.genealogytrails.com/ken/lee/wwi_draft.html",
     MIL / "gt-lee-wwi-pass90.html"),
    ("https://www.genealogytrails.com/ken/owsley/",
     MIL / "gt-owsley-pass90.html"),
    ("https://www.usgenweb.org/ky/lee/military.html",
     MIL / "usgw-lee-military-pass90.html"),

    # B082 Woodford
    ("https://genealogytrails.com/ken/woodford/obits.html",
     PRESS / "woodford-gt-obits-pass90.html"),
    ("https://www.kygenweb.net/woodford/",
     VITAL / "kygenweb-woodford-pass90.html"),
    ("https://www.findagrave.com/cemetery-browse/USA/Kentucky/Woodford-County?id=county_2462",
     VITAL / "fag-woodford-browse-pass90.html"),
    ("https://www.woodfordcountykyhistoricalsociety.com/booksandpublications",
     CAT / "wchs-books-pass90.html"),
    ("https://chroniclingamerica.loc.gov/search/pages/results/?andtext=%22John+Newman%22+Woodford&date1=1966&date2=1966&format=json&rows=10",
     PRESS / "ca-john-newman-woodford-1966-pass90.json"),
    ("https://ssdi.rootsweb.com/cgi-bin/ssdi.cgi",
     VITAL / "ssdi-rootsweb-shell-pass90.html"),

    # B016 Rissie
    ("https://www.findagrave.com/memorial/search?firstname=Rissie&lastname=Pelfrey&includeMaidenName=true",
     VITAL / "fag-rissie-pelfrey-pass90.html"),
    ("https://www.findagrave.com/memorial/search?firstname=Rissie&lastname=Stamper&includeMaidenName=true",
     VITAL / "fag-rissie-stamper-pass90.html"),
    ("https://www.findagrave.com/memorial/search?firstname=Rissie&lastname=Newnam&includeMaidenName=true",
     VITAL / "fag-rissie-newnam-pass90.html"),
    ("https://tngenweb.org/knox/",
     VITAL / "tngenweb-knox-pass90.html"),
    ("https://www.tngenweb.org/records/knox/",
     VITAL / "tngenweb-knox-records-pass90.html"),

    # B049 / B058 1926 papers
    ("https://chroniclingamerica.loc.gov/search/titles/results/?terms=yell+county+journal&format=json",
     PRESS / "ca-titles-yell-journal-pass90.json"),
    ("https://chroniclingamerica.loc.gov/search/titles/results/?terms=dardanelle+post-dispatch&format=json",
     PRESS / "ca-titles-dardanelle-pass90.json"),
    ("https://chroniclingamerica.loc.gov/search/titles/results/?terms=danville+democrat+arkansas&format=json",
     PRESS / "ca-titles-danville-democrat-pass90.json"),
    ("https://chroniclingamerica.loc.gov/lccn/sn89051008/",
     PRESS / "loc-sn89051008-pass90.html"),
    ("https://chroniclingamerica.loc.gov/lccn/sn90050035/",
     PRESS / "loc-sn90050035-pass90.html"),
    ("https://digitalheritage.arkansas.gov/",
     PRESS / "adh-landing-pass90.html"),
    ("https://chroniclingamerica.loc.gov/search/pages/results/?andtext=%22Dora+Stone%22+Ola&date1=1926&date2=1926&format=json&rows=10",
     PRESS / "ca-dora-stone-ola-1926-pass90.json"),
    ("https://chroniclingamerica.loc.gov/search/pages/results/?andtext=%22Posa+Stone%22&date1=1926&date2=1926&format=json&rows=10",
     PRESS / "ca-posa-stone-1926-pass90.json"),
    ("https://archive.org/advancedsearch.php?q=%22Dora+Stone%22+1926+yell+OR+ola+OR+dardanelle&fl[]=identifier,title&output=json&rows=10",
     CAT / "ia-solr-dora-stone-1926-pass90.json"),
    ("https://www.arkansas-heritage.com/arkansas-state-archives",
     PRESS / "ar-state-archives-pass90.html"),
]


def main() -> int:
    ok = 0
    for url, dest in JOBS:
        try:
            curl(url, dest)
            ok += 1
        except Exception as e:
            print(f"ERR {dest.name}: {e}", flush=True)
        time.sleep(0.25)
    print(f"FETCHED {ok}/{len(JOBS)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
