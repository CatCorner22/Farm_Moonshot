"""Chronological catalog of every preserved JPEG in the Dora Ella Newnam case.

Plate numbers are assigned by the date of the record (census night or index year),
not by the date the microfilm was scanned. Roles:

  family     — names Dora or a documented relative
  rejected   — a same-name person who fails the same-person test
  negative   — the alphabetical or dwelling slot where she would appear; she is not there
  context    — adjacent page or finding-aid divider, kept so the search can be verified
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "research" / "dora-ella-newnam" / "sources"

PLATES: list[dict] = [
    # --- 1870 ---
    dict(
        n=1, date="29 Jun 1870", year=1870, role="context",
        path="census/1870-lee-ky-sturgeon-p337a-context.jpg",
        title="Sturgeon Precinct, page 3 (stamped 337)",
        caption="Lee County, Kentucky, had been a county for one year. Enumerator Chas. D. Tyler took this sheet on 29 June 1870. Households Young, Kelly, Flanery, Horn and Bryant (dwelling 18) sit immediately before John Newman’s house on the next page.",
        source="S042",
    ),
    dict(
        n=2, date="29 Jun 1870", year=1870, role="family",
        path="census/1870-lee-ky-sturgeon-p337b-john-elizabeth-samuel.jpg",
        title="John, Elizabeth, and infant Samuel Newman",
        caption="Dwelling 19/19: Newman, John, 50, farm labourer; Elizabeth, 25, keeping house; and Samuel, aged 1, with eight others. This is the probable natal home of Dora’s later husband. Elizabeth, 25, cannot be the mother of Mary, 21 — the older girls belong to a prior wife or another relationship the schedule does not name. Not silently merged with the 1880 John-and-Mary house (conflict #9).",
        source="S042 · C062",
    ),
    # --- 1880 schedules ---
    dict(
        n=3, date="1 Jun 1880", year=1880, role="family",
        path="census/1880-lee-ky-ed59-sheet1-p725-john-samuel.jpg",
        title="John and Mary Newnam; Samuel, aged 11",
        caption="Lee County ED 59, dwelling 3: John Newnam, 69, farmer (father born North Carolina); Mary, 57; Eli, 16; Susan, 20; Samuel, 11; Hannah, 9. Age 11 in June 1880 matches the June 1869 birth of Dora’s husband and the sixteen-year-old of the 1885 marriage return. Identification remains probable pending conflict #9.",
        source="S040 · C060 · C061",
    ),
    dict(
        n=4, date="1 Jun 1880", year=1880, role="rejected",
        path="census/1880-lee-ky-ed59-sheet2-p726-mcqueary-samuel.jpg",
        title="Samuel McQueary, 13 — not a Newnam",
        caption="Continuation of dwelling 11, the McQueary household. Samuel, 13, is Samuel McQueary. The only Samuel Newnam in ED 59 is the eleven-year-old in Plate 3.",
        source="S044 · C063",
    ),
    dict(
        n=5, date="5 Jun 1880", year=1880, role="family",
        path="census/1880-lee-ky-ed59-sheet6-p730-elias-dora.jpg",
        title="Elias and Mary Newnam; Dora, aged 8",
        caption="The childhood record. Dwelling 46: Elias Newnam, 38, farmer; Mary, 38; William, 21; Malissa, 16; Francis, 14; Mary, 10; Dora, 8; Catharine, 6. A child of eight on 5 June 1880 was born in 1871 or early 1872. The death certificate’s year 1868 cannot stand. Neighbors: Joseph Newnam, 38, and John Newnam, 60.",
        source="S010 · C001 · C003 · C004",
    ),
    # --- 1880 Soundex ---
    dict(
        n=6, date="1880 (index)", year=1880, role="family",
        path="soundex/ky1880-n550-p2105-elias-newnam.jpg",
        title="Soundex card — Elias Newnam household",
        caption="NARA T750, code N-550. Family card for Newnam, Elias, 38, Lee County, vol. 18, ED 59, sheet 6, line 11. Lists Mary, William, Melissa (schedule: Malissa), Francis, and Mary. Footer “#1 see #2”.",
        source="S001",
    ),
    dict(
        n=7, date="1880 (index)", year=1880, role="family",
        path="soundex/ky1880-n550-p2106-elias-continuation-dora.jpg",
        title="Soundex continuation — Dora and Catharine",
        caption="Continuation card: Newnam, Dora, daughter, 8, Kentucky; Catharine, daughter, 6. This is the index confirmation of Plate 5.",
        source="S002",
    ),
    # --- 1900 Missouri Stone search ---
    dict(
        n=8, date="13 Jun 1900", year=1900, role="rejected",
        path="census/1900-douglas-mo-ed159-stone-sheet.jpg",
        title="Douglas County, Missouri — Thomas and Nancy E. Stone",
        caption="Buchanan Township, ED 159, sheet 9B. Thomas Stone, woodchopper, born May 1856, age 44, with wife Nancy E. and five daughters. Closest-age 1900 Missouri Thomas to the 1920 Arkansas widower Tom A. Stone — still not merged (no middle initial; wife living; conflict #11).",
        source="S085 · C101",
    ),
    dict(
        n=9, date="13 Jun 1900", year=1900, role="rejected",
        path="census/1900-douglas-mo-ed159-stone-hh-crop.jpg",
        title="Douglas County Stone household (crop)",
        caption="Crop of the Thomas and Nancy E. Stone lines. The Soundex clerk later wrote “Jesse C., son”; the original reads Ossie P., daughter.",
        source="S085 · C102",
    ),
    dict(
        n=10, date="1900 (index)", year=1900, role="rejected",
        path="soundex/mo1900-s350-p1678-stone-thomas-44-douglas.jpg",
        title="Missouri S-350 — Thomas Stone, 44, Douglas County",
        caption="Soundex card for the household in Plates 8–9. Finding aid only; the original schedule is the authority.",
        source="S085 · C092",
    ),
    dict(
        n=11, date="1900 (index)", year=1900, role="rejected",
        path="soundex/mo1900-s350-p1679-stone-thomas-douglas-jesse.jpg",
        title="Missouri S-350 — Douglas continuation, “Jesse C.”",
        caption="Clerk error: “Jesse C., son” is Ossie P., daughter, on the original (Plate 9). Not a son of Tom A. of Perry County.",
        source="S085 · C102",
    ),
    dict(
        n=12, date="1900 (index)", year=1900, role="rejected",
        path="soundex/mo1900-s350-p1680-stone-thomas-50-caldwell.jpg",
        title="Missouri S-350 — Thomas Stone, 50, Caldwell County",
        caption="Wrong county, wrong age trajectory versus 1920 Tom A. of Perry County, Arkansas. Rejected.",
        source="S085 · C092",
    ),
    dict(
        n=13, date="1900 (index)", year=1900, role="rejected",
        path="soundex/mo1900-s350-p1684-stone-thomas-a-32-dunklin.jpg",
        title="Missouri S-350 — Thomas A. Stone, 32, Dunklin County",
        caption="Has the middle initial A. Age 32 (born February 1868) with wife Matilda. Too young for the 1920 sixty-two-year-old. Not merged.",
        source="S085 · C092",
    ),
    dict(
        n=14, date="1900 (index)", year=1900, role="rejected",
        path="soundex/mo1900-s350-p1685-stone-thomas-a-24-cooper.jpg",
        title="Missouri S-350 — Thomas A. Stone, 24, Cooper County",
        caption="Nephew, born March 1876. Fails age. Not merged.",
        source="S085 · C092",
    ),
    dict(
        n=15, date="1900 (index)", year=1900, role="rejected",
        path="soundex/mo1900-s350-p1727-stone-tom-black-21.jpg",
        title="Missouri S-350 — Tom Stone, 21, Black",
        caption="Fails race, age, and household. Not Tom A. of 1920 Arkansas.",
        source="S085 · C092",
    ),
    dict(
        n=16, date="1900 (index)", year=1900, role="rejected",
        path="soundex/mo1900-s350-p1728-stone-tom-31-vernon.jpg",
        title="Missouri S-350 — Tom Stone, 31, Vernon County",
        caption="Coal-miner boarder, born May 1869. No wife, no daughters matching 1920. Not merged.",
        source="S085 · C092",
    ),
    dict(
        n=62, date="Jun 1900", year=1900, role="negative",
        path="census/1900-bollinger-liberty-ed4-sh5a-hdr.jpg",
        title="Bollinger Liberty ED 4 sheet 5 A header",
        caption="Supervisor 12, ED 4, sheet 5 A, enumerator James R. Hughey. First sheet after the pass-54 close of sheets 1–4. The name column has Null, Baker, Davis, Crites — no Conrad, Sullivan, or Newman.",
        source="S271 · C290",
    ),
    dict(
        n=63, date="Jun 1900", year=1900, role="negative",
        path="census/1900-bollinger-liberty-ed4-sh7b-names-bot.jpg",
        title="Bollinger Liberty ED 4 sheet 7 B names (ED tail)",
        caption="Last sheet of Liberty ED 4. Myers, Day, Huffstetter, Baker, Crites, Barret. Child Dorse E. Baker (November 1898, age 1) is not P001. The next PDF page is ED 5 sheet 1 A.",
        source="S271 · C290 · C294",
    ),
    dict(
        n=64, date="1900 (index)", year=1900, role="context",
        path="soundex/mo1900-c563-p2985-jacob-lorance.jpg",
        title="Missouri C-563 — Jacob Conrad of Lorance",
        caption="Inverted Soundex card. Conrad, Jacob I, Bollinger Lorance, born December 1835, age 64. Local FAN of the 1910 Liberty Jesse Conrad household. Other members Maud 22 and a child 19 — no Jesse, no infant Letha.",
        source="S272 · C292",
    ),
    dict(
        n=65, date="1900 (index)", year=1900, role="negative",
        path="soundex/mo1900-c563-p2998-john-after-jib-no-jesse.jpg",
        title="Missouri C-563 — John after Jib; no Jesse",
        caption="The Conrad given-name run jumps from Jib (p.2997) to John (p.2998). No Jesse, Jessie, or Jess head card in 1900 Missouri Soundex C-563.",
        source="S272 · C291",
    ),
    dict(
        n=66, date="1900 (index)", year=1900, role="rejected",
        path="soundex/mo1900-n550-p406-bella-stlouis-rejected.jpg",
        title="Missouri N-550 — Bella, 25, St Louis",
        caption="Individual card. Newman, Bella, about 1874, age 25, St Louis, Laclede Avenue 3751. Not the 1910 Liberty widow (age and city fail).",
        source="S273 · C293",
    ),
    dict(
        n=67, date="1900 (index)", year=1900, role="rejected",
        path="soundex/mo1900-n550-p407-belle-kc-rejected.jpg",
        title="Missouri N-550 — Belle, 29, Virginia, Kansas City",
        caption="Individual card. Newman, Belle, February 1871, age 29, born Virginia, Jackson County, Kansas City, Broadway 1021. Not the 1910 Liberty widow (birthplace and city fail).",
        source="S273 · C293",
    ),
    dict(
        n=68, date="23 Jun 1900", year=1900, role="context",
        path="census/1900-bollinger-lorance-ed6-sh14a-hdr.jpg",
        title="Bollinger Lorance ED 6 sheet 14 A header",
        caption="Supervisor 12, ED 6, sheet 14 A, stamped 74-01, enumerator Thomas H. Stevens, 23 June 1900. This is the sheet the Soundex clerk mis-cited as sheet 17.",
        source="S274 · C297",
    ),
    dict(
        n=69, date="23 Jun 1900", year=1900, role="context",
        path="census/1900-bollinger-lorance-ed6-sh14a-jacob-conrad.jpg",
        title="Jacob I Conrad household — Lorance ED 6 sheet 14 A",
        caption="Dwelling 265/266. Conrad, Jacob I, December 1835, age 64, married 39 years; daughter Maud, April 1878, 21; son Buen, October 1880, 19. No wife on the lines. No Jesse. No Letha. Local FAN of the 1910 Liberty Jesse Conrad house — not merged.",
        source="S274 · C296 · C292",
    ),
    dict(
        n=70, date="Jun 1900", year=1900, role="negative",
        path="census/1900-bollinger-liberty-ed5-sh15a-hdr.jpg",
        title="Bollinger Liberty ED 5 sheet 15 A header",
        caption="Supervisor 12, ED 5, sheet 15 A, enumerator DeKalb Westenhaver. First of the two sheets past the pass-58 close of sheets 1–14. Combined with those, Liberty ED 5 is complete — no Conrad, Sullivan, or Newman target.",
        source="S275 · C298",
    ),
    dict(
        n=71, date="Jun 1900", year=1900, role="context",
        path="census/1900-bollinger-lorance-ed6-sh1b-george-conrad.jpg",
        title="George E Conrad household — Lorance ED 6 sheet 1 B",
        caption="Household 16. Conrad, Geo E, March 1852, age 48, married 7 years; wife Flora A, March 1874, 26, 3/3. The three children were born 1894–1897. No Jesse. No Letha. Another local FAN — not merged.",
        source="S275 · C301",
    ),
    dict(
        n=72, date="1910 (index)", year=1910, role="negative",
        path="soundex/mo1910-c563-p140-jesse-window-no-liberty.jpg",
        title="Missouri C-563 — Jesse window; no Liberty card",
        caption="Typed Miracode. Jesse/Jessie heads are Pike Jessica 44, Buchanan Jesse 36 with Faerl, and Buchanan Jno 35 living alone. None is the Liberty Jesse 37 + Letha 12 household already read on the original.",
        source="S276 · C302",
    ),
    dict(
        n=73, date="1910 (index)", year=1910, role="context",
        path="soundex/mo1910-c563-p120-francis-m-bollinger.jpg",
        title="Missouri C-563 — Francis M Conrad of Bollinger",
        caption="Typed Miracode. Conrad, Francis M, Bollinger, age 68, with John R in the household. Local FAN of the Liberty Jesse house — not merged.",
        source="S276 · C303",
    ),
    dict(
        n=74, date="1900 (index)", year=1900, role="rejected",
        path="soundex/mo1900-c563-p2897-francis-e-whitewater.jpg",
        title="Missouri C-563 — Francis E Conrad of Whitewater",
        caption="Inverted Soundex card. Conrad, Francis E, Bollinger Whitewater, September 1868, age 32, with toddlers Willie (1897) and Iva (1898). Not Jesse Conrad.",
        source="S277 · C306",
    ),
    dict(
        n=75, date="1900 (index)", year=1900, role="context",
        path="soundex/mo1900-c563-p2898-francis-m-whitewater.jpg",
        title="Missouri C-563 — Francis M Conrad of Whitewater (elder)",
        caption="Inverted Soundex card. Conrad, Francis M, July 1841, age 58, Whitewater ED 10 sheet 8. Member list (W.I., Nella) is a clerk approximation — prefer the original on Plate 80.",
        source="S277 · C305 · C312",
    ),
    dict(
        n=76, date="1900 (index)", year=1900, role="rejected",
        path="soundex/mo1900-c563-p2899-francis-m-younger-whitewater.jpg",
        title="Missouri C-563 — Francis M Conrad of Whitewater (younger)",
        caption="Inverted Soundex card. Conrad, Francis M, March 1871, age 29, wife Mary C, April 1876, 24. Not Jesse. The card’s sheet 8 line 5 locator fails on the original.",
        source="S277 · C307 · C314",
    ),
    dict(
        n=77, date="1900 (index)", year=1900, role="context",
        path="soundex/mo1900-c563-p2936-george-e-lorance.jpg",
        title="Missouri C-563 — George E Conrad of Lorance",
        caption="Inverted Soundex card. Conrad, Geo. E, March 1852, age 48, Lorance Marble Hill, ED 6 sheet 1. Matches the original on Plate 71.",
        source="S277 · C308 · C301",
    ),
    dict(
        n=78, date="Jun 1900", year=1900, role="negative",
        path="census/1900-bollinger-lutesville-ed7-sh1a-hdr.jpg",
        title="Bollinger Lutesville ED 7 sheet 1 A header",
        caption="Supervisor 12, ED 7, sheet 1 A, Lutesville Village, stamped 260. First of seventeen sheets. Combined with sheets 1–17 B, Lutesville is complete — no Conrad, Sullivan, or Newman target.",
        source="S278 · C309",
    ),
    dict(
        n=79, date="Jun 1900", year=1900, role="context",
        path="census/1900-bollinger-whitewater-ed10-sh8a-hdr.jpg",
        title="Bollinger Whitewater ED 10 sheet 8 A header",
        caption="Supervisor 13, ED 10, sheet 8 A, Whitewater Township, stamped 319. The sheet the Soundex clerk cited for Francis M elder.",
        source="S279 · C311",
    ),
    dict(
        n=80, date="Jun 1900", year=1900, role="context",
        path="census/1900-bollinger-whitewater-ed10-sh8a-francis-m.jpg",
        title="Francis M Conrad household — Whitewater ED 10 sheet 8 A",
        caption="Dwelling 136/140. Conrad, Francis M, July 1841, age 58, married 39 years; wife Sophia B, 3 children / 2 living; son Recie, 20; boarder Sarah E. Seales, 8; son John R, 26, married, with a daughter-in-law. No Jesse. No Letha. Sophia’s 3/2 means Jesse is not a living child of this couple. Same man as the 1910 Francis M, 68, on Plate 73.",
        source="S279 · C311 · C315 · C313",
    ),
    # --- 1910 Soundex / Miracode ---
    dict(
        n=17, date="Apr 1910", year=1910, role="negative",
        path="soundex/ky1910-n550-p329-millie-missouri.jpg",
        title="Kentucky N-550 — Millie / Missouri; no McCoy",
        caption="Typed Miracode page for Kentucky Newman/Newnam. Alphabetically this is the slot immediately before Monroe, where a McCoy card would sit. None is printed. Dora’s son is not indexed in Kentucky that April.",
        source="S021 · C031",
    ),
    dict(
        n=18, date="Apr 1910", year=1910, role="negative",
        path="soundex/ky1910-n550-p330-monroe-no-mccoy.jpg",
        title="Kentucky N-550 — Monroe; still no McCoy",
        caption="The next printed page, beginning Monroe. Combined with Plate 17, Kentucky has no McCoy Newman/Newnam in 1910.",
        source="S021 · C031",
    ),
    dict(
        n=19, date="Apr 1910", year=1910, role="rejected",
        path="soundex/ky1910-n550-p342-sam-samuel-not-p002.jpg",
        title="Kentucky N-550 — Sam / Samuel, none is the husband",
        caption="Sam, 74, of Knox; Samuel of Newport; a Black Samuel Noonan; a Louisville Samuel, 31; Samuel C. of Butler. None is Samuel P. Newnam of Lee County with Dora’s children.",
        source="S027 · C039",
    ),
    dict(
        n=20, date="Apr 1910", year=1910, role="rejected",
        path="soundex/ky1910-n550-p343-samuel-e-muhlenberg-not-p002.jpg",
        title="Kentucky N-550 — Samuel E. of Muhlenberg",
        caption="Samuel E., 41, with Lou E. and children Bertha, Luea, Joseph, Mary, Minnie. Wrong county, wrong wife, wrong children. Closes the Kentucky-head search for Dora’s first husband in April 1910.",
        source="S027 · C039",
    ),
    dict(
        n=21, date="Apr 1910", year=1910, role="rejected",
        path="soundex/ky1910-s350-p149-dora-servant-louisville.jpg",
        title="Kentucky S-350 — Dora Stone, servant, Louisville",
        caption="STONE, DORA, servant, Black, 36, Louisville, with J. Frank Taylor. Fails race, age, occupation, and household. Dora Newnam was not indexed as Dora Stone in Kentucky that April.",
        source="S026 · C038",
    ),
    dict(
        n=22, date="Apr 1910", year=1910, role="rejected",
        path="soundex/ky1910-s350-p150-dora-18-wolfe.jpg",
        title="Kentucky S-350 — Dora Stone, 18, Wolfe County",
        caption="STONE, DORA, daughter-in-law, 18, Wolfe County, with Lucindy Stone. Age 18 versus about 39. The two Kentucky Dora Stones of 1910 are both the wrong women.",
        source="S026 · C038",
    ),
    dict(
        n=23, date="Apr 1910", year=1910, role="negative",
        path="soundex/ar1910-n550-p678-cora-dan-no-coy.jpg",
        title="Arkansas N-550 — Cora / Dan; no Coy",
        caption="No Coy between Cora and Dan. Dora’s son is not indexed in Arkansas as a Newman head in April 1910.",
        source="S022 · C032",
    ),
    dict(
        n=24, date="Apr 1910", year=1910, role="negative",
        path="soundex/ar1910-n550-p679-dan-e-no-dora.jpg",
        title="Arkansas N-550 — Dan E.; no Dora",
        caption="After Dan the cards run Daneil W., David R., Dut H., then the E-names. No Dora, no Ella.",
        source="S022 · C032",
    ),
    dict(
        n=25, date="Apr 1910", year=1910, role="negative",
        path="soundex/ar1910-n550-p701-mary-mayme.jpg",
        title="Arkansas N-550 — Mary / Mayme",
        caption="Mary through Mayme Newman cards. The McCoy window is the next plate.",
        source="S022 · C032",
    ),
    dict(
        n=26, date="Apr 1910", year=1910, role="negative",
        path="soundex/ar1910-n550-p702-melvina-no-mccoy.jpg",
        title="Arkansas N-550 — Melvina; no McCoy",
        caption="After Mayme comes Melvina. No McCoy. Arkansas is closed for Newman Dora ~39 and McCoy in April 1910.",
        source="S022 · C032",
    ),
    dict(
        n=27, date="Apr 1910", year=1910, role="negative",
        path="soundex/mo1910-n550-p710-cyrus-daisy-no-coy.jpg",
        title="Missouri N-550 — Cyrus / Daisy; no Coy",
        caption="No Coy between Cyrus and Daisy. The Sullivan-Missouri hypothesis fails for this surname in 1910.",
        source="S023 · C034",
    ),
    dict(
        n=28, date="Apr 1910", year=1910, role="rejected",
        path="soundex/mo1910-n550-p714-dollie-dora-l-neimann.jpg",
        title="Missouri N-550 — Dora L. Neimann of St. Louis",
        caption="The only Dora in the Missouri Newman block: Dora L. Neimann, 48, Illinois-born, mother-in-law of Arthur E. Felsh in St. Louis. Wrong age, birthplace, household. Not Dora Ella.",
        source="S023 · C035",
    ),
    dict(
        n=29, date="Apr 1910", year=1910, role="negative",
        path="soundex/mo1910-n550-p819-may-michael-no-mccoy.jpg",
        title="Missouri N-550 — May / Michael; no McCoy",
        caption="No McCoy between May and Michael. Missouri is closed for Newman Coy/McCoy in April 1910.",
        source="S023 · C034",
    ),
    dict(
        n=30, date="Apr 1910", year=1910, role="negative",
        path="soundex/ok1910-n550-newman-sample.jpg",
        title="Oklahoma N-550 — Newman sample; no Dora",
        caption="Card-by-card reading of the Oklahoma Newman block found no Dora of thirty-nine born Kentucky and no household matching Samuel’s Sturgeon children.",
        source="S049 · C068",
    ),
    dict(
        n=31, date="Apr 1910", year=1910, role="negative",
        path="soundex/tx1910-n550-newman-dennis.jpg",
        title="Texas N-550 — Dennis Newman sample",
        caption="Texas Soundex Newman window, sampled. Other Doras appear in adjacent surnames (for example Dixon) and fail. Dora Ella Newnam is not indexed here.",
        source="S050 · C069",
    ),
    dict(
        n=32, date="Apr 1910", year=1910, role="negative",
        path="soundex/tn1910-n550-p2177-d-tab-no-coy.jpg",
        title="Tennessee N-550 — “D” tab; no Coy",
        caption="Handwritten Tennessee N-550. After Clifford of Lauderdale comes a blank D tab. Coy is not there.",
        source="S025 · C036",
    ),
    dict(
        n=33, date="Apr 1910", year=1910, role="negative",
        path="soundex/tn1910-n550-p2461-mary-d.jpg",
        title="Tennessee N-550 — Mary D.",
        caption="Start of the M-window where McCoy would file. Mary D. is present; McCoy is not.",
        source="S028 · C031b",
    ),
    dict(
        n=34, date="Apr 1910", year=1910, role="negative",
        path="soundex/tn1910-n550-p2463-mek-g-not-mccoy.jpg",
        title="Tennessee N-550 — Mek. G.; not McCoy",
        caption="Mek. G. of Cheatham County sits in the slot a McCoy card would occupy. It is not McCoy Newnam.",
        source="S028 · C031b",
    ),
    dict(
        n=35, date="Apr 1910", year=1910, role="negative",
        path="soundex/tn1910-n550-p2465-melvin-giles.jpg",
        title="Tennessee N-550 — Melvin of Giles",
        caption="Two Melvins of Giles County. Still no McCoy.",
        source="S028 · C031b",
    ),
    dict(
        n=36, date="Apr 1910", year=1910, role="negative",
        path="soundex/tn1910-n550-p2466-minerva.jpg",
        title="Tennessee N-550 — Minerva",
        caption="Minerva and Minnie cards. The McCoy window is closing.",
        source="S028 · C031b",
    ),
    dict(
        n=37, date="Apr 1910", year=1910, role="negative",
        path="soundex/tn1910-n550-p2469-mitchell-after-mccoy-slot.jpg",
        title="Tennessee N-550 — Mitchell, after the McCoy slot",
        caption="Mitchell follows. Tennessee has no McCoy Newman/Newnam in 1910.",
        source="S028 · C031b",
    ),
    # --- 1910 Peebles / Peoples ---
    dict(
        n=38, date="Apr 1910", year=1910, role="context",
        path="soundex/ky1910-p142-p235-p142-starts.jpg",
        title="Kentucky P-142 — Peebles/Peeples/Peoples block begins",
        caption="Start of the statewide 1910 Miracode P-142 household block. Searched for a Dora of thirty-nine as head or wife. A later Peebles marriage is not supported.",
        source="S062 · C081",
    ),
    dict(
        n=39, date="Apr 1910", year=1910, role="negative",
        path="soundex/ky1910-p142-p238-dottie-clyde-no-dora.jpg",
        title="Kentucky P-142 — Dottie / Clyde; no Dora",
        caption="D-window of Kentucky Peebles/Peeples/Peoples. No Dora of thirty-nine as head.",
        source="S062 · C081",
    ),
    dict(
        n=40, date="Apr 1910", year=1910, role="rejected",
        path="soundex/ky1910-p142-p239-edora-peoples-65-graves-rejected.jpg",
        title="Kentucky P-142 — Edora Peoples, 65, Graves County",
        caption="The only near-hit in the D-window: Edora Peoples, a sixty-five-year-old Tennessee-born sister-in-law in Graves County. Fails age, birthplace, and relationship. Not Dora Ella.",
        source="S062 · C082",
    ),
    dict(
        n=41, date="Apr 1910", year=1910, role="negative",
        path="soundex/ar1910-p142-p188-d-window-clyde-dave-no-dora.jpg",
        title="Arkansas P-142 — Clyde / Dave; no Dora ~39",
        caption="Arkansas Peebles/Peeples D-window. Clyde through Dave. No Dora of thirty-nine.",
        source="S063 · C083",
    ),
    dict(
        n=42, date="Apr 1910", year=1910, role="rejected",
        path="soundex/ar1910-p142-p189-yell-e-edd-peoples-not-dora.jpg",
        title="Arkansas P-142 — E. Edd Peoples of Yell County",
        caption="Yell County did have an E. Edd Peoples household: he twenty-seven, wife Catharine twenty-one. That is not Dora.",
        source="S063 · C083",
    ),
    dict(
        n=43, date="Apr 1910", year=1910, role="rejected",
        path="soundex/ar1910-p142-p190-ed-peebles-dora-sykes-19-rejected.jpg",
        title="Arkansas P-142 — Dora Sykes, 19, stepdaughter",
        caption="Dora Sykes, nineteen, stepdaughter of Ed Peebles in Mississippi County. Age 19 versus about 39. Rejected.",
        source="S063 · C083",
    ),
    dict(
        n=44, date="Apr 1910", year=1910, role="rejected",
        path="soundex/ar1910-p142-p200-julius-dora-bell-16-rejected.jpg",
        title="Arkansas P-142 — Dora Bell Peoples, 16",
        caption="Dora Bell, sixteen, sister-in-law of Julius Peoples in Jefferson County. Age 16. Rejected. A third marriage to a Peebles before Stone is not supported.",
        source="S063 · C083 · C087",
    ),
    # --- 1910 original schedules, Lee County ---
    dict(
        n=45, date="Apr 1910", year=1910, role="context",
        path="census/1910-po478-p0499-lee-fincastle-ed96-sheet7a.jpg",
        title="Fincastle ED 96 sheet 7A — Internet Archive PDF page 499",
        caption="Method note. Ancestry’s “image 499” is not this PDF page. Page 499 on the Internet Archive reel is Fincastle, ED 96, not Sturgeon. Sturgeon sheet 9B is PDF page 568 (Plate 54).",
        source="S067 · C082/C084",
    ),
    dict(
        n=46, date="15 Apr 1910", year=1910, role="context",
        path="census/1910-lee-ky-ed99-p551.jpg",
        title="Sturgeon ED 99 sheet 1A — the precinct begins",
        caption="Lee County, Precinct 7, Mag. Dist. 7, 15 April 1910. Header on this pass read Elam Brandenburg (a later pass read Elton E. Newnam on sheet 8A — conflict #13, unresolved). Dwelling 1 is not a Newnam house. Dora is not on this sheet.",
        source="S067 · C088",
    ),
    dict(
        n=47, date="21 Apr 1910", year=1910, role="rejected",
        path="census/1910-lee-ky-ed99-p557.jpg",
        title="Sturgeon ED 99 sheet 4A — Richard Newnam; dwelling 67 is Hamilton",
        caption="Richard Newnam, 45, and Sarah, 44, with children including twins David and Georgia. Not Samuel and Dora. On this sheet the 1900 dwelling-number 67 site is occupied by a Hamilton household, not by Samuel P. Newnam.",
        source="S067 · S089 · C088 · C106",
    ),
    dict(
        n=48, date="21 Apr 1910", year=1910, role="negative",
        path="census/1910-po478-p0557-lee-sturgeon-ed99-sheet4a.jpg",
        title="Sturgeon ED 99 sheet 4A (second capture)",
        caption="Independent capture of the same sheet from a parallel research pass. Dwelling 67 = Hamilton, Robert. The 1900 Newnam house is gone.",
        source="S089 · C106",
    ),
    dict(
        n=49, date="Apr 1910", year=1910, role="rejected",
        path="census/1910-po478-p0559-lee-sturgeon-ed99-sheet5a-elijah-newnan.jpg",
        title="Sturgeon ED 99 sheet 5A — Elijah Newnan, dwelling 66",
        caption="Elijah Newnan at dwelling 66. Same-name neighbor, not Dora’s household.",
        source="S089 · C088",
    ),
    dict(
        n=50, date="26 Apr 1910", year=1910, role="rejected",
        path="census/1910-lee-ky-ed99-p561.jpg",
        title="Sturgeon ED 99 sheet 6A — Harry, Albert, John and Ollie Newman",
        caption="Sherman Ross’s brothers-in-law Harry Newman, 42, and Albert, 23. Next: John Newman, 31, married one year to Ollie, 19. Not Samuel (age, wife, duration).",
        source="S067 · C088",
    ),
    dict(
        n=51, date="Apr 1910", year=1910, role="negative",
        path="census/1910-po478-p0560-lee-sturgeon-ed99-sheet6b-dw67-garrett.jpg",
        title="Sturgeon ED 99 sheet 6B — dwelling 67 is Garrett",
        caption="A second 1910 dwelling numbered 67, occupied by John T. Garrett. The 1900 Samuel–Dora house is not here either.",
        source="S089 · C106",
    ),
    dict(
        n=52, date="27 Apr 1910", year=1910, role="rejected",
        path="census/1910-lee-ky-ed99-p563.jpg",
        title="Sturgeon ED 99 sheet 7A — Reuben Newnam",
        caption="Dwelling 101/134: Newnam, Reuben, 33, and Nannie, 26, with Edward, Elzie, and Mary. Not Samuel and Dora.",
        source="S067 · C088",
    ),
    dict(
        n=53, date="27 Apr 1910", year=1910, role="rejected",
        path="census/1910-po478-p0563-lee-sturgeon-ed99-sheet7a-ruben-newnam.jpg",
        title="Sturgeon ED 99 sheet 7A (second capture) — Ruben Newnam",
        caption="Parallel capture of Reuben/Ruben Newnam at dwelling 101. Same rejection.",
        source="S089 · C088",
    ),
    dict(
        n=54, date="Apr 1910", year=1910, role="context",
        path="census/1910-po478-p0568-lee-sturgeon-ed99-sheet9b.jpg",
        title="Sturgeon ED 99 sheet 9B — Ancestry image 499 = this PDF page 568",
        caption="The sheet Ancestry numbers as image 499. No Dora, Samuel, McCoy, or the 1899 child John H.",
        source="S089 · C088",
    ),
    dict(
        n=55, date="Apr 1910", year=1910, role="rejected",
        path="census/1910-lee-ky-ed99-p576.jpg",
        title="Sturgeon ED 99 sheet 13B — a different John H. Newman",
        caption="Dwelling 218/257: Newman, John H., about 45, married 25 years; son Malcum, about 27. Not Dora’s child John H., who was nine months old in June 1900. End of ED 99. She was not still on Sturgeon Creek as a Newnam.",
        source="S067 · C088 · C089",
    ),
    # --- 1920 ---
    dict(
        n=56, date="Jan 1920", year=1920, role="rejected",
        path="soundex/ky1920-n550-p4201-dora-29-paducah-rejected.jpg",
        title="Kentucky N-550 — Dora Newman, 29, Paducah",
        caption="Daughter of Mary E. Vaelkel, age 29. Dora Ella would have been about 48. Rejected.",
        source="S045 · C064",
    ),
    dict(
        n=57, date="Jan 1920", year=1920, role="rejected",
        path="soundex/ky1920-n550-p4203-dora-e-10-cumberland-rejected.jpg",
        title="Kentucky N-550 — Dora E. Newman, 10, Cumberland",
        caption="A child of ten. Not our Dora.",
        source="S045 · C064",
    ),
    dict(
        n=58, date="Jan 1920", year=1920, role="negative",
        path="soundex/ky1920-n550-p4205-e-tab-after-dora.jpg",
        title="Kentucky N-550 — “E” tab after the Dora window",
        caption="The Dora given-name window in Kentucky Newman/Newnam ends. No woman of forty-eight. She was not indexed in Kentucky as Newman Dora in January 1920.",
        source="S045 · C064",
    ),
    dict(
        n=59, date="Jan 1920", year=1920, role="family",
        path="soundex/ky1920-n550-p4208-et-newnam-beattyville.jpg",
        title="Kentucky N-550 — E. T. Neuman, grandfather, Beattyville",
        caption="Soundex card: Neuman, E.T., Grand Father of Burke, C.B., Beattyville. This is Dora’s father, living with his granddaughter Provie Hoover Burke. Derivative of Plate 60.",
        source="S046 · C091",
    ),
    dict(
        n=60, date="12 Jan 1920", year=1920, role="family",
        path="census/1920-lee-ky-ed111-sh6a-burke-et-newman.jpg",
        title="Beattyville ED 111 sheet 6A — C. B. Burke and E. T. Newman",
        caption="Original schedule, 12 January 1920, enumerator Harry L. Perkins. Dwelling 106: C.B. Burke, 40, postmaster, owns free; wife Provie, 30, assistant postmaster; children Vivie M., 14, Vedia G., 10, George P.; Newman, E.T., Grand Father, 75, widowed, occupation none; boarders Bertie Combs (railroad clerk) and Warren C. Miller, 23, of Pennsylvania. Relationship is to the head; E.T. is grandfather of Provie, not of C.B. (conflict #12, resolved).",
        source="S073 · C091 · C095",
    ),
    dict(
        n=61, date="12 Jan 1920", year=1920, role="family",
        path="census/1920-lee-ky-ed111-sh6a-burke-hh-crop.jpg",
        title="Burke household crop — E. T. Newman, grandfather",
        caption="Crop of lines 17–24. Dora is not in this house. Her father is. She is not in Coy’s house at Danville, Yell County, either. The 1920 hole remains.",
        source="S073 · C091",
    ),
]


def plate_path(plate: dict) -> Path:
    return SRC / plate["path"]


def missing_plates() -> list[dict]:
    return [p for p in PLATES if not plate_path(p).is_file()]


def uncatalogued_jpegs() -> list[Path]:
    catalogued = {plate_path(p).resolve() for p in PLATES}
    found = {
        p.resolve()
        for p in SRC.rglob("*")
        if p.suffix.lower() in {".jpg", ".jpeg", ".png"}
    }
    return sorted(found - catalogued)
