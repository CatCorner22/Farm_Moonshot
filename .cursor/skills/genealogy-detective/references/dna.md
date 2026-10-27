# DNA — autosomal, Y, mtDNA, and hypothesis testing

Load fully before any DNA work (Phase 6) and together with [raw-dna-files.md](raw-dna-files.md) when data files are involved. Pair with [ethics-and-privacy.md](ethics-and-privacy.md): DNA can expose misattributed parentage, donor conception, adoption, and living people's data.

## Non-negotiables

- DNA **suggests**, documents **prove**. Every DNA kinship claim names its documentary corroboration or is capped at `POSSIBLE`.
- Never estimate cM, segment counts, or haplogroups from memory or from a file you have not actually parsed. Report values as shown by the testing company / tool output, with company, date, and chip/build noted.
- A match's tree is a hypothesis. Build it from records before using it; unsourced match trees mislead entire clusters.
- **Ranges overlap.** The same cM total fits multiple relationships (e.g. half-aunt vs great-aunt vs first cousin once removed). Always present the *set* of consistent relationships, then narrow with age, geography, shared matches, and documents — never announce the single most exciting option. Use current Shared cM Project data (via DNA Painter) rather than memorised numbers.
- Small segments (<7 cM) are frequently false/IBC; do not base conclusions on them. Pile-up regions and endogamy inflate totals (below).
- Test-taker consent governs everything: uploads to GEDmatch or any database, law-enforcement visibility settings, sharing screenshots, and naming matches require the test-taker's informed consent. Record consent in `00-intake.md`; default law-enforcement matching to **off/opt-out** unless the user explicitly directs otherwise.

## Test types — what each can and cannot do

| Test | Inheritance | Use for | Limits |
|---|---|---|---|
| Autosomal (atDNA) | Both parents, all lines | Relatives to ~5th–6th cousins; unknown parentage; confirming/documenting lines within ~6–8 generations | Dilution: a real 4th+ cousin may share 0 cM. Cannot alone assign which line without clustering/triangulation |
| Y-DNA (STR + SNP/Big Y) | Father→son only | Direct paternal line surname/origin, distinguishing same-name paternal lines | Only males carry it; one line only; needs documented male-line testers, ideally two distantly related ones |
| mtDNA (HVR → full sequence) | Mother→children | Direct maternal line, maternity questions, historical identifications | One line only; mutations slow — a match can be centuries deep; full sequence needed for precision |
| X-DNA | Sex-dependent paths | Narrowing which ancestral paths could contribute (advanced, use inheritance charts) | Complex; never primary evidence |

## Standard autosomal workflow

1. **Inventory** (`05-dna.md` + file inventory in raw-dna-files.md): tester (initials/code, living = redacted), company, test date, raw-file name + SHA-256, build, kits uploaded where (with consent + date).
2. **Sort matches:** star/note matches with known relationships first; verify them against documents — they calibrate everything else.
3. **Cluster:** Leeds method (sort shared matches of matches in the ~90–400 cM band into grandparent-line clusters) or company shared-match groups. Name clusters by the ancestral couple they point to; unknown clusters are the research targets.
4. **Build quick-and-dirty trees** for clustered matches down to candidate ancestral couples — then verify key links with records before relying on them.
5. **Hypothesis test:** for unknown parentage/identity, use WATO (What Are The Odds, DNA Painter) with multiple competing hypotheses, documentary ages/places entered honestly; report odds *and* their sensitivity to missing people (untested lines, unknown siblings).
6. **Triangulate** where possible: three+ descendants of the same ancestral couple sharing overlapping segments on the same chromosome region strengthens a line; segment data is unavailable for Ancestry matches — say so, use companies/tools that provide it, with consent.
7. **Corroborate & write up:** DNA conclusion + documentary trail + confidence label in `05-dna.md`; update claim register. State plainly what DNA cannot distinguish in this case (e.g. two brothers as father).

## Special situations

- **Endogamy / pedigree collapse:** totals inflated, many small segments, everyone matches everyone. Work with segment data, lower-weight small segments, cluster by locality/family, test older generations, and lower confidence labels. Never apply standard cM tables naively in endogamous populations (e.g. Ashkenazi Jewish, Mennonite, island, French-Canadian founder populations).
- **Unknown / misattributed parentage (incl. NPE), adoption, donor conception:** follow the ethics reference — private, neutral language ("biological father differs from the father of record"), no contact with newly identified relatives without the user's explicit direction, no disclosure to third parties, suggest support resources when distressing. Build the biological tree in a *separate, clearly labelled* section/file from the documentary family.
- **Testing strategy:** test the oldest living generation first (with consent) — each generation up doubles relevant DNA. Recommend targeted tests (documented descendants of candidate lines) and explain costs/privacy before the user buys anything. Never pressure a relative; a refusal is final and logged without commentary.
- **Y-DNA surname projects / mtDNA:** join project results to documented lines; a haplogroup is an origin *hint* over centuries, not proof of a recent ancestor. Record STR marker values / SNP path as reported by the lab, not reinterpreted.
- **Historical / ancient remains, exhumation, celebrity DNA:** out of scope unless the user has legal authority and institutional/ethics approval — flag and stop.

## Reporting language (copy the discipline)

> "Tester A shares 214 cM across 9 segments with match M (Ancestry, accessed [date]). That total is consistent with relationships from 2nd cousin to half-2nd cousin once removed (Shared cM Project). Shared matches cluster with documented descendants of [couple], and M's documented great-grandmother [name] was in [place] in [year]. Conclusion: `PROBABLE` descent from [couple]; assignment to their daughter [X] specifically remains `POSSIBLE` until [named record] is obtained."

Forbidden: "DNA proves…", "definitely your grandfather", percentages of ethnicity treated as genealogy (ethnicity estimates are entertainment-grade context, labelled `SPECULATIVE`, never evidence of a specific ancestor or tribal/national identity).
