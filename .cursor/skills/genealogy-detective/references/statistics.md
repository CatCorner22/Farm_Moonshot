# Statistics — sophisticated analysis, honest risk, and detecting manipulation

Load for any quantitative claim: population/context comparisons, DNA probabilities, risk statements, demographic patterns, or reviewing anyone else's numbers (including published trees, ethnicity estimates, and "statistics show…" claims). Visual presentation of numbers: [visualisation.md](visualisation.md).

## The stance

Statistics in genealogy answer three kinds of question: **(a)** context ("was a marriage at 17 unusual in this parish in 1840?"), **(b)** probability ("how likely is this DNA match to be a 2nd vs 3rd cousin?", "how surprising is this name coincidence?"), **(c)** pattern detection across a family/population (mortality, fertility, migration, occupational mobility). Each demands a defined population, denominator, time period, and uncertainty. A number without those four is decoration, not analysis.

## Foundations — get these right every time

- **Define before computing:** population at risk, numerator, denominator, period, place, inclusion/exclusion rules. Write them in `09-statistics.md` *before* results.
- **Counts before rates.** Always report `k/n` alongside any %/rate. `2 of 5 children died` is honest; `40% child mortality!` from that family alone is not.
- **Uncertainty scales with √n.** Proportions get intervals (Wilson score interval preferred for small n); means of skewed things (age at death) get median + IQR as well. `scripts/stats.py` computes these — never eyeball an interval.
- **Base rates govern everything.** A rare-event test/match/coincidence means little without how common the event is in the relevant population (see Bayes below).
- **Correlation ≠ cause; record linkage ≠ identity; significance ≠ importance.** A p-value (if used at all) is reported with effect size and interval, never alone, and never as "proof." Prefer estimation over binary significance theatre.
- **Multiple comparisons:** scanning 40 parishes / 200 matches / 12 hypotheses guarantees false "hits." State how many things were tried; adjust confidence (at minimum qualitatively, Bonferroni-style reasoning where formal testing is used).
- **Priors are stated.** Bayesian results name the prior and show sensitivity ("posterior 0.6–0.9 across plausible priors"), or they are not reported.

## Absolute vs relative risk — the core fluency (never report one without the other)

Definitions (exposed/group A vs baseline/group B, risk = events/people at risk over a stated period):

| Measure | Formula | What it answers | How it's abused |
|---|---|---|---|
| Baseline (absolute) risk | \(p_B\) | "How likely anyway?" | Omitted — the master key to most deception |
| Absolute risk in group | \(p_A\) | "How likely for them?" | — |
| **Absolute risk difference (ARD/ARR)** | \(p_A-p_B\) (percentage **points**) | "How much does it actually change?" | Confused with % change |
| **Relative risk (RR)** | \(p_A/p_B\) | "How many times as likely?" | Headlined alone: "DOUBLES your risk!" (of a 1-in-a-million event) |
| Relative risk change | \((p_A-p_B)/p_B\) | "% increase/decrease" | Same, plus sign games |
| Odds ratio (OR) | \(\frac{p_A/(1-p_A)}{p_B/(1-p_B)}\) | Case-control studies | Read as RR — equal only when events are rare; with common events OR exaggerates |
| Hazard ratio (HR) | ratio of instantaneous rates | Survival over time | Read as RR; hides the time axis and absolute survival |
| NNT / NNH | \(1/|ARD|\) | "How many people for one outcome to change?" | Rarely shown — because it deflates drama |
| Attributable fraction | \((RR-1)/RR\) (among exposed) | "Share of their outcomes linked to exposure" | Read as individual causation for a specific person — it is not |

**Mandatory reporting format for any risk comparison** (copy this shape):

> Baseline: 4 in 1,000 [people/period/place]. Group: 8 in 1,000. **That is 4 extra cases per 1,000 people (absolute), i.e. twice the relative risk (RR 2.0), NNH ≈ 250.** Individuals: this describes groups; it does not determine any one person's outcome.

- Use **natural frequencies with a common denominator** (per 1,000 or per 100,000, same denominator for both groups) — the single most effective anti-deception format. Pair with an icon array for delivery.
- "Percent" vs "percentage points": a fall from 4% to 2% is **2 percentage points**, a **50% relative** fall. Mixing these deliberately is a classic; catch it in others, never do it.
- Historical application: compare an ancestor's outcomes (age at death, child loss, remarriage) to the *period life table / parish cohort*, with cohort size stated. "Died young at 52" in 1880 (when conditional life expectancy at 20 was ~60) is a different claim than it sounds today — compute, don't vibe.
- Genealogy/DNA "risk" language: penetrance and carrier statements from DNA files are **health** content — out of scope (ethics reference). Relationship probability is *not* risk; use the Bayes/DNA framing below, not RR theatre.

## Bayesian reasoning — how evidence actually combines

\[Posterior\ odds = Prior\ odds \times Likelihood\ ratio(s)\]

