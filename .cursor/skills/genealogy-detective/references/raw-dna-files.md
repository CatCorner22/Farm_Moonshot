# Raw DNA files — CRAM, BAM, SAM, VCF, FASTQ, and consumer genotype files

Load whenever the user supplies, asks about, or wants analysis of a DNA *file* (as opposed to a match list on a website). This file covers file-level skills: identify, validate, preserve, convert, inspect, and analyse without corrupting data or overstating results.

## Golden rules for all DNA files

1. **Originals are read-only evidence.** On receipt: record filename, source (company/lab/person), date received, stated genome build and test/chip if known, and a **SHA-256 checksum**; store a copy in `research/<person>/sources/dna/` untouched. All work happens on copies. Never edit, rename-in-place, re-zip, or "clean" an original.
2. **Never guess a file's contents, build, or values.** Detect format from headers/magic, parse with a real tool, and report tool output. If a tool is unavailable, say so and give the user the exact command to run — do not simulate results.
3. **Privacy before analysis.** These files are the most identifying data a person has — they can reveal health risks, parentage, and relatives. Apply [ethics-and-privacy.md](ethics-and-privacy.md): get the test-taker's consent for each analysis/upload, never upload to a new service, public share link, or law-enforcement-visible database without explicit consent, never commit raw DNA files to git or publish them in a PR/repo (the scaffold's `.gitignore` helps — verify it), and redact living testers as `Living` in outputs. Warn the user: uploading a relative's file without their consent is not theirs to give.
4. **Build honesty.** State GRCh37 vs GRCh38 (a.k.a. hg19/hg38) for every file, dataset merge, and report. Positions, and some rsIDs, differ. Never merge or compare files on different builds without a documented liftover step — silent build mixing is the #1 raw-data error.
5. **Reproducibility:** log every tool name + version, command, reference file (name + checksum), and date in `05-dna.md`. Another researcher must be able to rerun your work byte-for-byte.

## Format map

| Format | What it is | Typical genealogy source | Binary? | First check |
|---|---|---|---|---|
| Consumer genotype TXT/CSV/ZIP (`.txt`, `.csv`, sometimes zipped) | Tested SNP panel (rsID, chromosome, position, genotype), ~500k–800k SNPs | AncestryDNA, 23andMe, MyHeritage, FamilyTreeDNA (Family Finder), Living DNA downloads | No | Header lines naming company, chip, and build |
| VCF (`.vcf`, `.vcf.gz`) | Variant calls (CHROM/POS/ID/REF/ALT/QUAL/FILTER/INFO/FORMAT) | Whole-genome sequencing (e.g. Nebula, Dante, Sequencing.com), clinical labs, exports | No (may be gzipped) | `##fileformat=VCF`, `##reference=`, header line `#CHROM` |
| SAM (`.sam`) | Sequence *alignments* (reads mapped to a reference) | WGS/WES providers, labs, research data | No (large) | `@HD/@SQ` header lines |
| BAM (`.bam`) | Binary, compressed SAM | WGS/WES providers, labs | Yes, BGZF | Magic bytes; inspect with samtools, never by eye |
| **CRAM** (`.cram`) | **Reference-compressed alignments** — smaller successor to BAM; stores differences from a reference genome | Modern sequencing labs/pipelines (increasingly the default delivery format) | Yes | Magic `CRAM`; needs the right reference to fully decode (below) |
| FASTQ (`.fastq`, `.fq`, `.fastq.gz`) | **Raw reads** before alignment (basecalls + quality scores), often paired `_R1/_R2` | Sequencing labs, WGS providers | No (gzipped, huge) | 4-line records starting `@`; no reference — not yet interpretable as variants |
| BCF, `.gvcf` | Binary VCF / genomic VCF (adds non-variant blocks) | Pipelines, clinical | Yes / No | As VCF, plus `bcftools` for BCF |
| PLINK (`.bed/.bim/.fam`), 23andMe-style exports from tools | Analysis-ready genotype sets | DNA tools, research | Mixed | `.fam/.bim` companions must stay together |

Rule of thumb: **genotype files → genealogy (matching/kinship) as-is. FASTQ → must be aligned then variant-called. SAM/BAM/CRAM → alignments that can be variant-called or interrogated at specific positions. VCF → called variants, may be genome-wide or targeted.**

