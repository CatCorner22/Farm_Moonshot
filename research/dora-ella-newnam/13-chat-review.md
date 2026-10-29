# 13 — Chat review: sources of the master biography

Reviewed 28 October 2026 (America/New_York) from Cursor cloud-agent transcripts on repository `CatCorner22/Farm_Moonshot`. Sixteen chats were listed in that environment. **Supplement 29 October 2026 (UTC):** twenty-six accessible cloud agents on the same repo (transcripts fetched with `cursor-cloud-batch-fetch-details`, `includeTranscripts: true`). Findings are folded into `06-dossier.md` and `book/Dora-Ella-Newnam-Stone-A-Life.md`. Living testers and DNA/health files were not used.

## Primary research chats (biography content)

| Chat | URL | What it contributed |
|---|---|---|
| **Dora** (mobile, opened the case) | https://cursor.com/agents/bc-01a17a5a-f7be-70f0-8063-d9a0707aebd1 | Research question; user-supplied Arkansas death certificate (Dora Stone, noon 23 Aug 1926, Ola, cert. 1524, informant Coy, spouse T. A. Stone, parents E. T. Newnam & Mary Smallwood, burial Carters Chapel, residence “Mammoth, Ark.”, apoplexy); studio portrait (family ID only); WikiTree Newnam-49; 1885 marriage lead; 1900 Sturgeon household; McCoy × Sullivan 1917 Ola; Pearl/Mary NUMIDENT; Carter Cove “Newman, Dora” / “Stone, Thomas 1845–1925”; 1920 Tom A. Stone of Perry Co.; no DNA. |
| **Ancestry research skill** | https://cursor.com/agents/bc-2ffa148f-bd17-4e95-beef-aa2f31940c4a | Authored the genealogy-detective skill. **No additional Dora biography facts.** |
| **Dora’s early 1900s** | https://cursor.com/agents/bc-a16def3b-c4be-41e9-846c-f31bc0f8dd81 | 1910 hole; KY/AR/MO/OK/TX/TN Soundex negatives; original Sturgeon ED 99 (not still on the creek as Newnam); enumerator-name conflict; source JPEGs; 1880 Dora 8. |
| **Dora research continuation** | https://cursor.com/agents/bc-0bd3b0b2-ec76-4a5c-93c7-10c0bfe1f312 | 1920 Beattyville original (E.T. in C.B. Burke’s house); Peebles hypothesis tested and not supported; 1900 MO Stone originals; image gallery; merge of parallel PRs; master book. |
| **Dora biography research** (pass 18–22) | https://cursor.com/agents/bc-01a183ca-4028-7f9b-9d4c-34d4ab6671f6 | FAG Carter **S117–S118**; pass 21–22 Louisa/Larkin Mays (**C130–C133**); Rissie Lee books nil (**C134**); Word `.docx` kept current. |
| **Dora master biography** | https://cursor.com/agents/bc-01a18285-696d-761f-be7a-74d897313200 | HTML book `book/index.html`; 1900 Sturgeon original plates; Greene **Thomas A. Stone** sh 18A (**C117**); PR #13–#15 narrative — **no new residence for P001** beyond case file. |
| **Dora Word book + git sync** | https://cursor.com/agents/bc-3b441f4a-2cce-5eb2-bfc4-5a210a6ac0ce | `.docx` / git hygiene (parallel to book agents). **No location fieldwork.** |
| **Dora location search** (orchestrator) | https://cursor.com/agents/bc-995d22ea-9633-4d0d-a5ef-c36b6ff78d03 | User goal: locations **1900 → death**; spawned web-search workers; **no new record-backed residence** in transcript (delegation only). |
| **Dora 1900–1912 location web search** | https://cursor.com/agents/bc-e3326e8c-597f-53c8-b831-fd8cc5dec482 | Sub-agent of location pass; transcript **empty** at fetch (still RUNNING). |
| **Dora 1913–1926 location web search** | https://cursor.com/agents/bc-359a99fe-a390-5c02-a0a4-986d794942fa | Sub-agent of location pass; transcript **empty** at fetch (still RUNNING). |
| **Review Farm_Moonshot project chats** | https://cursor.com/agents/bc-281c57f3-937a-5920-aa1c-3d8221b38f54 | This inventory pass (**L161**). |


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
| Jan 1920 | E.T. Newman in **Beattyville** (C.B. Burke hh) — grandfather, not Dora (**PROBABLE**) | bc-0bd3b0b2 | Yes |
| Jan 1920 | Tom A. Stone **Howell Twp, Perry Co., AR** (**PROBABLE** m2 husband) | bc-01a17a5a | Yes |
| Jan 1920 | **1920 town of Ola**, Yell Co. = ED **200**, NARA **T625-86** — no free IA/transcript; Dora Stone **not** in published extracts (**chat lead → B046**) | bc-01a17a5a only | **Not** in `.md` book yet |
| 1920–1925 | m2 Stone; Yell/Perry license unread (**PROBABLE**) | bc-01a17a5a | Yes |
| 23–24 Aug 1926 | Death **Ola**; res. field “Mammoth, Ark.” (**S003**); burial **Carters Chapel** / Carter Cove (**PROBABLE**) | bc-01a17a5a (user DC image) | Yes |

**Chat-only FAN (not P001 residence):** Carters Chapel name absent from Yell’s published ~167-cemetery list; FAG town cemeteries at Ola = Hale, Oakland, Wilson — Dora Stone not indexed there (original chat canvas narrative; aligns with **B020**).

## Workspace paths searched (29 Oct 2026)

- `/workspace/README.md` (Farm_Moonshot)
- `/workspace/.cursor/skills/genealogy-detective/` (skill only; no chat exports)
- `/workspace/research/dora-ella-newnam/` (case file; prior **`13-chat-review.md`**, **`02-log.md` L090**)
- No local `transcript.json` or chat export files in-repo; all chat text via **cursor-cloud** MCP (`/tmp/cursor/cloud-agent-transcripts/2026-10-29T14-49-01Z-98fc`, `…14-50-00Z-483d`)

## Instruction for the next chat

Treat `book/Dora-Ella-Newnam-Stone-A-Life.md` and `06-dossier.md` as the combined master. Rebuild the PDF with `python3 scripts/build_dora_book.py` after narrative edits. Do not reopen Peebles as a third marriage without a license. Do not print 1868 or 24 February 1906 as facts. Redact living people. Ancestry remains 403 from this VM — ask the user for a local pull of the 1925 Stone certificate and the 1885 marriage image.
