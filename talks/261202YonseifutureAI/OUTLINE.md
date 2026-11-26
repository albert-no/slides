# 261202YonseifutureAI/ — Trustworthy AI talk for senior leaders (2026-12-02)

One English deck, 45 minutes (43:00 of speech + 2:00 reserve), CEO-level general audience.
**Concept-first** (DESIGN_SYSTEM §5): case → intuition → qualified claim; no math, no code,
no tech supplement. Built from the trustworthy-ai course (lec01 spine; lec02–14 for cases
and distinctions). Thread: Albert's own weekly-manual workflow (email reader → approval →
coding agent → private manual) opens the talk, returns in §03 as the injection case, and
closes it with five delegation questions.

| Deck | Slides | Companion |
|---|---|---|
| `261202YonseifutureAI.html` | 45 | `261202YonseifutureAI-note.html` (English speaker notes, 45 articles, pacing table) |

Built by pipeline job `2026-11-26-261202YonseifutureAI-overview` (plan-v2; revised by plan-v3). Slide IDs are
`data-slide-id` on each slide div and note article; display order = ID order (S01–S46,
no splits; S27 retired in plan-v3, its ID not reused).

Shared visual kit `.fa-*` (top of the deck `<style>`): role colours used on every flow
diagram — `.fa-user` blue (me), `.fa-out` red dashed (outside text), `.fa-agent` gray (AI
system), `.fa-check` green (human approval), `.fa-act` charcoal (consequential action),
`.fa-rec` amber dashed (recommended check); tags `.fa-tag-case` / `-demo` / `-ill`.

## Sections

| # | Section | Slides | IDs | Lines | Time |
|---|---|---|---|---|---|
| — | Title, weekly-manual opening, contents | 1–10 | S01–S10 | `:367-608` | 8:00 |
| 01 | More Capable, More Consequential | 11–14 | S11–S14 | `:613-688` | 4:00 |
| 02 | When Useful AI Goes Wrong | 15–27 | S15–S26, S28 | `:694-977` | 14:40 |
| 03 | Who Can Steer Your AI? | 28–36 | S29–S37 | `:983-1187` | 9:20 |
| 04 | What Leaders Should Ask | 37–45 | S38–S46 | `:1193-1375` | 7:00 |

## Slide pointers

- `:381` S02–`:559` S09 opening: paperwork → email-to-manual → weekly update → agents read and act → injected email (S06) → access ≠ authority → read/approve/build (S08, green approval) → the talk question.
- `:625` S12–`:672` S14: answers → actions; same error, different stakes; capability ≠ assurance.
- `:706` S16 Mata v. Avianca (fabricated citations); `:728` S17 Moffatt v. Air Canada chatbot; `:769` S19 GPT-4o "too agreeable" update and rollback (OpenAI posts, 2025); `:788` S20 invented AI support agent closes a refund request: score up, refund still missing (motivated by Krakovna et al. 2020, specification gaming); S21 two privacy risks: what you share now vs what a model learned in training.
- `:836` S22 Carlini et al. training-data extraction (`figs/p5-carlini-fig1.png`, USENIX Security 2021 Fig. 1, recaptured p. 2 at 200 dpi); `:857` S23 deletion meanings; `:881` S24 Obermeyer cost-as-proxy; `:905` S25 “One System, Very Unequal Errors”: Gender Shades IBM error bars (inline HTML chart redrawn from Buolamwini & Gebru 2018 Table 4: 34.7 / 12.0 / 7.1 / 0.3 %, 15 px per point, axis 0–40 %; inputs recorded in an HTML comment on the slide); `:929` S26 Hong Kong deepfake video-meeting fraud (HK Government LCQ9, 2024).
- `:995` S30 Eykholt stop sign (`figs/p3-eykholt-fig1.png`, arXiv 1707.08945 Fig. 1); `:1013` S31 attacks at training time (tampered examples) vs use time (instructions in documents); `:1047` S32 requests vs retrieved instructions; `:1073` S33 Reddit comment → Comet AI browser → private email login code → public Reddit reply (Brave, 2025 research demonstration); `:1100` S34–`:1171` S37 the weekly manual as an injection case and its controls.
- `:1205` S39–`:1304` S43 leader checklist: bounded job, test the workflow, detect/stop/recover, safety score in context, named human owner; `:1325` S44 weekly manual revisited; `:1354` S45 five questions (Task · Information · Authority · Checks · Owner).

## Cross-deck links

Course sources: `courses/trustworthy-ai/lec01-introduction.html` (spine, trust dimensions),
lec02–lec14 for the cases. The Eykholt figure is a byte-identical copy of
`courses/trustworthy-ai/figs/eykholt-fig1-stopsign.png`.
