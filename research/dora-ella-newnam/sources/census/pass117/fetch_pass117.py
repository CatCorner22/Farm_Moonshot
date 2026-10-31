#!/usr/bin/env python3
"""Pass 117: B058 one catalog reconfirm; B071 remaining N-walks."""
from __future__ import annotations

import concurrent.futures
import json
import pathlib
import ssl
import urllib.error
import urllib.request

from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps

CEN = pathlib.Path("/workspace/research/dora-ella-newnam/sources/census/pass117")
OLD = pathlib.Path("/workspace/research/dora-ella-newnam/sources/census/pass116")
CAT = pathlib.Path("/workspace/research/dora-ella-newnam/sources/catalog")
PRESS = pathlib.Path("/workspace/research/dora-ella-newnam/sources/press")
UA = "Mozilla/5.0 (compatible; genealogy-research/1.0)"
CTX = ssl._create_unverified_context()


def get(url: str, dest: pathlib.Path, timeout: int = 50) -> tuple[int, int]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            data = r.read()
        dest.write_bytes(data)
        print(f"ok {dest.name} {len(data)}", flush=True)
        return 200, len(data)
    except urllib.error.HTTPError as e:
        body = e.read() if e.fp else b""
        dest.write_bytes(body)
        print(f"http {e.code} {dest.name} {len(body)}", flush=True)
        return e.code, len(body)
    except Exception as e:
        dest.write_text(str(e))
        print(f"fail {dest.name}: {e}", flush=True)
        return 0, 0


def leaf(item: str, n: int, w: int, dest: pathlib.Path) -> bool:
    if dest.exists() and dest.stat().st_size >= 800:
        return True
    url = f"https://archive.org/download/{item}/page/leaf{n:04d}_w{w}.jpg"
    code, size = get(url, dest)
    return code == 200 and size >= 800


def enhance_crop(src: pathlib.Path, dest: pathlib.Path, box_frac: tuple[float, float, float, float]) -> None:
    im = Image.open(src).convert("L")
    w, h = im.size
    box = (int(w * box_frac[0]), int(h * box_frac[1]), int(w * box_frac[2]), int(h * box_frac[3]))
    crop = im.crop(box)
    crop = ImageOps.autocontrast(crop, cutoff=1)
    crop = ImageEnhance.Contrast(crop).enhance(1.8)
    crop = ImageEnhance.Sharpness(crop).enhance(1.4)
    dest.parent.mkdir(parents=True, exist_ok=True)
    crop.save(dest, quality=90)


def crop_namecol(src: pathlib.Path, dest: pathlib.Path, box_frac=(0.06, 0.08, 0.42, 0.96)) -> None:
    if dest.exists() and dest.stat().st_size >= 400:
        return
    try:
        enhance_crop(src, dest, box_frac)
        print(f"namecol {dest.name}", flush=True)
    except Exception as e:
        print(f"namecol-fail {src.name}: {e}", flush=True)


def crop_header(src: pathlib.Path, dest: pathlib.Path) -> None:
    if dest.exists() and dest.stat().st_size >= 400:
        return
    try:
        enhance_crop(src, dest, (0.05, 0.02, 0.95, 0.14))
        print(f"header {dest.name}", flush=True)
    except Exception as e:
        print(f"header-fail {src.name}: {e}", flush=True)


def montage(srcs: list[pathlib.Path], dest: pathlib.Path, cols: int = 6, thumb_w: int = 220) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    tiles = []
    for p in srcs:
        try:
            im = Image.open(p).convert("L")
        except Exception:
            continue
        h = int(im.height * thumb_w / max(im.width, 1))
        im = im.resize((thumb_w, max(h, 1)), Image.Resampling.LANCZOS)
        im = ImageOps.autocontrast(im, cutoff=1)
        label = Image.new("L", (thumb_w, im.height + 18), 255)
        label.paste(im, (0, 18))
        d = ImageDraw.Draw(label)
        d.text((2, 1), p.name.replace("-names.jpg", ""), fill=0)
        tiles.append(label)
    if not tiles:
        return
    rows = (len(tiles) + cols - 1) // cols
    cell_h = max(t.height for t in tiles)
    canvas = Image.new("L", (cols * thumb_w, rows * cell_h), 255)
    for i, t in enumerate(tiles):
        r, c = divmod(i, cols)
        canvas.paste(t, (c * thumb_w, r * cell_h))
    canvas.save(dest, quality=85)
    print(f"montage {dest.name} {len(tiles)}", flush=True)


