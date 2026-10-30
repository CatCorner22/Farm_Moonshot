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
