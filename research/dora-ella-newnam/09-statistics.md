# 09 — Statistics worksheet: Dora Ella Newnam Stone

Write population/denominator/period/exclusions BEFORE computing (statistics.md).

## Analyses
### A001 — Age at first marriage (Dora)
- Population & denominator: one person (P001). Period/place: Lee Co., KY, 10 Dec 1885.
- Counts first: event age computed from preferred birth 11 Aug 1871 (day POSSIBLE) to 10 Dec 1885 = **14 years** (`kinship.py age 1871-08-11 1885-12-10`). If DC birth 11 Aug 1868: 17 years.
- This is a **single-person fact**, not a rate. No RR.
- Interpretation limits: U.S. 1880s Appalachian first-marriage ages clustered in the late teens; 14 is young but attested in the same Book 2 (several brides 16). Does **not** prove coercion; the record is a first marriage at father’s house with father as witness.
- 1880 age 8 independently requires the 14-year figure, not 17.

### A002 — Children dead before 1900
- Population: Dora’s children ever born, as she reported 1 Jun 1900.
- Denominator: 7 born; numerator: 2 dead; period: 1886–1 Jun 1900, Lee Co.
- Tool: `python3 scripts/stats.py proportion --k 2 --n 7`
- Result: **2/7 = 28.6% (Wilson 95% CI 8.2%–64.1%)**
- Mandatory-format sentence:
> Two of Dora’s seven children had died by 1 June 1900 (2/7). That is 286 per 1,000 of **her** births, but the Wilson interval is 82–641 per 1,000 because n=7. This is **not** a county infant-mortality rate and must not be compared to a state rate without a defined cohort of all births in Sturgeon 1886–1900.
- Interpretation limits: names of the two dead children unknown; one or both may have been neonatal. U.S. white rural child mortality was high in this era; 2/7 is compatible with that background and is **not** evidence of an unusual family disaster.

### A003 — Age at death
- Preferred: b. Aug 1871, d. 23 Aug 1926 → **55 years** (`kinship.py age 1871-08-11 1926-08-23`).
- DC arithmetic: 58 years 12 days from 11 Aug 1868 (internally consistent with the false year).
- Not compared here to a 1926 Arkansas female life table (table not pulled this session). Do not say “died young” without that denominator.

### A004 — Same-person coincidence (Dora of Carter Cove)
- Prior: how many adult women named Dora Newman/Newnam were likely to be buried at Carter Cove in 1926?
- Base rate: cemetery is a small rural yard; 1993 reading shows one “Newman, Dora” and the certificate names burial Carters Chapel the previous day.
- Qualitative LR: name + cemetery + date alignment is high; still not a photograph of the stone. Identification PROBABLE pending a photo.

## Misleading-presentation screen (20-item catalogue in statistics.md)
- Screened my claims ☑ · Screened key cited sources ☑ (WikiTree “abt. 1930” is an unsourced round year — discarded)
- Issues found & fixed: do not convert 2/7 into “40% child mortality in the family” without n and CI; do not average 1868 and 1871 into 1869–70; do not treat Soundex absence as “she did not exist” — it is “not under that surname in that state.” Do not promote a Peebles third marriage from family memory: every located Dora Peebles/Peeples fails the same-person test, and home-county licenses are nil; “not supported” ≠ “impossible in an unread county.” Do not treat “Newnams in 1910 Sturgeon” as Dora’s household — four other Newnam houses are in ED 99 and fail the same-person test. Do not average 1920 age 62 with 1900 ages 32/44/50 into a fake birth year for Tom A. Stone. Do not read 1920 “Grand Father” of C.B. Burke as proof that an Elias daughter is C.B.’s mother — 1900 and the 1904 license show E.T. is grandfather of **Provie**. Do not treat census age 75 (Jan 1920) as disproving a birth of 18 Apr 1842 (that man would be 77); two-year census drift is common. Do not treat Soundex “Jesse C. son” as a sixth child of Douglas Thomas Stone — the original says Ossie P. daughter. Do not treat a 2-year census-age gap (44 in 1900 vs 62 in 1920) as a second identifier for a merge.

### A007 — Soundex vs original (Douglas Stone 1900)
- Population: one household, six named members on ED 159 sh 9B lines 67–73 versus the Soundex card pair (IA n1678–1679).
- Counts: **3 of 6 given-name/date fields on the derivative card disagree** with the original (Nancy’s month/year/age; Etta vs Ella; Ossie P. dau vs Jesse C. son). Agreement: surname Stone, head Thomas, May 1856 age 44, ED 159 sheet 9 line 67, wife Nancy E., daughters Minnie and Rosena, Missouri.
- This is a **concordance count**, not a rate. It supports treating the original as the source (C101) and the Soundex as a finding aid with known error (C102). It does **not** change the same-person test against 1920 Tom A. (still one identifier).

### A006 — 1920 Burke household (whose grandfather?)
- Population: one enumerated relationship (“Grand Father”) plus two independent records of Provie Hoover’s tie to Elias.
- Counts: (1) 1900 Provy Hoover **gdau** of Elias; (2) 1904 “E. T. Newnam Granfather appeared” at Provie × C.B. Burke; (3) 1900 Charles B. **son** of George Burke. **Zero** records name an Elias daughter as C.B.’s mother.
- This is a **concordance count**, not a rate. It supports C097 as a resolved conflict, not a probability of relatedness.

### A005 — 1910 Sturgeon ED 99 Newnam households (negative control)
- Population: named Newnam/Newman persons on the original ED 99 schedules (sheets 1A–13B).
- Count: **≥5 households** containing the surname (Richard+Sarah; Harry/Albert in Ross hh; John+Ollie; Reuben+Nannie; John H.+Malcum). **Zero** of those households contains Dora ~39, Samuel ~41, McCoy ~20, or John H. ~10.
- This is a **count of examined households**, not a rate. It supports C088 as a precinct-level negative, not “no Newnams lived there.”
