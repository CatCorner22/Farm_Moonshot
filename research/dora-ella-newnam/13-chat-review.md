# 13 — Chat review: sources of the master biography

Reviewed 28 October 2026 (America/New_York) from Cursor cloud-agent transcripts on repository `CatCorner22/Farm_Moonshot`. Sixteen chats were listed in this environment. Their findings are folded into `06-dossier.md` and `book/Dora-Ella-Newnam-Stone-A-Life.md`. Living testers and DNA/health files were not used.

## Primary research chats (biography content)

| Chat | URL | What it contributed |
|---|---|---|
| **Dora** (mobile, opened the case) | https://cursor.com/agents/bc-01a17a5a-f7be-70f0-8063-d9a0707aebd1 | Research question; user-supplied Arkansas death certificate (Dora Stone, noon 23 Aug 1926, Ola, cert. 1524, informant Coy, spouse T. A. Stone, parents E. T. Newnam & Mary Smallwood, burial Carters Chapel, residence “Mammoth, Ark.”, apoplexy); studio portrait (family ID only); WikiTree Newnam-49; 1885 marriage lead; 1900 Sturgeon household; McCoy × Sullivan 1917 Ola; Pearl/Mary NUMIDENT; Carter Cove “Newman, Dora” / “Stone, Thomas 1845–1925”; 1920 Tom A. Stone of Perry Co.; no DNA. |
| **Ancestry research skill** | https://cursor.com/agents/bc-2ffa148f-bd17-4e95-beef-aa2f31940c4a | Authored the genealogy-detective skill. **No additional Dora biography facts.** |
| **Dora’s early 1900s** | https://cursor.com/agents/bc-a16def3b-c4be-41e9-846c-f31bc0f8dd81 | 1910 hole; KY/AR/MO/OK/TX/TN Soundex negatives; original Sturgeon ED 99 (not still on the creek as Newnam); enumerator-name conflict; source JPEGs; 1880 Dora 8. |
| **Dora research continuation** (this chat) | https://cursor.com/agents/bc-0bd3b0b2-ec76-4a5c-93c7-10c0bfe1f312 | 1920 Beattyville original (E.T. in C.B. Burke’s house); Peebles hypothesis tested and not supported; 1900 MO Stone originals; image gallery; merge of parallel PRs; this master book. |

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

## Instruction for the next chat

Treat `book/Dora-Ella-Newnam-Stone-A-Life.md` and `06-dossier.md` as the combined master. Rebuild the PDF with `python3 scripts/build_dora_book.py` after narrative edits. Do not reopen Peebles as a third marriage without a license. Do not print 1868 or 24 February 1906 as facts. Redact living people. Ancestry remains 403 from this VM — ask the user for a local pull of the 1925 Stone certificate and the 1885 marriage image.