## CRAM skills — the details that matter

CRAM is not "a smaller BAM you can open the same way." It stores sequence as differences from a reference, so:

- **You must know (and have) the exact reference** (e.g. GRCh37/hs37d5 vs GRCh38, and whether decoy/ALT contigs were used). Decoding against the wrong reference yields errors or garbled sequence in reference-dependent regions. The reference used is usually recorded in the CRAM header (`@SQ` lines with `M5` checksums / `UR`). Check header first; if reference files aren't local, samtools can retrieve reference sequences on demand (see below), which requires network and should be logged.
- **Lossy vs lossless:** CRAM can be encoded lossily (e.g. quality-score binning/discarding, names omitted). A lossy CRAM cannot be restored to the original BAM/FASTQ exactly. Ask/record: encoding profile if stated by the provider, and never promise a user that CRAM→FASTQ recovers their "original reads" until you've verified qual/names survived (`samtools view` flags/header, provider docs).
- **Integrity:** CRAM has per-container checksums; verify with `samtools quickcheck` and full decode test before analysis. A CRAM that fails quickcheck or references missing external reference data is quarantined — report it, don't force it.
- **Index:** `.crai` (samtools) or `.cram.crai`. Index before random access: `samtools index file.cram`.
- **Don't convert reflexively.** If analysis only needs genotypes at known SNPs, call/extract variants from the CRAM rather than round-tripping CRAM→BAM→FASTQ→… Each conversion risks loss; log every conversion and keep the CRAM as the archival original.

### CRAM/BAM/SAM command cookbook (samtools/htslib; run locally, log versions)

```bash
samtools --version                                  # record in 05-dna.md
sha256sum sample.cram                               # checksum BEFORE anything else
samtools quickcheck -v sample.cram                  # integrity; silence = OK
samtools view -H sample.cram                        # header: @SQ M5/UR = reference identity, read groups, source pipeline
samtools flagstat sample.cram                       # alignment stats (mapped %, paired, etc.)
samtools idxstats sample.cram                       # per-chromosome coverage (index first)
samtools index sample.cram                          # creates .crai
samtools mpileup -r chr1:12345-12345 sample.cram    # interrogate specific position(s) (after index)
samtools view sample.cram chr7:1000000-2000000 > region.sam   # extract a region (SAM text, on a COPY)
# Conversions (on copies; only when analysis requires; log them)
samtools view -b -o sample.bam sample.cram          # CRAM -> BAM (reference must resolve)
samtools view -T GRCh38.fa -o sample.rescued.cram sample.cram  # decode with explicit reference FASTA
export REF_PATH=https://www.ebi.ac.uk/ena/cram/md5/%s  # on-demand reference retrieval (network; log if used; prefer local reference for privacy/reproducibility)
export REF_CACHE=./refcache/%2s/%s                  # cache retrieved reference locally
bcftools mpileup -f GRCh38.fa sample.cram | bcftools call -m -Oz -o calls.vcf.gz   # variant calling (parameters matter — record them; calling quality drives every downstream claim)
```

If samtools/bcftools are absent, instruct: `conda install -c bioconda samtools bcftools` or OS packages (`apt install samtools bcftools` / `brew install samtools bcftools`) — then have the user paste outputs back. Never invent `flagstat` percentages or coverage from a filename.

For CRAM in a browser viewer (IGV etc.): load `.cram` + its `.crai` and set the same reference genome in the viewer; mismatched viewer reference = misleading display.

## FASTQ skills

- Paired-end files come in mates (`_R1/_R2`, `_1/_2`); never analyse one mate alone without saying so. Check read counts match between mates.
- QC before alignment: read count, length, quality encoding (Phred+33 vs +64 on old data), adapters, duplication — e.g. `seqkit stats`, FastQC. Log output.
- FASTQ → variants requires alignment (e.g. BWA-MEM to a named reference) + variant calling (e.g. bcftools/GATK). That is sequencing analysis, not genealogy magic: state compute/time needs, record reference + parameters, and prefer a provider's own BAM/CRAM/VCF if one exists.
- Converting BAM/CRAM back to FASTQ (`samtools fastq`) only recovers what the alignment file retained (see lossy CRAM above).

