#!/usr/bin/env python3
"""Pass 95: Antioch/Clifty catalog hunt + Estill 33-8 reel 743 + other-pass sources."""
from __future__ import annotations

import subprocess
import time
from pathlib import Path

ROOT = Path("/workspace/research/dora-ella-newnam/sources")
OUT = ROOT / "census/pass95"
CAT = ROOT / "catalog"
VIT = ROOT / "vital"
PRESS = ROOT / "press"
MIL = ROOT / "military"
OUT.mkdir(parents=True, exist_ok=True)
CAT.mkdir(parents=True, exist_ok=True)
VIT.mkdir(parents=True, exist_ok=True)
PRESS.mkdir(parents=True, exist_ok=True)
MIL.mkdir(parents=True, exist_ok=True)

UA = "Mozilla/5.0 (compatible; genealogy-research/1.0; +https://archive.org)"


def curl(url: str, dest: Path, min_size: int = 80) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        ["curl", "-sS", "-L", "-A", UA, "--retry", "2", "--retry-delay", "1",
         "--max-time", "50", "-o", str(dest), "-w", "%{http_code}", url],
        capture_output=True, text=True,
    )
    code = (r.stdout or "").strip()
    size = dest.stat().st_size if dest.exists() else 0
    ok = r.returncode == 0 and size >= min_size and code.startswith("2")
    print(f"{'OK' if ok else 'FAIL'} {dest.name} HTTP {code} size={size}", flush=True)
    if not ok and dest.exists() and size < min_size:
        dest.unlink(missing_ok=True)
    return ok


def ia_leaf(item: str, leaf: int, width: int, dest: Path) -> bool:
    url = f"https://archive.org/download/{item}/page/leaf{leaf:04d}_w{width}.jpg"
    return curl(url, dest, min_size=8000)


