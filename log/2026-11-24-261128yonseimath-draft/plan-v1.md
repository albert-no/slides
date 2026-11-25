# Plan v1 — approval proposal, stages 1–3

**Job:** 2026-11-24-261128yonseimath-draft  
**Baseline:** 95df062f8f980c686f0ef45974ebd3f626ff79d2  
**Target:** `talks/261128yonseimath/` (new)  
**Status:** awaiting Albert. This is not a work order. Stage 4's full per-slide specs, file ownership and packages will be plan-v2 after approval.

## 1. Audience, objective, exclusions, cutoff

**Proposed title:** AI가 수학 문제를 푸는 시대, 무엇이 진짜 실력일까?

Korean, concept-first, celebratory alumni talk. Speaker is a fellow program graduate and now a Yonsei professor. Make the ideas accessible to a mathematically curious middle-school pupil; do not require university probability, softmax, neural-network internals or prior LLM knowledge. The supplied brief says high school, but the institution's Article 4 indicates a primarily middle-school program (E11). Exact ceremony attendance remains unconfirmed; do not describe it as exclusively middle-school or high-school.

**Objectives:** listeners can (1) distinguish finding an answer from understanding a question and its assumptions, (2) retell the watermark example as “선택 확률에 흔적을 남기고, 우연인지 살핀다,” and (3) leave with a concrete habit: explain why, test when it fails, try a new question. Celebrate their learning; do not threaten them with obsolescence.

**Time:** 25 minutes total: 24 minutes planned speaking/short participation + 1 minute buffer. No separate Q&A assumed. Attachment's 30-minute / five-part allocation is superseded by Albert's direct 25-minute request. Proposed 22 pages including all structural pages; count and layouts remain targets, not constraints.

**Exclusions:** dgMARK, survey of watermark families, full Navier–Stokes mathematics, proof derivations, regulatory compliance details, live AI demo, an AI-vs-students ranking, fictional autobiographical material. No technical supplement by default: companion notes are sufficient.

**Research cutoff:** 2026-11-24; verify dated announcements and policy wording again at final review. Keep two AI-math examples from the attachment, not a growing news survey.

## 2. Evidence map and conflicts resolved

| Role in argument | Evidence | Decision |
|---|---|---|
| Speaker returning as an alumnus | E01 | Use only directly supplied identity; specific memories need Albert |
| AI can perform difficult mathematical reasoning | E02 | IMO 2025 advanced system, 35/42 and 5/6, “금메달 수준” |
| AI is being used at research frontiers | E03 | Dated Navier–Stokes announcement, not a claim of finalized recognition |
| Origin transparency creates a real question | E08 | Brief motivation; no algorithm mandated by either law |
| A model's choices can carry a statistical signal | E04, E09 | One original Korean toy example; scope it to this mechanism |
| Small statistical patterns can be tested | E05 | Independent fair-coin example; real text is not assumed iid |
| An honest model has failure conditions | E06–E07 | Short text, editing, mismatched scheme; absence is not proof of human origin |
| Mathematical intuition can guide AI-assisted exploration | E10 | Speaker's viewpoint plus an illustrative workflow, no measured speedup |

**Binding proposed resolutions:**
1. **30 → 25 minutes.** Compress repeated motivation and merge the final two sections, not the intellectual center of the watermark example.
2. **University-ready high school → accessible without that prerequisite.** Use counts and pictures. Z-statistic, logit bias, binomial calculation and qualifications remain in the paired notes. The on-slide conclusion and limitations remain visible; notes do not conceal them.
3. **16 fixed slides → about 22 short pages.** Adds necessary build-up and structural pages rather than shrinking type or cramming five stages into one slide.
4. **Personal-story placeholder → a complete, factual alumni/congratulations segment.** A real 60–90-second anecdote can later replace part of it. No “[연사 추가 예정]” or invented first-person experience in the deck.
5. **“비밀 규칙” simplified safely.** Teach a shared grouping rule that changes with context. A private-key implementation is an option, not a cryptographic security theorem or a universal feature of Algorithm 2.
6. **Diagram redrawing.** The lunch/coin examples are new illustrative data. Published empirical figures, if used, are captured/cropped/cited, never repainted. No assets or deck sources are produced by slides-review.

## 3. Argument and time budget

