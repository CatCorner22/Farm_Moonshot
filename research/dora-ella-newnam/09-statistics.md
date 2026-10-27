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
- Issues found & fixed: do not convert 2/7 into “40% child mortality in the family” without n and CI; do not average 1868 and 1871 into 1869–70; do not treat Soundex absence as “she did not exist” — it is “not under that surname in that state.”