def main() -> int:
    # B089: confirm reel 743 is Fayette, not missing Estill 33-8
    for leaf in (1, 2, 3, 4, 5, 10, 20, 50):
        ia_leaf("kentuckycensus00reel743", leaf, 1200,
                OUT / f"t626-743-leaf{leaf:04d}-w1200.jpg")
        time.sleep(0.15)

    jobs = [
        # B088 / B089 catalogs
        (CAT / "ahgp-ky-census-images-pass95.html",
         "https://ahgp.org/ky/free-kentucky-census-images.html"),
        (CAT / "uscensus-estill-1930-pass95.html",
         "https://www.us-census.org/states/kentucky/teams/Estill1930-T626-742.htm"),
        (CAT / "uscensus-estill-1930-partial-pass95.txt",
         "https://www.us-census.org/pub/usgenweb/census/ky/estill/1930/_partial.txt"),
        (CAT / "ia-meta-t625-603-pass95.json",
         "https://archive.org/metadata/14thcensusofpopu603unit"),
        (CAT / "ia-meta-t626-743-pass95.json",
         "https://archive.org/metadata/kentuckycensus00reel743"),
        (CAT / "ia-meta-t625-602-pass95.json",
         "https://archive.org/metadata/14thcensusofpopu602unit"),
        (CAT / "lds-wolfe-census-pass95.html",
         "https://ldsgenealogy.com/KY/Wolfe-County-Census-Records.htm"),
        (CAT / "lds-estill-census-pass95.html",
         "https://ldsgenealogy.com/KY/Estill-County-Census-Records.htm"),
        (CAT / "fs-127913-pass95.html",
         "https://www.familysearch.org/search/catalog/127913"),
        (CAT / "fs-127869-pass95.html",
         "https://www.familysearch.org/search/catalog/127869"),
        (CAT / "fs-1146342-pass95.html",
         "https://www.familysearch.org/search/catalog/1146342"),
        # B045 / B061 probate substitutes
        (CAT / "usgennet-lee-wills-pass95.html",
         "https://www.usgennet.org/usa/ky/county/lee/wills/wills.html"),
        (CAT / "usgennet-lee-court-pass95.html",
         "https://www.usgennet.org/usa/ky/county/lee/court/court.html"),
        (CAT / "ia-solr-lee-will-pass95.json",
         "https://archive.org/advancedsearch.php?q=%28%22samuel+p%22+OR+newnam+OR+newman%29+AND+%28will+OR+probate%29+AND+%28%22lee+county%22+OR+beattyville%29+AND+kentucky&fl[]=identifier&fl[]=title&fl[]=year&output=json&rows=20"),
        (CAT / "courtlistener-newnam-pass95.json",
         "https://www.courtlistener.com/api/rest/v3/search/?q=Newnam%20OR%20Newman&type=o&court=kyctapp&stat_Precedential=on"),
        # B069 / B047 WWI
        (MIL / "nara-m1509-wwi-pass95.html",
         "https://www.archives.gov/research/military/ww1/draft-registration"),
        (MIL / "gt-lee-wwi-n-pass95.html",
         "https://genealogytrails.com/ken/lee/wwi_draft_cards.html"),
        (CAT / "ia-solr-m1509-pass95.json",
         "https://archive.org/advancedsearch.php?q=M1509+AND+%28Kentucky+OR+Lee+OR+Owsley%29+AND+%28draft+OR+registration%29&fl[]=identifier&fl[]=title&output=json&rows=15"),
        # B082 Woodford
        (CAT / "kygenweb-woodford-obits-pass95.html",
         "https://kygenweb.net/woodford/obits.html"),
        (CAT / "ldsgenealogy-woodford-deaths-pass95.html",
         "https://ldsgenealogy.com/KY/Woodford-County-Death-Records.htm"),
        (CAT / "ia-solr-duell-clark-pass95.json",
         "https://archive.org/advancedsearch.php?q=%28duell+OR+%22duell-clark%22+OR+%22duell+clark%22%29+AND+%28woodford+OR+versailles+OR+funeral%29&fl[]=identifier&fl[]=title&output=json&rows=15"),
        # B016 Rissie
        (VIT / "rootsweb-ssdi-rissie-pass95.html",
         "https://ssdi.rootsweb.com/cgi-bin/ssdi.cgi?lastname=Pelfrey&firstname=Rissie"),
        (VIT / "sortedbyname-rissie-pass95.html",
         "https://sortedbyname.com/letter_p/pelfrey/rissie.html"),
        (VIT / "wikitree-newnam-46-pass95.html",
         "https://www.wikitree.com/wiki/Newnam-46"),
        # B049 / B058 1926 papers
        (PRESS / "ca-dora-stone-1926-pass95.json",
         "https://chroniclingamerica.loc.gov/search/pages/results/?state=&date1=1926&date2=1926&proxtext=Dora+Stone&x=0&y=0&dateFilterType=yearRange&rows=20&searchType=basic&format=json"),
        (PRESS / "ca-posa-stone-1926-pass95.json",
         "https://chroniclingamerica.loc.gov/search/pages/results/?state=Arkansas&date1=1926&date2=1926&proxtext=Posa+Stone&dateFilterType=yearRange&rows=10&searchType=basic&format=json"),
        (PRESS / "ca-newnam-ola-1926-pass95.json",
         "https://chroniclingamerica.loc.gov/search/pages/results/?state=Arkansas&date1=1926&date2=1926&proxtext=Newnam+Ola&dateFilterType=yearRange&rows=10&searchType=basic&format=json"),
        # B055 / B080 Madison / Berea Citizen
        (PRESS / "ca-citizen-newman-1958-pass95.json",
         "https://chroniclingamerica.loc.gov/search/pages/results/?lccn=sn85052076&date1=1958&date2=1958&proxtext=Newman&dateFilterType=yearRange&rows=20&searchType=basic&format=json"),
        (PRESS / "ca-citizen-newnam-1958-pass95.json",
         "https://chroniclingamerica.loc.gov/search/pages/results/?lccn=sn85052076&date1=1958&date2=1958&proxtext=Newnam&dateFilterType=yearRange&rows=10&searchType=basic&format=json"),
        (PRESS / "ca-citizen-frank-newman-pass95.json",
         "https://chroniclingamerica.loc.gov/search/pages/results/?lccn=sn85052076&date1=1939&date2=1958&proxtext=Frank+Newman&dateFilterType=yearRange&rows=15&searchType=basic&format=json"),
        (CAT / "lds-madison-obits-pass95.html",
         "https://ldsgenealogy.com/KY/Madison-County-Newspapers-and-Obituaries.htm"),
        (CAT / "berea-archives-citizen-pass95.html",
         "https://bereaarchives.libraryhost.com/repositories/2/resources/128"),
    ]
    for dest, url in jobs:
        curl(url, dest, min_size=60)
        time.sleep(0.2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