**One argument:** AI의 발전은 수학 학습의 종말이 아니라, 이해한 수학으로 더 많은 질문을 탐색할 기회다. A single watermark example earns this claim: everyday provenance concern → probabilistic generation → a deliberate small bias → a statistical question → assumptions and limits → a new experiment.

The alumnus identity appears at the opening, not only as a late biography. The closing honors the students and offers a doable habit; it is not a generic “work harder” exhortation.

| Section | Target pages | Time | Purpose |
|---|---|---:|---|
| Opening + 01 AI 이후의 수학 | S01–S08 | 6:00 | Welcome, recognize AI progress, ask what learning is for |
| 02 글에 숨긴 확률 | S09–S17 | 11:00 | The main intellectual experience, including coin participation |
| 03 직관과 함께 커지는 가능성 | S18–S22 | 7:00 | Use the insight, speak as a senior alumnus, finish with encouragement |
| Pacing buffer | — | 1:00 | Audience response and transitions; no extra content |
| **Total** | **22 target pages** | **25:00** | |

### Proposed title sequence (not yet a build specification)

IDs below are reserved within the new deck; no baseline page numbers exist. Match note articles to the same IDs when built. Each content row names the point and the exhibit so the argument can be reviewed without prescribing implementation.

| ID | Proposed title / point | Exhibit and scope | Seconds | Evidence / brief |
|---|---|---|---:|---|
| S01 | AI가 수학 문제를 푸는 시대, 무엇이 진짜 실력일까? | Title; alumnus → professor return, congratulations. Ask “왜 수학을 배울까?”; promise and later deliver an answer | 50 | E01; C01, C05 |
| S02 | 오늘의 세 가지 질문 | AI 이후의 수학 / 글에 숨긴 확률 / 직관과 함께 커지는 가능성, matching dividers | 20 | C02, C04 |
| S03 | 01 AI 이후의 수학 | Section divider | 10 | C04 |
| S04 | AI도 올림피아드 문제를 증명한다 | Six problem blocks, five solved; dated 35/42 advanced-system result, gold-medal standard, not medal award | 70 | E02; C06 |
| S05 | 연구의 최전선에도 등장한 AI | Fluid-flow concept plus dated proof-announcement marker; “발표와 최종 인정은 별개.” No PDE lesson | 70 | E03; C07 |
| S06 | 정답 다음의 질문 | Answer-finding vs deciding what the question means; explicit answer: both matter, neither is human-exclusive | 30 | E10; C08 |
| S07 | 도구가 바꾸는 질문 | Calculator → computer → AI as a conceptual analogy, not a claim that AI merely calculates | 40 | E10; C09 |
| S08 | 현상을 질문으로 바꾸는 힘 | Everyday concern → useful abstraction → test; understanding includes assumptions and failure | 70 | E10; C10–C11 |
| S09 | 02 글에 숨긴 확률 | Section divider; lead into one concrete example | 10 | C04 |
| S10 | 글에 출처를 남길 수 있을까? | Two illustrative ordinary-looking texts; shift from guessing author to deliberately embedding evidence. Optional brief legal motivation only | 60 | E08–E09; C12 |
| S11 | 다음 조각을 고르는 확률 | Korean lunch candidate probabilities, explicitly fictional; explain token as text fragment, only autoregressive sampling | 100 | E04, E09; C13 |
| S12 | 같은 규칙으로 묶고 세기 | Context-dependent candidate grouping; generator and detector must reproduce the same rule. Color is a diagram key | 90 | E04; C14 |
| S13 | 조금 바꾼 선택에 흔적이 남는다 | Gentle preference → accumulated marked choices; no guarantee of 8/10, perfect quality, or fixed word lists | 100 | E04, E09; C14 |
| S14 | 동전 100번, 앞면 70번? | Ask for a short vote/thought, show expected 50 vs observed 70. Reveal that it is unusual under independent fair flips, not impossible | 80 | E05; C15 |
| S15 | 우연이라면 얼마나 드문가? | Correct binomial bars, mean and right tail; state independence/fairness. A rare event is evidence, not posterior certainty | 100 | E05; C16 |
| S16 | 흔적은 단서, 판결은 아니다 | Supported mark → conditional evidence; no mark ≠ human. Editing/short text can weaken it. No accusation example | 60 | E06–E07; C22 |
| S17 | 출처의 질문이 확률의 질문으로 | Local example recap: origin concern → biased choices → chance test. This is the abstraction lesson, not another global conclusion | 60 | E04–E06, E10; C17 |
| S18 | 03 직관과 함께 커지는 가능성 | Section divider | 10 | C04 |
| S19 | 좋은 질문을 더 많이 시험하기 | Reuse coin example: change length/bias → ask AI for code → inspect/check → new question; illustrative workflow, no live dependency | 110 | E10; C18 |
| S20 | 같은 출발점에서, 새로운 질문으로 | Alumnus returning as professor; genuine congratulations and encouragement. Optional real anecdote can replace 60–90 seconds, not add time | 130 | E01, E10; C19 |
| S21 | 왜 맞을까? 언제 달라질까? | One closing takeaway: explain in your own words, change one assumption, test another use. Small worked callback, not a repeat of the agenda | 130 | E10; C20 |
| S22 | 여러분의 다음 질문을 응원합니다 | Clean closer and answer to title: deeply understood math opens more possibilities with AI. Congratulate the graduates | 40 | E01, E10; C20 |

