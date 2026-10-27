# Genealogy Detective — Cursor skill

A project skill (`.cursor/skills/genealogy-detective/`) that turns Cursor into a PhD-level genealogist + private investigator + biographer + investigative journalist for **deceased** historical relatives of the user or their spouse.

## Use it

In Cursor chat, invoke the skill (e.g. `@genealogy-detective`) and give a target + question:

- "Research Anna Braun, b. ~1843, d. 1911, my 3rd-great-grandmother. Question: who were her parents?"
- "Brick-wall: find my great-grandfather's birthplace and immigration record."
- "DNA: how do these matches connect to my ancestor?" / "Check this CRAM file from my mother's WGS test."
- "Audit this family tree before I share it."

The agent will scaffold `research/<person>/`, work Phases 0–8 in `SKILL.md`, and deliver a cited dossier — not a chat-only answer.

## What's inside

| Path | Purpose |
|---|---|
| `SKILL.md` | Core workflow: 9 hard rules, Phases 0–8 with gates (GPS, same-person test, red-team) |
| `references/source-matrix.md` | Record types × repositories × substitutes, jurisdiction starters, access honesty |
| `references/methods.md` | GPS, evidence classes, conflict resolution, brick-wall protocol, naming/calendar traps |
| `references/dna.md` | atDNA/Y/mtDNA, clustering, triangulation, WATO, endogamy, NPE handling |
| `references/raw-dna-files.md` | **Raw DNA files:** consumer genotype TXT/CSV, **CRAM** (reference genome, lossy encoding, samtools cookbook), BAM/SAM, VCF/gVCF, FASTQ, PLINK — validation, conversion, privacy |
| `references/ethics-and-privacy.md` | Deceased-only scope, living-person & DNA consent, sensitive findings, cultural care |
| `templates/` | Intake, plan, research log, timeline, evidence/claim register, DNA worksheet (file inventory w/ checksums), dossier, conflicts |
| `scripts/scaffold_case.py` | Create a case folder (with a DNA-excluding `.gitignore`) |
| `scripts/audit_dossier.py` | Mechanical audit: uncited `PROVEN` claims, open GPS gates, DNA rows missing SHA-256/build |
| `scripts/dna_file_check.py` | Read-only format/build/count detection for CRAM, BAM, VCF, FASTQ, genotype files |
| `scripts/kinship.py` | Exact ages, cousin-relationship computation, Soundex + variant hints |
| `examples/fictional-mini-case.md` | Worked example (all names invented) |

## Design choices

- **Effective over efficient:** exhaustive-search and red-team gates block premature `PROVEN` conclusions; token savings come from the on-disk claim/source/file IDs and loading one reference per phase.
- **Files over chat:** the case folder is the single source of truth, so multi-session research stays consistent.
- **Privacy by default:** deceased targets only, living people redacted, raw DNA (CRAM/genotype files) checksummed, kept out of git, and never uploaded without the test-taker's consent.