def main() -> None:
    CEN.mkdir(parents=True, exist_ok=True)
    (CEN / "estill1840").mkdir(exist_ok=True)
    (CEN / "clay1840").mkdir(exist_ok=True)
    (CEN / "laurel209").mkdir(exist_ok=True)
    (CEN / "mont214").mkdir(exist_ok=True)
    (CEN / "montages").mkdir(exist_ok=True)

    # --- B058 one catalog reconfirm ---
    get("https://www.loc.gov/item/sn89051008/?fo=json", PRESS / "loc-item-sn89051008-pass117.json", timeout=40)
    get(
        "https://archive.org/advancedsearch.php?q=collection%3Aamericana+AND+(title%3A%22Dardanelle+Post%22+OR+title%3A%22Post-Dispatch%22)+AND+year%3A1926&fl[]=identifier,title,year&rows=5&output=json",
        CAT / "ia-solr-postdispatch-1926-pass117.json",
        timeout=40,
    )

    jobs: list[tuple[str, int, int, pathlib.Path]] = []

    # Estill 1840 remaining n0115–n0154 (window isolated)
    have_109 = {int(p.name[1:5]) for p in (OLD / "ky1840-109").glob("n????-w*.jpg") if p.name[1:5].isdigit()}
    for n in range(115, 155):
        dest = CEN / "estill1840" / f"n{n:04d}-w1100.jpg"
        if n not in have_109 and not (dest.exists() and dest.stat().st_size >= 800):
            jobs.append(("populationsc18400109unit", n, 1100, dest))

    # Clay 1840 remaining NAME pages = odd leaves after n0099
    have_108 = {int(p.name[1:5]) for p in (OLD / "ky1840-108").glob("n????-w*.jpg") if p.name[1:5].isdigit()}
    for n in range(101, 180, 2):
        dest = CEN / "clay1840" / f"n{n:04d}-w1100.jpg"
        if n not in have_108 and not (dest.exists() and dest.stat().st_size >= 800):
            jobs.append(("populationsc18400108unit", n, 1100, dest))

    # Laurel isolate end (n0381 Laurel; n0395 Lawrence)
    for n in [384, 386, 388, 390, 392, 394, 396, 400, 410]:
        dest = CEN / "laurel209" / f"n{n:04d}-w1000.jpg"
        old = list((OLD / "laurel209").glob(f"n{n:04d}-w*.jpg"))
        if old:
            continue
        jobs.append(("populationschedu0209unix", n, 1000, dest))

    # Montgomery isolate end (n0140 still Dist 2)
    for n in [145, 150, 155, 160, 165, 170, 175, 180, 190, 200, 220]:
        dest = CEN / "mont214" / f"n{n:04d}-w1000.jpg"
        old = list((OLD / "mont214").glob(f"n{n:04d}-w*.jpg"))
        if old:
            continue
        jobs.append(("populationschedu0214unix", n, 1000, dest))

    def one(args):
        item, n, w, dest = args
        return n, leaf(item, n, w, dest), dest.name

    print(f"jobs {len(jobs)}", flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for n, ok, name in ex.map(one, jobs):
            if not ok:
                print(f"miss {name}", flush=True)

    # header crops for isolation samples
    for folder, item_glob in [
        (CEN / "laurel209", "n????-w*.jpg"),
        (CEN / "mont214", "n????-w*.jpg"),
        (CEN / "estill1840", "n????-w*.jpg"),
        (CEN / "clay1840", "n????-w*.jpg"),
    ]:
        for src in sorted(folder.glob(item_glob)):
            crop_header(src, folder / "headers" / src.name.replace("-w1100.jpg", "-hdr.jpg").replace("-w1000.jpg", "-hdr.jpg"))

    # 1840 name-column crops (Estill evens = names; Clay odds = names)
    for src in sorted((CEN / "estill1840").glob("n????-w*.jpg")):
        n = int(src.name[1:5])
        crop_namecol(src, CEN / "estill1840" / "namecols" / f"n{n:04d}-names.jpg", (0.04, 0.10, 0.28, 0.94))
    for src in sorted((OLD / "ky1840-109").glob("n????-w*.jpg")):
        n = int(src.name[1:5])
        if 90 <= n <= 155:
            dest = CEN / "estill1840" / "namecols" / f"n{n:04d}-names.jpg"
            crop_namecol(src, dest, (0.04, 0.10, 0.28, 0.94))

    for src in sorted((CEN / "clay1840").glob("n????-w*.jpg")):
        n = int(src.name[1:5])
        crop_namecol(src, CEN / "clay1840" / "namecols" / f"n{n:04d}-names.jpg", (0.04, 0.10, 0.28, 0.94))
    for src in sorted((OLD / "ky1840-108").glob("n????-w*.jpg")):
        n = int(src.name[1:5])
        if 91 <= n <= 179 and n % 2 == 1:
            dest = CEN / "clay1840" / "namecols" / f"n{n:04d}-names.jpg"
            crop_namecol(src, dest, (0.04, 0.10, 0.28, 0.94))

    # reuse existing Laurel/Mont namecols into montages
    laurel_cols = sorted((OLD / "laurel209" / "namecols").glob("n????-names.jpg"))
    mont_cols = sorted((OLD / "mont214" / "namecols").glob("n????-names.jpg"))
    for i in range(0, len(laurel_cols), 12):
        montage(laurel_cols[i : i + 12], CEN / "montages" / f"laurel-names-{laurel_cols[i].name[1:5]}.jpg", cols=6, thumb_w=200)
    for i in range(0, len(mont_cols), 12):
        montage(mont_cols[i : i + 12], CEN / "montages" / f"mont-names-{mont_cols[i].name[1:5]}.jpg", cols=6, thumb_w=200)

    estill_cols = sorted((CEN / "estill1840" / "namecols").glob("n????-names.jpg"))
    clay_cols = sorted((CEN / "clay1840" / "namecols").glob("n????-names.jpg"))
    for i in range(0, len(estill_cols), 10):
        montage(estill_cols[i : i + 10], CEN / "montages" / f"estill1840-names-{estill_cols[i].name[1:5]}.jpg", cols=5, thumb_w=240)
    for i in range(0, len(clay_cols), 10):
        montage(clay_cols[i : i + 10], CEN / "montages" / f"clay1840-names-{clay_cols[i].name[1:5]}.jpg", cols=5, thumb_w=240)

    # residual catalogs (free only; phones not re-asked)
    catalogs = [
        ("https://kykinfolk.com/estill/marriages/grooms-to1850.htm", CEN / "estill-grooms-to1850-pass117.html"),
        ("https://kykinfolk.com/estill/marriages/brides-to1850.htm", CEN / "estill-brides-to1850-pass117.html"),
        ("https://kykinfolk.com/estill/marriages/grooms-n.htm", CEN / "estill-grooms-n-pass117.html"),
        ("https://www.usgenwebsites.org/KYEstill/marriages/grooms-to1850.htm", CEN / "usgw-estill-grooms-pass117.html"),
        ("https://www.usgenwebsites.org/KYEstill/census/1840.htm", CEN / "usgw-estill-1840-pass117.html"),
        ("https://www.skcensus.com/1850-census-index-laurel-county-kentucky/", CEN / "sk-laurel-1850-pass117.html"),
        ("https://www.skcensus.com/1850-census-index-montgomery-county-kentucky/", CEN / "sk-mont-1850-pass117.html"),
        ("https://www.skcensus.com/1840-census-index-estill-county-kentucky/", CEN / "sk-estill-1840-pass117.html"),
        ("https://www.skcensus.com/1840-census-index-clay-county-kentucky/", CEN / "sk-clay-1840-pass117.html"),
        ("https://kykinfolk.com/owsley/marriages.htm", CAT / "kykinfolk-owsley-marr-pass117.html"),
        ("https://libraryguides.berea.edu/faq/9938", CAT / "hutchins-faq-9938-pass117.html"),
        ("https://www.familysearch.org/search/catalog/1146342", CAT / "fs-1146342-pass117.html"),
        ("https://www.familysearch.org/search/catalog/127913", CAT / "fs-127913-pass117.html"),
        ("https://usgennet.org/usa/ky/county/lee/wills/", CAT / "usgennet-lee-wills-pass117.html"),
        ("https://archive.org/metadata/14thcensusofpopu602unit", CAT / "ia-602-meta-pass117.json"),
        ("https://archive.org/advancedsearch.php?q=collection%3Awwi_draft+AND+subject%3AKentucky&fl[]=identifier,title&rows=5&output=json", CAT / "ia-solr-m1509-ky-pass117.json"),
        ("https://www.genealogytrails.com/ken/lee/wwi_draft_cards.html", CAT / "gt-lee-wwi-pass117.html"),
    ]
    for url, dest in catalogs:
        get(url, dest, timeout=40)

    # LOC digitized flag extract
    loc = PRESS / "loc-item-sn89051008-pass117.json"
    try:
        d = json.loads(loc.read_text())
        item = d.get("item") or d
        print("LOC digitized", item.get("digitized") or d.get("digitized"), flush=True)
        print("LOC title", (item.get("title") or "")[:80], flush=True)
    except Exception as e:
        print("LOC parse fail", e, flush=True)

    solr = CAT / "ia-solr-postdispatch-1926-pass117.json"
    try:
        s = json.loads(solr.read_text())
        print("Solr 1926 numFound", (s.get("response") or {}).get("numFound"), flush=True)
    except Exception as e:
        print("Solr parse fail", e, flush=True)


if __name__ == "__main__":
    main()