## Consumer genotype files (the common genealogy case)

- Identify vendor from the header comment lines (AncestryDNA exports begin with `#AncestryDNA raw data download`; 23andMe with `# This data file generated by 23andMe`; MyHeritage/FTDNA are CSV with quoted fields). Record chip/version if stated; note stated build (most legacy exports are GRCh37; newer may differ — verify in header, don't assume).
- Validate before use: expected columns (`rsid, chromosome, position, allele1, allele2` or combined `genotype`), plausible SNP count for the chip, chromosomes present (incl. X, Y, MT where provided), no-calls (`--` / `00` / blank) rate. `scripts/dna_file_check.py` does this detection/counting on a copy.
- **Cross-company uploads** (with consent) change match databases, not the underlying kinship: log every upload destination + date + opt-in/out settings. Raw files from different chips overlap only partially; imputed or merged files must be labelled as such and never passed off as a lab original.
- **Merging multiple tests of one person** can increase coverage but creates artefacts; record sources per file, keep originals separate, label the merge `derived`, and never merge two *different people* (a classic silent error — one file per tester folder, checksum-verified).
- Sex chromosome / MT fields in SNP exports can hint at sex and maternal haplogroup *only crudely*; a haplogroup claim needs dedicated Y/mtDNA testing or a named prediction tool with its version — report as `POSSIBLE` at best.

## VCF skills (WGS-derived genealogy)

- Read the header: `##reference`, `##contig`, caller (`##source`/GATK/bcftools lines), sample name, and whether it's filtered (`PASS`). A VCF's value depends entirely on caller, reference, and filters — record all three.
- `.gvcf` includes reference-confidence blocks; converting gVCF→VCF needs joint-typing awareness (`bcftools convert --gvcf2vcf` with the reference) — don't treat non-PASS or block records as variants.
- Genealogy use: extract genotypes at rsIDs comparable to consumer panels for matching uploads only where the destination accepts VCF/derived uploads and consent covers it; label derived uploads. For kinship math (shared segments/IBD) use purpose tools (e.g. GEDmatch, DNA Painter) rather than hand-computed VCF diffs.
- Clinical-looking findings in any VCF/WGS file: do **not** interpret health variants. Note "health-related content may be present; not analysed — consider genetic counselling" and stop. Genealogy scope only.

## Tooling map (name the tool; never hand-wave)

| Job | Tool(s) | Notes |
|---|---|---|
| Inspect/convert SAM/BAM/CRAM, QC | samtools, mosdepth (coverage) | Version + reference logged |
| Variant call/query VCF/BCF | bcftools (`view`, `query`, `stats`) | Record filters used |
| FASTQ QC | FastQC, seqkit | Paired-mate checks |
| Liftover GRCh37↔38 | CrossMap, UCSC liftOver, Picard LiftoverVcf | Log chain file; some variants fail liftover — report count |
| Kinship/clustering from genotype files | GEDmatch (consent!), DNA Painter (Shared cM, WATO, chromosome painting), company match tools | Online uploads need explicit consent per destination |
| Haplogroup from Y/mt files | YFull, FamilyTreeDNA projects, MitoYDNA, Haplogrep (mtDNA) | Report tool + version + rank; predictions ≠ lab-confirmed deep SNP tests |
| Local file detection/counts (this skill) | `scripts/dna_file_check.py <file>` | Read-only header/count inspection; no upload, no network |

## File workflow (every DNA file, every time)

1. Intake → consent recorded → checksum → read-only archival copy in `sources/dna/<tester-code>/`.
2. `dna_file_check.py` (or format tool above) on the file; paste tool output into `05-dna.md` file-inventory table.
3. State what the file can answer for the *research question* (and what it cannot — e.g. a mother-only atDNA test can't identify a paternal grandfather alone).
4. Analyse on copies with logged commands/tools; derived files prefixed `derived-` and never mixed with originals.
5. Conclusions into the claim register with documentary corroboration requirements from `dna.md`.
6. Delivery reminds the user where originals live, what was uploaded where (with dates/settings), and how to revoke/delete uploads if they wish.
