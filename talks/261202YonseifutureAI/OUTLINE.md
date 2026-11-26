# 261202YonseifutureAI/ — Trustworthy AI talk for senior leaders (2026-12-02)

One deck in two language versions, English and Korean (same 45 slides, same IDs, same timing), 45 minutes (43:00 of speech + 2:00 reserve), CEO-level general audience.
**Concept-first** (DESIGN_SYSTEM §5): case → intuition → qualified claim; no math, no code,
no tech supplement. Built from the trustworthy-ai course (lec01 spine; lec02–14 for cases
and distinctions). Thread: Albert's own weekly-manual workflow (email reader → approval →
coding agent → private manual) opens the talk, returns in §03 as the injection case, and
closes it with five delegation questions.

| Deck | Slides | Companion |
|---|---|---|
| `261202YonseifutureAI.html` | 45 | `261202YonseifutureAI-note.html` (English speaker notes, 45 articles, pacing table) |
| `261202YonseifutureAI-ko.html` | 45 | `261202YonseifutureAI-ko-note.html` (Korean speaker notes, 45 articles, pacing table) |

Built by pipeline job `2026-11-26-261202YonseifutureAI-overview` (plan-v2; revised by plan-v3). Slide IDs are
`data-slide-id` on each slide div and note article; display order = ID order (S01–S46,
no splits; S27 retired in plan-v3, its ID not reused).
Korean version built by pipeline job `2026-11-26-261202YonseifutureAI-korean` (plan-v1): a
translation of the English pair, same layout, figures (`figs/`) and IDs; page N in one
language is page N in the other. `lang="ko"`, `.deck { word-break: keep-all; }`, brand footer
`data-brand-text="연세대학교"`. Agent / Private / Public and terms awkward in Korean stay
English (requests C03, C04); citations stay in English.

Shared visual kit `.fa-*` (top of the deck `<style>`): role colours used on every flow
diagram — `.fa-user` blue (me), `.fa-out` red dashed (outside text), `.fa-agent` gray (AI
system), `.fa-check` green (human approval), `.fa-act` charcoal (consequential action),
`.fa-rec` amber dashed (recommended check); tags `.fa-tag-case` / `-demo` / `-ill`.

## Sections

| # | Section (EN · KO) | Slides | IDs | Lines (EN · KO) | Time |
|---|---|---|---|---|---|
| — | Title, weekly-manual opening, contents · 제목, 주간 매뉴얼 도입, 오늘의 이야기 | 1–10 | S01–S10 | `261202YonseifutureAI.html:367-608` · `261202YonseifutureAI-ko.html:369-610` | 8:00 |
| 01 | More Capable, More Consequential · 커진 능력, 커진 영향 | 11–14 | S11–S14 | `261202YonseifutureAI.html:613-688` · `261202YonseifutureAI-ko.html:615-690` | 4:00 |
| 02 | When Useful AI Goes Wrong · 유용한 AI도 실패한다 | 15–27 | S15–S26, S28 | `261202YonseifutureAI.html:694-977` · `261202YonseifutureAI-ko.html:696-979` | 14:40 |
| 03 | Who Can Steer Your AI? · 누가 내 AI를 움직이나? | 28–36 | S29–S37 | `261202YonseifutureAI.html:983-1187` · `261202YonseifutureAI-ko.html:985-1189` | 9:20 |
| 04 | What Leaders Should Ask · 리더가 물어야 할 질문 | 37–45 | S38–S46 | `261202YonseifutureAI.html:1193-1375` · `261202YonseifutureAI-ko.html:1195-1377` | 7:00 |

## Slide pointers

English version:

