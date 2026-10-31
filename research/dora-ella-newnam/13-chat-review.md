# 13 — Chat review: sources of the master biography

Reviewed 28 October 2026 (America/New_York) from Cursor cloud-agent transcripts on repository `CatCorner22/Farm_Moonshot`. Sixteen chats were listed in that environment. **Supplement 29 October 2026 (UTC):** twenty-six accessible cloud agents on the same repo (transcripts fetched with `cursor-cloud-batch-fetch-details`, `includeTranscripts: true`). Findings are folded into `06-dossier.md` and `book/Dora-Ella-Newnam-Stone-A-Life.md`. Living testers and DNA/health files were not used.

## Primary research chats (biography content)

| Chat | URL | What it contributed |
|---|---|---|
| **Dora** (mobile, opened the case) | https://cursor.com/agents/bc-01a17a5a-f7be-70f0-8063-d9a0707aebd1 | Research question; user-supplied Arkansas death certificate (Dora Stone, noon 23 Aug 1926, Ola, cert. 1524, informant Coy, spouse T. A. Stone, parents E. T. Newnam & Mary Smallwood, burial Carters Chapel, residence “Mammoth, Ark.”, apoplexy); studio portrait (family ID only); WikiTree Newnam-49; 1885 marriage lead; 1900 Sturgeon household; McCoy × Sullivan 1917 Ola; Pearl/Mary NUMIDENT; Carter Cove “Newman, Dora” / “Stone, Thomas 1845–1925”; 1920 Tom A. Stone of Perry Co.; no DNA. |
| **Ancestry research skill** | https://cursor.com/agents/bc-2ffa148f-bd17-4e95-beef-aa2f31940c4a | Authored the genealogy-detective skill. **No additional Dora biography facts.** |
| **Dora’s early 1900s** | https://cursor.com/agents/bc-a16def3b-c4be-41e9-846c-f31bc0f8dd81 | 1910 hole; KY/AR/MO/OK/TX/TN Soundex negatives; original Sturgeon ED 99 (not still on the creek as Newnam); enumerator-name conflict; source JPEGs; 1880 Dora 8. |
| **Dora research continuation** | https://cursor.com/agents/bc-0bd3b0b2-ec76-4a5c-93c7-10c0bfe1f312 | 1920 Beattyville original (E.T. in C.B. Burke’s house); Peebles hypothesis tested and not supported; 1900 MO Stone originals; image gallery; merge of parallel PRs; master book. |
| **Dora biography research** (pass 18–30) | https://cursor.com/agents/bc-01a183ca-4028-7f9b-9d4c-34d4ab6671f6 | FAG Carter **S117–S118**; Louisa/Larkin Mays FAN (**C130–C192**); Greene Stone rejects (**C200–C202**); Vestie 1958 DC; Word `.docx` kept current. |
| **Dora master biography** | https://cursor.com/agents/bc-01a18285-696d-761f-be7a-74d897313200 | HTML book `book/index.html`; Greene **Thomas A. Stone** sh 18A (**C117**); PR #13–#15 — no new P001 residence beyond case file. |
| **Dora Word book + git sync** | https://cursor.com/agents/bc-3b441f4a-2cce-5eb2-bfc4-5a210a6ac0ce | `.docx` / git hygiene; § *Places: 1900 to death*. |
| **Dora location search** (orchestrator) | https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03 | Goal: locations **1900 → death**; spawned web-search workers. |
| **Dora 1900–1912 location web search** | https://cursor.com/agents/bc-e3326e8c-597f-53c8-b831-fd8cc5dec482 | **C203** Rosa Banks; **C204** transcripts; **L147–L160**. |
| **Dora 1913–1926 location web search** | https://cursor.com/agents/bc-359a99fe-a390-5c02-a0a4-986d794942fa | **L162–L169**; Carter gazetteer; **no new PROVEN residence** beyond Coy 1917 Ola and 1926 death. |
| **Review Farm_Moonshot project chats** | https://cursor.com/agents/bc-281c57f3-937a-5920-aa1c-3d8221b38f54 | Inventory pass (**L161**); **B046** ED 200 lead. |


## Helper chats (extractors, not new fieldwork)

These internal runs parsed the transcripts above. They did not create new claims. Unique facts they surfaced (Pearl 1910 with Elizabeth; NUMIDENT; 1870 Samuel; DC particulars) were already in the primary chats and are now in the dossier.

| Chat | URL |
|---|---|
| Parse original Dora transcript | https://cursor.com/agents/bc-8286c652-a1aa-5dbb-ab90-cc2b8895ee94 |
| Extract Dora research state (this environment) | https://cursor.com/agents/bc-62de7db1-7290-5623-bc0c-8367354d88a5 |
| Summarize latest Dora findings | https://cursor.com/agents/bc-becce541-0459-5d97-b5f0-409bad2e072a |
| Extract Pearl breakthrough | https://cursor.com/agents/bc-589f63df-4d1c-5cc3-99e8-c31bef2eb44a |
| Summarize Pearl breakthrough from transcript | https://cursor.com/agents/bc-4bc6adb0-9219-5895-986c-fa21e5cbeb24 |
| Summarize latest Dora research | https://cursor.com/agents/bc-352be520-d192-5b41-a04b-1dea8135a1a3 |
| Extract Dora research state (earlier) | https://cursor.com/agents/bc-41e4c7da-d929-5e23-b808-89ad12711316 |
| Summarize original Dora chat | https://cursor.com/agents/bc-95a4d0c6-b500-5aa3-b9d3-eca0e43fdb58 |
| Summarize early-1900s Dora chat | https://cursor.com/agents/bc-a00fe62a-a1b3-5693-9ded-09fde0d88e90 |
| Summarize extract/pearl helper chats | https://cursor.com/agents/bc-98b5c0ac-172b-555e-8d60-7d06811e0b69 |
| Parse ancestry skill transcript | https://cursor.com/agents/bc-ddbf6d0b-4e48-5086-b854-d359ec987b09 |

## Failed browser hunts (no biography content)

Ancestry and FamilySearch browser sub-agents that died at start (Cloudflare / ERROR). They did not add facts.

- https://cursor.com/agents/bc-3db016fa-fdb4-5c11-981a-ff0769a16da0
- https://cursor.com/agents/bc-5f387719-eeb1-5806-8407-93ba585780ac
- https://cursor.com/agents/bc-9759714e-33fc-55d4-99c3-0a1fd082a36b
- https://cursor.com/agents/bc-12ae958f-d3cf-532c-8bf7-db037fd78879

## Facts the chats had that a thin GPS file can drop

Folded into the book and dossier in this pass:

1. Death-certificate particulars: noon, housework, apoplexy one day, Dr. Thos. W. Beal, Mammoth, file ~1524, dist. 676, buried 24 Aug 1926.
2. User portrait exists and is not independently identified.
3. Pearl’s Banford birthplace, 1910 Buck Creek household, 1922 Elizabeth will, 1920 Clyde Jackson household, 1980 Shelby Co. TN death.
4. Mary Magdalene NUMIDENT (Bunch; 12 Jun 1893 vs 1900 Jun 1892).
5. McCoy’s 1917 Ola marriage, 1920 Danville, 1930 return to Owsley.
6. 1880 Dora 8 in Elias’s house — recovered after the first chat’s free-search miss.
7. Two marriages only; Peebles not supported.
8. 1910 Sturgeon ED 99 original: not as Newnam; dwelling 67 reoccupied.
9. 1920 E.T. Newman, grandfather, in the Beattyville postmaster’s house.
10. Tom A. Stone 1920 Perry Co. probable, 1900 MO candidates all rejected or unmerged.

### Locations 1900 → 23 Aug 1926 (chat-sourced; see `03-timeline.md`)

| When | Place (confidence) | Chat source | In book/dossier? |
|---|---|---|---|
| 1 Jun 1900 | Sturgeon, Lee Co., KY hh **67/67** (**PROVEN**, census) | bc-01a17a5a, bc-a16def3b, bc-01a18285 | Yes |
| Apr 1910 | **Not** Sturgeon ED 99 as Newnam; not KY/AR/MO Soundex ~39 (**negative**) | bc-a16def3b, bc-0bd3b0b2 | Yes |
| Apr 1910 | Parents Proctor ED 100; Pearl Owsley Buck (**FAN**, not P001 residence) | bc-a16def3b | Yes |
| 18 Feb 1917 | Coy marries at **Ola**, Yell Co., AR (**PROVEN**, license) | bc-01a17a5a | Yes |
| Jan 1920 | **Not** KY/AR Soundex as Dora ~48 (**negative**) | bc-0bd3b0b2, bc-a16def3b | Yes |
| Jan 1920 | E.T. Newman in **Beattyville** (C.B. Burke hh) — grandfather, not Dora | bc-0bd3b0b2 | Yes |
| Jan 1920 | Tom A. Stone **Howell Twp, Perry Co., AR** (**PROBABLE** m2 husband) | bc-01a17a5a | Yes |
| Jan 1920 | **ED 200** Ola read (**C213** nil P001; **C214** homonyms rejected) | bc-01a17a5a; **L184** | Yes |
| 1920–1925 | m2 Stone; Yell/Perry license unread (**PROBABLE**) | bc-01a17a5a | Yes |
| 23–24 Aug 1926 | Death **Ola**; burial **Carters Chapel** / Carter Cove (**C206**) | bc-01a17a5a (user DC) | Yes |

**Chat-only FAN (not P001 residence):** Carters Chapel vs Yell cemetery index; FAG Ola town cemeteries — aligns with **B020**.

## Workspace paths searched (29 Oct 2026)

- `/workspace/README.md` (Farm_Moonshot)
- `/workspace/.cursor/skills/genealogy-detective/` (skill only)
- `/workspace/research/dora-ella-newnam/` (case file; **`13-chat-review.md`**, **`02-log.md` L090+**)
- Cloud-agent transcripts via **cursor-cloud** MCP (`/tmp/cursor/cloud-agent-transcripts/…`)

## Pass 24 (28 Oct 2026, America/New_York)

T623-856 PDF retained (865 pages). Greene ED **39** mapped and visually read for Stone — **nil**. Thomas A. remains reel 855 ED 37 sh 18 A. 1910 Proctor full transcript: no Louisa Mays/Brandenburg; three Dora daughters rejected. TSLA named search still not executed. Word book rebuilt.

## Pass 32 (30 Oct 2026, America/New_York) — all 49 chats

`cursor-cloud-list-cloud-agents` returned **49** accessible agents on `CatCorner22/Farm_Moonshot` (this run + 48 others). Transcripts fetched for running siblings, scan/helper PNG readers, and three review sub-agents. **This VM independently image-read** the 1910 KY Ella Miracode plates and USGenNet wills/deeds; sibling census hits that were **not** re-opened here are labelled **not independently verified**.

