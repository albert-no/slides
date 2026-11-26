# 261202YonseifutureAI/ — Trustworthy AI talk for senior leaders (2026-12-02)

One English deck, 45 minutes (43:00 of speech + 2:00 reserve), CEO-level general audience.
**Concept-first** (DESIGN_SYSTEM §5): case → intuition → qualified claim; no math, no code,
no tech supplement. Built from the trustworthy-ai course (lec01 spine; lec02–14 for cases
and distinctions). Thread: Albert's own weekly-manual workflow (email reader → approval →
coding agent → private manual) opens the talk, returns in §03 as the injection case, and
closes it with five delegation questions.

| Deck | Slides | Companion |
|---|---|---|
| `261202YonseifutureAI.html` | 46 | `261202YonseifutureAI-note.html` (English speaker notes, 46 articles, pacing table) |

Built by pipeline job `2026-11-26-261202YonseifutureAI-overview` (plan-v2). Slide IDs are
`data-slide-id` on each slide div and note article; display order = ID order (S01–S46,
no splits, no retirements).

Shared visual kit `.fa-*` (top of the deck `<style>`): role colours used on every flow
diagram — `.fa-user` blue (me), `.fa-out` red dashed (outside text), `.fa-agent` gray (AI
system), `.fa-check` green (human approval), `.fa-act` charcoal (consequential action),
`.fa-rec` amber dashed (recommended check); tags `.fa-tag-case` / `-demo` / `-ill`.

## Sections

| # | Section | Slides | IDs | Lines | Time |
|---|---|---|---|---|---|
| — | Title, weekly-manual opening, contents | 1–10 | S01–S10 | `:376-617` | 8:00 |
| 01 | More Capable, More Consequential | 11–14 | S11–S14 | `:622-697` | 4:00 |
| 02 | When Useful AI Goes Wrong | 15–28 | S15–S28 | `:703-1012` | 15:00 |
| 03 | Who Can Steer Your AI? | 29–37 | S29–S37 | `:1018-1221` | 9:00 |
| 04 | What Leaders Should Ask | 38–46 | S38–S46 | `:1227-1409` | 7:00 |

## Slide pointers

- `:390` S02–`:568` S09 opening: paperwork → email-to-manual → weekly update → agents read and act → injected email (S06) → access ≠ authority → read/approve/build (S08, green approval) → the talk question.
- `:634` S12–`:681` S14: answers → actions; same error, different stakes; capability ≠ assurance.
- `:715` S16 Mata v. Avianca (fabricated citations); `:737` S17 Moffatt v. Air Canada chatbot; `:778` S19 GPT-4o "too agreeable" update and rollback (OpenAI posts, 2025); `:797` S20 invented closed-tickets example (motivated by Krakovna et al. 2020, specification gaming).
- `:843` S22 Carlini et al. training-data extraction (`figs/p5-carlini-fig1.png`, USENIX Security 2021 Fig. 1, recaptured p. 2 at 200 dpi); `:864` S23 deletion meanings; `:888` S24 Obermeyer cost-as-proxy; `:912` S25 “One System, Very Unequal Errors”: Gender Shades IBM error bars (inline HTML chart redrawn from Buolamwini & Gebru 2018 Table 4: 34.7 / 12.0 / 7.1 / 0.3 %, 15 px per point, axis 0–40 %; inputs recorded in an HTML comment on the slide); `:936` S26 Hong Kong deepfake video-meeting fraud (HK Government LCQ9, 2024); `:970` S27 provenance ≠ truth (C2PA explainer).
- `:1030` S30 Eykholt stop sign (`figs/p3-eykholt-fig1.png`, arXiv 1707.08945 Fig. 1); `:1048` S31 attacks at training time (tampered examples) vs use time (instructions in documents); `:1082` S32 requests vs retrieved instructions; `:1108` S33 public issue → private repositories (2025 research demonstration); `:1134` S34–`:1205` S37 the weekly manual as an injection case and its controls.
- `:1239` S39–`:1338` S43 leader checklist: bounded job, test the workflow, detect/stop/recover, safety score in context, named human owner; `:1359` S44 weekly manual revisited; `:1388` S45 five questions (Task · Information · Authority · Checks · Owner).

## Cross-deck links

Course sources: `courses/trustworthy-ai/lec01-introduction.html` (spine, trust dimensions),
lec02–lec14 for the cases. The Eykholt figure is a byte-identical copy of
`courses/trustworthy-ai/figs/eykholt-fig1-stopsign.png`.
