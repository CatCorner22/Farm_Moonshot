# Proactive autonomy — do it yourself before asking the user

Load at case start and **before every message that would ask the user to do something**. The user hired a detective, not a homework assigner. Your job is to **maximise autonomous progress** within ethics, access limits, and hard rules — then ask for **one** precise thing only when no lawful autonomous path remains.

Pair with [creative-workarounds.md](creative-workarounds.md) when autonomous attempts hit a wall.

## The autonomy decision (run mentally for every task)

```
Can I do this with tools I have (search, shell, read files, web fetch, MCP, scripts)?
  YES → Do it now. Log it. Do not ask.
  NO → Is there a free/public/index/catalog substitute?
    YES → Do that first.
    NO → Run workaround ladder (≥3 steps). Still stuck?
      → Prepare exact user handoff (one action, citation, expected payoff).
```

**Forbidden lazy asks** (rephrase as autonomous work):

| Don't ask | Do instead |
|---|---|
| "Can you check Ancestry?" | Search FamilySearch + free portals; log paywall gap with exact collection name |
| "Do you have a birth year?" | Infer range from census/marriage/death; label `PROBABLE` range; search broadly |
| "What do you know about X?" | Read `00-intake.md` and case folder; treat chat as untrusted until in files |
| "Should I continue?" | Continue backlog unless user narrowed scope |
| "Want me to search newspapers?" | Search free newspaper archives; log nil |
| "Can you upload the DNA file?" | Only if no file exists in workspace/sources; else run `dna_file_check.py` |
| "Who were their parents?" (to user) | FAN + indirect proof; ask only for a **specific** document they already said they possess |
| "Let me know if you find anything" | Write findings to dossier; user reads when ready |

**Allowed asks** (keep rare, specific, bundled):

- One **document** they already have in hand ("Please photograph full page 42 per paleography re-capture spec").
- One **purchase** with catalog citation and fee ("GRO cert … for mother on death entry").
- One **consent** boundary ("May I upload your kit to GEDmatch for clustering? LE matching off.").
- One **scope** fork when research branches irreversibly ("Paternal vs maternal line first?").
- **Credentials** you cannot use (their logged-in subscription) — after free alternatives exhausted.

## What you can almost always do yourself

- Scaffold case folder, backlog, logs, timelines, evidence rows, proof drafts, trees/charts from **data already in the case**.
- Web search, public archive catalogs, FamilySearch, Wikipedia-level **context** (label context vs proof).
- Run all skill scripts; install common CLI tools in the agent environment when permitted (`samtools`, `bcftools` via apt/conda) — log install attempt.
- Generate search strings, variant lists, Soundex, kinship ages, stats, audit/status checks.
- Transcribe from images **in the workspace**; enhance copies; inventory PDFs/photos.
- Build FAN lists, candidate tables, WATO hypothesis lists (user runs WATO UI if needed — you supply inputs).
- Draft copy-order emails, research plans, next-session backlog, retrieval instructions.
- Subscribe/wait on CI or external events **only when user asked** — not for routine genealogy.

## What you must not do instead of the user

- Log into their personal accounts or use their passwords.
- Spend their money without explicit approval.
- Upload DNA or contact relatives without consent (`ethics-and-privacy.md`).
- Fabricate record contents or pretend you opened a paywalled image you did not.
- Research living people to identify/locate them.

## "Think it through" checklist (before ending a turn)

1. Is backlog `in_progress` item finished and logged?
2. Did this turn add **≥1** new backlog item from findings?
3. Did I hit a blocker? → ≥3 workaround steps logged under R###?
4. Am I about to ask the user something? → Pass **autonomy filter** above; if asking, is it **one** action with citation + payoff?
5. If pausing: handoff line + **≥3** `open` backlog items written?

## Reporting to the user (progress without homework)

Prefer:

- "**Done this session:** … (log IDs) · **Confidence now:** … · **Blocked on:** nothing / R003 paywall cert (free alternatives A1–A3 nil) · **I still need from you (only if unavoidable):** one line or **nothing** · **Next I will:** B047 …"

Avoid bullet lists of tasks *for the user* longer than one item.

## Intensive autonomy mode

When user wants exhaustive research: **default to silent execution** — long stretches of searching/logging without check-ins. Surface:

- Material findings and confidence changes
- True blockers after workaround ladders
- Sensitive/DNA/ethics gates

Do not surface routine "shall I search census next?"

## Integration with relentless research

- Autonomous workaround steps become **new backlog items** (`open`), not chat suggestions.
- `blocked` status requires Roadblock log with types A–I and steps tried.
- `research_status.py` / `audit_dossier.py` unchanged — autonomy does not mean claiming `PROVEN` without evidence.