- **Genealogy use:** probability that two same-name records are one person; that a candidate is the parent; that a DNA relationship hypothesis holds vs rivals. Priors come from base rates: how many men named Elias Venn of plausible age lived within 20 miles in 1850? If twelve, a name+age match is weak evidence (LR small); if one, strong.
- **Coincidence discipline:** estimate the expected number of coincidences *by chance* (shared birthday, same name, same occupation) across the number of comparisons actually made — most "astonishing coincidences" are birthday-problem arithmetic.
- **DNA:** shared-cM distributions overlap heavily; combine cM likelihoods across *all* candidate relationships with documentary priors (age/place feasibility can zero-out a hypothesis no cM value can rescue). Tools like WATO implement this — feed them honest hypotheses including unglamorous ones, and report the prior assumptions. A "99% confident" output from garbage hypotheses is garbage.
- **Absence as evidence:** a missing record updates belief only in proportion to P(no record | exists) — record survival/detection probability. "Not in the index" after poor coverage is near-zero evidence; after complete, well-indexed coverage it's strong. Quantify coverage when claiming negative evidence.
- Worked via `scripts/stats.py bayes --prior 0.1 --lr 8` etc. Show prior, each LR with its justification, and posterior as a *range* across defensible priors.

## Catalogue: misleading but technically accurate — detect in others, never use

Each entry: technique → example → antidote. In Phase 7, screen the dossier *and every source it cites* against this list.

1. **Relative without absolute** — "risk doubles" (1→2 per million). → Demand baseline + ARD.
2. **Truncated/expanded axes** — tiny change fills the chart. → Check axis origin; re-plot from zero.
3. **Cherry-picked time window** — start at a peak/trough year. → Ask "why this start?"; extend the series.
4. **Denominator switching** — % of deaths vs % of population; per-family vs per-child. → One denominator, stated.
5. **Percent vs percentage points** swap. → Restate both.
6. **Survivorship/selection bias** — studying only lines that survived/left records ("our family always lived to 90" — the dead left no descendants). → Define who could enter the sample.
7. **Base-rate neglect** — rare surname match trumpeted, commonness unexamined. → Frequency in the actual population/period.
8. **Small-n drama** — 2/2 = "100%". → Counts + Wilson interval.
9. **Averaging the skewed** — mean age at death dragged by infant mortality. → Median, distribution, separate infant/child/adult mortality (period life tables: \(q_0\), life expectancy *at age x*, not just at birth).
10. **Simpson's paradox** — trend reverses when parishes/cohorts combined (different age structures). → Stratify before pooling; standardise rates to a common structure when comparing populations.
11. **Ecological fallacy** — county-level wealth → this family's wealth. → Individual-level records or label as context only.
12. **Regression to the mean** — extreme first observation "improves." → Expect it; don't credit a cause.
13. **False precision** — "born 1841.37", ethnicity "23.7% Irish". → Round to what measurement supports; label estimates as estimates.
14. **Imputed/merged data presented as measured** (DNA chip imputation, merged kits, transcribed ages). → Provenance per datapoint.
15. **Multiple-comparison fishing** — the one "significant" parish of 40. → Count the tries.
16. **OR read as RR; HR read as RR** for common outcomes. → Convert with baseline risk (`stats.py`).
17. **Cumulative vs per-period framing** — lifetime risk vs annual risk chosen for drama either way. → Give both, same denominator.
18. **Missing-data invisibility** — rates computed only on complete records (which are systematically richer/literate/settled). → Report missingness % and who is likely missing.
19. **Age heaping & rounding** treated as exact (census ages ending 0/5). → Analyse as ranges; check Whipple-style heaping before precision claims.
20. **Presenting a model as a measurement** — ethnicity estimates, imputed segments, "predicted" relationships. → Name model, version, reference panel, interval.

## Demographic & historical measures (use correctly)

- **Life expectancy at birth** is a *period synthetic* measure depressed by infant mortality — pair with life expectancy at 5/20 and modal adult age at death. Never say "people died at 40" from \(e_0\) alone.
- **Infant/child mortality:** \(q_0\) (die <1) and under-5 rates per 1,000 live births; a family's experience is one draw — compare to parish/national rates *with the family n shown*.
- **Fertility:** children per woman requires exposure (marriage duration, survival); "she had 9 children" vs completed-family-size distributions of her cohort.
- **Rates need person-time / standardisation:** crude rates compared across populations with different age structures mislead — direct/indirect standardisation or stratified comparison, method stated.
- **Record survival is a sampling process:** estimate coverage (known events captured ÷ expected) before treating a dataset as a population.

## DNA statistics specifics (with dna.md)

- Report match probabilities as sets of relationships with cM *distributions* (Shared cM Project ranges), segment counts/sizes, and the documentary filters applied — never a single anointed relationship.
- Ethnicity admixture %: stochastic model output, changes between company versions, meaningless for a specific ancestor/tribe — `SPECULATIVE` context only (see ethics).
- Endogamy/pedigree collapse invalidates standard cM tables (state it, widen relationship sets, lean on segment + documentary work).

## Workflow (every quantitative claim)

1. Write the question, population, denominator, period, exclusions in `09-statistics.md` **before** computing.
2. Compute with `scripts/stats.py` (or named tool + version); paste inputs + outputs in the worksheet.
3. Report: counts, absolute **and** relative (if comparative), interval, base rate, n, missingness — in the mandatory format above.
4. Screen the write-up against the 20-item catalogue; note the screen in Phase 7.
5. Visualise per visualisation.md (natural frequencies/icon arrays for risk; uncertainty drawn in).

```bash
python3 scripts/stats.py risk --a-events 8 --a-n 1000 --b-events 4 --b-n 1000
python3 scripts/stats.py proportion --k 7 --n 42
python3 scripts/stats.py bayes --prior 0.10 --lr 8 --lr 3
python3 scripts/stats.py or-to-rr --or 2.4 --baseline 0.20
```