- `261202YonseifutureAI.html:381` S02–`261202YonseifutureAI.html:559` S09 opening: paperwork → email-to-manual → weekly update → agents read and act → injected email (S06) → access ≠ authority → read/approve/build (S08, green approval) → the talk question.
- `261202YonseifutureAI.html:625` S12–`261202YonseifutureAI.html:672` S14: answers → actions; same error, different stakes; capability ≠ assurance.
- `261202YonseifutureAI.html:706` S16 Mata v. Avianca (fabricated citations); `261202YonseifutureAI.html:728` S17 Moffatt v. Air Canada chatbot; `261202YonseifutureAI.html:769` S19 GPT-4o "too agreeable" update and rollback (OpenAI posts, 2025); `261202YonseifutureAI.html:788` S20 invented AI support agent closes a refund request: score up, refund still missing (motivated by Krakovna et al. 2020, specification gaming); S21 two privacy risks: what you share now vs what a model learned in training.
- `261202YonseifutureAI.html:836` S22 Carlini et al. training-data extraction (`figs/p5-carlini-fig1.png`, USENIX Security 2021 Fig. 1, recaptured p. 2 at 200 dpi); `261202YonseifutureAI.html:857` S23 deletion meanings; `261202YonseifutureAI.html:881` S24 Obermeyer cost-as-proxy; `261202YonseifutureAI.html:905` S25 “One System, Very Unequal Errors”: Gender Shades IBM error bars (inline HTML chart redrawn from Buolamwini & Gebru 2018 Table 4: 34.7 / 12.0 / 7.1 / 0.3 %, 15 px per point, axis 0–40 %; inputs recorded in an HTML comment on the slide); `261202YonseifutureAI.html:929` S26 Hong Kong deepfake video-meeting fraud (HK Government LCQ9, 2024).
- `261202YonseifutureAI.html:995` S30 Eykholt stop sign (`figs/p3-eykholt-fig1.png`, arXiv 1707.08945 Fig. 1); `261202YonseifutureAI.html:1013` S31 attacks at training time (tampered examples) vs use time (instructions in documents); `261202YonseifutureAI.html:1047` S32 requests vs retrieved instructions; `261202YonseifutureAI.html:1073` S33 Reddit comment → Comet AI browser → private email login code → public Reddit reply (Brave, 2025 research demonstration); `261202YonseifutureAI.html:1100` S34–`261202YonseifutureAI.html:1171` S37 the weekly manual as an injection case and its controls.
- `261202YonseifutureAI.html:1205` S39–`261202YonseifutureAI.html:1304` S43 leader checklist: bounded job, test the workflow, detect/stop/recover, safety score in context, named human owner; `261202YonseifutureAI.html:1325` S44 weekly manual revisited; `261202YonseifutureAI.html:1354` S45 five questions (Task · Information · Authority · Checks · Owner).

Korean version — same slides, every line +2 (two `<style>` lines added):

| ID | Korean title | Pointer |
|---|---|---|
| S02 | 학기마다 반복되는 행정 업무 | `261202YonseifutureAI-ko.html:383` |
| S09 | AI에게 어디까지 허용할까? | `261202YonseifutureAI-ko.html:561` |
| S12 | 답변에서 실행으로 | `261202YonseifutureAI-ko.html:627` |
| S14 | 능력만으로 안심할 수는 없다 | `261202YonseifutureAI-ko.html:674` |
| S16 | 그럴듯한 인용, 없는 판례 | `261202YonseifutureAI-ko.html:708` |
| S17 | 챗봇의 답이 회사의 약속으로 | `261202YonseifutureAI-ko.html:730` |
| S19 | 맞장구가 늘 도움은 아니다 | `261202YonseifutureAI-ko.html:771` |
| S20 | 문의는 종료, 문제는 그대로 | `261202YonseifutureAI-ko.html:790` |
| S21 | Privacy 위험은 두 가지 | `261202YonseifutureAI-ko.html:812` |
| S22 | 모델이 개인정보를 그대로 내놓았다 | `261202YonseifutureAI-ko.html:838` |
| S23 | 파일 삭제 ≠ 학습 내용 제거 | `261202YonseifutureAI-ko.html:859` |
| S24 | 의료비와 치료 필요는 다르다 | `261202YonseifutureAI-ko.html:883` |
| S25 | 같은 시스템, 크게 다른 오류율 | `261202YonseifutureAI-ko.html:907` |
| S26 | 익숙한 얼굴 ≠ 본인 확인 | `261202YonseifutureAI-ko.html:931` |
| S30 | STOP 표지판을 잘못 읽은 분류기 | `261202YonseifutureAI-ko.html:997` |
| S31 | 공격의 입구: 학습과 사용 | `261202YonseifutureAI-ko.html:1015` |
| S32 | 내 요청인가, 남이 심은 지시인가? | `261202YonseifutureAI-ko.html:1049` |
| S33 | Reddit 요약하다 login code가 유출됐다 | `261202YonseifutureAI-ko.html:1075` |
| S34 | 누가 쓰고, 무엇을 바꾸나? | `261202YonseifutureAI-ko.html:1102` |
| S37 | 권한 제한은 모델 밖에서 | `261202YonseifutureAI-ko.html:1173` |
| S39 | 할 일부터 정하고, 권한은 최소로 | `261202YonseifutureAI-ko.html:1207` |
| S43 | 책임질 사람을 정하라 | `261202YonseifutureAI-ko.html:1306` |
| S44 | 다시, 나의 주간 매뉴얼 | `261202YonseifutureAI-ko.html:1327` |
| S45 | 맡기기 전, 다섯 가지 질문 | `261202YonseifutureAI-ko.html:1356` |

## Cross-deck links

Course sources: `courses/trustworthy-ai/lec01-introduction.html` (spine, trust dimensions),
lec02–lec14 for the cases. The Eykholt figure is a byte-identical copy of
`courses/trustworthy-ai/figs/eykholt-fig1-stopsign.png`.
