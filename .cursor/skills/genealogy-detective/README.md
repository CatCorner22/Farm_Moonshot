# Genealogy Detective — Cursor skill

A project skill (`.cursor/skills/genealogy-detective/`) that turns Cursor into a team of eight experts — world-class PhD genealogist/ancestry researcher, private investigator, biographer, investigative journalist, palaeographer-archivist, statistician, information designer, and resourceful operator — for **deceased** historical relatives of the user or their spouse. Built for **intensive, exhaustive research that does not stop early**, and **proactive problem-solving**: creative workaround ladders before declaring blockers, autonomy-first (do it yourself with free sources/tools before asking the user), plus backlog, nine search passes, and completion contract enforced by `research_status.py` and `audit_dossier.py`.

## Use it

In Cursor chat, invoke the skill (e.g. `@genealogy-detective`) and give a target + question:

- "Research Anna Braun, b. ~1843, d. 1911, my 3rd-great-grandmother. Question: who were her parents?"
- "Brick-wall: find my great-grandfather's birthplace and immigration record."
- "DNA: how do these matches connect to my ancestor?" / "Check this CRAM file from my mother's WGS test."
- "Transcribe this 1780s parish-register photo and tell me what it actually says."
- "Draw our family tree (5 generations) and a migration map for a reunion — mark what's not proven."
- "Is it true our family had double the infant mortality of the time?"
- "Audit this family tree before I share it."

The agent will scaffold `research/<person>/`, work Phases 0–8 in `SKILL.md`, and deliver a cited dossier with generated visuals — not a chat-only answer.

## What's inside

| Path | Purpose |
|---|---|
| `SKILL.md` | Core workflow: 14 hard rules, relentless loop + autonomy-first roadblocks, Phases 0–8 with gates |
| `references/exhaustive-research.md` | **Don't stop early:** completion contract, `11-backlog.md` queue, nine search passes, FAN escalation, multi-session handoff, intensive mode |
| `references/genealogy-mastery.md` | **World-class ancestry/genealogy:** BCG-level proof architecture, FAN/cluster, land/probate/military/press, global repositories, identity & migration |
| `references/creative-workarounds.md` | **Roadblocks:** nine blocker ladders (paywall, nil index, illegible, …), roadblock log, reframe tactics |
| `references/proactive-autonomy.md` | **Do it yourself first:** decision tree, forbidden lazy asks, one precise user handoff when unavoidable |
| `scripts/workaround_playbook.py` | CLI checklist for a blocker type before `blocked`/user ask |
| `references/source-matrix.md` | Record types × repositories × substitutes, jurisdiction starters, access honesty |
| `references/methods.md` | GPS, evidence classes, conflict resolution, brick-wall protocol, naming/calendar traps |
| `references/dna.md` | atDNA/Y/mtDNA, clustering, triangulation, WATO, endogamy, NPE handling |
| `references/raw-dna-files.md` | **Raw DNA files:** consumer genotype TXT/CSV, **CRAM** (reference genome, lossy encoding, samtools cookbook), BAM/SAM, VCF/gVCF, FASTQ, PLINK — validation, conversion, privacy |
| `references/paleography.md` | **Handwritten sources from photos/PDFs:** image QC & re-capture standards, two-pass diplomatic transcription with `[?]`/`[illegible]` conventions, scripts/languages (secretary hand, Kurrent/Sütterlin, Latin registers…), HTR/OCR limits |
| `references/statistics.md` | **Sophisticated statistics:** absolute vs relative risk (mandatory dual reporting in natural frequencies), RR/OR/HR/NNT, Bayes & base rates, demographic measures done right, and a 20-item catalogue of misleading-but-technically-accurate presentations to detect and never use |
| `references/visualisation.md` | **Visual display:** chart selection by question, honesty rules (zero axes, uncertainty drawn in, n always shown), accessibility, reproducible generation |
| `references/family-tree-design.md` | **Family tree design:** pedigree/descendant/hourglass/bowtie/fan/Ahnentafel, confidence encoded in line styles, biological vs adoptive/step lines, pedigree collapse, unknown boxes, large-tree pagination |
| `references/ethics-and-privacy.md` | Deceased-only scope, living-person & DNA consent, sensitive findings, cultural care |
| `templates/` | Intake, plan, log, timeline, evidence/claims, DNA (checksum inventory), dossier, conflicts, transcriptions, statistics, visuals register |
| `scripts/scaffold_case.py` | Create a case folder incl. `11-backlog.md` (with a DNA-excluding `.gitignore`) |
| `scripts/research_status.py` | Fails (exit 1) while backlog has open/in_progress items — research not complete |
| `scripts/audit_dossier.py` | Mechanical audit: open backlog, uncited `PROVEN` claims, GPS gates, DNA rows, relative-risk-without-absolute |
| `scripts/dna_file_check.py` | Read-only format/build/count detection for CRAM, BAM, VCF, FASTQ, genotype files |
| `scripts/document_inventory.py` | Photo/PDF inventory (dimensions, pages, SHA-256) before transcription |
| `scripts/make_pedigree.py` | Generate pedigree/descendant SVG family trees from JSON — confidence line styles, Unknown boxes, cycle/impossibility validation |
| `scripts/make_charts.py` | Honest SVG timeline (lifespans/events) and bar charts (zero axis, n labelled) from CSV |
| `scripts/stats.py` | Risk (absolute+relative+CIs, NNT/NNH), Wilson proportion intervals, Bayesian updating, OR→RR conversion |
| `scripts/kinship.py` | Exact ages, cousin-relationship computation, Soundex + variant hints |
| `examples/` | Worked fictional examples: mini-case, plus visuals/statistics/transcription |

## Design choices

- **Relentless over comfortable:** the `11-backlog.md` queue and completion contract stop "one-database and done"; intensive mode cycles nine search passes until gates close or the user defers specific items with exact retrieval instructions.
- **Effective over efficient:** token savings come from structure (backlog, claim/source IDs, one reference per phase), never from skipped matrix rows or silent FAN gaps.
- **Files over chat:** the case folder is the single source of truth, so multi-session research stays consistent.
- **Nothing laundered:** uncertain readings keep `[?]` marks into the claims they support; uncertain links are dashed on the tree itself; relative risks never appear without absolute values — speculation cannot become "fact" by passing through a chart, a percentage, or a confident transcription.
- **Privacy by default:** deceased targets only, living people redacted, raw DNA (CRAM/genotype files) checksummed, kept out of git, and never uploaded without the test-taker's consent.