**Do not duplicate (siblings still RUNNING):**
- [`bc-b0a6ba89`](https://cursor.com/agents/bc-b0a6ba89-91b4-4a8c-a51c-1725f6ff1f8c) — PR **#29** `cursor/dora-research-pass-21`: T623-**537** hh **85** nativity; Greene T623-**856** ED **42–43** name columns in flight. Reused **C221+** (collision).
- [`bc-995d22ea`](https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03) — PR **#26** OPEN `cursor/dora-locations-1900-death-8d03`: 1900 T623-**839** Liberty ED **4–5**; already finished T624-769 pp **351–434** and 1910 Ella Miracode. **ID collision** with `main` C221–C223. Mid-merge with `origin/main` when last fetched.
- [`bc-0039b8bf`](https://cursor.com/agents/bc-0039b8bf-7edb-593b-82c3-cb59471d392a) — Scan ED5 405–434: **empty transcript**.

### Inventory (49)

| Chat | URL | Class | What it contributed this review |
|---|---|---|---|
| **Genealogy detective project updates** (this run) | https://cursor.com/agents/bc-01a18bb4-e162-785c-9724-86a7c5663bf1 | Primary | Pass 32: Ella reel images **C301+**; wills/deeds; Word rebuild |
| Review running sibling chats | https://cursor.com/agents/bc-012dea72-5247-52b3-91ca-c6af8180be7b | Helper | Nested summary of 4 running chats; **no independent images** |
| Review scan and helper chats | https://cursor.com/agents/bc-4410686b-67f6-5635-888b-5e1198b52db3 | Helper | Nested summary of 20 scan/helpers |
| Review older primary chats | https://cursor.com/agents/bc-3fd159b6-6b21-5c9b-9da9-763c4cdf91a8 | Helper | Nested summary of 19 older primaries |
| Scan 1900 Liberty PNGs | https://cursor.com/agents/bc-b2cfe195-dad1-510f-a5d3-e14453ad915f | Scan | 1900 Liberty even-page sample: **no** infant Letha/Viola Sullivan head; William H. Sullivan 16 servant ED 5. **PNGs not re-read here** |
| **Genealogy detective Dora research** | https://cursor.com/agents/bc-b0a6ba89-91b4-4a8c-a51c-1725f6ff1f8c | Primary RUNNING | PR #29; Ella cards + Hardin 1900 original claimed; **skip duplicate reels** |
| Scan ED5 pages 405–434 | https://cursor.com/agents/bc-0039b8bf-7edb-593b-82c3-cb59471d392a | Scan RUNNING | Empty |
| Scan ED5 census PNGs names | https://cursor.com/agents/bc-55740f1c-00e0-5951-8953-15d6d9d5d758 | Scan | Claimed Liberty ED 5 sh 10A John H. Sullivan + **Dora A. 31** + McCoy W. 7 — **ED stamp disputed** by location agent (**C316**, **B048**) |
| Scan mo233 John band / head / PNGs / mo234 | https://cursor.com/agents/bc-887a76bb-8390-5fe6-a397-34447bdd0d0f · [bc-2eacda92](https://cursor.com/agents/bc-2eacda92-fbec-5222-9084-d4894995d612) · [bc-2c2b6383](https://cursor.com/agents/bc-2c2b6383-4de9-5124-bcaf-8a2e5e4521fb) · [bc-4d290b6c](https://cursor.com/agents/bc-4d290b6c-09a4-5003-9330-57e96bcab7d2) | Scan | 1910 MO Soundex S-415/S-435 samples: **nil** Bollinger / Letha / Viola / John H. Sullivan head. **Not re-read here** |
| TSLA death search Rissie | https://cursor.com/agents/bc-b43a15fd-3e65-5113-9179-222ec8344456 | Failed | ERROR, empty; TSLA still not name-queried |
| B043 sweep; Close B023/B044/B043; Goal audit; B046 ED 200; B042–B045 | https://cursor.com/agents/bc-8e76cea0-c388-5c48-a33d-243f2e5d63b5 · [bc-cc229b3e](https://cursor.com/agents/bc-cc229b3e-5272-5612-ab17-04537c722c44) · [bc-7ca3e767](https://cursor.com/agents/bc-7ca3e767-4efb-549f-900c-e5f362c805de) · [bc-8288e8fb](https://cursor.com/agents/bc-8288e8fb-8eb6-57ad-887f-c07fba5b98e8) · [bc-f3cfb3e7](https://cursor.com/agents/bc-f3cfb3e7-759e-5add-bde6-3939f547f485) | Helper | Location/book closers already in **C213–C219** / **C216**; no new independently verified P001 line |
| Book/PR helpers | https://cursor.com/agents/bc-cb3a3891-3e21-51a9-8a3c-78e22ea353f6 · [bc-3796a2aa](https://cursor.com/agents/bc-3796a2aa-d5db-5a1d-b141-eee0ff23fd1a) · [bc-e8dfdb73](https://cursor.com/agents/bc-e8dfdb73-a6e4-53b4-b343-d8fb8c6fb7d1) · [bc-cd08a20a](https://cursor.com/agents/bc-cd08a20a-763d-5a53-b340-4930221d6f8e) · [bc-00e3bde6](https://cursor.com/agents/bc-00e3bde6-2d2d-5097-8628-cfb202372bf1) | Helper | Git/book only |
| **Dora location search** | https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03 | Primary RUNNING | PR **#26**. Claims (***not independently verified here***): Hardin Gray 1910 original would DISPROVE **C194** (their C225); Letha 12 servant ED 4 **POSSIBLE** (their C244); Dora E. Stone 37 MO ED1 and Dora Newnam 36 IN ED2 **rejected**; Hardin K. Gray 7 Sep 1967 vol 042 #20591 **index only**. **ID collision** with `main` C221–C223 |
| **Dora biography research** | https://cursor.com/agents/bc-01a183ca-4028-7f9b-9d4c-34d4ab6671f6 | Primary | Already in dossier (C130–C223, Word) |
| **Dora master biography** | https://cursor.com/agents/bc-01a18285-696d-761f-be7a-74d897313200 | Primary | HTML book; C117 |
| **Dora Word book + git sync** | https://cursor.com/agents/bc-3b441f4a-2cce-5eb2-bfc4-5a210a6ac0ce | Helper | `.docx` hygiene |
| **Dora 1900–1912 / 1913–1926 web search** | https://cursor.com/agents/bc-e3326e8c-597f-53c8-b831-fd8cc5dec482 · [bc-359a99fe](https://cursor.com/agents/bc-359a99fe-a390-5c02-a0a4-986d794942fa) | Primary | C203 Rosa Banks; C204 transcripts; no new PROVEN 1913–26 residence |
| **Review Farm_Moonshot project chats** | https://cursor.com/agents/bc-281c57f3-937a-5920-aa1c-3d8221b38f54 | Helper | Prior inventory (**L161**) |
| **Dora / early 1900s / continuation** | https://cursor.com/agents/bc-01a17a5a-f7be-70f0-8063-d9a0707aebd1 · [bc-a16def3b](https://cursor.com/agents/bc-a16def3b-c4be-41e9-846c-f31bc0f8dd81) · [bc-0bd3b0b2](https://cursor.com/agents/bc-0bd3b0b2-ec76-4a5c-93c7-10c0bfe1f312) | Primary | Already the biography spine |
| **Ancestry research skill** | https://cursor.com/agents/bc-2ffa148f-bd17-4e95-beef-aa2f31940c4a | Helper | Skill only |
| Extract/summarize helpers (10) | bc-8286c652, bc-62de7db1, bc-becce541, bc-589f63df, bc-4bc6adb0, bc-352be520, bc-41e4c7da, bc-95a4d0c6, bc-a00fe62a, bc-98b5c0ac, bc-ddbf6d0b | Helper | No independent facts |
| Ancestry/FS browser hunts (4) | bc-3db016fa, bc-5f387719, bc-9759714e, bc-12ae958f | Failed | ERROR at start |

**Count check:** primary + running + scan + helper + failed = **49** listed in the cloud catalog (including this run and the three review sub-agents spawned for this pass).

### Sibling claims **not** filed as PROVEN here

1. **C194 vs their C225** — **resolved in pass 33** (**C317** / **C318**). Their fam-248 number is Miracode, not original visitation (**C319**).
2. **Their C235** — Hardin K. Gray 7 Sep 1967 vol 042 #20591: statewide index **not seen**; Lee 1967 extract still **nil** (**C311**).
3. **Their C244** — Letha 12 servant, Jesse Conrad, Liberty ED 4: **POSSIBLE FAN**, image not re-seen.
4. **pdfp0367** Sullivan/Dora A./McCoy W. — ED stamp disputed (**C316**, **B048**).
5. **Their C249/C250** — 1910 Bollinger Dora E. Stone 37 MO / Dora Newnam 36 IN: location agent **rejected**; not re-seen.

** collides with `main`:** do **not** reuse C221–C250 / L245–L287. This pass is **C301+ / L301+ / S301+**.

## Instruction for the next chat

Treat `book/Dora-Ella-Newnam-Stone-A-Life.md` and `06-dossier.md` as the combined master. Rebuild Word with `python3 scripts/build_dora_word.py` and PDF with `python3 scripts/build_dora_book.py` after narrative edits. **B011** first (Posa/cert 1524). Skip Greene ED 42–43, T623-839, and T623-537 hh 85 while PR #26/#29 run. Do not reopen Peebles as a third marriage without a license. Do not print 1868 or 24 February 1906 as facts. Redact living people. Ancestry remains 403 from this VM — one user ask: screenshot of AR Death Index **Posa/Dora Stone** cert **1524** and Tom/T.A. Stone **1925**.

## Pass 33 (30 Oct 2026, America/New_York) — all 53 chats

`cursor-cloud-list-cloud-agents` returned **53** accessible agents (was 49). Four new internal summarizers (`bc-e5f39fe4`, `bc-d50aea9c`, `bc-02919df5`, `bc-3a362662`) nested prior chats and **did not re-open images**. PR **#29** (`bc-b0a6ba89`) is now **IDLE**; PR **#26** (`bc-995d22ea`) still **RUNNING** on T623-839 Liberty odds + 1900 MO Soundex S-415. Scan ED5 `bc-0039b8bf` transcript still **empty**.

**This VM independently re-read** gallery plate `1910-lee-ky-ed99-p576.jpg` (ED 99 sh **13 B**): **Gray, Hardin** + **Vista** at dw **241** fam **251** (**C317**). **C194 DISPROVED.** Original fam **248** is Treadway (**C319**). Sibling “fam 248” followed Miracode **0248**.

**Do not duplicate (siblings still in flight):**
- [`bc-995d22ea`](https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03) — PR **#26**: T623-**839** Liberty ED **4–5** + 1900 S-415. They also claim T623-537 hh 85 original and T624-769 pp 351–434 **done**.
- [`bc-b0a6ba89`](https://cursor.com/agents/bc-b0a6ba89-91b4-4a8c-a51c-1725f6ff1f8c) — PR **#29** IDLE: Greene T623-**856** ED **42–43** name columns (their conclusion: **nil** Thomas A. Stone). Do not re-sweep those sheets here until the PR merges.
- [`bc-0039b8bf`](https://cursor.com/agents/bc-0039b8bf-7edb-593b-82c3-cb59471d392a) — Scan ED5 405–434: empty transcript.

### Sibling claims still **not** filed as PROVEN here

1. **Their C235** — Hardin K. Gray 7 Sep 1967 vol 042 #20591: statewide index **not seen**; Lee 1967 extract still **nil** (**C311** / **L320**).
2. **Their C244** — Letha 12 servant, Jesse Conrad, Liberty ED 4: **POSSIBLE FAN**, image not re-seen.
3. **pdfp0367** Sullivan/Dora A./McCoy W. — location agent: Crooked Creek ED **1**, not Liberty ED 5. **No local PNG** (**C316**, **B048**, **L318**).
4. **Their C249/C250** — 1910 Bollinger Dora E. Stone 37 MO / Dora Newnam 36 IN: location agent **rejected**; not re-seen.
5. **Their C191 original-backed hh 85** — skip T623-537 while PR #29 holds the nativity crop.

** collides with `main`:** do **not** reuse C221–C250 / L245–L287. This pass is **C317+ / L317+ / S311+**.

## Pass 34–36 (30 Oct 2026, America/New_York) — 56 then 58 then 59 chats

`cursor-cloud-list-cloud-agents` (`includeArchived`) returned **56** (pass 34), **58** (pass 34/35 filing), then **59** (pass 36). New since pass 33: nested review helpers (`bc-01571c02`, `bc-554687c0`, `bc-b9ee7cdf`, `bc-929b8124`, `bc-f672cc5c`, `bc-28cdb8cd`). None of those helpers opened original images.

**This branch independently image-read** (passes 34–36): T624-769 PDF **366/369** headers (**C323** ED 1 sequence); ED **1** sh **10 A** PNG (**C338** Rhodes, not Stone; **C339** John H. not Sullivan); 1900 Sturgeon hh **84** (**C326** William age **53**); 1910 William crop (**C321**); 1870 Proctor **333a** original (**C356**); 1870 Silas **336b–337a** original (**C348**); 1880 G-600 Elisha/Caroline/Lewis cards (**C342–C344**); 1920 N-550 p.4205 invert (**C325** Dowsjal, not Ella 48).

**NEW independently image-backed P001 1900–1926 residence: NONE.**

**MUST NOT import:** PR #26 **C249** “Dora E. Stone” — same PNG is **Rhodes, Henry C.** + **Dora M.** 37 MO (**C338**). Helper `bc-929b8124` “verified YES” from filename — surname is wrong. Scan `pdfp0367` Sullivan/Dora A./McCoy W. is the same ED 1 sh 10 A misread. Do not steal **C221–C250 / L245–L287** or **their C260–C262**.

**Do not duplicate (siblings in flight):** Greene T623-856 ED **42–43** remaining B-sides; T623-**839** Liberty; T623-**537** hh **85**. PR **#26** OPEN MERGEABLE (Pass **54** committed `90785ab`). PR **#29** OPEN CONFLICTING. PR **#30** this branch. ED5 scan `bc-0039b8bf` transcript still empty.

Full 59-agent table: `/tmp/dora-pass36/chat-review-pass36.md`.


# Pass 37 (30 Oct 2026 ~09:24Z) — cloud-agent catalog **60** (was **59** on pass 36; **58** on pass 34/35)

`cursor-cloud-list-cloud-agents` (`includeArchived: true`, `limit: 200`, `offset: 0`) → **60** / `hasMore: false` / `totalMatched: 60`. Archived: **0**. Killed: **0**. Statuses: **IDLE 51 · RUNNING 4 · ERROR 5**.

This nested reviewer is `bc-fa32244b-c7f6-596c-97b5-2df617923c9b` (“Review all cloud chats”) — **RUNNING**, transcript **empty** (`{"messages":[]}`). Parent case agent `bc-01a18bb4-e162-785c-9724-86a7c5663bf1` (“Genealogy detective project updates”, branch `cursor/dora-continue-chat-review-3bf1`) **RUNNING** — **identity + PR #30 diff-metadata only**; own transcript **not** fetched.

Transcripts: `/tmp/cursor/cloud-agent-transcripts/2026-10-30T09-24-28Z-e3c1/` (50 with transcripts+diff) + `…09-25-21Z-4cee/` (9 remaining) + `…09-24-28Z-43c7/` (parent, diff only). **59** transcripts fetched. Empty (`{"messages":[]}`, 21 bytes): `bc-fa32244b`, `bc-0039b8bf`, `bc-b43a15fd`, `bc-3db016fa`, `bc-5f387719`, `bc-9759714e`, `bc-12ae958f`. Sidecar: `/tmp/dora-pass37/catalog.json`.

**Watch (still skip while in flight):** Greene T623-856 ED **42–43** remaining B-sides (PR #26 Pass 54 sampled; Pass 55 is reading more, **uncommitted**); T623-**839** Liberty ED **5** interior (Pass 55 **in flight**); unread S-415 **John** cards; T623-**537** hh **85** nativity (PR #29 holds it). Do **not** reuse C221–C250 / L245–L287 or PR #26 C260–C262 **or in-flight C263–C266**. Living WikiTree DNA testers: do not research. None named here.

## Catalog count vs prior

| Pass | Count | Delta |
|---|---|---|
| Pass 34 / C335 | 56 | — |
| Pass 34/35 (`/tmp/dora-pass34/chat-review-pass34.md`) | **58** | +2 helpers |
| Pass 36 (`/tmp/dora-pass36/chat-review-pass36.md`) | **59** | +1 (`bc-28cdb8cd`, then RUNNING/empty) |
| **This pass 37** | **60** | **+1 NEW** |

## NEW agents since Pass 36

**One** new bcId. The other 59 match the Pass 36 catalog (none gone).

| bcId | name | class | status | created (UTC) |
|---|---|---|---|---|
| `bc-fa32244b-c7f6-596c-97b5-2df617923c9b` | Review all cloud chats | helper (this nested Pass 37 review) | **RUNNING**; transcript **empty** | 2026-10-30 09:23:01 |

**Status/content change, not new:** `bc-28cdb8cd` (Pass 36 nested reviewer) **RUNNING/empty → IDLE, 107 msgs**. It wrote `/tmp/dora-pass36/chat-review-pass36.md`. No images. Do not treat as fieldwork.

## Independently image-backed P001 1900–1926 hits

**NO.** None. No sibling transcript in this fetch asserts a new P001 census/residence line for 1900–1926 that this branch independently re-read from an original image.

Residence chain on this case is unchanged: **1900 Sturgeon C011 → 1910 UNKNOWN → 1917 Ola Coy C027 → 1926 Ola/Carter**.

Pass 54 on PR #26 is **negatives and FAN**, not a P001 pin. Pass 55 (in flight) found a **Dora E. wife** opening T623-839 p.**1124** (Liberty ED **5** continuation) and is identifying the husband — they currently guess **Cato, William** and plan to **reject** vs P001. **This pass did not re-read p1123–1124.** Treat as **unverified sibling saying**, not a hit.

Citation for the NO: grepped `bc-995d22ea` last ~400 msgs + Pass 54 commit `90785ab` note `sources/census/b040-b007-pass54-2026-10-30.txt`; no committed claim that P001 lived anywhere new 1900–1926.

## Import-do-not list

Do **not** import / do **not** reuse these IDs or readings on this branch:

1. **PR #26 C249 “Dora E. Stone 37, wife of Henry C., Crooked Creek ED 1 sh 10A.”** Same PNG SHA-256 `5eab4793bf42d8c18b7ef43a6296495620392c100c0e1ed8ad59bfe6c4bf769b` independently read here as **Rhodes, Henry C.** + wife **Dora M.[?] 37 MO**, 6-6, m. 18 (**C338**). Birthplace **MO ≠ KY**; husband Rhodes ≠ T.A./Samuel; 6-6 ≠ 7-5; no Sturgeon children. Helper `bc-929b8124` previously “verified YES” C249 as Stone from filename+SHA — **surname is wrong.** PR #26 Pass 54 book text still names “Dora E. Stone … Henry C. Stone (**C249**)”.
2. **C250** Dora Newnam 36 IN, wife of John H., Fillmore ED 2 — IN ≠ KY; Oscar–Anthony ≠ Samuel/Coy set. PNG SHA-256 `34b9dd557be2d0d03ce86ac7cba15f2bc67f2e1276ec029f558375c1d399864c`.
3. **C221–C250 / L245–L287** — ID collision with `main`.
4. **Their C260–C262** (Pass 54 committed) — do not file under those numbers here; not independently verified.
5. **Their C263–C266** (Pass 55 **uncommitted**, drafting in transcript msg 4351) — do not reuse those IDs.
6. **Scan `pdfp0367` as John H. Sullivan + Dora A. 31 + McCoy W. 7 = P001/FAN.** Same ED 1 sh 10A: dw **174** is **John H.** surname **McCamie[?]/Larrille[?]** (**C339**); dw **178** is the Rhodes house (**C338**). `bc-55740f1c` still asserts the Sullivan reading.
7. **Wright, Dora 34 b. Apr 1866 MO** (their C258) — age/place fail vs P001.
8. **Pass 55 p1124 “Dora E. wife”** — not identified in a committed claim; they lean Cato/William reject. **Not P001 until independently image-read.**
9. **T623-537 hh 85 nativity** while PR #29 holds it.
10. **Living WikiTree DNA testers** — do not research.

Skip-reels (siblings own them): Greene remaining B-sides, T623-839 Liberty interior, T623-537 hh 85.

## PR #26 — latest pass vs what we independently verified

Agent `bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03`. GitHub **OPEN / MERGEABLE / CLEAN**. Branch `cursor/dora-locations-1900-death-8d03`. Title unchanged: “Dora research: 1870 Elias original, 1910 Ella Miracode, birth-to-death pass”. Updated 09:11:37Z.

| | Pass 36 fetch | This Pass 37 fetch |
|---|---|---|
| Messages | **4116** | **4351** (+235) |
| Last **committed** pass | **54** `90785ab` 09:10:41Z | **still 54** `90785ab` (HEAD unchanged) |
| In flight | not started 55 | **Pass 55 running** (turn-42; crops `/tmp/b007-pass55/ed5/`) |
| GitHub files | 76, +564/−72 | 76, +564/−72 |
| cursor diff-metadata | +1344/−878, 75 files | **+1387/−878, 76 files** |

### What they **committed** (Pass 54) — sibling sayings, **not** independently re-read here

- **C260** Liberty ED **4** sh **1A–4B** (T623-839 pp **1091–1098**) **nil** Sullivan/Letha/Newnam. Child Dora Snider on 1A; “Store, Thomas” on 2B ≠ Stone.
- **C261** 1900 S-415 **William** window, T1055 roll **249** (~PDF 200–275): St Louis/Adair/Cape Girardeau/Franklin/Randolph/Buchanan/Jackson/Iron/Caldwell — **no Bollinger**.
- **C262** Greene ED **42–43** B-sides **sampled** nil Stone (ED 42 listed in their L311; ED 43 **259, 265**; Binis hh p.259 wife Ella — Springfield, not P001). Residual unread B-sides remained at commit time.

### What they **claim now vs what **this case independently verified**

| Their claim | Their status | Independently verified here? |
|---|---|---|
| C249 Dora E. **Stone** / Henry C. | still in their book as Stone reject vs P001 | **YES as household, NO as Stone** — **C338 Rhodes, Henry C. + Dora M.[?]** |
| C250 Dora Newnam 36 IN | they already reject vs P001 | **Not re-read this pass**; reject stands on identifiers |
| C244 Letha 12 servant | POSSIBLE FAN | **Not re-read** |
| C245 John Sullivan + Sarah Newman MIL | FAN | **Not re-read** |
| C255–C257 S-415 / Huffman withdrawal | their Pass 52 | **Not re-read** |
| C258–C259 Wright Dora / Greene A-sides | Pass 53 | skip-reel / **not re-read** |
| C260–C262 Pass 54 negatives | committed `90785ab` | **NO** |
| C263–C266 Pass 55 | **draft only** (remaining B-sides nil Stone; ED 5 interior nil Sullivan/Letha/Newnam + rejected Dora E wife / child Doras) | **NO** — uncommitted |
| p1124 Dora E. wife (Liberty ED 5, 1900) | identifying husband (leaning Cato William); Fordney dau Dora M p1129 not P001 | **NO** — not a P001 pin even on their saying |

### What Pass 55 is doing **now** (transcript tail, msgs 4170–4351)

- Resume: remaining Greene B-sides + Liberty ED **5** name columns; next IDs they named **L313, C263, S259**.
- They report remaining ED 42/43 B-sides **nil Stone** (vision model “struggling”; treat as weak until committed+re-read).
- ED 5 = **1900** T623-839 pp **1105–1132** (month-of-birth columns). Bridwell dau **Dora C** p1109 = child, not P001.
- **p1124 opens with “Dora E. Wife”** continuing from p1123. They have **not** finished the wider crop. Last thinking: identify that wife, then write Pass 55 claims, rebuild book, commit. **No Pass 55 commit exists.**

## PR #29 status

Agent `bc-b0a6ba89-91b4-4a8c-a51c-1725f6ff1f8c`. **IDLE**. GitHub **OPEN / CONFLICTING / DIRTY**. Branch `cursor/dora-research-pass-21`. 30 files, +176/−26. Two commits: pass 21 `21fa8a0` (07:37:49Z), pass 22 `819751e` (07:50:35Z). Updated 07:50:58Z. **864 msgs** (unchanged vs Pass 36).

Last assistant: fetched `origin/main`, reviewed in-progress merge — **not committed**. Conflict markers remain in `04-evidence.md`, `06-dossier.md`, `11-backlog.md` (B040) and related. ID collision C221–C223 (their Ella/Hardin vs `main` Solomon/William/Greene). p.250 sh **36 A** vs **86 A**. Holds **hh 85** nativity crop — **skip**.

## Open GitHub PRs (`CatCorner22/Farm_Moonshot`)

| PR | Agent | Head | GitHub | Notes |
|---|---|---|---|---|
| **#26** | `bc-995d22ea` | `cursor/dora-locations-1900-death-8d03` | **OPEN MERGEABLE CLEAN** | Pass **54** committed; Pass **55** in chat only |
| **#29** | `bc-b0a6ba89` | `cursor/dora-research-pass-21` | **OPEN CONFLICTING DIRTY** | Merge of `origin/main` uncommitted |
| **#30** | `bc-01a18bb4` (parent) | `cursor/dora-continue-chat-review-3bf1` | **OPEN MERGEABLE CLEAN** | 27 files +2584/−47; title “Dora research passes 32–33…”; last commit `ae2ebe04` 08:18:49Z |

Merged (historical, already on `main`): #28 biography, #27 deep research, #25 locations, #24–#13 biography/book chain, #7/#5/#4 Dora primaries, #3–#1 skill.

## Exact SHA / filenames to copy via `git show` **without merging**

Do **not** merge #26/#29. Copy individual blobs if needed:

```bash
# SHA-256 is file content; git: is the tree blob on that branch
git show origin/cursor/dora-locations-1900-death-8d03:<path> > <local>
```

Branch HEAD: **`90785abc63bbc9ab109e24613e199ee473e80159`** (Pass 54).

| SHA-256 (content) | git blob | path | note |
|---|---|---|---|
| `5eab4793bf42d8c18b7ef43a6296495620392c100c0e1ed8ad59bfe6c4bf769b` | `226c4b7e4b2a71aa3c341bfad19ce8a0763605e1` | `research/dora-ella-newnam/sources/census/1910-bollinger-ed1-dora-e-stone-rejected.png` | **C249 filename.** Already in this working tree (uncommitted) and independently read as **Rhodes (C338)**. Copy only for archive. **Do not import as Stone.** |
| `34b9dd557be2d0d03ce86ac7cba15f2bc67f2e1276ec029f558375c1d399864c` | `9cb228e80cb3a84170a6ec86c535567cde8b331a` | `research/dora-ella-newnam/sources/census/1910-bollinger-ed2-john-h-newnam-dora-rejected.png` | C250 reject |
| `417f903621cefc063a9a069ab604e4ace745348e3bf5bb078dec52058d4a6f0a` | `e1e6d2a0576984b883036a082b2aecbc5ec7a5c0` | `research/dora-ella-newnam/sources/census/1910-bollinger-ed4-letha-sullivan-servant.png` | their C244 FAN; **not P001 residence**; not re-read this pass |
| `b4d6f1ce8d0e71d7908e3a17e01c4525d885e410d5e011ba6ba234651cfefa71` | `9adc5500a8c5dacad120de17b8063e6b9f158bae` | `research/dora-ella-newnam/sources/census/1910-bollinger-ed4-sullivan-newnam-mil.png` | their C245 FAN |
| `9eceebc4aaad36c50842d0755ecaa2d29f6ed6148d9626104d2ffbccc61e0308` | `1cbdfcf302641037409a1a66b837d597dbba786c` | `research/dora-ella-newnam/sources/census/1910-bollinger-ed5-sullivan-letha-e-dau2.png` | rejected age-2 Letha E. |
| `aa56943106e30f0cf2e03cbd9349749a5b4e1695170f8e4f46071157b886831f` | `be6d5e022b64418f0fd9f658093a7a149637fbc9` | `research/dora-ella-newnam/sources/census/1870-owsley-travrest-elias-hh131-pdfp090.jpg` | 1870 Elias original (**pre-1900**, not a 1900–26 P001 pin) |
| `cd0d71c30e7286bc9b475a1fc18c86e4855354694001c821523ad1b00c2831fd` | `0cff923f39795a19ef90a3336ac4dd996f5e9254` | `research/dora-ella-newnam/sources/census/1880-lee-ed59-p738-dw102-flanary.jpg` | 1880 original (pre-1900) |
| `feee3e433ee0a8181e4aaf3a17f8f9acf5ca26d4e2dbf6ad2500458fc22363ee` | `4c742cc8181be0184f5f652cc9d755c53093e669` | `research/dora-ella-newnam/sources/census/1910-lee-ky-ed99-p576-hardin248-crop.jpg` | Hardin crop; this branch already has full plate `1910-lee-ky-ed99-p576.jpg` (**C317**) |

**Do not copy (skip-reels / in-flight):**

- Liberty ED 4/5 pass51–55 PNG folders — **not committed** on #26 (Pass 54 used local PNGs; Pass 55 lives in their `/tmp/b007-pass55/`).
- Greene B-side name crops (`/tmp/b040-pass54/names/` on their VM).
- PR #29 hh 85 nativity `research/dora-ella-newnam/sources/census/1900-lee-ky-ed52-sh5b-hh84-85-nativity.jpg` SHA-256 `e6e7f1c744a50a02ff1e9f1ce5253941f2f6e0f5ef323cd32c541e7a6e228eac` git `ed8daf9776452dd80993fe34ecb9c00944d02183` — **skip while #29 holds T623-537**.

55 other image paths exist only on #26 vs this HEAD (mostly `b007-liberty-ed5-pass48/pdfp0348–0480.png` every-3rd-page 1910 sector). Those are **1910 Bollinger**, already sampled for C244–C250; not new 1900–26 P001 residence. Copy the named rejects/FAN crops above if a local original is missing; do not bulk-merge the folder.

## Primaries / scans (named watch list)

| Agent | Msgs | Status | PR / branch | Now doing |
|---|---|---|---|---|
| `bc-995d22ea` Dora location search | **4351** (was 4116) | **RUNNING** | **#26 OPEN MERGEABLE CLEAN** | **Pass 54 committed.** **Pass 55 in flight:** Greene remaining B-sides + Liberty ED 5; p1124 Dora E. wife ID pending. No Pass 55 commit. |
| `bc-b0a6ba89` Genealogy detective | **864** | **IDLE** | **#29 OPEN CONFLICTING DIRTY** | Pass 21–22 pushed. `origin/main` merge **not committed**; markers remain. Holds hh 85. |
| `bc-0039b8bf` Scan ED5 405–434 | **0** | **RUNNING** | none | Transcript still **empty**. No pages 405–434. |
| `bc-55740f1c` Scan ED5 PNGs | **152** | IDLE | none | Same 54-PNG table. Headline `pdfp0367` Sullivan/Dora A. — **do not import**. |
| `bc-b2cfe195` Scan 1900 Liberty PNGs | **99** | IDLE | none | Unchanged even-page nil; still lists withdrawn William H. Sullivan. |
| `bc-01a183ca` Dora biography | **3417** | IDLE | **#28 MERGED** | No new 1900–26 P001 pin. |
| `bc-01a18bb4` parent | — | **RUNNING** | **#30 OPEN** | Identity only this review. |
| `bc-28cdb8cd` Pass 36 reviewer | **107** | IDLE | none | Wrote pass-36 report; no images. |
| `bc-fa32244b` this review | **0** | **RUNNING** | none | Empty; in flight. |

## Sibling claims still **not** independently verified on this case

1. Their **C235** Hardin K. Gray 7 Sep 1967 vol 042 #20591 (index only; Lee 1967 extract **nil** / **C311**).
2. Their **C244** Letha 12 servant, Jesse Conrad, Liberty ED 4.
3. Their **C245** John Sullivan hh, Sarah Newman 60 MIL + Oscar 21 BIL.
4. **pdfp0367** as Liberty ED 5 sh 10A Sullivan/Dora A./McCoy W. — this branch: Crooked Creek ED 1 (**C316** / **C323** / **C338–C339** / **B048**).
5. Their **C250** Dora Newnam 36 IN (already rejected; image not re-seen this pass).
6. **T623-537 hh 85** nativity — skip while #29 holds it.
7. Their **C255–C257, C258–C259**.
8. Their **C260–C262** (Pass 54).
9. Their **C263–C266** and p1124 Dora E. wife (Pass 55 uncommitted).
10. 1900 Liberty extra FAN from `bc-b2cfe195` (Simon P. ED 51; John H. 40 ED 3).
11. L312 Binis / Ella p.259 Springfield.

*(Hardin 1910 original is already **C317** here. C194 DISPROVED. C249-as-Stone DISPROVED as surname via **C338**.)*

## ED5 transcript

`bc-0039b8bf-7edb-593b-82c3-cb59471d392a` — **empty**: `{"messages":[]}`. Status still **RUNNING**. No pages 405–434 were read in any fetched chat.

## Full catalog (60)

Newest first, as returned. Msgs from fetched `transcript.json` (`messages` length). Parent = identity only.

| # | bcId | name | status | created (UTC) | msgs | PR | empty? | 1-line finding |
|---|---|---|---|---|---:|---|---|---|
| 1 | `bc-fa32244b-c7f6-596c-97b5-2df617923c9b` | Review all cloud chats | **RUNNING** | 2026-10-30 09:23:01 | 0 |  | yes | NEW this nested Pass 37 reviewer; transcript empty (in flight); identity only. |
| 2 | `bc-28cdb8cd-212b-57bc-af34-4e66f5fa62bf` | Review all Dora cloud chats | **IDLE** | 2026-10-30 09:10:07 | 107 |  | no | Pass 36 nested reviewer; now IDLE with 107 msgs (was empty/RUNNING last pass); wrote `/tmp/dora-pass36`; no images. |
| 3 | `bc-f672cc5c-c4fd-5ed0-a1fe-3ee8490bd474` | Review all Dora chats | **IDLE** | 2026-10-30 08:56:13 | 147 |  | no | Pass 34/35 nested catalog (58 agents); no images. |
| 4 | `bc-929b8124-6bf2-5c95-a507-70dea3e72f5b` | Review running chat transcripts | **IDLE** | 2026-10-30 08:39:36 | 115 |  | no | Helper; earlier wrongly treated C249 filename as Stone; last text still does not retract surname error (C338 Rhodes). |
| 5 | `bc-01571c02-d829-5f15-92db-ab8f34af1c1d` | Review remaining cloud chats | **IDLE** | 2026-10-30 08:22:03 | 144 |  | no | Helper nested remaining chats (catalog 56); no fieldwork. |
| 6 | `bc-554687c0-96cf-5d4e-bf70-ed0f37f02406` | Summarize PR26 transcript | **IDLE** | 2026-10-30 08:10:16 | 87 |  | no | Helper summarized PR #26 at 3412 msgs (now stale vs 4351). |
| 7 | `bc-b9ee7cdf-0249-5215-9f62-57aa37f0ecc1` | Summarize sibling+helper chats | **IDLE** | 2026-10-30 08:10:16 | 70 |  | no | Helper sibling+scan summary; noted ED5 empty. |
| 8 | `bc-e5f39fe4-de72-5c8b-8a7c-484a187312e0` | Summarize remaining helper transcripts | **IDLE** | 2026-10-30 07:50:00 | 137 |  | no | Helper remaining helpers; MO Soundex PNG not re-read. |
| 9 | `bc-d50aea9c-69e1-54d3-a241-586a10cf4171` | Summarize review-helper transcripts | **IDLE** | 2026-10-30 07:45:24 | 74 |  | no | Helper review-of-reviewers; no fieldwork. |
| 10 | `bc-02919df5-2e86-5974-941a-35f559593645` | Summarize running sibling transcripts | **IDLE** | 2026-10-30 07:45:24 | 73 |  | no | Helper running-sibling summary; ED5 empty. |
| 11 | `bc-3a362662-09b7-59a0-949b-571159302c05` | Summarize census-scan transcripts | **IDLE** | 2026-10-30 07:45:24 | 45 |  | no | Helper census-scan summary; PNG blobs not in JSON. |
| 12 | `bc-012dea72-5247-52b3-91ca-c6af8180be7b` | Review running sibling chats | **IDLE** | 2026-10-30 07:29:58 | 162 |  | no | Helper nested running siblings; no independent images. |
| 13 | `bc-4410686b-67f6-5635-888b-5e1198b52db3` | Review scan and helper chats | **IDLE** | 2026-10-30 07:29:58 | 131 |  | no | Helper nested 20 scan/helpers. |
| 14 | `bc-3fd159b6-6b21-5c9b-9da9-763c4cdf91a8` | Review older primary chats | **IDLE** | 2026-10-30 07:29:58 | 68 |  | no | Helper nested 19 older primaries. |
| 15 | `bc-b2cfe195-dad1-510f-a5d3-e14453ad915f` | Scan 1900 Liberty PNGs for Sullivan | **IDLE** | 2026-10-30 07:29:43 | 99 |  | no | Scan 17 even-page 1900 Liberty PNGs: nil infant Letha/Viola head; still lists withdrawn William H. Sullivan. |
| 16 | `bc-01a18bb4-e162-785c-9724-86a7c5663bf1` | Genealogy detective project updates | **RUNNING** | 2026-10-30 07:27:30 | — | #30 OPEN | n/a | PARENT case agent (this env); identity+PR #30 only — transcript not fetched. |
| 17 | `bc-b0a6ba89-91b4-4a8c-a51c-1725f6ff1f8c` | Genealogy detective Dora research | **IDLE** | 2026-10-29 23:07:09 | 864 | #29 OPEN | no | PR #29 IDLE CONFLICTING; pass 21–22 pushed; origin/main merge uncommitted; markers remain; holds hh 85 nativity. |
| 18 | `bc-0039b8bf-7edb-593b-82c3-cb59471d392a` | Scan ED5 pages 405-434 | **RUNNING** | 2026-10-29 22:31:25 | 0 |  | yes | Scan ED5 405–434 still RUNNING with empty transcript — no PNG claims. |
| 19 | `bc-55740f1c-00e0-5951-8953-15d6d9d5d758` | Scan ED5 census PNGs names | **IDLE** | 2026-10-29 22:18:38 | 152 |  | no | Scan 54 PNGs; still asserts pdfp0367 John H. Sullivan + Dora A. 31 as Liberty ED 5 — do not import (C338/C339). |
| 20 | `bc-887a76bb-8390-5fe6-a397-34447bdd0d0f` | Scan mo233 John band PNGs | **IDLE** | 2026-10-29 21:53:31 | 95 |  | no | MO Soundex S-415 John-band sample: nil Bollinger/Letha head. |
| 21 | `bc-2eacda92-fbec-5222-9084-d4894995d612` | Scan mo233 head PNGs Sullivan | **IDLE** | 2026-10-29 21:45:25 | 149 |  | no | MO Soundex S-415 head PNGs: nil target Sullivan head. |
| 22 | `bc-2c2b6383-4de9-5124-bcaf-8a2e5e4521fb` | Scan mo233 PNGs for Sullivan | **IDLE** | 2026-10-29 21:41:36 | 147 |  | no | MO Soundex mo233 Sullivan sample: nil Letha/Viola/John H. head. |
| 23 | `bc-4d290b6c-09a4-5003-9330-57e96bcab7d2` | Read MO soundex PNGs Sullivan | **IDLE** | 2026-10-29 21:37:02 | 82 |  | no | MO Soundex S-435 (Shelton band) pass49: not Sullivan. |
| 24 | `bc-b43a15fd-3e65-5113-9179-222ec8344456` | TSLA death search Rissie | **ERROR** | 2026-10-29 20:47:26 | 0 |  | yes | ERROR empty; TSLA Rissie still not name-queried. |
| 25 | `bc-8e76cea0-c388-5c48-a33d-243f2e5d63b5` | B043 sweep + goal completion | **IDLE** | 2026-10-29 17:24:07 | 272 |  | no | Closed B043 Yell 1910 IA sweep nil P001 (already in dossier C153). |
| 26 | `bc-cc229b3e-5272-5612-ab17-04537c722c44` | Close B023 B044 B043 location | **IDLE** | 2026-10-29 16:26:57 | 294 |  | no | Closer: no new P001 residence pin. |
| 27 | `bc-7ca3e767-4efb-549f-900c-e5f362c805de` | Goal audit + location backlog | **IDLE** | 2026-10-29 16:07:24 | 222 |  | no | Location backlog audit; 1900–1926 chain unchanged. |
| 28 | `bc-cb3a3891-3e21-51a9-8a3c-78e22ea353f6` | Book: B046 ED 200 nil | **IDLE** | 2026-10-29 15:44:42 | 45 |  | no | Book fold-in of B046 ED 200 nil. |
| 29 | `bc-3796a2aa-d5db-5a1d-b141-eee0ff23fd1a` | Sync C146 into book | **IDLE** | 2026-10-29 14:56:39 | 40 |  | no | Synced C146 into book Places; no new pin. |
| 30 | `bc-e8dfdb73-a6e4-53b4-b343-d8fb8c6fb7d1` | B046 fold-in + PR retry | **IDLE** | 2026-10-29 14:56:24 | 334 |  | no | B046 fold-in + PR retry; git/book only. |
| 31 | `bc-cd08a20a-763d-5a53-b340-4930221d6f8e` | Open PR + branch sync | **IDLE** | 2026-10-29 14:56:07 | 47 |  | no | Open-PR/branch sync helper; no research. |
| 32 | `bc-00e3bde6-2d2d-5097-8628-cfb202372bf1` | Merge 1913–1926 branch + book | **IDLE** | 2026-10-29 14:55:08 | 113 |  | no | Merge 1913–1926 book helper; could not open PR. |
| 33 | `bc-8288e8fb-8eb6-57ad-887f-c07fba5b98e8` | Execute B046 1920 Ola census | **IDLE** | 2026-10-29 14:52:21 | 278 |  | no | Executed B046 1920 Ola ED 200 IA read (C213). |
| 34 | `bc-f3cfb3e7-759e-5add-bde6-3939f547f485` | Follow-up B042–B045 gaps | **IDLE** | 2026-10-29 14:50:55 | 197 |  | no | B042–B045: C146 USGenNet 1910 transcripts nil P001. |
| 35 | `bc-281c57f3-937a-5920-aa1c-3d8221b38f54` | Review Farm_Moonshot project chats | **IDLE** | 2026-10-29 14:48:26 | 117 |  | no | Prior project-chat inventory (L161); B046 lead. |
| 36 | `bc-359a99fe-a390-5c02-a0a4-986d794942fa` | Dora 1913–1926 location web search | **IDLE** | 2026-10-29 14:47:59 | 131 |  | no | 1913–1926 web search; no new PROVEN residence beyond Coy 1917 / 1926 death. |
| 37 | `bc-3b441f4a-2cce-5eb2-bfc4-5a210a6ac0ce` | Dora Word book + git sync | **IDLE** | 2026-10-29 14:47:59 | 145 |  | no | Word book + git hygiene; Places 1900-death. |
| 38 | `bc-e3326e8c-597f-53c8-b831-fd8cc5dec482` | Dora 1900–1912 location web search | **IDLE** | 2026-10-29 14:47:59 | 126 |  | no | 1900–1912 web search; C203 Rosa Banks; no new P001 pin. |
| 39 | `bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03` | Dora location search | **RUNNING** | 2026-10-29 14:47:15 | 4351 | #26 OPEN | no | PR #26 RUNNING 4351 msgs; Pass 54 committed; Pass 55 IN FLIGHT (C263–C266 draft; p1124 Dora E wife unidentified). No P001 pin. |
| 40 | `bc-01a183ca-4028-7f9b-9d4c-34d4ab6671f6` | Dora biography research | **IDLE** | 2026-10-28 18:33:52 | 3417 | #28 MERGED | no | Biography passes 18–31; PR #28 MERGED; no new 1900–26 P001 pin. |
| 41 | `bc-95a4d0c6-b500-5aa3-b9d3-eca0e43fdb58` | Summarize original Dora chat | **IDLE** | 2026-10-28 12:40:01 | 44 |  | no | Summarizer of original Dora chat; no independent images. |
| 42 | `bc-a00fe62a-a1b3-5693-9ded-09fde0d88e90` | Summarize early-1900s Dora chat | **IDLE** | 2026-10-28 12:40:01 | 51 |  | no | Summarizer of early-1900s chat; no independent images. |
| 43 | `bc-98b5c0ac-172b-555e-8d60-7d06811e0b69` | Summarize extract/pearl helper chats | **IDLE** | 2026-10-28 12:40:00 | 49 |  | no | Summarizer of extract/pearl helpers; no fieldwork. |
| 44 | `bc-01a18285-696d-761f-be7a-74d897313200` | Dora master biography | **IDLE** | 2026-10-28 12:39:04 | 2414 | #13 MERGED | no | HTML master biography; C117 Greene Thomas A.; PR #13 MERGED. |
| 45 | `bc-a16def3b-c4be-41e9-846c-f31bc0f8dd81` | Dora's early 1900s | **IDLE** | 2026-10-27 15:14:04 | 1718 | #7 MERGED | no | Early-1900s primary; 1910 hole; Sturgeon ED 99 original; PR #7 MERGED. |
| 46 | `bc-3db016fa-fdb4-5c11-981a-ff0769a16da0` | FamilySearch census browser hunt | **ERROR** | 2026-10-27 13:59:55 | 0 |  | yes | ERROR empty; FamilySearch browser hunt died at start. |
| 47 | `bc-ddbf6d0b-4e48-5086-b854-d359ec987b09` | Parse ancestry skill transcript | **IDLE** | 2026-10-27 13:49:02 | 63 |  | no | Parse ancestry-skill transcript; skill-building only. |
| 48 | `bc-62de7db1-7290-5623-bc0c-8367354d88a5` | Extract Dora research state | **IDLE** | 2026-10-27 13:49:02 | 169 |  | no | Extract research-state helper; no new facts. |
| 49 | `bc-becce541-0459-5d97-b5f0-409bad2e072a` | Summarize latest Dora findings | **IDLE** | 2026-10-27 13:49:02 | 77 |  | no | Summarize latest findings helper. |
| 50 | `bc-589f63df-4d1c-5cc3-99e8-c31bef2eb44a` | Extract Pearl breakthrough | **IDLE** | 2026-10-27 13:49:02 | 77 |  | no | Extract Pearl breakthrough helper. |
| 51 | `bc-8286c652-a1aa-5dbb-ab90-cc2b8895ee94` | Parse original Dora transcript | **IDLE** | 2026-10-27 13:49:02 | 99 |  | no | Parse original Dora transcript helper. |
| 52 | `bc-0bd3b0b2-ec76-4a5c-93c7-10c0bfe1f312` | Dora research continuation | **IDLE** | 2026-10-27 13:47:22 | 4887 | #5 MERGED | no | Continuation primary; 1920 Beattyville E.T.; PR #5 MERGED. |
| 53 | `bc-2ffa148f-bd17-4e95-beef-aa2f31940c4a` | Ancestry research skill | **IDLE** | 2026-10-27 10:46:44 | 393 | #1 MERGED | no | Authored genealogy-detective skill; PR #1 MERGED; no Dora facts. |
| 54 | `bc-4bc6adb0-9219-5895-986c-fa21e5cbeb24` | Summarize Pearl breakthrough from transcript | **IDLE** | 2026-10-27 10:41:57 | 87 |  | no | Summarize Pearl breakthrough helper. |
| 55 | `bc-5f387719-eeb1-5806-8407-93ba585780ac` | Ancestry Dora browser search | **ERROR** | 2026-10-27 10:01:30 | 0 |  | yes | ERROR empty; Ancestry browser hunt. |
| 56 | `bc-9759714e-33fc-55d4-99c3-0a1fd082a36b` | Ancestry browser Dora search | **ERROR** | 2026-10-27 10:01:06 | 0 |  | yes | ERROR empty; Ancestry browser hunt. |
| 57 | `bc-12ae958f-d3cf-532c-8bf7-db037fd78879` | Ancestry.com Dora research | **ERROR** | 2026-10-27 10:00:54 | 0 |  | yes | ERROR empty; Ancestry.com Dora hunt. |
| 58 | `bc-352be520-d192-5b41-a04b-1dea8135a1a3` | Summarize latest Dora research | **IDLE** | 2026-10-27 09:45:52 | 197 |  | no | Summarize latest Dora research helper. |
| 59 | `bc-41e4c7da-d929-5e23-b808-89ad12711316` | Extract Dora research state | **IDLE** | 2026-10-27 09:30:31 | 74 |  | no | Extract Dora research state helper. |
| 60 | `bc-01a17a5a-f7be-70f0-8063-d9a0707aebd1` | Dora | **IDLE** | 2026-10-26 22:35:47 | 3682 | #4 MERGED | no | Opened the case (DC, WikiTree, 1900 Sturgeon); PR #4 MERGED. |

**Count check:** 60 listed = `totalMatched`. Empty transcripts: 7 (this run + ED5 + 5 ERROR hunts). Parent transcript not fetched.

## Empty / ERROR transcripts

| bcId | name | transcript |
|---|---|---|
| `bc-fa32244b` | this nested review | **empty** `{"messages":[]}` |
| `bc-0039b8bf` | Scan ED5 405–434 | **empty** `{"messages":[]}` (RUNNING) |
| `bc-b43a15fd` | TSLA death search Rissie | **empty** (ERROR) |
| `bc-3db016fa` | FamilySearch census browser hunt | **empty** (ERROR) |
| `bc-5f387719` | Ancestry Dora browser search | **empty** (ERROR) |
| `bc-9759714e` | Ancestry browser Dora search | **empty** (ERROR) |
| `bc-12ae958f` | Ancestry.com Dora research | **empty** (ERROR) |

## Ten most important findings

1. **Catalog 60** (was 59). Only **NEW** agent is this reviewer `bc-fa32244b`. `bc-28cdb8cd` filled in (Pass 36 report) and went IDLE.
2. **No independently image-backed P001 1900–1926 residence.** Chain still 1900 Sturgeon → 1910 hole → 1917 Ola → 1926 death.
3. **PR #26 still Pass 54 on disk** (`90785ab`) but the chat has moved to **Pass 55** (4351 msgs). Do not wait on their uncommitted C263–C266.
4. Pass 55 **p1124 Dora E. wife** (1900 Liberty ED 5) is a same-name collision they are identifying — **not** a P001 hit; **do not steal** that sheet while they are on it (T623-839 skip).
5. **Do not import C249 as Stone** — **C338** Rhodes. Helper `bc-929b8124` still has not retracted the filename-based “Stone” verification. `bc-55740f1c` still publishes the pdfp0367 Sullivan/Dora A. misread.
6. **Do not reuse C221–C250 / L245–L287 / C260–C262 / in-flight C263–C266.**
7. **PR #29 still OPEN CONFLICTING**; merge uncommitted; hh 85 remains theirs.
8. **ED5 `bc-0039b8bf` still empty RUNNING** — pages 405–434 unread in every chat.
9. Copy-without-merge originals worth having: C249/C250/C244/C245 PNGs (SHA-256 above) via `git show origin/cursor/dora-locations-1900-death-8d03:<path>`. Skip Greene B-sides, Liberty interior, hh 85.
10. Open PRs: **#26, #29, #30**. Ancestry still 403; living DNA testers untouched.

## Next chat

Keep skipping Greene 42–43 remaining B-sides / T623-839 / hh 85 until #26/#29 merge or go idle with a finished B-side + ED 5 log. Do not file C249 as Stone (**C338**). Do not file their C260–C266 under those numbers. If Pass 55 commits a p1124 crop, copy via `git show` and re-read independently before any P001 language. Rebuild Word/PDF only after narrative edits on **this** branch. Ancestry still 403; one user ask remains Posa/Dora Stone cert **1524** + Tom/T.A. **1925**.

**Status update on this filing (later 30 Oct 2026, America/New_York):** a second `list-cloud-agents` on this continuation still returned **60** / `hasMore: false`. Nested reviewer `bc-fa32244b` is now **IDLE** (142 messages; catalog above). `bc-28cdb8cd` IDLE. RUNNING: this run `bc-01a18bb4`, PR **#26** `bc-995d22ea`, ED5 `bc-0039b8bf`. ERROR: five Ancestry/FS/TSLA browser hunts, unchanged. **No** new independently image-backed P001 pin. Do **not** import Pass 55 draft **C263–C266** or the in-flight Liberty p.1124 “Dora E. wife” guess.



---

# Pass 38 filing note (30 Oct 2026, America/New_York)

Live re-list after this filing still returned **62** / `hasMore: false`. Nested reviewer `bc-87c7034f` is now **IDLE** (was RUNNING/empty when that nested run started). Parent `bc-01a18bb4` still RUNNING. Independently image-backed P001 1900–1926 residence: **NONE**. Do **not** steal C263–C266 / L313–L316 / S259. C266 on PR #26 is **Dora E. Copley**, not Cato. Full nested catalog follows.

# Pass 38 (30 Oct 2026 ~09:49–09:50Z) — cloud-agent catalog **62** (was **60** on pass 37; **59** on pass 36; **58** on pass 34/35)

`cursor-cloud-list-cloud-agents` (`includeArchived: true`, `limit: 200`, `offset: 0`) → **62** / `hasMore: false` / `totalMatched: 62`. Archived: **0**. Killed: **0**. Statuses: **IDLE 53 · RUNNING 4 · ERROR 5**.

**Count check:** 62 listed = `returned` = `agentCount` = `totalMatched`. `hasMore: false` (no further pages). Gone since 60-catalog: **0**.

This nested reviewer is `bc-87c7034f-e5f6-5607-8a63-67e4a5a3c588` (“Review all cloud chats”) — **RUNNING**, transcript **empty** (`{"messages":[]}`). Parent case agent `bc-01a18bb4-e162-785c-9724-86a7c5663bf1` (“Genealogy detective project updates”, branch `cursor/dora-continue-chat-review-3bf1`) **RUNNING** — **identity + PR #30 GitHub only**; own transcript **not** fetched (forbidden).

Fetched this pass (`batch-fetch-details`, transcripts + diff-metadata + events): **6** agents under `/tmp/cursor/cloud-agent-transcripts/2026-10-30T09-50-11Z-5879/` —

| bcId | why fetched | msgs |
|---|---|---:|
| `bc-87c7034f-e5f6-5607-8a63-67e4a5a3c588` | NEW since 60 | 0 (empty) |
| `bc-dd16e045-050e-55f6-a9ca-de4e3af8848d` | NEW + MUST-FETCH | 64 |
| `bc-fa32244b-c7f6-596c-97b5-2df617923c9b` | MUST-FETCH (was empty RUNNING) | 142 |
| `bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03` | MUST-FETCH PR #26 | 4508 |
| `bc-0039b8bf-7edb-593b-82c3-cb59471d392a` | MUST-FETCH ED5 scan | 0 (empty) |
| `bc-b0a6ba89-91b4-4a8c-a51c-1725f6ff1f8c` | MUST-FETCH PR #29 | 864 |

Unfetched 56 agents reuse Pass 37 findings/message counts (status refreshed from this list). No living WikiTree DNA testers named or researched.

**Watch (still skip while in flight):** T623-**839** leftover work is now **Pass 56** unread S-415 **John** cards (roll **248** between L303 samples) on PR #26; Greene ED **37–41** residual; T623-**537** hh **85** nativity (PR #29 holds it). Do **not** reuse **C221–C266 / L245–L287 / S259** (sibling-owned, including newly **committed** C263–C266 / L313–L316 / S259). Living people: do not research.

## Catalog count vs prior

| Pass | Count | Delta |
|---|---|---|
| Pass 34 / C335 | 56 | — |
| Pass 34/35 (`/tmp/dora-pass34/chat-review-pass34.md`) | **58** | +2 helpers |
| Pass 36 (`/tmp/dora-pass36/chat-review-pass36.md`) | **59** | +1 (`bc-28cdb8cd`) |
| Pass 37 (`/tmp/dora-pass37/chat-review-pass37.md` / full copy `…-full-from-reviewer.md`) | **60** | +1 (`bc-fa32244b`) |
| **This pass 38** | **62** | **+2 NEW** |

## NEW agents since 60-catalog (Pass 37)

Compared 60 Pass-37 `catalog.json` bcIds vs 62 this list: intersection **60**, gone **0**, new **2**.

| bcId | name | class | status | created (UTC) | msgs |
|---|---|---|---|---|---:|
| `bc-87c7034f-e5f6-5607-8a63-67e4a5a3c588` | Review all cloud chats | helper (this nested Pass 38 review) | **RUNNING**; transcript **empty** | 2026-10-30 09:49:24 | 0 |
| `bc-dd16e045-050e-55f6-a9ca-de4e3af8848d` | Summarize nested chat review | helper (Pass 37 compact extract of `bc-fa32244b`) | **IDLE** | 2026-10-30 09:32:57 | 64 |

**Status/content change, not new:**

- `bc-fa32244b` (Pass 37 nested reviewer) **RUNNING/empty → IDLE, 142 msgs** (1 user / 83 assistant / 58 tool). Wrote `/tmp/dora-pass37/chat-review-pass37.md` + `catalog.json`. **Stale:** it recorded Pass 55 as uncommitted and p1124 husband as a **Cato, William** guess.
- `bc-995d22ea` still RUNNING; **4351 → 4508** msgs; **Pass 55 now committed**.
- `bc-0039b8bf` still RUNNING/empty.
- `bc-b0a6ba89` still IDLE, 864 msgs, PR #29 CONFLICTING.

## Independently image-backed P001 1900–1926 residence

**NO. Expectation met: NONE.** No fetched transcript asserts a new P001 census/residence line for 1900–1926 that this branch independently re-read from an original image.

Residence chain on this case is unchanged: **1900 Sturgeon C011 → 1910 UNKNOWN → 1917 Ola Coy C027 → 1926 Ola/Carter**.

Pass 55 on PR #26 is **negatives + a rejected same-name collision (Copley)**, not a P001 pin. **This pass did not re-read p1123–1124 or Greene B-sides.** Treat C263–C266 as sibling sayings.

## PR #26 — Pass 55 **is committed**

Agent `bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03`. GitHub:

```json
{
  "title": "Dora research: 1870 Elias original, 1910 Ella Miracode, birth-to-death pass",
  "state": "OPEN",
  "mergeable": "MERGEABLE",
  "mergeStateStatus": "CLEAN",
  "headRefName": "cursor/dora-locations-1900-death-8d03",
  "headRefOid": "ff58673ee8aeefa8ee6b4f9d94119a14c0e4ba05",
  "url": "https://github.com/CatCorner22/Farm_Moonshot/pull/26",
  "additions": 616,
  "deletions": 72,
  "changedFiles": 77
}
```

`git log -1 --format='%H %s' origin/cursor/dora-locations-1900-death-8d03` after fetch:

`ff58673ee8aeefa8ee6b4f9d94119a14c0e4ba05 Pass 55: Greene ED 42–43 B-sides nil Stone; Liberty ED 5 nil Sullivan`

Committed **2026-10-30T09:36:23Z**. Parent of that commit is still Pass 54 `90785abc63bbc9ab109e24613e199ee473e80159` (09:10:41Z).

Cursor diff-metadata this fetch: PR **OPEN**, not merged, **+1439 / −878 / 77 files** (was +1387/−878/76 on Pass 37).

Transcript: **4508** messages (44 user / 2671 assistant / 1793 tool). Last substantial assistant after the Pass 55 close: started **Pass 56** on leftover S-415 **John** cards, roll **248** (“I'll map the unread John cards on roll 248, invert them, and read for Bollinger.”). **No Pass 56 commit.**

### Exact C263–C266 claim wording (on that branch evidence)

Command: `git show origin/cursor/dora-locations-1900-death-8d03:research/dora-ella-newnam/04-evidence.md | rg -n 'C263|C264|C265|C266'`

Verbatim lines from that command (sibling-owned; do not steal IDs):

```
426:| C263 | 1900 Greene ED **42** remaining B-sides listed in **L313** contain **no** Stone / Thomas A. head. With **L311** this is every ED **42** B-side (odd pp **181–253**) | PROVEN (negative for that ED’s B-sides) | S256 L313 C262 | B040 / #11 |
427:| C264 | 1900 Greene ED **43** remaining B-sides listed in **L314** contain **no** Stone / Thomas A. head. Combined with **C259** (A-sides), **C262**, and **C263**, ED **42** (p.**180–255**) and ED **43** (p.**256–319**) are name-column swept | PROVEN (negative for those two EDs) | S256 L314 C259 C262 C263 | B040 / #11; ED **37–41** still residual |
428:| C265 | 1900 Bollinger Liberty ED **5** sheets **1 A–14 B** (T623-839 pp **1105–1132**) contain **no** Sullivan / Letha / Newnam household and **no** infant Letha | PROVEN (negative on those twenty-eight sheets) | S259 L315 | B007; does not disprove **C244** (1910) |
429:| C266 | **Dora E.** Copley, **26**, wife of **Abraham Copley** **33** (b. Jan 1867 KY), 1900 Liberty ED **5** sh **10 A–B** dw/fam **124** (T623-839 pp **1123–1124**), born **Oct 1873 Missouri**, **3/3** children, parents MO/TN — **is not** P001 | PROVEN (rejected) | Birth month/year and state (Oct 1873 MO vs Aug 1871 KY); husband Copley ≠ Samuel P.; P001 is at Sturgeon KY the same census day (**C011**) | S259 L316 | B007 |
437:| 1900 Liberty ED 5 sh 10A–B Dora E. Copley 26 b. Oct 1873 MO + P001 | Given name Dora E. | Age 26 vs 28; b. MO vs KY; husband Abraham Copley; P001 enumerated at Sturgeon KY | **Rejected (C266)** |
```

C266 is **Copley**, not Cato. Sibling-owned.

Matching log rows (`02-log.md` L313–L316) and source **S259** (Liberty ED 5 name columns + Copley household **seen**; log `sources/census/b040-b007-pass55-2026-10-30.txt`). Pass 55 note: crops under `/tmp/b007-pass55/ed5/` and `/tmp/b040-pass54/names/` **not committed**.

### Cato vs Copley

| Stage | Husband ID for p1124 “Dora E. Wife” |
|---|---|
| In-flight Pass 37 catalogs (`bc-fa32244b`, `bc-dd16e045`) | **Guess: Cato, William** Head on p1123; not finished; not a P001 hit |
| PR #26 chat msg[4323] (thinking, before close) | “Page 1123 likely ends with **Cato William** Head. Dora E on page 1124 is his wife.” (**one** Cato mention in the whole 4508-msg transcript) |
| Chat msg[4409] | “Surname reads **Copley**. I’m writing the Pass 55 logs…” |
| **Committed** `ff58673` / C266 / L316 / S259 | **Abraham Copley**, 33, b. Jan 1867 KY, farmer, m. 7 yrs; wife **Dora E.**, 26, b. Oct 1873 **Missouri**, 3/3, parents MO/TN. **No “Cato” in 04-evidence.md on that branch.** |

**Do not import Cato.** **Do not import Copley as P001.** Sibling-owned **C266**. Not independently image-read here.

### What they committed vs what this case independently verified

| Their claim | Their status | Independently verified here? |
|---|---|---|
| C249 Dora E. **Stone** / Henry C. | still in their book as Stone reject vs P001 | **YES as household, NO as Stone** — **C338 Rhodes, Henry C. + Dora M.[?]** |
| C250 Dora Newnam 36 IN | they already reject vs P001 | **Not re-read this pass** |
| C260–C262 Pass 54 | committed `90785ab` | **NO** (sibling-owned) |
| **C263–C266 Pass 55** | **committed `ff58673`** | **NO** — not re-read; **do not steal IDs** |
| p1124 Dora E. wife | **Copley** reject (C266) | **NO** — not a P001 pin even on their saying |
| Pass 56 John cards | in flight after msg 4483 | **NO** |

## FLAG — chats that still treat C249 as Dora E. Stone

C249 is **Rhodes, Henry C. + Dora M.[?]** (**C338**). SHA-256 `5eab4793bf42d8c18b7ef43a6296495620392c100c0e1ed8ad59bfe6c4bf769b`. MO ≠ KY; Rhodes ≠ T.A./Samuel; 6-6 ≠ 7-5; no Sturgeon children.

| Chat | Evidence this pass |
|---|---|
| **`bc-995d22ea` / PR #26** | **YES, still.** Committed `04-evidence.md` line 379 after Pass 55 still reads: “**Dora E. Stone**, **37**, wife of **Henry C. Stone**, Crooked Creek Twp … ED **1**, sh **10 A**”. Filename on that branch remains `1910-bollinger-ed1-dora-e-stone-rejected.png`. Transcript has **50** “Dora E. Stone” / **62** C249 hits; **1** “Rhodes”. Recent assistant texts after msg 4000 do not retract the surname. |
| `bc-929b8124` | **Prior FLAG, not re-fetched.** Pass 37: helper “verified YES” C249 as Stone from filename+SHA; last text did not retract. Still **IDLE**. Treat as unretracted unless a later fetch shows otherwise. |

Nested reviewers (`bc-fa32244b`, `bc-dd16e045`, this pass) **correctly flag** the Stone error; they do not treat C249 as P001/Stone as a positive ID.

## FLAG — chats that still treat pdfp0367 as Liberty ED 5 Sullivan

pdfp0367 is **Crooked Creek ED 1** (this branch: **C316 / C323 / C338–C339 / B048**). Dw 174 **C339** McCamie[?]/Larrille[?]; dw 178 Rhodes **C338**. Not Liberty ED 5 (Liberty ED 5 on T623-839 is 1900 pp 1105–1132).

| Chat | Evidence this pass |
|---|---|
| **`bc-55740f1c`** | **Prior FLAG, not re-fetched.** Pass 37: 152 msgs, still asserts pdfp0367 John H. Sullivan + Dora A. 31 + McCoy W. 7 as Liberty ED 5. Still **IDLE**. Headline misread stands until a later fetch shows a retraction. |
| `bc-995d22ea` / PR #26 | **Does not currently treat pdfp0367 as Liberty ED 5 Sullivan.** Early thinking (msg 2908) copied the Sullivan headline, then msg 2916 corrected “pdfp0367 is actually Crooked Creek ED 1 sh 10A, not John H Sullivan” — but then filed that sheet as **Henry C. Stone** (C249). Zero `pdfp0367` in later assistant `text`. |

## Sibling-owned IDs — do **not** steal

User rule: **C221–C266 / L245–L287 / S259** are sibling-owned. Report only; do not file under those numbers on this branch.

**New this pass (now committed on PR #26, still do not steal):**

| ID | Owner | Status | steal? |
|---|---|---|---|
| **C263** remaining Greene ED 42 B-sides nil Stone | PR #26 `bc-995d22ea` | committed Pass 55 `ff58673` | **NO** |
| **C264** remaining Greene ED 43 B-sides nil Stone | same | committed | **NO** |
| **C265** Liberty ED 5 sh 1A–14B nil Sullivan/Letha/Newnam | same | committed | **NO** |
| **C266** Dora E. Copley 26 (Abraham Copley) reject vs P001 | same | committed | **NO** |
| **L313 L314 L315 L316** | same | committed | **NO** |
| **S259** Liberty ED 5 originals + Copley household | same | committed | **NO** |
| Ford/Fordney dau **Dora M** p1129; Bridwell dau **Dora C** p1109; Laughlin dau Dora p229 | same | they already reject vs P001 | **NO** |
| In-flight Pass 56 S-415 John cards | same | uncommitted | **NO** / skip-reel |

Also still forbidden from prior passes: **C221–C250 / L245–L287 / C260–C262 / C249-as-Stone / pdfp0367-as-Sullivan / C258 Wright Dora / PR #29 T623-537 hh 85**.

Skip-reels still held: unread S-415 John cards; Greene ED 37–41; T623-537 hh 85.

## PR #29

Agent `bc-b0a6ba89-91b4-4a8c-a51c-1725f6ff1f8c`. **IDLE**. GitHub **OPEN / CONFLICTING / DIRTY**. Branch `cursor/dora-research-pass-21`. HEAD `819751ee8c41cae432ffe58ab5cbfae7c6a91491`. Diff-metadata: +176/−26, 30 files. **864 msgs** (unchanged vs Pass 36/37). Last assistant still: fetched `origin/main`, in-progress merge **not committed**; conflict markers remain in `04-evidence.md`, `06-dossier.md`, `11-backlog.md`. Holds **hh 85** nativity — **skip**. ID collision C221–C223 vs `main`.

## Open GitHub PRs (`CatCorner22/Farm_Moonshot`)

| PR | Agent | Head | GitHub | Notes |
|---|---|---|---|---|
| **#26** | `bc-995d22ea` | `cursor/dora-locations-1900-death-8d03` @ `ff58673` | **OPEN MERGEABLE CLEAN** | **Pass 55 committed**; Pass **56** in chat only (John cards) |
| **#29** | `bc-b0a6ba89` | `cursor/dora-research-pass-21` @ `819751e` | **OPEN CONFLICTING DIRTY** | Merge of `origin/main` uncommitted |
| **#30** | `bc-01a18bb4` (parent) | `cursor/dora-continue-chat-review-3bf1` @ `49b86c55583ba8d0c23588501d3e382bed341b16` | **OPEN MERGEABLE CLEAN** | Title “Dora research passes 32–37: 1870 Gray originals, Rhodes not Stone, Word book”; 77 files +33544/−54. Identity only this review (HEAD moved vs Pass 37 `ae2ebe04`) |

Merged (historical, already on `main`): #28 biography, #27 deep research, #25 locations, #24–#13 biography/book chain, #7/#5/#4 Dora primaries, #3–#1 skill.

## Primaries / scans (named watch list)

| Agent | Msgs | Status | PR / branch | Now doing |
|---|---|---|---|---|
| `bc-995d22ea` Dora location search | **4508** (was 4351) | **RUNNING** | **#26 OPEN MERGEABLE CLEAN** | **Pass 55 committed `ff58673`.** **Pass 56 in flight:** leftover S-415 John cards roll 248. C249 still Stone in their book. C266 = Copley reject. |
| `bc-b0a6ba89` Genealogy detective | **864** | IDLE | **#29 OPEN CONFLICTING DIRTY** | Unchanged. Holds hh 85. |
| `bc-0039b8bf` Scan ED5 405–434 | **0** | **RUNNING** | none | Transcript still **empty**. No pages 405–434. |
| `bc-55740f1c` Scan ED5 PNGs | 152 (prior) | IDLE | none | Not re-fetched. Still the pdfp0367 Sullivan FLAG. |
| `bc-b2cfe195` Scan 1900 Liberty PNGs | 99 (prior) | IDLE | none | Unchanged even-page nil; still lists withdrawn William H. Sullivan. |
| `bc-01a183ca` Dora biography | 3417 (prior) | IDLE | **#28 MERGED** | No new 1900–26 P001 pin. |
| `bc-01a18bb4` parent | — | **RUNNING** | **#30 OPEN** | Identity only this review. |
| `bc-fa32244b` Pass 37 reviewer | **142** | IDLE | none | Was empty RUNNING; wrote 60-catalog; stale on Pass 55. |
| `bc-dd16e045` Pass 37 extract | **64** | IDLE | none | **NEW.** Compact extract; stale (Pass 55 uncommitted / Cato). |
| `bc-87c7034f` this review | **0** | **RUNNING** | none | Empty; in flight. |

## Nested Pass 37 extract (`bc-dd16e045`) — what it got right / what is now stale

Usable for the 60-agent inventory as of ~09:32Z. **Wrong as of 09:36Z:**

- “No Pass 55 commit exists” / “uncommitted Pass 55” / draft C263–C266 → **superseded by `ff58673`**.
- p1124 husband “lean Cato, William” → **committed as Abraham Copley (C266)**.
- PR #26 msgs **4351** → now **4508**.
- `bc-fa32244b` “RUNNING / empty” → **IDLE / 142**.

Do not take Cato into this case’s evidence from that extract.

## ED5 transcript

`bc-0039b8bf-7edb-593b-82c3-cb59471d392a` — **empty**: `{"messages":[]}` (21 bytes). Status still **RUNNING**. Events: two `mcp_auth_error` Gmail warnings only. No pages 405–434 were read in any fetched chat.

## Full catalog (62)

Newest first, as returned. Msgs from this-pass `transcript.json` (`messages` length) when fetched; otherwise Pass 37 count. Parent = identity only.

| # | bcId | name | status | created (UTC) | msgs | PR | empty? | 1-line finding |
|---|---|---|---|---|---:|---|---|---|
| 1 | `bc-87c7034f-e5f6-5607-8a63-67e4a5a3c588` | Review all cloud chats **NEW** | **RUNNING** | 2026-10-30 09:49:24 | 0 |  | yes | NEW this nested Pass 38 reviewer; transcript empty (in flight); identity only; no images. |
| 2 | `bc-dd16e045-050e-55f6-a9ca-de4e3af8848d` | Summarize nested chat review **NEW** | IDLE | 2026-10-30 09:32:57 | 64 |  | no | NEW Pass 37 compact extractor (64 msgs); cataloged 60 agents from bc-fa32244b. STALE vs this pass: still says Pass 55 uncommitted and p1124 husband = Cato, William. No images. |
| 3 | `bc-fa32244b-c7f6-596c-97b5-2df617923c9b` | Review all cloud chats | IDLE | 2026-10-30 09:23:01 | 142 |  | no | Pass 37 nested reviewer now IDLE (was empty RUNNING); 142 msgs; wrote /tmp/dora-pass37 (60 agents). STALE: Pass 55 then uncommitted / Cato guess. No images. |
| 4 | `bc-28cdb8cd-212b-57bc-af34-4e66f5fa62bf` | Review all Dora cloud chats | IDLE | 2026-10-30 09:10:07 | 107 |  | no | Pass 36 nested reviewer; now IDLE with 107 msgs (was empty/RUNNING last pass); wrote /tmp/dora-pass36; no images. |
| 5 | `bc-f672cc5c-c4fd-5ed0-a1fe-3ee8490bd474` | Review all Dora chats | IDLE | 2026-10-30 08:56:13 | 147 |  | no | Pass 34/35 nested catalog (58 agents); no images. |
| 6 | `bc-929b8124-6bf2-5c95-a507-70dea3e72f5b` | Review running chat transcripts | IDLE | 2026-10-30 08:39:36 | 115 |  | no | Helper; earlier wrongly treated C249 filename as Stone; last text still does not retract surname error (C338 Rhodes). |
| 7 | `bc-01571c02-d829-5f15-92db-ab8f34af1c1d` | Review remaining cloud chats | IDLE | 2026-10-30 08:22:03 | 144 |  | no | Helper nested remaining chats (catalog 56); no fieldwork. |
| 8 | `bc-554687c0-96cf-5d4e-bf70-ed0f37f02406` | Summarize PR26 transcript | IDLE | 2026-10-30 08:10:16 | 87 |  | no | Helper summarized PR #26 at 3412 msgs (now stale vs 4508). |
| 9 | `bc-b9ee7cdf-0249-5215-9f62-57aa37f0ecc1` | Summarize sibling+helper chats | IDLE | 2026-10-30 08:10:16 | 70 |  | no | Helper sibling+scan summary; noted ED5 empty. |
| 10 | `bc-e5f39fe4-de72-5c8b-8a7c-484a187312e0` | Summarize remaining helper transcripts | IDLE | 2026-10-30 07:50:00 | 137 |  | no | Helper remaining helpers; MO Soundex PNG not re-read. |
| 11 | `bc-d50aea9c-69e1-54d3-a241-586a10cf4171` | Summarize review-helper transcripts | IDLE | 2026-10-30 07:45:24 | 74 |  | no | Helper review-of-reviewers; no fieldwork. |
| 12 | `bc-02919df5-2e86-5974-941a-35f559593645` | Summarize running sibling transcripts | IDLE | 2026-10-30 07:45:24 | 73 |  | no | Helper running-sibling summary; ED5 empty. |
| 13 | `bc-3a362662-09b7-59a0-949b-571159302c05` | Summarize census-scan transcripts | IDLE | 2026-10-30 07:45:24 | 45 |  | no | Helper census-scan summary; PNG blobs not in JSON. |
| 14 | `bc-012dea72-5247-52b3-91ca-c6af8180be7b` | Review running sibling chats | IDLE | 2026-10-30 07:29:58 | 162 |  | no | Helper nested running siblings; no independent images. |
| 15 | `bc-4410686b-67f6-5635-888b-5e1198b52db3` | Review scan and helper chats | IDLE | 2026-10-30 07:29:58 | 131 |  | no | Helper nested 20 scan/helpers. |
| 16 | `bc-3fd159b6-6b21-5c9b-9da9-763c4cdf91a8` | Review older primary chats | IDLE | 2026-10-30 07:29:58 | 68 |  | no | Helper nested 19 older primaries. |
| 17 | `bc-b2cfe195-dad1-510f-a5d3-e14453ad915f` | Scan 1900 Liberty PNGs for Sullivan | IDLE | 2026-10-30 07:29:43 | 99 |  | no | Scan 17 even-page 1900 Liberty PNGs: nil infant Letha/Viola head; still lists withdrawn William H. Sullivan. |
| 18 | `bc-01a18bb4-e162-785c-9724-86a7c5663bf1` | Genealogy detective project updates | **RUNNING** | 2026-10-30 07:27:30 | — | #30 OPEN | n/a | PARENT case agent (this env); identity+PR #30 only — transcript not fetched (forbidden). |
| 19 | `bc-b0a6ba89-91b4-4a8c-a51c-1725f6ff1f8c` | Genealogy detective Dora research | IDLE | 2026-10-29 23:07:09 | 864 | #29 OPEN | no | PR #29 still IDLE OPEN CONFLICTING DIRTY; 864 msgs unchanged; pass 21–22 pushed; origin/main merge uncommitted; holds hh 85 nativity. |
| 20 | `bc-0039b8bf-7edb-593b-82c3-cb59471d392a` | Scan ED5 pages 405-434 | **RUNNING** | 2026-10-29 22:31:25 | 0 |  | yes | Scan ED5 405–434 still RUNNING with empty transcript {"messages":[]} — no PNG claims. Events: two Gmail MCP auth warnings only. |
| 21 | `bc-55740f1c-00e0-5951-8953-15d6d9d5d758` | Scan ED5 census PNGs names | IDLE | 2026-10-29 22:18:38 | 152 |  | no | Scan 54 PNGs; still asserts pdfp0367 John H. Sullivan + Dora A. 31 as Liberty ED 5 — do not import (C338/C339). |
| 22 | `bc-887a76bb-8390-5fe6-a397-34447bdd0d0f` | Scan mo233 John band PNGs | IDLE | 2026-10-29 21:53:31 | 95 |  | no | MO Soundex S-415 John-band sample: nil Bollinger/Letha head. |
| 23 | `bc-2eacda92-fbec-5222-9084-d4894995d612` | Scan mo233 head PNGs Sullivan | IDLE | 2026-10-29 21:45:25 | 149 |  | no | MO Soundex S-415 head PNGs: nil target Sullivan head. |
| 24 | `bc-2c2b6383-4de9-5124-bcaf-8a2e5e4521fb` | Scan mo233 PNGs for Sullivan | IDLE | 2026-10-29 21:41:36 | 147 |  | no | MO Soundex mo233 Sullivan sample: nil Letha/Viola/John H. head. |
| 25 | `bc-4d290b6c-09a4-5003-9330-57e96bcab7d2` | Read MO soundex PNGs Sullivan | IDLE | 2026-10-29 21:37:02 | 82 |  | no | MO Soundex S-435 (Shelton band) pass49: not Sullivan. |
| 26 | `bc-b43a15fd-3e65-5113-9179-222ec8344456` | TSLA death search Rissie | **ERROR** | 2026-10-29 20:47:26 | 0 |  | yes | ERROR empty; TSLA Rissie still not name-queried. |
| 27 | `bc-8e76cea0-c388-5c48-a33d-243f2e5d63b5` | B043 sweep + goal completion | IDLE | 2026-10-29 17:24:07 | 272 |  | no | Closed B043 Yell 1910 IA sweep nil P001 (already in dossier C153). |
| 28 | `bc-cc229b3e-5272-5612-ab17-04537c722c44` | Close B023 B044 B043 location | IDLE | 2026-10-29 16:26:57 | 294 |  | no | Closer: no new P001 residence pin. |
| 29 | `bc-7ca3e767-4efb-549f-900c-e5f362c805de` | Goal audit + location backlog | IDLE | 2026-10-29 16:07:24 | 222 |  | no | Location backlog audit; 1900–1926 chain unchanged. |
| 30 | `bc-cb3a3891-3e21-51a9-8a3c-78e22ea353f6` | Book: B046 ED 200 nil | IDLE | 2026-10-29 15:44:42 | 45 |  | no | Book fold-in of B046 ED 200 nil. |
| 31 | `bc-3796a2aa-d5db-5a1d-b141-eee0ff23fd1a` | Sync C146 into book | IDLE | 2026-10-29 14:56:39 | 40 |  | no | Synced C146 into book Places; no new pin. |
| 32 | `bc-e8dfdb73-a6e4-53b4-b343-d8fb8c6fb7d1` | B046 fold-in + PR retry | IDLE | 2026-10-29 14:56:24 | 334 |  | no | B046 fold-in + PR retry; git/book only. |
| 33 | `bc-cd08a20a-763d-5a53-b340-4930221d6f8e` | Open PR + branch sync | IDLE | 2026-10-29 14:56:07 | 47 |  | no | Open-PR/branch sync helper; no research. |
| 34 | `bc-00e3bde6-2d2d-5097-8628-cfb202372bf1` | Merge 1913–1926 branch + book | IDLE | 2026-10-29 14:55:08 | 113 |  | no | Merge 1913–1926 book helper; could not open PR. |
| 35 | `bc-8288e8fb-8eb6-57ad-887f-c07fba5b98e8` | Execute B046 1920 Ola census | IDLE | 2026-10-29 14:52:21 | 278 |  | no | Executed B046 1920 Ola ED 200 IA read (C213). |
| 36 | `bc-f3cfb3e7-759e-5add-bde6-3939f547f485` | Follow-up B042–B045 gaps | IDLE | 2026-10-29 14:50:55 | 197 |  | no | B042–B045: C146 USGenNet 1910 transcripts nil P001. |
| 37 | `bc-281c57f3-937a-5920-aa1c-3d8221b38f54` | Review Farm_Moonshot project chats | IDLE | 2026-10-29 14:48:26 | 117 |  | no | Prior project-chat inventory (L161); B046 lead. |
| 38 | `bc-359a99fe-a390-5c02-a0a4-986d794942fa` | Dora 1913–1926 location web search | IDLE | 2026-10-29 14:47:59 | 131 |  | no | 1913–1926 web search; no new PROVEN residence beyond Coy 1917 / 1926 death. |
| 39 | `bc-3b441f4a-2cce-5eb2-bfc4-5a210a6ac0ce` | Dora Word book + git sync | IDLE | 2026-10-29 14:47:59 | 145 |  | no | Word book + git hygiene; Places 1900-death. |
| 40 | `bc-e3326e8c-597f-53c8-b831-fd8cc5dec482` | Dora 1900–1912 location web search | IDLE | 2026-10-29 14:47:59 | 126 |  | no | 1900–1912 web search; C203 Rosa Banks; no new P001 pin. |
| 41 | `bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03` | Dora location search | **RUNNING** | 2026-10-29 14:47:15 | 4508 | #26 OPEN | no | PR #26 RUNNING 4508 msgs (was 4351). Pass 55 COMMITTED ff58673 09:36Z (C263–C266; C266 = Dora E. Copley not Cato). Pass 56 in flight: unread S-415 John cards roll 248. Still files C249 as Dora E. Stone. No new P001 pin. |
| 42 | `bc-01a183ca-4028-7f9b-9d4c-34d4ab6671f6` | Dora biography research | IDLE | 2026-10-28 18:33:52 | 3417 | #28 MERGED | no | Biography passes 18–31; PR #28 MERGED; no new 1900–26 P001 pin. |
| 43 | `bc-95a4d0c6-b500-5aa3-b9d3-eca0e43fdb58` | Summarize original Dora chat | IDLE | 2026-10-28 12:40:01 | 44 |  | no | Summarizer of original Dora chat; no independent images. |
| 44 | `bc-a00fe62a-a1b3-5693-9ded-09fde0d88e90` | Summarize early-1900s Dora chat | IDLE | 2026-10-28 12:40:01 | 51 |  | no | Summarizer of early-1900s chat; no independent images. |
| 45 | `bc-98b5c0ac-172b-555e-8d60-7d06811e0b69` | Summarize extract/pearl helper chats | IDLE | 2026-10-28 12:40:00 | 49 |  | no | Summarizer of extract/pearl helpers; no fieldwork. |
| 46 | `bc-01a18285-696d-761f-be7a-74d897313200` | Dora master biography | IDLE | 2026-10-28 12:39:04 | 2414 | #13 MERGED | no | HTML master biography; C117 Greene Thomas A.; PR #13 MERGED. |
| 47 | `bc-a16def3b-c4be-41e9-846c-f31bc0f8dd81` | Dora's early 1900s | IDLE | 2026-10-27 15:14:04 | 1718 | #7 MERGED | no | Early-1900s primary; 1910 hole; Sturgeon ED 99 original; PR #7 MERGED. |
| 48 | `bc-3db016fa-fdb4-5c11-981a-ff0769a16da0` | FamilySearch census browser hunt | **ERROR** | 2026-10-27 13:59:55 | 0 |  | yes | ERROR empty; FamilySearch browser hunt died at start. |
| 49 | `bc-ddbf6d0b-4e48-5086-b854-d359ec987b09` | Parse ancestry skill transcript | IDLE | 2026-10-27 13:49:02 | 63 |  | no | Parse ancestry-skill transcript; skill-building only. |
| 50 | `bc-62de7db1-7290-5623-bc0c-8367354d88a5` | Extract Dora research state | IDLE | 2026-10-27 13:49:02 | 169 |  | no | Extract research-state helper; no new facts. |
| 51 | `bc-becce541-0459-5d97-b5f0-409bad2e072a` | Summarize latest Dora findings | IDLE | 2026-10-27 13:49:02 | 77 |  | no | Summarize latest findings helper. |
| 52 | `bc-589f63df-4d1c-5cc3-99e8-c31bef2eb44a` | Extract Pearl breakthrough | IDLE | 2026-10-27 13:49:02 | 77 |  | no | Extract Pearl breakthrough helper. |
| 53 | `bc-8286c652-a1aa-5dbb-ab90-cc2b8895ee94` | Parse original Dora transcript | IDLE | 2026-10-27 13:49:02 | 99 |  | no | Parse original Dora transcript helper. |
| 54 | `bc-0bd3b0b2-ec76-4a5c-93c7-10c0bfe1f312` | Dora research continuation | IDLE | 2026-10-27 13:47:22 | 4887 | #5 MERGED | no | Continuation primary; 1920 Beattyville E.T.; PR #5 MERGED. |
| 55 | `bc-2ffa148f-bd17-4e95-beef-aa2f31940c4a` | Ancestry research skill | IDLE | 2026-10-27 10:46:44 | 393 | #1 MERGED | no | Authored genealogy-detective skill; PR #1 MERGED; no Dora facts. |
| 56 | `bc-4bc6adb0-9219-5895-986c-fa21e5cbeb24` | Summarize Pearl breakthrough from transcript | IDLE | 2026-10-27 10:41:57 | 87 |  | no | Summarize Pearl breakthrough helper. |
| 57 | `bc-5f387719-eeb1-5806-8407-93ba585780ac` | Ancestry Dora browser search | **ERROR** | 2026-10-27 10:01:30 | 0 |  | yes | ERROR empty; Ancestry browser hunt. |
| 58 | `bc-9759714e-33fc-55d4-99c3-0a1fd082a36b` | Ancestry browser Dora search | **ERROR** | 2026-10-27 10:01:06 | 0 |  | yes | ERROR empty; Ancestry browser hunt. |
| 59 | `bc-12ae958f-d3cf-532c-8bf7-db037fd78879` | Ancestry.com Dora research | **ERROR** | 2026-10-27 10:00:54 | 0 |  | yes | ERROR empty; Ancestry.com Dora hunt. |
| 60 | `bc-352be520-d192-5b41-a04b-1dea8135a1a3` | Summarize latest Dora research | IDLE | 2026-10-27 09:45:52 | 197 |  | no | Summarize latest Dora research helper. |
| 61 | `bc-41e4c7da-d929-5e23-b808-89ad12711316` | Extract Dora research state | IDLE | 2026-10-27 09:30:31 | 74 |  | no | Extract Dora research state helper. |
| 62 | `bc-01a17a5a-f7be-70f0-8063-d9a0707aebd1` | Dora | IDLE | 2026-10-26 22:35:47 | 3682 | #4 MERGED | no | Opened the case (DC, WikiTree, 1900 Sturgeon); PR #4 MERGED. |

**Count check:** 62 listed = `totalMatched` 62. Empty transcripts this pass among fetched: **2** (`bc-87c7034f`, `bc-0039b8bf`). Empty from prior catalog and still ERROR/unfetched: **5** hunts (`bc-b43a15fd`, `bc-3db016fa`, `bc-5f387719`, `bc-9759714e`, `bc-12ae958f`). Parent transcript not fetched. `bc-fa32244b` is **no longer empty**.

## Empty / ERROR transcripts

| bcId | name | transcript |
|---|---|---|
| `bc-87c7034f` | this nested review | **empty** `{"messages":[]}` (RUNNING) |
| `bc-0039b8bf` | Scan ED5 405–434 | **empty** `{"messages":[]}` (RUNNING) |
| `bc-b43a15fd` | TSLA death search Rissie | **empty** (ERROR; not re-fetched) |
| `bc-3db016fa` | FamilySearch census browser hunt | **empty** (ERROR; not re-fetched) |
| `bc-5f387719` | Ancestry Dora browser search | **empty** (ERROR; not re-fetched) |
| `bc-9759714e` | Ancestry browser Dora search | **empty** (ERROR; not re-fetched) |
| `bc-12ae958f` | Ancestry.com Dora research | **empty** (ERROR; not re-fetched) |

## Ten most important findings

1. **Catalog 62** (was 60). **NEW:** this reviewer `bc-87c7034f` (empty RUNNING) and `bc-dd16e045` (IDLE, 64 msgs, Pass 37 compact extract). `bc-fa32244b` filled in (142 msgs) and went IDLE. Count check **62 = totalMatched**, `hasMore: false`, gone **0**.
2. **No independently image-backed P001 1900–1926 residence.** Chain still 1900 Sturgeon → 1910 hole → 1917 Ola → 1926 death. Pass 55 is negatives + a Copley reject, not a pin.
3. **PR #26 Pass 55 IS committed** — `ff58673ee8aeefa8ee6b4f9d94119a14c0e4ba05` (09:36:23Z), GitHub HEAD matches, OPEN/MERGEABLE/CLEAN. Pass 37 catalogs that said “uncommitted” are stale.
4. **C266 wording is Dora E. Copley, not Cato.** Exact: “**Dora E.** Copley, **26**, wife of **Abraham Copley** **33** (b. Jan 1867 KY), 1900 Liberty ED **5** sh **10 A–B** dw/fam **124** (T623-839 pp **1123–1124**), born **Oct 1873 Missouri**, **3/3** children, parents MO/TN — **is not** P001.” Chat had a brief Cato guess (msg 4323) then corrected. Nested reviewers still repeat Cato. **Not P001. Do not steal C266.**
5. **Sibling-owned now includes committed C263–C266 / L313–L316 / S259** plus the standing ban on C221–C262 / L245–L287. Do not reuse those IDs.
6. **FLAG C249-as-Stone:** PR #26 evidence line 379 still names “Dora E. Stone … Henry C. Stone” after Pass 55. This branch: **C338 Rhodes**. Helper `bc-929b8124` unretracted (not re-fetched).
7. **FLAG pdfp0367 as Liberty ED 5 Sullivan:** `bc-55740f1c` still (prior catalog; still IDLE). PR #26 itself later placed that PNG in Crooked Creek ED 1 but as Stone (wrong surname). It is Crooked Creek ED 1.
8. **PR #26 already started Pass 56** (unread S-415 John cards, roll 248). Skip that reel. Residual Greene ED 37–41 also theirs.
9. **PR #29 still OPEN CONFLICTING DIRTY**; 864 msgs unchanged; hh 85 remains theirs. **ED5 `bc-0039b8bf` still empty RUNNING** — pages 405–434 unread in every fetched chat.
10. Nested Pass 37 extract (`bc-dd16e045`) is a valid 60-snapshot but **wrong on Pass 55 commit state and Cato**. Open PRs: **#26, #29, #30**. Ancestry still 403 in prior catalogs; living DNA testers untouched.

## Next chat

Keep skipping unread S-415 John cards / Greene ED 37–41 / hh 85 until #26/#29 merge or go idle with a finished log. Do not file C249 as Stone (**C338**). Do not file pdfp0367 as Liberty ED 5 Sullivan. Do not file their C221–C266 / L245–L287 / S259 / L313–L316 under those numbers. If Pass 56 commits John-card crops, copy via `git show` and re-read independently before any P001 language. Rebuild Word/PDF only after narrative edits on **this** branch.

## Method notes

- List: one page, offset 0, limit 200, `includeArchived: true`, `hasMore: false`.
- MUST-FETCH all retrieved. Parent `bc-01a18bb4` identity only.
- PR #26 evidence read from `origin/cursor/dora-locations-1900-death-8d03` after `git fetch` of that branch; working tree **not** edited.
- No living-person research.


---

# Pass 39 filing note (30 Oct 2026, America/New_York)

Nested report: `/tmp/dora-pass39/chat-review-pass39.md`. Catalog **63** / `hasMore: false`. NEW vs 62: `bc-9c0756fe` (this nested reviewer; empty when listed). PR **#26** HEAD `df9e4cce6410f66c7e1eed3aa61b38f7d94431e5` (Pass 56 committed; Pass 57 in flight on T623-855). PR **#29** then still OPEN CONFLICTING. **No** new independently image-backed P001 1900–1926 residence. Skip-reel held. Do **not** steal **C221–C268 / L245–L318 / S259–S260**.

# Pass 40 filing note (30 Oct 2026, America/New_York)

Nested report: `/tmp/dora-pass40/chat-review-pass40.md`. Catalog **64** / `hasMore: false` at that nested list. NEW vs 63: `bc-42eadea9-319d-533d-9395-742284b79ca4` (“B045 B047 free workarounds”) — transcript **empty**. PR **#29 MERGED** (`3c77377`). PR **#26** still `df9e4cc`, GitHub **CONFLICTING DIRTY**; Pass 57 uncommitted; highest committed **C268 / L318 / S260**. C249 on that branch is still labelled Stone — this case keeps **C338 Rhodes**. Hh **85** is now on `origin/main` via #29; this branch does **not** re-read it this pass. **No** new independently image-backed P001 1900–1926 residence. Nested Pass 40 reviewer `bc-58a9a05d` did not edit the case folder.

# Pass 41 listing (this continuation, 30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 50 + offset 50) → **65** / `hasMore: false` / `totalMatched: 65`. NEW vs 64: `bc-58a9a05d-b921-5aed-826e-3c3a87f3f548` (Pass 40 nested reviewer, now IDLE). A further nested reviewer `bc-d60ec7c1-d58a-5ba7-90c8-e6ebb025101b` was spawned this continuation and is **not** in the 65-count. RUNNING at list time: this parent `bc-01a18bb4`; PR **#26** `bc-995d22ea`; ED5 `bc-0039b8bf`. `bc-42eadea9` now IDLE. **No** new independently image-backed P001 pin in the identity-level listing. Fold `bc-d60ec7c1` when it lands.

# Pass 41 filing (later 30 Oct 2026, America/New_York) — catalog **67**

`list-cloud-agents` (limit 200, offset 0) → **67** / `hasMore: false` / `totalMatched: 67`. NEW vs 65:

| bcId | Name | Status | Note |
|---|---|---|---|
| `bc-d60ec7c1-d58a-5ba7-90c8-e6ebb025101b` | Review all Dora chats | IDLE | Nested reviewer spawned mid-Pass-41; identity-level listing only this pass |
| `bc-d47797ef-e801-5f07-87e1-d67682056417` | Review all cloud chats | RUNNING | This nested reviewer; fold when it lands |

RUNNING also: parent `bc-01a18bb4`; PR **#26** `bc-995d22ea`; ED5 `bc-0039b8bf`. **No** new independently image-backed P001 1900–1926 residence. Do **not** steal **C221–C268 / L245–L318 / S259–S260**. PR **#29** remains **MERGED**. This pass’s original-image work (1850 Owsley Gray pages; Madison 1860 name columns) is filed under **C424–C440 / L392–L400 / S380–S391 / DOC044–046**.

# Pass 41 nested fold (later 30 Oct 2026, America/New_York) — [Review all cloud chats](bc-d47797ef-e801-5f07-87e1-d67682056417) landed

Nested dump: `/tmp/dora-pass41/chat-review-pass41.md`. Catalog **67** / `hasMore: false` / statuses then RUNNING **4** · IDLE **58** · ERROR **5**. NEW vs 65: this nested reviewer + [Review all Dora chats](bc-d60ec7c1-d58a-5ba7-90c8-e6ebb025101b) (IDLE, inventory-only; stale on PR **#26** HEAD `df9e4cc`). Working tree **not** edited by the nested reviewer. Transcripts were searched, not read end-to-end. **No** new independently image-backed P001 1900–1926 residence.

**Stale pin in that nested report:** it stopped at PR **#26** HEAD `44cca6c` (Pass **57**). Independent `git fetch` + `gh pr view 26` this fold: HEAD **`650a475580bdc799cd51176555a0e20f9a4d16c8`** — `Pass 58: ED 37 A-sides and ED 41 B-sides complete; no second Stone` (committed 2026-10-30T11:28:39Z). GitHub still **OPEN / CONFLICTING / DIRTY**.

**Do not steal** sibling IDs now through Pass **58**: **C221–C276 / L245–L326 / S259–S264**. Highest committed on that HEAD: **C276 / L326 / S264**. Do **not** mint **C274–C276** here. Skip-reel held for Greene ED **42–43**, T623-839 Liberty, unread S-415 John, and T623-537 hh **85** (hh **85** still not independently re-read on this branch after #29 merge).

Sibling wording on that HEAD (inventory only — **not** re-read as originals on this branch):

| ID | sibling wording (do not steal) |
|---|---|
| **C269** / L319 / S261 | Greene ED **41** remaining A-sides nil Stone; every ED **41** A-side swept; B-sides then unread |
| **C270** | T623-855 map: ED **37** p.781–834, ED **38** p.835–916, ED **39** sh 1–5 p.917–926; p.815 = Thomas A. sh 18A (C117) |
| **C271** | Sampled ED **37** A-sides nil second Stone head |
| **C272** / L322 / S262 | B045 free substitutes still nil Samuel P. death/probate |
| **C273** / L323 / S263 | B047 free WWI still nil John H. / McCoy; M1509 rolls named, cards not examined |
| **C274** / L324 / S264 | Every ED **37** A-side: only Stone head is Thomas A. sh **18 A**; p.813 Elizabeth J. MIL (C112) |
| **C275** / L325 | Every ED **41** B-side nil Stone; ED **41** A+B swept |
| **C276** / L326 | Sampled ED **38** A-sides + ED **39** sh **1 A–5 A** nil Stone; **Stowe, John C.** rejected; **Dora Lucy A.** child rejected |

C249 on that HEAD is still labelled “Dora E. Stone … Henry C. Stone”; this case keeps **C338 Rhodes**. C266 remains **Copley** (not Cato).

[B045 B047 free workarounds](bc-42eadea9-319d-533d-9395-742284b79ca4) (now IDLE, ~180 msgs) did **not** write case files. Nested summary of that chat is index-only and matches sibling **C272 / C273**. This branch does **not** re-file those nils. ED5 helper [Scan ED5 pages 405-434](bc-0039b8bf-7edb-593b-82c3-cb59471d392a) still has an empty transcript (Gmail `mcp_auth_error` only).

This branch’s original-image work remains **C424–C440 / L392–L400 / S380–S391 / DOC044–046**. This fold uses **C441 / L401 / S392**. Next unused **C442+ / L402+ / S393+ / DOC047+**.

# Pass 42 listing (this continuation, 30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200, offset 0) → **68** / `hasMore: false` / `totalMatched: 68`. NEW vs 67: [Review all cloud chats](bc-b9d3861e-db5c-5ba2-95a8-bc5261f79593) (RUNNING, nested this pass). RUNNING also: parent `bc-01a18bb4`; PR **#26** `bc-995d22ea`; ED5 `bc-0039b8bf`. Independent fetch: PR **#26** HEAD **`b37864c69d92220574cd7b71dda2805a3b2fbd7c`** (`Merge origin/main 1fca25c; remap pass 21–22 colliding IDs`). Highest sibling IDs **C277 / L339 / S265**. Do **not** steal **C221–C277 / L245–L339 / S259–S265**. **No** new independently image-backed P001 1900–1926 residence. Fold `bc-b9d3861e` when it lands. This pass’s original-image work (1850 Estill 99B Marcus Gray; Breathitt/Madison headers + Madison 214B Gay) is filed under **C442–C455 / L402–L410 / S393–S402 / DOC047**.

# Pass 42 nested fold (later 30 Oct 2026, America/New_York) — [Review all cloud chats](bc-b9d3861e-db5c-5ba2-95a8-bc5261f79593) landed

Nested dump: `/tmp/dora-pass42/chat-review-pass42.md`. Catalog **68** / `hasMore: false` / RUNNING **4** · IDLE **59** · ERROR **5**. NEW vs 67: this nested reviewer only. Working tree **not** edited. Transcripts searched, not linear-read. **No** new independently image-backed P001 1900–1926 residence.

**Stale pins in that nested report:** (1) PR **#26** HEAD `650a475` (Pass **58**) — independent fetch this fold still **`b37864c`**. (2) “C277 not on origin” — **C277 / L333–L334 / S265** are on that HEAD (AR DH CertificateSearch modern-era nil, remapped from `main` **C227**; **n/a** for the 1914–1950 index; not a P001 pin). (3) parent HEAD `2701378` — this branch is now **`4b08fbc`** (Pass **42**). GitHub PR **#26** is now **OPEN / MERGEABLE / CLEAN**.

Skip remains **C221–C277 / L245–L339 / S259–S265**. Do **not** mint C274–C277. Pass **59** (ED 40 / reel-855 B-sides) is still **chat-only** beyond that HEAD. ED5 helper [Scan ED5 pages 405-434](bc-0039b8bf-7edb-593b-82c3-cb59471d392a) still empty. [B045 B047 free workarounds](bc-42eadea9-319d-533d-9395-742284b79ca4) still matches sibling **C272/C273**, not re-filed.

This fold uses **C456 / L411 / S403**. Next unused **C457+ / L412+ / S404+ / DOC048+**. 1850 Estill/Breathitt/Madison work remains **C442–C455 / DOC047**.

# Pass 43 listing (this continuation, 30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200, offset 0) at spawn → **68** / `hasMore: false`. Nested [Review all cloud chats](bc-55b44cd3-e8e5-5a91-8bea-a131a184de2a) spawned (NEW vs 68). **No** new independently image-backed P001 1900–1926 residence in that listing. Do **not** steal **C221–C277 / L245–L339 / S259–S265**. This pass’s original-image work (Breathitt 1A–44B + Madison 212A John Green / Silas 20) is filed under **C457–C471 / L412–L423 / S404–S413 / DOC048–051**.

# Pass 43 nested fold (later 30 Oct 2026, America/New_York) — [Review all cloud chats](bc-55b44cd3-e8e5-5a91-8bea-a131a184de2a) landed

Nested dump: `/tmp/dora-pass43/chat-review-pass43.md`. Catalog **69** / `hasMore: false` / RUNNING **4** · IDLE **60** · ERROR **5**. NEW vs 68: this nested reviewer only. Working tree **not** edited. Transcripts searched, not linear-read. **No** new independently image-backed P001 1900–1926 residence. **No** Bollinger “Dora E. Stone” claim in that nested transcript (C338 Rhodes stands).

PR **#26** HEAD still **`b37864c69d92220574cd7b71dda2805a3b2fbd7c`**. GitHub **OPEN / MERGEABLE / CLEAN**. Highest sibling IDs **C277 / L339 / S265**. Skip remains **C221–C277 / L245–L339 / S259–S265**. Do **not** mint C274–C277. Pass **59** is still **chat-only** beyond that HEAD — do **not** steal drafts **C278–C280 / L340–L342 / S266**. ED5 helper [Scan ED5 pages 405-434](bc-0039b8bf-7edb-593b-82c3-cb59471d392a) still empty. [B045 B047 free workarounds](bc-42eadea9-319d-533d-9395-742284b79ca4) still matches sibling **C272/C273**, not re-filed.

This fold uses **C472 / L424 / S414**. Next unused **C473+ / L425+ / S415+ / DOC052+**. Parent-county 1850 Gray **heads** are **C442–C471 / DOC047–051**.

# Pass 44 listing (30 Oct 2026, America/New_York)

Catalog **not** re-listed this pass (still **69** after the Pass 43 nested fold). **No** new independently image-backed P001 1900–1926 residence. Original-image work this pass: Owsley **279A** Silas Ratliff **8/12** (**C474 / DOC052**); Bawden **277A–296A** every-person (**C473**). Residual B055: visual given-name Silas on stamped **296B–321**. Skip **C221–C277 / L245–L339 / S259–S265**. Do **not** steal **C278–C280 / L340–L342 / S266**. Next unused **C477+ / L429+ / S418+ / DOC053+**.

# Pass 45 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) at spawn → **71** / `hasMore: false`. Nested [Review all cloud chats](bc-47d4740e-0026-5d85-a28b-0d525c60af4e) spawned after that listing. Independent `gh pr view 26`: **MERGED** (`f00adcd`; last commit **`2147e1da`** Pass **59**). Highest sibling IDs now **C280 / L342 / S266**. Skip-reel **C221–C280 / L245–L342 / S259–S266**. **No** new independently image-backed P001 1900–1926 residence. Original-image work this pass: Owsley **298A** Wilson Silas **6** (**C478 / DOC054**); **309B** Phillips Silas **15** (**C479 / DOC055**); **320A** Bowman **Squire 24** (Cyrus withdrawn, **C480 / DOC053**); Flannigan parts **1–5** (**C477**). **B055 done** (**C483**). This listing uses **C484 / L436 / S423**.

# Pass 45 nested fold (later 30 Oct 2026, America/New_York) — [Review all cloud chats](bc-47d4740e-0026-5d85-a28b-0d525c60af4e) landed

Transcript searched, not linear-read. Nested catalog **71** / `hasMore: false` / RUNNING **4** · IDLE **62** · ERROR **5**. Working tree **not** edited by the nested reviewer. **No** new independently image-backed P001 1900–1926 residence. Chain unchanged: 1900 Sturgeon → 1910 hole → 1917 Ola → 1926 death. **C338 Rhodes** stands. PR **#26** **MERGED** confirmed (`2147e1da` / `f00adcd`). Skip **C221–C280 / L245–L342 / S259–S266**. Pass 59 Greene Stone-nils remain sibling skip-reel (C278–C280), not re-filed here.

Independent parent re-list after the five Visual Silas PDF locals: **77** / `hasMore: false`. NEW vs 71: [Visual Silas PDF 384-393](bc-b8706b04-a903-5edf-8d4b-efd60a55e065), [Visual Silas PDF 394-403](bc-15ecaad8-0d95-5e2c-a227-c2ba2e58ac1d), [Visual Silas PDF 404-413](bc-d1cb279d-bfdd-5513-b1d4-27208dc05342), [Visual Silas PDF 414-423](bc-518d700c-0822-50d8-85f4-855c36f17392), [Visual Silas PDF 424-433](bc-86f103f0-efbe-5f79-b358-e577cacd83ff), plus the fold Task. This fold uses **C485 / L438 / S424**.

# Pass 46 listing (30 Oct 2026, America/New_York)

Catalog still **77** from the Pass 45 nested fold re-list. **No** new independently image-backed P001 1900–1926 residence. Original-image work this pass: Owsley **299B** Harrison Newman **33** + **Elias 8** (**C486 / DOC056**). Flannigan Elias **3** withdrawn. Identity with P004 **POSSIBLE**, unmerged (**C487**). **B057 done** as to the 1850 original. Skip **C221–C280 / L245–L342 / S259–S266**. Next unused **C491+ / L441+ / S427+ / DOC057+**.

# Pass 47 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200, offset 0 then 50) → **77** / `hasMore: false` / `totalMatched: 77`. Unchanged vs Pass 45 nested fold. Nested reviewer **not** respawned (zero delta). **No** new independently image-backed P001 1900–1926 residence. Original-image work this pass: Owsley **299B** William Newman **26** (**C491 / DOC057**); **300A** John Newman **60** b. **Tennessee** (**C492 / DOC058**, DISPROVED as 1880 John 69); Andrew Mays **Giles 1/12** (**C493 / DOC059**, Flannigan 5/12 withdrawn). **B058 done**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C495 / L441 / S430**. Next unused after Pass 47 filing was **C497+ / L446+ / S431+ / DOC060+**.

# Pass 48 listing (30 Oct 2026, America/New_York)

Catalog still **77**. Nested reviewer **not** respawned (zero delta). **No** new independently image-backed P001 1900–1926 residence. Original-image work this pass: 1860 Owsley Page **54** **H.H. Newman** 44 + **Elias 18** (**C497 / DOC060**), **PROVEN** same house as 1850 Harrison (**C498**); PDF **354** Andrew **Giles 11** (**C500 / DOC061**); Pages **59–60** John **68 Del** + Harrison 15 (**C501 / DOC062**). **B059 done**. Skip **C221–C280 / L245–L342 / S259–S266**. Next unused after Pass 48 filing **C506+ / L451+ / S434+ / DOC063+**.

# Pass 48 closeout listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **77** / `hasMore: false` / `totalMatched: 77`. Transcript of idle helper [Fold nested chat transcript](bc-b9846733-604b-5292-9b04-9b7d2f34aabb) **searched**, not linear-read: it folded [Review all cloud chats](bc-47d4740e-0026-5d85-a28b-0d525c60af4e), minted **no** IDs, edited **no** case files, and is **stale** on catalog (**71**) and next unused (**C477+**). Already folded as **C485 / L438 / S424**. **No** new independently image-backed P001 1900–1926 residence. Nested reviewer **not** respawned. Skip **C221–C280 / L245–L342 / S259–S266**. Pass 47–48 originals and Word closeout use the IDs already minted (**C491–C505 / L441–L450 / S427–S433 / DOC057–062**). Next unused **C506+ / L451+ / S434+ / DOC063+**.

# Pass 49 listing (30 Oct 2026, America/New_York)

Catalog **77** at Pass 49 research (`hasMore: false`). Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Derivative work this pass: Lee 1932 DC **extract** names father **Henry Harrison Newnam** and mother **Millie Tincher Newnam** (**C506 / DOC063**); KYDI **NEWMAN ELIAS T** vol **020** #**09525** (**C507**); C487/C499 upgraded **POSSIBLE → PROBABLE** (**C509**), **not PROVEN**. Lee 1918 extract + KYDI 1918 **nil** Mary in Lee (**C512**). Estill marry03 A-brides **nil** 1840 (**C511**). **B060 done** as derivative. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C514 / L457 / S430**. Next unused after Pass 49 filing was **C515+ / L458+ / S439+ / DOC064+**.

# Pass 50 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **78** / `hasMore: false` / `totalMatched: 78`. NEW vs 77: [Summarize nested fold transcript](bc-5743837b-acbb-5614-b6cc-a1bc3aac45d7) **searched**, not linear-read: stale catalog **71** / next unused **C477+**; minted **no** IDs; edited **no** case files. Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Cemetery work: Brandenburg-Quillen transcripts **Mary A. NEWNAM** 11 Jul 1918 and **Elias T.** 18 Apr 1932 (**C516 / C517 / DOC064**); parent notes **not** a second original (**C518**); KYDI 1917–1919 **nil** vs stone date (**#22** **C520**). Estill marry04 F–W **opened**: years **1809–1825 only** (**C522 / DOC065**). Original 1932 DC **still unseen**. **B061 remains open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C515 / L458 / S439**. Next unused **C527+ / L466+ / S448+ / DOC066+**.

# Pass 51 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **80** / `hasMore: false` / `totalMatched: 80`. NEW vs 78: [Fold nested fold transcript](bc-f8b797ad-cf13-5adb-ba0c-6cbee81ac92d) and [Search nested fold transcript](bc-a145ed68-b870-5030-b524-9c6172cf771d) **searched**, not linear-read (expected stale nested folds of already-folded helpers). Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Derivative work this pass: KYDI **NEWMAN HENRY H 72 OWSLY 08/06/1916** vol **044** #**21663** (**C528**); Owsley 1916 extracts **parents blank** (**C529**); identity vs 1860 H.H. 15 **PROBABLE**, not proved (**C530**); Josephine Gilbert FAN (**C531**); Lee 1911–1945 **nil** sibling parents except Elias T. 1932 (**C537**); FAG 101658752 photo is a **portrait**, not a stone (**C532 / DOC067**); Estill 1840 still a coverage hole (**C536**); authored **Abt. 1839** vs **27 Feb 1840** (**C535**). Original 1932 and 1916 DCs **still unseen**. **B061 / B062 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C527 / L466 / S448**. Next unused after Pass 51 filing was **C542+ / L477+ / S458+ / DOC070+**.

# Pass 52 listing (30 Oct 2026, America/New_York)

Catalog still **80** (not re-listed). Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Original-image work this pass: 1870 Travellers Rest sheet after Page **14**, dw **134/131 Newman, Harrison** 53 + Susan 47 (**C542 / DOC070**), **PROVEN** the 1860 H.H. 44 house (**C543**); Henry ~25 **absent** (**C544**); **Marshay** 16 F **DISPROVED** as Marshall V. 8 M (**C547**). **B064 opened**. Skip **C221–C280 / L245–L342 / S259–S266**. Next unused after Pass 52 filing was **C549+ / L479+ / S460+ / DOC071+**.

# Pass 53 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **82** / `hasMore: false` / `totalMatched: 82`. NEW vs 80: [Fold nested fold transcript](bc-c14c247f-b15e-56f8-8342-2371a48b4bba) and [Search nested fold transcript](bc-867adf0c-1481-5bd6-a9bf-066f6b47dabc) **searched**, not linear-read (nested folds of already-folded helpers). Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Original-image work this pass: 1870 Town of Beattyville stamp **315** dw **19/19 Newman, Henry** 24 + Mary 23 + Ellen 5 **F** + Millia 3 + John 8/12 (**C550 / DOC071**); **PROBABLE** the 1860 H.H. 15 (**C551**); **PROVEN** the 1880 Buck Creek Henry 34 house from Kendrick (**C555**). Millia **DISPROVED** as Millie Tincher (**C552**). **B065 opened**. Skip **C221–C280 / L245–L342 / S259–S266**. Next unused after Pass 53 filing was **C561+ / L486+ / S467+ / DOC073+**.

# Pass 54 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **82** / `hasMore: false` / `totalMatched: 82`. Unchanged vs Pass 53. Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Original-image work this pass: 1880 Owsley ED **80** Page **9** stamp **309**, **8 Jun 1880**, dw **74/77 Newman, Henry** 34 Farm Laborer + Mary 33 (father **England**) + Ellen F. 14 + Milla A. 12 (**C561 / DOC073**). T9-**438** (not 391). **PROVEN** the 1870 Beattyville house; vs 1860 H.H. 15 still **PROBABLE**. **B065 done**. Skip **C221–C280 / L245–L342 / S259–S266**. Next unused **C567+ / L490+ / S468+ / DOC074+**.

# Pass 55 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **84** / `hasMore: false` / `totalMatched: 84`. NEW vs 82: [Continue Dora genealogy](bc-d7a3569c-3baa-589d-8f26-02d269c034dd) (RUNNING, internal) and [Dora's biography research](bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) (WAITING_FOR_BACKGROUND_WORK, web) — process claims only, not linear-read. Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Original-image work this pass: 1840 Estill M704-**109** / IA `populationsc18400109unit` — overlay **0059** **John Tincher** + **Christian Tincher** young heads (**C567/C568 / DOC074**); Lewis name pages **nil** Newman/Elias-Tincher heads (**C569/C570**); overlay **0081** recap **5535** (**C571 / DOC075**); overlay **0063** **William Newton** not Tincher (**C572 / DOC076**). KY Footsteps C-grooms coverage hole (**C573**). Clay 1840 transcript **nil** (**C574**). McIlvain overlay **0084** **Abner Wiseman** / **Harrison Wray** / **Jas. Newland** are not Newman (**C577**). fishergenes p.68 **unmatched** (**C578**). Original 1932 DC and 1840 bond **still unseen**. Do **not** promote **C509**. **B061 remains open**. **B066 opened**. Skip **C221–C280 / L245–L342 / S259–S266**. Next unused **C579+ / L501+ / S474+ / DOC077+**.

# Pass 56 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **84** / `hasMore: false` / `totalMatched: 84`. Unchanged vs Pass 55. Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Original-image work this pass: 1840 Clay M704-**108** / IA `populationsc18400108unit` — all **23** name pages **nil** Newman/Tincher heads (**C579 / DOC077**); recap overlay **0127** pages **1–23** (**C580 / DOC078**); Smallwood heads **unmerged** (**C581**). Edmonson KyGenWeb index: McIlvain overlay **0084** is **not** published page 84 (**C582**). Breathitt original **unread**. fishergenes p.68 still unmatched. Original 1932 DC and 1840 bond **still unseen**. Do **not** promote **C509**. **B061 remains open**. **B066 partial**. Skip **C221–C280 / L245–L342 / S259–S266**. Next unused **C584+ / L507+ / S476+ / DOC079+**.

# Pass 57 listing (30 Oct 2026, America/New_York)

Catalog **84** not re-listed. Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Original-image work this pass: 1840 Breathitt M704-**105** / IA `populationsc18400105unit` — all **12** even name pages `_0132`–`_0154` **nil** Newman/Tincher heads (**C584 / DOC079**); recap `_0156` Abstract, 11 rows; certification **13 Nov 1840** (**C585 / DOC080**). **John Bowman** is not Newman. McIlvain county and fishergenes p.68 **still residual**. Original 1932 DC and 1840 bond **still unseen**. Do **not** promote **C509**. **B061 remains open**. **B066 partial**. Skip **C221–C280 / L245–L342 / S259–S266**. Next unused **C587+ / L511+ / S477+ / DOC081+**.

# Pass 58 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **84** / `hasMore: false` / `totalMatched: 84`. Unchanged vs Pass 55. [Continue Dora genealogy](bc-d7a3569c-3baa-589d-8f26-02d269c034dd) now **IDLE**; [Dora's biography research](bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **RUNNING** — process claims only, not linear-read. Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Original-image work this pass: 1840 Estill McIlvain M704-**109** / IA `populationsc18400109unit` — left margin **Estill County** overlay **0088** (**C587 / DOC081**); all **25** even name pages `_0092`–`_0140` **nil** Newman/Tincher heads (**C588**); fishergenes “Estill p.68” **is** overlay **0129** **Valentine R. Ward** (**C589 / DOC082**); overlay **0121** **Wm Fincher** not Tincher (**C590 / DOC083**); Edmonson divider overlay **0141**, **W. Edwards**, total **2914** (**C591 / DOC084**). Unmerged FAN Smallwood/Stone/Wiseman (**C592**). Original 1932 DC and 1840 bond **still unseen**. Do **not** promote **C509**. **B061 remains open**. **B066 done**. Skip **C221–C280 / L245–L342 / S259–S266**. Next unused **C596+ / L517+ / S478+ / DOC085+**.

# Pass 59 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **85** / `hasMore: false` / `totalMatched: 85`. NEW vs Pass 58: [Dora passes from B049](bc-6a14d74c-f8ff-5225-b59a-0fd32ced5617) (RUNNING, internal) — process claims only, not linear-read. Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Work this pass: IA Burns title **numFound 0** (**C599**); Estill IGI **M517301** / KDLA **994033** skip 1840 (**C598**); TFKRHA Williams/Dishon Owsley list (Wayback) **21 Jul 1864** **Harry H. Newnam** × **Mary J. Partington** (**C596 / DOC085**), **PROBABLE** the 1870 Henry 24 couple; 1843–49 slice **nil** Harrison×Susan on that partial list (**C597**). Original 1932 DC and 1840 bond **still unseen**. Do **not** promote **C509**. **B061 remains open**. Skip **C221–C280 / L245–L342 / S259–S266**. Next unused **C603+ / L524+ / S481+ / DOC086+**.

# Pass 60 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **85** / `hasMore: false` / `totalMatched: 85`. Unchanged vs Pass 59. [Dora passes from B049](bc-6a14d74c-f8ff-5225-b59a-0fd32ced5617) still **RUNNING**; [Dora's biography research](bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK** on `cursor/dora-biography-passes-5b6a` (commit `c6d2369` claims B040 ED 38 closed as **their C281** — **not imported**). Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Work this pass: 1890 veterans **transcript** Elias T. Bugler Co C 14 Ky Cav Old Landing (**C603 / DOC086**); discharge **6/16** vs roster **9/16** (**#23** **C604**); Henry H. Pvt unit **blank**, Proctor PO (**C605 / DOC087**); KYDI 1918 statewide **07/11** **nil** Newman/Lee (**C611**); Owsley 1917–19 extracts **nil** (**C612**). Original M123-**3**, 1932 DC, and 1840 bond **still unseen**. Do **not** promote **C509**. **B061 / B062 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C615 / L529 / S485**. Next unused after Pass 60 filing was **C619+ / L534+ / S487+ / DOC088+**.

# Pass 61 listing (30 Oct 2026, America/New_York)

Catalog **85** unchanged. Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Work this pass: 1883 Lee/Owsley pensioner tables **nil** Newman (**C619/C620 / DOC091**); Speed 1897 **BUGLERS—Elias T. Newman** (**C621 / DOC088**); IA `beatty` **30 Nov 1928** Uncle Doll Newman sick (**C623 / DOC089**) and **1 Apr 1932** Sparks visiting Uncle Doll Newnam (**C624 / DOC090**); Bio_C parents/pension **blank** (**C622**); NPS unit MO window (**C625**). GPO 1883 original unread. Original 1932 DC and 1840 bond **still unseen**. Do **not** promote **C509**. **B061 remains open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C630 / L541 / S493**. Next unused after Pass 61 filing was **C633+ / L543+ / S495+ / DOC092+**.

# Pass 62 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **85** / `hasMore: false` / `totalMatched: 85`. Unchanged vs Pass 59. Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Work this pass: live TFKRHA `14THNT.htm` **Newnam, Elias T.** rank **Bug**, MO **16 Sep 1863** Maysville (**C633 / DOC092**); Henry H. rank **blank** (**C634**); IA T288 title **numFound 0** (**C635**); FS coll. **1919699** **403** (**C640**); NPS soldier search JS shell (**C636**); USGW Estill N/T **timeout** (**C637**); UK omeka **65438** scattered issues (**C638**). John Henry “Uncle Doll” Herald **not merged** (**C643**). Original 1932 DC, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 remains open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C642 / L549 / S493**. Next unused after Pass 62 filing was **C646+ / L551+ / S502+ / DOC093+**.

# Pass 63 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **86** / `hasMore: false` / `totalMatched: 86`. NEW vs 85: [Dora B045 B061 films](bc-9acea467-c941-5e47-8401-8d443a3b0c7e) **RUNNING**, internal, **no** PR, **no** branch — process-only, **not** linear-read (**C667**). Nested reviewer **not** respawned. **No** new independently image-backed P001 1900–1926 residence. Work this pass: NARA M850 reel **1661** original **Newnam, Elias T.** Army Invalid cert **631218**, Bugler Co. 14 Ky V Cav, Proctor (**C646 / DOC093**); **Newnam, Henry H.** cert **798864**, Pvt Co C, died **6 Aug 1916** Travelers Rest, widow **Manerva** cert **837778**, married **1895**, d. **28 Aug 1920** (**C648/C650 / DOC094/DOC095**, **#24**); reel **1660** Newman spelling Eli O. 9 Ind / Henry H. 81 Pa **not** the 14 Ky Cav pair (**C651 / DOC096**); GPO vol. 5 Lee OCR **nil** Newman (**C657 / DOC097**). Original 1932 DC, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C656 / L551 / S505**. Next unused **C669+ / L561+ / S508+ / DOC098+**.

# Pass 64 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **86** / `hasMore: false` / `totalMatched: 86`. Unchanged vs Pass 63. Nested reviewer **not** respawned. [Dora B045 B061 films](bc-9acea467-c941-5e47-8401-8d443a3b0c7e) still **RUNNING**, process-only. [Dora's biography research](bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK**. Message queue empty. **No** new independently image-backed P001 1900–1926 residence. Work this pass: 1900 original T623-**547** leaf **579** ED **89** sh **7 B** dw **114/115 Newnam, Henry H.** 55 + Minerva (**C669 / DOC098**); 1910 original T624-**498** leaf **988** ED **170** sh **2 A** dw **20/20 Newman, Henry H.** 68 **m2 15y** + Manerva (**C672 / DOC099**); conflict **#25** (Mary J. ≠ Manerva); KYDI 1920 **nil** Manerva Newman civil row (**C677 / DOC100**). Original 1932 DC, 1916 DC, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C684 / L561 / S515**. Next unused **C689+ / L571+ / S517+ / DOC101+**.

# Pass 65 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (limit 200) → **86** / `hasMore: false` / `totalMatched: 86`. Unchanged vs Pass 64. Nested reviewer **not** respawned. Message queue empty. NEW vs 86: none. Process-only folds not previously named on this file: [Dora location search](bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03) **RUNNING**, PR **#31** OPEN, branch `cursor/dora-locations-1900-death-8d03` (Bollinger 1900 Whitewater ED 10 / Union ED 8; **their IDs not imported**). [Scan ED5 pages 405-434](bc-0039b8bf-7edb-593b-82c3-cb59471d392a) **RUNNING**. [Dora B045 B061 films](bc-9acea467-c941-5e47-8401-8d443a3b0c7e) still **RUNNING**. [Dora's biography research](bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK**, PR **#33** OPEN (sibling C281 **not imported**). [Dora passes from B049](bc-6a14d74c-f8ff-5225-b59a-0fd32ced5617) **IDLE**. This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: 1910 original T624-**498** leaf **881** ED **165** sh **7 B** dw **119/119 Newman, Arthur** 27 + Florence + Omer (**C693 / DOC101**), **PROBABLE** 1900 son (**C694**); 1920 original T625-**594** ED **94** Wild Dog sh **1 A–7 B** hh **1–129 nil** Newman/Manerva Newnam (**C690 / DOC102**); Evans+Minerva 67 **DISPROVED** (**C691**); Lee 1920 Manervas other women (**C692**); 1880 Burris×Manerva 25 VA **POSSIBLE**, unmerged (**C695**). Original 1932 DC, 1916 DC, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C689 / L571 / S517**. Next unused **C699+ / L580+ / S524+ / DOC103+**.

# Pass 66 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **90** / `hasMore: false` / `totalMatched: 90`. Was **86**. NEW vs 86: four nested IDLE helpers of PR **#31** — [Read ED9 sheets 20-23](https://cursor.com/agents/bc-72256edf-57e1-5271-ac6b-c39a4996b00a), [Read ED9 sheets 9-14](https://cursor.com/agents/bc-3a494f12-b6f0-5e39-bd94-e5262725a6d7), [Read ED9 sheets 3-8](https://cursor.com/agents/bc-1939d385-feff-5860-8edb-77e36e1c09fc), [Read ED9 sheets 15-19](https://cursor.com/agents/bc-2c28b46e-4813-50d2-889d-b8e6c560f097) — process-only, **their IDs not imported**. Nested reviewer **not** respawned. Message queue empty. Still RUNNING: [Dora location search](https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03) PR **#31**; [Scan ED5 pages 405-434](https://cursor.com/agents/bc-0039b8bf-7edb-593b-82c3-cb59471d392a); [Dora B045 B061 films](https://cursor.com/agents/bc-9acea467-c941-5e47-8401-8d443a3b0c7e). [Dora's biography research](https://cursor.com/agents/bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK**, PR **#33** OPEN (sibling C281 **not imported**). This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: 1920 original T625-**594** leaf **1114** ED **90** sh **7 A** dw **113/121 Newman, Arthur** 45 + Florence 33 + Omer 12 + Grant 3½ (**C700 / DOC103**), **PROBABLE** 1910 man (**C701**); Manerva **not** in that house (**C702**); ED **89** sh **11 A–13 B** remainder **nil** Newman head (**C703 / DOC105**); Tymes child Manerva 2 **DISPROVED** (**C704**); Soundex N-550 leaf **4109** matches the original (**S526**); leaves **4582–4639** **nil** Manerva/Minerva Newman (**C705 / DOC104**). Original 1932 DC, 1916 DC, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C699 / L580 / S524**. Next unused **C709+ / L589+ / S530+ / DOC106+**.

# Pass 67 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (`includeArchived: true`, limit 200) → **95** / `hasMore: false` / `totalMatched: 95`. Was **91** mid-pass / **90** at Pass 66. NEW vs 91: [Read ED1 sheets 8-15](https://cursor.com/agents/bc-8d42d917-c7e9-5a6a-8f46-d9f89bce2b44) **RUNNING** empty transcript; [Read ED1 sheets 1-8](https://cursor.com/agents/bc-0d3e2cc8-f7d8-5ad9-a406-12fc3aa1270f) **RUNNING** empty; [Fold nested Dora chats](https://cursor.com/agents/bc-9858a928-741f-5e75-a156-f65d9b9fa4ae) IDLE process-fold of `bc-988b2961` (no minted IDs); [Summarize B045 B061 films](https://cursor.com/agents/bc-37d21a44-2e0e-5311-9298-1893db087a43) IDLE null-fold of empty parent. Earlier NEW vs 90: [Fold nested Dora chats](https://cursor.com/agents/bc-988b2961-b14b-53ee-b3b1-25f15fd9a8b1) — read-only, **no case edits, no minted IDs**. Nested reviewer **not** respawned. Message queue empty. Still RUNNING empty: [Dora B045 B061 films](https://cursor.com/agents/bc-9acea467-c941-5e47-8401-8d443a3b0c7e). PR **#31** ED9/ED1 helpers and location-search IDs **not imported**. PR **#33** sibling C281 **not imported**. This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: Rosenbalm 1916 C third **Widowed**/blank-parents extract (**C709 / DOC106**); entire ED **90** original one Newman house (**C713 / DOC107**); Barker Malvera / Wilson×Minerva / Baker Sarah / Manerva SMITH **DISPROVED** as C650; ED **91** sh **1 A–3 B** **partial nil** (**C715**); Soundex N-550 Walter window **nil** Owsley/Lee Walter with Manerva (**C717 / DOC108**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C724 / L589 / S536**. Next unused **C729+ / L604+ / S539+ / DOC109+**.

# Pass 68 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (limit 50 + offset 50) → **98** / `hasMore: false` / `totalMatched: 98`. Was **95**. NEW vs 95: [Fold nested chats transcript](https://cursor.com/agents/bc-ebb7fcf9-8dac-5db9-ac5d-795e15ba63f5), [Summarize B045 films transcript](https://cursor.com/agents/bc-f6db645d-c52e-56b0-b9d0-3058626d171a), [Fold ED1 sheets 8-15](https://cursor.com/agents/bc-e553a117-8285-5a1d-8c69-d5fede775721) — process-folds only, **no IDs imported**. [Read ED1 sheets 1-8](https://cursor.com/agents/bc-0d3e2cc8-f7d8-5ad9-a406-12fc3aa1270f) now IDLE with content: 1900 Bollinger Crooked Creek ED **1** sh **1 A–8 A** **nil** Newman; three Dora lines rejected as P001; **no minted IDs**. Nested reviewer **not** respawned. Message queue empty. Still RUNNING empty: [Dora B045 B061 films](https://cursor.com/agents/bc-9acea467-c941-5e47-8401-8d443a3b0c7e). PR **#31** ED9/ED1 helpers and location-search IDs **not imported**. PR **#33** sibling C281 **not imported**. This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: entire ED **91** Cow Creek original **nil** Newman head (**C729 / DOC109**); Cale Minerva 73 **DISPROVED** as C650 (**C730**); Allen Ella 30 / Cale wife 42 / Smith Dora 12 **DISPROVED** as P001; ED **92** sh **1 A** header only; TFKRHA 1916 G **429** (**C734**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C735 / L604 / S543**. Next unused **C739+ / L612+ / S546+ / DOC110+**.

# Pass 69 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (limit 200) → **114** / `hasMore: false` / `totalMatched: 114`. Was **98**. NEW vs 98: sixteen nested IDLE helpers — [Visual-read ED88 Booneville 1038-1052](https://cursor.com/agents/bc-b5228199-be20-5b42-95b6-713698b9f01f), [Visual-read ED88 Booneville 1053-1075](https://cursor.com/agents/bc-d4f76b2a-3914-517c-a1a8-a76558cf12c6), [Visual-read ED93 B-side names](https://cursor.com/agents/bc-64a803d9-b4d9-5343-a96a-3288dc23374e), [Visual-read ED93 Buck Creek names](https://cursor.com/agents/bc-c49ec96e-1d33-51da-a0ce-5b96e625d5df), [Visual-read ED92 names 1156-1162](https://cursor.com/agents/bc-223fa532-0efb-57f1-84cb-91ffa94d87af), [Visual-read ED92 names 1163-1169](https://cursor.com/agents/bc-e98a6512-0939-519a-aabf-b0976f74dcb0), ED2 Fillmore (`bc-f57a2903`, `bc-aee8af5b`, fold `bc-0a95f53b`), ED3 German (`bc-83740d97`, `bc-bc656991`, fold `bc-a42becc8`), ED **91** remainder (`bc-e5dd296c`, `bc-7e36c479`, `bc-8b95e960`), ED1 1–8 transcript fold (`bc-d4a90edf`) — process-folds only, **no IDs imported**. Nested reviewer **not** respawned. Message queue empty. Still RUNNING empty: [Dora B045 B061 films](https://cursor.com/agents/bc-9acea467-c941-5e47-8401-8d443a3b0c7e). PR **#31** ED9/ED1 helpers and location-search IDs **not imported**. PR **#33** sibling C281 **not imported**. This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: entire ED **88** Booneville original **nil** Newman head (**C739 / DOC110**); Taylor Manerva 73 **DISPROVED** as C650 (**C740**); ED **92** Buffalo filmed leaves **nil** Newman head (**C743 / DOC111**); hh **1–13** residual (**C752**); entire ED **93** Buck Creek original **nil** Newman head (**C746 / DOC112**); Marcum Manerva 54 **DISPROVED** (**C747**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C749 / L612 / S556**. Next unused **C753+ / L623+ / S558+ / DOC113+**.

# Pass 70 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (limit 200) → **114** / `hasMore: false` / `totalMatched: 114`. Unchanged vs Pass 69. Nested reviewer **not** respawned. Message queue empty. Still RUNNING empty: [Dora B045 B061 films](https://cursor.com/agents/bc-9acea467-c941-5e47-8401-8d443a3b0c7e). PR **#31** ED9/ED1/ED2/ED3 helpers and location-search IDs **not imported**. PR **#33** sibling C281 **not imported**. This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: 1910 original T624-**498** leaf **884** ED **165** sh **9 A** dw **147/147 Gilbert, Robert** 29 m2 8 + **Josie** 26 m1 8 1-0 (**C753 / DOC113**), **PROBABLE** 1900/1916 Josephine (**C754**); sh **9 B** **Lynch, Benton** × **Laura** 34 — Newman **not** on the original (**C759**); 1920 G-416 **nil** Robert ~39 Owsley head (**C755 / DOC114**); Soundex Robert 84 = original **Gilbert, John** FIL 84 (**C756 / DOC115**); VS 1908–1910 **nil** Josephine×Gilbert (**C758**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C760 / L623 / S563**. Next unused **C763+ / L633+ / S564+ / DOC116+**.

# Pass 71 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (limit 200, includeArchived) → **114** / `hasMore: false` / `totalMatched: 114`. Unchanged vs Pass 70. Nested reviewer **not** respawned. Message queue empty. Still RUNNING empty: [Dora B045 B061 films](https://cursor.com/agents/bc-9acea467-c941-5e47-8401-8d443a3b0c7e). PR **#31** ED9/ED1/ED2/ED3 helpers and location-search IDs **not imported**. PR **#33** sibling C281 **not imported**. This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: 1910 original T624-**498** leaf **957** ED **168** sh **5 B** dw **76/76 Gilbert, John** 74 m2 18 + **Darkis[?]** Wife 39 (**C765 / DOC116**), **PROBABLE** 1920 FIL 84; next-door **Baker, Robert H.** × **Laura** 28 **not merged** with 1920 Louise[?] (**C766**); Lee Books **4–9** / Owsley VS **1903–4** / Jackson G/N-P **nil** Josephine Newnam × Gilbert (**C763/C764/C767**); G-416 **Douglas** ED **92** sh **2** proves Soundex indexed filmed sheets (**C768 / DOC117**); C512 sampled **nil** vol **76** ED **92** sh **1** (**C769**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C770 / L633 / S572**. Next unused **C775+ / L645+ / S573+ / DOC118+**.

# Pass 72 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (limit 200, includeArchived) → **114** / `hasMore: false` / `totalMatched: 114`. Unchanged vs Pass 71. Nested reviewer **not** respawned. Message queue empty. Still RUNNING empty: [Dora B045 B061 films](https://cursor.com/agents/bc-9acea467-c941-5e47-8401-8d443a3b0c7e). PR **#31** ED9/ED1/ED2/ED3 helpers and location-search IDs **not imported**. PR **#33** sibling C281 **not imported**. This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: 1910 original T624-**498** leaves **948–949** ED **168** sh **1 A / 1 B** Buffalo openers (**C775 / DOC118**); Rice **Dora** 2 2/12 **DISPROVED** as P001 (**C776**); C-512 **Combs, Samuel B.** 42 vol **76** ED **90** ln **72**, **PROBABLE** 1910 dw 1, **not** ED 92 sh 1 (**C777 / DOC119**); G-163 **Gabbard, Elijah** 41 Lee **not merged** with 1910 Elijah × Amy (**C779 / DOC120**); **Gabbard, Lee** 47 Breathitt **not merged** with 1910 Lee × Eliza (**C780**); C512 **nil** Combs, Lowe (Louise 1252 / Loya 1253 consecutive) (**C789**); Wolfe/Clay compiled **nil** Josephine×Gilbert (**C782/C783**); two Estill 1901–02 return plates **nil** (**C784**); Breathitt still **403** (**C785**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C786 / L645 / S579**. Next unused **C790+ / L659+ / S581+ / DOC121+**.

# Pass 73 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (includeArchived, offset 0 + 50 + 100) → **114** / `hasMore: false` / `totalMatched: 114`. Unchanged vs Pass 72. Nested reviewer **not** respawned. Message queue empty. Still RUNNING empty: [Dora B045 B061 films](https://cursor.com/agents/bc-9acea467-c941-5e47-8401-8d443a3b0c7e). PR **#31** ED9/ED1/ED2/ED3 helpers and location-search IDs **not imported**. PR **#33** sibling C281 **not imported**. This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: G-000 **Gay, Walker** 44 vol **76** ED **90** sh **3**, **not** missing sh 1 and **not** 1910 Matilda (**C790 / DOC121**); G-000 **nil** Gay Matilda ~42 Wd, Gee Matilda 19 Fayette SIL **DISPROVED** (**C791**); R-200 sampled Rice Williams **DISPROVED** / **nil** Owsley William E × Eliza (**C792 / DOC122**); H-435 Helton Williams **DISPROVED** / **nil** Owsley × Eliza (**C793 / DOC123**); B-653 **nil** Robb (**C794 / DOC124**); R-300 Reed David M 45 Clark × Nannie **DISPROVED** (**C795 / DOC125**); S-520 ended at Dollie, **nil** William (**C796 / DOC126**); H-630 Howard Drucilla 16 Leslie DIL **DISPROVED** as 1910 Hardy 40 Wd (**C797 / DOC127**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C800 / L659 / S588**. Next unused **C801+ / L672+ / S589+ / DOC128+**.

# Pass 74 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (includeArchived, limit 200) → **115** / `hasMore: false` / `totalMatched: 115`. Was **114**. NEW vs 114: [Dora B088 John Jennie](https://cursor.com/agents/bc-864394d5-805a-5cb7-a6cd-a6babdbb5a6b) RUNNING, 0 events, **no IDs imported**. Nested reviewer **not** respawned. Message queue empty. [Dora B045 B061 films](https://cursor.com/agents/bc-9acea467-c941-5e47-8401-8d443a3b0c7e) now IDLE. Still RUNNING: [Dora location search](https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03) PR **#31**; [Scan ED5 pages 405-434](https://cursor.com/agents/bc-0039b8bf-7edb-593b-82c3-cb59471d392a). [Dora's biography research](https://cursor.com/agents/bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK** PR **#33** (sibling C281 **not imported**). This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: 1910 original T624-**498** leaf **949** ED **168** sh **1 B** dw **14/14 Baker, Jesse** 42 × Emily and dw **15/15 Evans, John** 45 × Susan (**C801 / DOC128**); leaves **950–951** sh **2 A/2 B** FAN dw **16–33** including **Gay, Henry** 46 × Nancy 40 10-9 (**C802 / DOC129**); 1920 original T625-**594** leaf **1166** ED **92** stamped **6 A** dw **105/105 Gay, Henry** 55[?] (**C803 / DOC130**), Soundex G-000 **3995** copies that original (**DOC131**), **PROBABLE** 1910 dw 26, **not** missing sh 1; R-200 Elizabeth 17 Greenup SIL and 82 Lawrence **DISPROVED**, Ben A/H/W **DISPROVED**, **nil** Rice Benjamin ~35 × Cynthia Owsley (**C804 / DOC132**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C805 / L672 / S594**. Next unused **C808+ / L683+ / S595+ / DOC133+**.

# Pass 76 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (includeArchived, offset 0 + 50 + 100) → **115** / `hasMore: false` / `totalMatched: 115`. Unchanged vs Pass 74. NEW vs 114 still only [Dora B088 John Jennie](https://cursor.com/agents/bc-864394d5-805a-5cb7-a6cd-a6babdbb5a6b) RUNNING, 0 events, **no IDs imported**. Nested reviewer **not** respawned. Message queue empty. Still RUNNING: [Dora location search](https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03) PR **#31**; [Scan ED5 pages 405-434](https://cursor.com/agents/bc-0039b8bf-7edb-593b-82c3-cb59471d392a). [Dora's biography research](https://cursor.com/agents/bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK** PR **#33** (sibling C281 **not imported**). This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: 1920 original T625-**594** leaf **1167** ED **92** stamped **6 B** dw **113/113 Abner, Lewis** 50 × Susan (**C808 / DOC133**), **PROBABLE** 1910 dw 16, **not** missing sh 1; dw **111/111 Abner, Casey** 32 **not merged** (**C818**); dw **115/115 Barrett, Bruce** 42 × Anna **POSSIBLE** 1910 Ben (**C819**); leaf **1168** stamped **7 A** dw **117/117 Abner, Samuel** 53 × Maria (**C809 / DOC134**), **PROBABLE** 1910 dw 20; dw **118/118 Baker, James** 29 × Dorothy **DISPROVED** as 1910 James 35 × Caroline (**C814**); dw **119/119 Gabbard, W.B.** 42 × **Rosa** **POSSIBLE** only (**C813**); ln **34** dw **124/124 Baker, Jesse** 54 × Emily (**C810**), Soundex B-260 **5030/5031** copies that original (**C811 / DOC135**), **PROBABLE** 1910 dw 14, **not** missing sh 1; E-152 sampled Johns **DISPROVED** / **nil** Evans, John ~55 × Susan Owsley as head (**C812 / DOC136**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C815 / L683 / S599**. Next unused **C820+ / L696+ / S600+ / DOC137+**.

# Pass 77 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (includeArchived, offset 0 + 50 + 100) → **116** / `hasMore: false` / `totalMatched: 116`. Was **115**. NEW vs 115: [Dora B088 Bell Wolfe](https://cursor.com/agents/bc-f2d926d6-72d5-54d0-92fb-9429a0cf9afa) RUNNING; events are Gmail MCP auth warnings only; **no IDs imported**. [Dora B088 John Jennie](https://cursor.com/agents/bc-864394d5-805a-5cb7-a6cd-a6babdbb5a6b) now IDLE; **no IDs imported**. Nested reviewer **not** respawned. Message queue empty. Still RUNNING: [Dora location search](https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03) PR **#31**; [Scan ED5 pages 405-434](https://cursor.com/agents/bc-0039b8bf-7edb-593b-82c3-cb59471d392a). [Dora's biography research](https://cursor.com/agents/bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK** PR **#33** (sibling C281 **not imported**). This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: 1920 original T625-**594** filmed ED **92** sh **1 A–5 B** **nil Evans, John as head** (**C820 / DOC137**); leaf **1161** stamped **3 B** dw **59/59 Bowman, Henry** 67 Wd (**C821 / DOC138**), **not merged** with 1910 dw **31**; dw **60/60 Bowman, Sile** 60 and dw **61/61 Bowman, Andy** 37 (**C822**); leaf **1165** stamped **5 B** dw **98/98 Bowman, Jack** f 57 Wd (**C823 / DOC139**), Soundex B-550 **2400** Pike Jack **DISPROVED**; dw **100/100 Dean, George** 44 × Jane **DISPROVED** as 1910 George × Martha (**C824**); 1910 original dw **31/31 Bales, John B.** 40 × Annie (**C825 / DOC140**), Pass 74 “Bowman[?]” **corrected**; B-550 denser Henry **2321–2358** **nil** Bowman Henry 67 ED **92**, Owsley hits are ED **89** ages **20** and **43** (**C826 / DOC141**); C-652 sampled James **nil** Carmack James Owsley (**C827 / DOC142**); **nil** McIntosh Daniel ~52; Gabbard Michael 67 **DISPROVED** as 1910 Michael (**C828**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C829 / L696 / S606**. Next unused **C832+ / L711+ / S607+ / DOC143+**.

# Pass 78 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (includeArchived, limit 200) → **117** / `hasMore: false` / `totalMatched: 117`. Was **116**. NEW vs 116: [Dora B088 Wolfe sheets](https://cursor.com/agents/bc-729f9487-47ca-51ff-81b5-6be4bd4a10ab) RUNNING; **no IDs imported**. [Dora B088 Bell Wolfe](https://cursor.com/agents/bc-f2d926d6-72d5-54d0-92fb-9429a0cf9afa) now IDLE; [Dora B088 John Jennie](https://cursor.com/agents/bc-864394d5-805a-5cb7-a6cd-a6babdbb5a6b) IDLE; **no IDs imported**. Nested reviewer **not** respawned. Message queue empty. Still RUNNING: [Dora location search](https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03) PR **#31**; [Scan ED5 pages 405-434](https://cursor.com/agents/bc-0039b8bf-7edb-593b-82c3-cb59471d392a). [Dora's biography research](https://cursor.com/agents/bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK** PR **#33** (sibling C281 **not imported**). This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: 1910 original T624-**498** leaves **950–951** ED **168** sh **2 A/2 B** dw **27/27 Gaine[?], Reece** 26 × wife line written **Daniel, Linda** 19 + Bessie 4/12 (**C832 / DOC143**); 1920 original T625-**594** leaf **1166** ED **92** stamped **6 A** dw **106/106 Daniel, Reece** 38 × Lula + Bessie 10 (**C833 / DOC145**), **PROBABLE** 1910 dw 27, **not** missing sh 1; G-500 denser Reece **nil** Owsley, Guyn Raymond / Gwinn Robert **DISPROVED** (**C834 / DOC146**); McIntosh Daniel 42 × Fannie[?] Harris (**C835**); M-253 denser **nil** Daniel ~52, Mackintosh 23 Knox **DISPROVED** (**C836 / DOC147**); Jacob × **Lyda** 77 **CORRECTED** (**C837**); James × **Maribe** (**C838**); C-652 remaining James **nil** (**C839 / DOC149**); Gabbard Michael 25 × Addie / **Willis** 30 × Jane **CORRECTED** (**C840 / DOC144**); G-163 **nil** Willis and Michael; Mellie 15 ED **94** FAN (**C841/C842 / DOC148**); Dean **Maggie** 65 **CORRECTED** (**C843**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C844 / L711 / S614**. Next unused **C847+ / L727+ / S615+ / DOC150+**.

# Pass 79 listing (30 Oct 2026, America/New_York)

`list-cloud-agents` (includeArchived, offset 0+50) → **118** / `hasMore: false` / `totalMatched: 118`. Was **117**. NEW vs 117: [Dora pass 90 backlog](https://cursor.com/agents/bc-bb0d46cb-78de-55bf-ac6d-1b18beb4b660) RUNNING; **no IDs imported**. [Dora B088 Wolfe sheets](https://cursor.com/agents/bc-729f9487-47ca-51ff-81b5-6be4bd4a10ab) now IDLE; [Dora B088 Bell Wolfe](https://cursor.com/agents/bc-f2d926d6-72d5-54d0-92fb-9429a0cf9afa) IDLE; [Dora B088 John Jennie](https://cursor.com/agents/bc-864394d5-805a-5cb7-a6cd-a6babdbb5a6b) IDLE; **no IDs imported**. Nested reviewer **not** respawned. Message queue empty. Still RUNNING: [Dora pass 90 backlog](https://cursor.com/agents/bc-bb0d46cb-78de-55bf-ac6d-1b18beb4b660). [Dora's biography research](https://cursor.com/agents/bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK** PR **#33** (sibling C281 **not imported**). This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: 1920 original T625-**594** leaf **1039** ED **88** sh **1 B** ln **72 Edmonds, John W.** 54 S + nephew Carielee + niece Molly (**C847 / DOC150**); Soundex E-152 **1511** “Evans, John W.” is that Edmonds house (**C848 / DOC151**, Hard Rule 6); leftover-even Johns **nil** Evans, John ~55 × Susan ED **92** (**C849**); leaf **1432** Alice house **DISPROVED**, ED **300** not Owsley (**C850**); densified Susan **2151–2169** **nil** Evans, Susan ~39 Owsley (**C851 / DOC152**); Owsley 1911–1920 DC extracts **nil** matching John Evans decedent (**C852 / DOC153**); Josephine neighboring-county substitutes this pass **nil**/n/a (**C853**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C856 / L727 / S615**. Next unused **C857+ / L739+ / S622+ / DOC154+**.

# Pass 80 listing (31 Oct 2026, America/New_York)

`list-cloud-agents` (includeArchived, limit 200) → **135** / `hasMore: false` / `totalMatched: 135`. Was **118**. NEW vs 118 (17; **no IDs imported**): [Read MO William fam sheets](https://cursor.com/agents/bc-c4020172-274a-50ef-a295-086eb12500f3) RUNNING; [Read MO Thomas fam sheets](https://cursor.com/agents/bc-482ecd04-8fa1-56c7-812d-fb82d25c2420) RUNNING; [Read MO James fam sheets](https://cursor.com/agents/bc-b77c4c20-e4e2-5fd2-91d4-c3b88793377d) RUNNING; [Read MO John fam sheets](https://cursor.com/agents/bc-6f4d1f71-347f-5c27-bf2a-9c33f58d712b) RUNNING; [Dora open backlog B058](https://cursor.com/agents/bc-fc8fc249-d72f-56b3-881f-27ea729c62c7) RUNNING; [Dora B089 Estill 33-11](https://cursor.com/agents/bc-647ba72a-69ff-5808-8cb8-6d70cab6d565) IDLE; [Dora B089 Estill 33-6](https://cursor.com/agents/bc-da32ff59-2721-5bc3-b5d2-54b3f18b0982) IDLE; [Dora B089 Estill 33-8](https://cursor.com/agents/bc-f051b252-00aa-5e9b-92c1-a03875af0ff3) IDLE; [Read TN Thomas/William sheets](https://cursor.com/agents/bc-17bb034f-09af-5c04-95b6-7026d3f9fdd4) IDLE; [Read TN James/John fam sheets](https://cursor.com/agents/bc-5808b02d-31a5-5cee-9caa-11ab31229b42) IDLE; [Read IL402 William sheets](https://cursor.com/agents/bc-5a7c8f29-3863-578f-9a7c-f4b721af81f4) IDLE; [Read IL Thomas + early IL402](https://cursor.com/agents/bc-7370f418-7b5d-59eb-8441-e032864872ec) IDLE; [Read IL John fam sheets 046-090](https://cursor.com/agents/bc-f1fe77da-967a-527c-96d8-d8a2ac72c7d1) IDLE; [Read IL John fam sheets 000-045](https://cursor.com/agents/bc-5d3584a5-ce3e-541e-87d0-088528c1517b) IDLE; [Read IL James fam sheets](https://cursor.com/agents/bc-2a7d4e51-99f8-5c06-8bf4-e9ceba42036a) IDLE; [Dora pass 101 other passes](https://cursor.com/agents/bc-10c54e42-5af0-5bba-879c-f7c4eee90d06) IDLE; [Dora B088 Antioch 242](https://cursor.com/agents/bc-e38544a3-f653-5370-a4b4-dfd0d2eb5ef0) IDLE. [Dora pass 90 backlog](https://cursor.com/agents/bc-bb0d46cb-78de-55bf-ac6d-1b18beb4b660) now IDLE. Nested reviewer **not** respawned. Message queue empty. Still RUNNING: [Dora location search](https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03) PR **#31**; [Scan ED5 pages 405-434](https://cursor.com/agents/bc-0039b8bf-7edb-593b-82c3-cb59471d392a). [Dora's biography research](https://cursor.com/agents/bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK** PR **#33** (sibling C281 **not imported**). This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: E-152 L-window **1651–1695** **nil** Evans, Lula ~14 Owsley; **1684** Lula 14 Carter SIL **DISPROVED** (**C857 / DOC154**); R-window **2001–2040** **nil** Evans, Robert ~11 Owsley; **2023** Robert E 53 Owsley ED **89** **DISPROVED** as Buffalo child, not merged (**C859/C860 / DOC155**); leftover odd Johns **1421–1513** **nil** Evans, John ~55 × Susan ED **92**; John window through Joseph **1515** image-closed (**C861 / DOC156**); **1479** Lee Beattyville John H × Julia **DISPROVED** (**C862**); **1509** Lee John W × Dora 24 **DISPROVED as P001** (**C863**); Josephine this pass **nil**/n/a (**C864 / DOC157**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. Do **not** close B063. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C867 / L739 / S622**. Next unused **C868+ / L752+ / S627+ / DOC158+**.

# Pass 81 listing (31 Oct 2026, America/New_York)

`list-cloud-agents` (includeArchived, limit 200) → **135** / `hasMore: false` / `totalMatched: 135`. Unchanged vs Pass 80. Already-folded chats: [Read MO William fam sheets](https://cursor.com/agents/bc-c4020172-274a-50ef-a295-086eb12500f3) now IDLE; [Read MO Thomas fam sheets](https://cursor.com/agents/bc-482ecd04-8fa1-56c7-812d-fb82d25c2420) now IDLE; [Read MO James fam sheets](https://cursor.com/agents/bc-b77c4c20-e4e2-5fd2-91d4-c3b88793377d) still RUNNING; **no IDs imported**. Nested reviewer **not** respawned. Message queue empty. Still RUNNING: [Dora location search](https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03) PR **#31**; [Scan ED5 pages 405-434](https://cursor.com/agents/bc-0039b8bf-7edb-593b-82c3-cb59471d392a); [Read MO James fam sheets](https://cursor.com/agents/bc-b77c4c20-e4e2-5fd2-91d4-c3b88793377d). [Dora's biography research](https://cursor.com/agents/bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK** PR **#33** (sibling C281 **not imported**). This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: original T625-**594** leaf **1092** ED **89** sh **9 A** ln **30 Evans, Robert E.** 53 × Margie (**C868 / DOC158**), Hard Rule 6 of Soundex **2023**; A-156 **1450** “Arch” is original **Casey** (**C869 / DOC159**); Casey window **nil** Casey given-name (**C870**); **1520** Isaac W A-2 ED **90** proves Owsley indexing (**C871**); Lewis window **nil**, **1585** Louis 41 Lee **DISPROVED**, original Lewis is a Soundex miss (**C872 / DOC160**); **1628** Samuel copies original Maria house, A-156 given-name block closed (**C873**); C-652 **2751–2769** / G-500 **2361–2364** / M-253 **3729** residuals **closed** (**C874/C875/C876 / DOC161**); Floyd Josephine substitutes **nil**/other (**C877 / DOC162**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. Do **not** hunt D-540 to prove **C833**. Do **not** close B063. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C878 / L752 / S627**. Next unused **C879+ / L765+ / S634+ / DOC163+**.

# Pass 82 listing (31 Oct 2026, America/New_York)

`list-cloud-agents` (includeArchived, limit 200) → **139** / `hasMore: false` / `totalMatched: 139`. Was **135**. NEW vs 135 (4; **no IDs imported**): [Dora B058 1926 papers](https://cursor.com/agents/bc-ff41393b-080c-52e0-b023-f345305c8e21) now IDLE; [Read MO Edward/Francis sheets](https://cursor.com/agents/bc-202ca84f-38a2-546d-bc31-0a71cbd5c3fa) now IDLE; [Read MO Michael/Patrick sheets](https://cursor.com/agents/bc-090ec6e6-1ac5-5bd2-be32-3092d7a6370e) RUNNING; [Dora B071 1850 Tincher](https://cursor.com/agents/bc-56af7e0b-6086-5aa3-9345-a9662f10bc21) RUNNING (closeout re-list vs 138). Nested reviewer **not** respawned. Message queue empty. Still RUNNING: [Dora location search](https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03) PR **#31**; [Scan ED5 pages 405-434](https://cursor.com/agents/bc-0039b8bf-7edb-593b-82c3-cb59471d392a); [Read MO Michael/Patrick sheets](https://cursor.com/agents/bc-090ec6e6-1ac5-5bd2-be32-3092d7a6370e); [Dora B071 1850 Tincher](https://cursor.com/agents/bc-56af7e0b-6086-5aa3-9345-a9662f10bc21). [Dora's biography research](https://cursor.com/agents/bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK** PR **#33** (sibling C281 **not imported**). This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: G-416 Louis window **2054–2072** **nil** Lewis/Louis 67 Owsley; **2059** Loue I 69 Cumberland and **2060** Louis H 19 Jefferson **DISPROVED**; original Lewis is a Soundex miss (**C880 / DOC163**); Soundex **2063** Loyd A-2; original leaf **1159** sh **2 B** dw **48 Colwell, William** + **Gilbert, Loyd** Step son **10** ln **39** (Hard Rule 6 of clerk 16 / ln 59) and **Douglas** 7 ln **42** (**C881/C882 / DOC164**); 1920 DC **GILBERT, John** 85 **PROBABLE** C765/C756 (**C883 / DOC165**); 1913 John Robert **DISPROVED** (**C884**); 1917 Tildy **POSSIBLE unmerged** (**C885**); Josephine remaining-county **nil**/n/a (**C887 / DOC166**); Baker Hubert dau **Dora** 21 **DISPROVED as P001** (**C888**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. Do **not** hunt D-540 to prove **C833**. Do **not** close B063. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C879 / L765 / S634**. Next unused **C891+ / L773+ / S639+ / DOC167+**.

# Pass 83 listing (31 Oct 2026, America/New_York)

`list-cloud-agents` (includeArchived, limit 200) → **141** / `hasMore: false` / `totalMatched: 141`. Was **139**. NEW vs 139 (2; **no IDs imported**): [Read IN Michael/Patrick sheets](https://cursor.com/agents/bc-c74206b6-0485-506e-9463-ba2b4a0badbb) RUNNING; [Read IN Edward/Francis/George sheets](https://cursor.com/agents/bc-858b6ee9-7f69-507a-8ce3-b70e641fff6b) RUNNING. [Read MO Michael/Patrick sheets](https://cursor.com/agents/bc-090ec6e6-1ac5-5bd2-be32-3092d7a6370e) now IDLE. Nested reviewer **not** respawned. Message queue empty. Still RUNNING: [Dora location search](https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03) PR **#31**; [Scan ED5 pages 405-434](https://cursor.com/agents/bc-0039b8bf-7edb-593b-82c3-cb59471d392a); [Dora B071 1850 Tincher](https://cursor.com/agents/bc-56af7e0b-6086-5aa3-9345-a9662f10bc21); [Read IN Michael/Patrick sheets](https://cursor.com/agents/bc-c74206b6-0485-506e-9463-ba2b4a0badbb); [Read IN Edward/Francis/George sheets](https://cursor.com/agents/bc-858b6ee9-7f69-507a-8ce3-b70e641fff6b). [Dora's biography research](https://cursor.com/agents/bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK** PR **#33** (sibling C281 **not imported**). This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: G-416 Lewis denser **2038–2053** **nil** Lewis 67 Owsley as a head; **2043** Lewis 55 Harlan A-2 and **2052** Lewis H 53 Jefferson **DISPROVED**; Lewis/Louis/Loyd given-name block **image-closed**; original Lewis is a Soundex miss (**C892–C895 / DOC167**); Johnson 1900–03 **nil**/other Josies (**C896 / DOC168**); Magoffin/Laurel/Whitley/Pulaski/Clay **404** (**C897**); Cecil cemetery HTML **404** (**C898**); IA T288 / 1916 DC **numFound 0**; Chronicling **404**; TFKRHA SSL/429 (**C899**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. Do **not** hunt D-540 to prove **C833**. Do **not** close B063. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C891 / L773 / S639**. Next unused **C902+ / L782+ / S644+ / DOC169+**.

# Pass 84 listing (31 Oct 2026, America/New_York)

`list-cloud-agents` (includeArchived, limit 200) → **141** / `hasMore: false` / `totalMatched: 141`. Unchanged vs Pass 83. Status-only (no new chats; **no IDs imported**): [Read IN Michael/Patrick sheets](https://cursor.com/agents/bc-c74206b6-0485-506e-9463-ba2b4a0badbb) now IDLE; [Read IN Edward/Francis/George sheets](https://cursor.com/agents/bc-858b6ee9-7f69-507a-8ce3-b70e641fff6b) now IDLE. Nested reviewer **not** respawned. Message queue empty. Still RUNNING: [Dora location search](https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03) PR **#31**; [Scan ED5 pages 405-434](https://cursor.com/agents/bc-0039b8bf-7edb-593b-82c3-cb59471d392a); [Dora B071 1850 Tincher](https://cursor.com/agents/bc-56af7e0b-6086-5aa3-9345-a9662f10bc21). [Dora's biography research](https://cursor.com/agents/bc-aea168dd-1a56-45e2-aaf6-7a6753ba5b6a) **WAITING_FOR_BACKGROUND_WORK** PR **#33** (sibling C281 **not imported**). This run `bc-01a18bb4-e162-785c-9724-86a7c5663bf1`. **No** new independently image-backed P001 1900–1926 residence. Work this pass: D-500 **5090** Dean, George 43 Owsley ED **92** sh **6** ln **93** × Martha = original dw **107** (**C903/C904 / DOC169–170**), **PROBABLE** 1910 dw **29**, **not** missing sh 1; C824 George × Jane stands; **5100** / **4760 DISPROVED**; Daniel/Maggie windows **nil** matching 1910 identities (**C905**); B-260 James **4982/4984/4986 DISPROVED**; **5025** Jerry is original Baker granddaughter (**C906 / DOC171**); G-163 **3198** Elisha 20 Jackson **DISPROVED**; **3199** Elisha 40 is original **Gilbert, Chester** (**C907 / DOC172**); B-630 Barrett Ben sampled-nil, residual **2326–2424** (**C908**); Josephine remaining **nil**/other (**C909 / DOC173**); obits Luther-only; IA T288/M123 **numFound 0**; Rogers **401** (**C910**). Original 1932 DC, 1916 DC face, 1840 bond, and M123-**3** **still unseen**. Do **not** promote **C509**. Do **not** hunt D-540 to prove **C833**. Do **not** close B063. **B061 / B063 remain open**. Skip **C221–C280 / L245–L342 / S259–S266**. This listing uses **C902 / L782 / S644**. Next unused **C913+ / L793+ / S653+ / DOC174+**.