## Request coverage

The original attachment is a brief, not existing deck pages. “Brief #” below means its proposed slide; final page mapping will be supplied by slides.

| Comment | Baseline page / title | Proposed IDs | Stage-4 package target |
|---|---|---|---|
| C01 | New deck; 25-minute ceremony request | All; S01/S20/S22 | All / shared |
| C02 | Purpose and core messages | S06–S08, S17, S19–S22 | P1–P3 |
| C03 | Audience and style | All; modified audience prerequisite pending approval | All |
| C04 | 30-minute timeline | New 25-minute table above | Shared |
| C05 | Brief #01 Opening | S01, S22 | Shared |
| C06 | Brief #02 IMO | S04 | P1 |
| C07 | Brief #03 Navier–Stokes | S05 | P1 |
| C08 | Brief #04 Question | S06 | P1 |
| C09 | Brief #05 Calculator | S07 | P1 |
| C10 | Brief #06 Layers | S08 | P1 |
| C11 | Brief #07 Reframing | S08, S17 | P1/P2 |
| C12 | Brief #08 Origin / regulation | S10 + note | P2 |
| C13 | Brief #09 Generation | S11 + note | P2 |
| C14 | Brief #10 Green list | S12–S13 + note | P2 |
| C15 | Brief #11 Coin participation | S14 | P2 |
| C16 | Brief #12 Test / z-score | S15; formal statistic in note | P2 |
| C17 | Brief #13 Abstraction recap | S17 | P2 |
| C18 | Brief #14 AI expands exploration | S19 | P3 |
| C19 | Brief #15 Personal story | S20; no fabricated anecdote | P3 |
| C20 | Brief #16 Closing | S21–S22 | P3/shared |
| C21 | References R01–R12 | E01–E12, per-slide notes | All |
| C22 | Fact guardrails | All; especially S04–S05/S11–S16/S20 | All |
| C23 | Handoff / visuals / interaction | All; length, formula placement and fixed count revised above | All |

## Stage 4 after approval

Expected deliverables: `261128yonseimath.html`, paired `261128yonseimath-note.html`, local `figs/` assets and any figure generator, leaf `OUTLINE.md`; add the new-talk entry to the existing root map. Final filenames and authorized shared surfaces will be explicit in plan-v2.

Proposed contiguous content packages: P1 S04–S08, P2 S10–S17, P3 S19–S21. Structural pages S01–S03/S09/S18/S22, contents, totals, citations/notes consistency, root/leaf outline and local ID mapping are shared integration work by slides. These are organizational packages, not authorization to spawn workers or start implementation yet.

The approved plan will give each slide its must/prefer/decides priority, exact required claim qualifiers, source locators, main/note split, an exhibit reading instruction, component vocabulary only, timing and an acceptance check. No markup, typography sizes, CSS or fixed-layout prescription.

**Review emphasis:** sincere ceremony tone; one earned narrative rather than an AI-news collage; truthful personal voice; original-experiment labels; readable Korean diagram labels; correct coin plot; same qualifications in slides/notes; pacing includes participation. Main deck must work without an internet connection. No type reduction to fit.
