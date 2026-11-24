# Plan v2 — authorized first draft

## Changes since v1

1. **C27 authorizes building now.** Albert explicitly says to draft first and discuss example choices afterward. This closes the stages 1–3 approval gate for the proposed 25-minute arc, with his audience correction. Do not wait for another example-selection approval.
2. **Audience corrected:** middle-school students who understand university-level mathematics. Keep conceptual depth; avoid an elementary-school tone. Concept-first means explain meaning, not avoid interesting mathematics.
3. **C24 supplies the personal reflection.** Use Albert's own emphasis on understanding mathematics in words across his life; do not invent a concrete childhood episode.
4. **C25 removes detailed derivations, including mandatory formula appendices.** A compact meaningful inequality can remain, especially given C27's AM–GM/Jensen suggestion. No z-score or logit derivation lesson and no technical supplement.
5. **Add one connected higher-level example in two pages:** S23 and S24, inserted after S20 and before S21. AM–GM as fixed-sum balance, then log concavity/Jensen as the organizing idea. It is a complete draft example, replaceable later without delaying the rest. Do not include the circle/average alternatives from E14–E16.
6. Closing-section time is redistributed, not extended. Target 24 pages, 24 minutes of content plus 1 minute buffer. All specs/packages are now complete for implementation.

## Header and summary

- Job: `2026-11-24-261128yonseimath-draft`; branch must have this exact name.
- Baseline: `95df062f8f980c686f0ef45974ebd3f626ff79d2`, not moving main.
- Target: repo-relative `talks/261128yonseimath/`. Create this folder, not `slides/talks/` inside the repository.
- Main: `talks/261128yonseimath/261128yonseimath.html`.
- Companion: `talks/261128yonseimath/261128yonseimath-note.html`.
- Occasion: Yonsei science-gifted-program graduation special lecture, Korean; alumnus and current professor speaking to the graduates. Date 2026-11-28 follows the requested folder/date brief; do not add an unprovided room, cohort year, or rank.
- Audience/mode: mathematically advanced middle-school students; concept-first special talk, not a proof lecture. University-level ideas are appropriate, while unfamiliar AI vocabulary needs a short explanation.
- No prior deck exists; baseline page/title map is empty. Attachment slide numbers are brief references, not repository pages.

**Thesis:** AI의 발전은 수학 학습의 종말이 아니라, 이해한 수학으로 더 많은 질문을 탐색할 기회다. The watermark example makes abstraction tangible; AM–GM/Jensen shows how a familiar formula can become a reusable conceptual lens. Do not claim intuition belongs exclusively to humans or that AI merely calculates.

**Objectives:** listeners can retell the watermark mechanism and its limits, distinguish getting an answer from understanding assumptions, and describe an inequality in words rather than merely manipulate it. Preserve ceremony warmth, curiosity and celebration.

**Scope/exclusions:** retain the two dated AI-math examples, one watermark mechanism, two brief audience questions, truthful personal reflection and the linked inequality example. No dgMARK, watermark-family survey, detailed PDE mathematics, legal-compliance tutorial, live AI dependency, full proofs, or invented personal story. Research/news cutoff remains 2026-11-24; current audience/build instructions are from Nov 25. Refresh time-sensitive claims during final review.

## Evidence map and continuity

| Argument role | Evidence | Treatment |
|---|---|---|
| Speaker/occasion/reflection | E01, E13, E17 | Personal claims only from Albert; examples are illustrations, not memories |
| Competition performance | E02 | Special advanced system, dated result, gold-medal standard |
| Research frontier | E03 | Dated announcement; final recognition is separate |
| Origin transparency | E08 | Brief motivation; neither law mandates this algorithm |
| Probabilistic generation and grouping | E04, E09, E20 | Korean toy example, not measured probabilities |
| Chance test | E05 | Independent fair-coin calculation; actual text can violate assumptions |
| Limits | E06–E07 | Evidence not a verdict; no mark does not establish human origin |
| Intuition and AI | E10 | Speaker's viewpoint, not a quantified productivity result |
| AM–GM/Jensen | E18–E19 | Positive values, fixed-sum interpretation, exact log/chord geometry |

Read/reuse decisions at the frozen baseline:
- Root `OUTLINE.md` and invited-talk exemplar `talks/kics260521dllm/OUTLINE.md` / deck: adapt pacing and visual-first presentation, not its vocabulary density.
- `courses/trustworthy-ai/OUTLINE.md`, lec11 S15–S20: adapt sampling → grouping → count; do not inherit the lecture's no-activities rule, its lengthy survey, or its old numerical examples.
- `courses/privacy/lectures/06-watermark/OUTLINE.md`: consult source locators/qualifiers, not theorem/proof content for this ceremony.
- `courses/deepmath/OUTLINE.md`, prob01 Jensen/concavity pages: adapt the distinction between average of values and value at the average. Its illustrative arch is not a log graph; do not relabel it as log. E19 gives a new exact example.
- No target leaf exists: create its outline stub before drafting, then fill it with the actual page/line map. Main deck is self-contained; no references to lecture numbers.

## Timing and title sequence

Times include short audience thought/voting pauses. The page count is a target; splits may change it, but not the 25-minute teaching scope. If a proposed split adds exposition time, raise it as a plan issue rather than silently growing the talk.

| Section | IDs in display order | Time |
|---|---|---:|
| Opening + 01 AI 이후의 수학 | S01–S08 | 6:00 |
| 02 글에 숨긴 확률 | S09–S17 | 11:00 |
| 03 직관과 함께 커지는 가능성 | S18, S19, S20, S23, S24, S21, S22 | 7:00 |
| Pacing buffer | — | 1:00 |
| **Total** | **24 target pages** | **25:00** |

## Coverage

| Comment | Baseline page / brief location | Slide IDs | Package |
|---|---|---|---|
| C01 | New talk / 25 minutes / target folder | All | All |
| C02 | Purpose and three messages | S06–S08, S17, S19–S24 | P1–P3 / shared |
| C03 | Audience/style | All; audience superseded by C27 | All |
| C04 | Original 30-minute timeline | 25-minute table above | Shared |
| C05 | Brief #01 opening | S01, S22 | Shared |
| C06 | Brief #02 IMO | S04 | P1 |
| C07 | Brief #03 Navier–Stokes | S05 | P1 |
| C08 | Brief #04 core question | S06 | P1 |
| C09 | Brief #05 calculator | S07 | P1 |
| C10 | Brief #06 skill layers | S08 | P1 |
| C11 | Brief #07 reframing | S08, S17 | P1/P2 |
| C12 | Brief #08 origin need | S10 | P2 |
| C13 | Brief #09 sampling | S11 | P2 |
| C14 | Brief #10 grouping/bias | S12–S13 | P2 |
| C15 | Brief #11 coin question | S14 | P2 |
| C16 | Brief #12 test | S15; detailed formulas omitted per C25 | P2 |
| C17 | Brief #13 abstraction | S17 | P2 |
| C18 | Brief #14 AI expansion | S19 | P3 |
| C19 | Brief #15 personal story | S20; supplied reflection C24 replaces placeholder | P3 |
| C20 | Brief #16 close | S21–S22 | P3/shared |
| C21 | Source register R01–R12 | E01–E12; sources per note | All |
| C22 | Fact guardrails | S04–S05, S11–S16, S20 | All |
| C23 | Handoff/figures/interaction | All; fixed count/time/math revised by C01/C25/C27 | All |
| C24 | Actual personal reflection | S20–S21 | P3 |
| C25 | No detailed formulas | All; one compact inequality per example page only | All |
| C26 | Intuition example request | S23–S24 | P3 |
| C27 | Advanced audience / build first / AM–GM or Jensen | All; S23–S24 | All |

## Slide specs

`Must` applies to the point, claim scope, evidence and acceptance checks. Titles and component suggestions are `prefer` unless noted; exact composition and splits are `slides decides`. All content pages have one exhibit; a before/after comparison is one coherent exhibit, not a collage. Notes carry message → explanation → sources/details, not an unrequested textbook. No tech file.

### S01 — AI가 수학 문제를 푸는 시대, 무엇이 진짜 실력일까?
- **Must / point:** welcome graduates as their senior alumnus and frame the question without making their skills feel worthless.
- **Required:** Albert No / 노알버트, Yonsei affiliation, ceremony context. Brief opening question “AI가 수학을 푼다면, 우리는 왜 배울까?” with a short promising subtitle about understanding and new questions, not permanent human superiority.
- **Exhibit/read:** title composition or simple alumnus-to-professor return motif; no invented dates or childhood photo.
- **Evidence:** E01, E10, E17; C01/C05.
- **Main / note:** concise title/identity; note holds greeting, congratulations and a short pause for thought. Detailed biography excluded.
- **Layout/time:** title-slide; 50 sec.
- **Acceptance:** no unverified personal detail; warm tone; opening question is answered by the ending.

### S02 — 오늘의 세 가지 질문
- **Must / point:** listeners see one connected journey, not unrelated AI news and mathematics.
- **Required:** exact section names “AI 이후의 수학”, “글에 숨긴 확률”, “직관과 함께 커지는 가능성”; same numbering/order as dividers.
- **Exhibit/read:** three-step roadmap, AI changes → mathematical case → personal takeaway.
- **Evidence:** author-approved arc C01/C02/C27; narrative, not empirical claim.
- **Main / note:** section labels on main; note gives one sentence tying them together.
- **Layout/time:** toc-list; 20 sec.
- **Acceptance:** names match S03/S09/S18; no technical terminology before context.

### S03 — 01 AI 이후의 수학
- **Must / point:** acknowledge the change before discussing learning.
- **Required/exhibit:** section divider with a short orientation question; not a fourth agenda item.
- **Evidence:** C04 and E10 as framing.
- **Main / note:** section label; one transitional cue in note.
- **Layout/time:** section-slide.left; 10 sec.
- **Acceptance:** numbering/name match S02.

### S04 — AI도 올림피아드 문제를 증명한다
- **Must / point:** difficult mathematical reasoning is no longer outside demonstrated AI capabilities.
- **Required:** IMO 2025, advanced Gemini Deep Think, 35/42, 5/6 fully solved; “금메달 수준” rather than medal recipient. This is the evaluated advanced system, not every chatbot.
- **Exhibit/read:** six problem blocks with five solved and one not, linked to the total score. A numeric teaching summary is acceptable; no human-vs-AI leaderboard invented.
- **Evidence:** E02, supplied official DeepMind report section; C06.
- **Main / note:** result, dated system identity and scope on main; note explains official grading, no general claim of universal superiority.
- **Layout/time:** grid-3 or slides decides; 70 sec.
- **Acceptance:** exactly five full solves; score denominator 42; advanced-system scope visible, source valid.

### S05 — 연구의 최전선에도 등장한 AI
- **Must / point:** research uses go beyond solving contest exercises, while a proof announcement is not final institutional recognition.
- **Required:** date 2026-09, OpenAI's announced AI-produced Navier–Stokes proof; “발표와 최종 인정은 별개.” Introduce the problem in words as a question about the mathematical description of fluid motion.
- **Exhibit/read:** a sourced fluid image or plainly illustrative flow concept paired with dated announcement/verification distinction; no purported proof visualization.
- **Evidence:** E03, OpenAI introduction/“The result” and Clay conclusion; C07.
- **Main / note:** qualified announcement on main; note records exact dates, forced-alternative scope, and source URLs. No equation, prize claim, new consensus assertion, or proof audit.
- **Layout/time:** slides decides; 70 sec.
- **Acceptance:** cannot be read as “official prize awarded” or “all fluid equations resolved.” New factual developments are a plan issue.

### S06 — 정답 다음의 질문
- **Must / point:** obtaining an answer and understanding the question are related but distinct skills.
- **Required:** explicit answer to the opening worry: learning meaning/assumptions helps ask, check and extend questions; do not allocate problem solving to AI and insight exclusively to humans.
- **Exhibit/read:** answer-finding vs understanding/choosing/testing, with collaboration rather than a human/AI capability wall.
- **Evidence:** E10; C08.
- **Main / note:** short contrast and explicit point; note connects to the central case without a technology prediction.
- **Layout/time:** grid-2; 30 sec.
- **Acceptance:** no “AI does not understand” assertion; not just an unanswered rhetorical question.

### S07 — 도구가 바꾸는 질문
- **Must / point:** stronger tools can change what we attempt, not make understanding pointless.
- **Required:** calculator/computer/AI conceptual progression; label functions as examples, not exclusive historical stages or a dated causal study.
- **Exhibit/read:** one progression from arithmetic to larger experiments and assisted reasoning.
- **Evidence:** E10; C09.
- **Main / note:** simple analogy; note acknowledges that AI also assists reasoning and problem formulation.
- **Layout/time:** diagram-flow; 40 sec.
- **Acceptance:** no invented historical statistics/dates; no “AI is only a calculator.”

### S08 — 현상을 질문으로 바꾸는 힘
- **Must / point:** abstraction chooses what matters and makes a question testable.
- **Required:** understand → formulate → test; technique is valuable, not dismissed. No ladder that implies AI cannot do upper steps.
- **Exhibit/read:** everyday concern mapped to a mathematical question, then a check; vocabulary reused in S17.
- **Evidence:** E10; C10–C11.
- **Main / note:** three short steps and point; note explains that choices/assumptions are the intellectual work, not merely writing symbols.
- **Layout/time:** diagram-flow; 70 sec.
- **Acceptance:** a listener can say what “추상화” means before the watermark case begins.

### S09 — 02 글에 숨긴 확률
- **Must / point:** move from a general claim about intuition to one concrete case.
- **Required/exhibit:** matching divider and one-line question about embedding a trace in ordinary text.
- **Evidence:** E04; C04.
- **Main / note:** section label; short transition only.
- **Layout/time:** section-slide.left; 10 sec.
- **Acceptance:** consistent section name and no new watermark jargon overload.

### S10 — 글에 출처를 남길 수 있을까?
- **Must / point:** deliberately embedding a trace is a different problem from guessing authorship after the fact.
- **Required:** ordinary-looking generated text; the actual question is “생성할 때 확인 가능한 흔적을 남기자.” Origin transparency is social motivation, not proof that a text is true.
- **Exhibit/read:** illustrative text/label that can be removed contrasted with a generation-time signal; not a fake detector evaluation.
- **Evidence:** E08–E09; C12.
- **Main / note:** visual/problem on main. A very brief Korea/EU source cue is optional; note preserves legal scope and says this algorithm is not mandatory. No compliance dates lesson.
- **Layout/time:** grid-2 or slides decides; 60 sec.
- **Acceptance:** watermark ≠ universal detector; any sample text clearly illustrative; laws not overstated.

### S11 — 다음 조각을 고르는 확률
- **Must / point:** generation provides a distribution of choices that a watermark can influence.
- **Required:** autoregressive next-token sampling; token is a text fragment, not always a word. Use one illustrative Korean continuation, not a claim about a real tokenizer.
- **Exhibit/read:** “오늘 점심은…” with choices/probability bars from E20; select a continuation and repeat. Label “설명용 가상 예시.”
- **Evidence:** E04, E09, E20; C13.
- **Main / note:** distribution and repeat idea, no softmax formula; note explains the autoregressive scope and invented values. A simple conditional-probability symbol is optional, not required.
- **Layout/time:** slides decides; 100 sec.
- **Acceptance:** bars sum to one, no implication every AI model decodes this way, token definition visible.

### S12 — 같은 규칙으로 묶고 세기
- **Must / point:** the generator and detector must reconstruct the same token-group assignment.
- **Required:** assignment depends on context; groups are not a permanent dictionary. Color is a diagram aid, not ink in actual output. A keyed implementation may be described as a variant, not an unsupported universal claim about Algorithm 2.
- **Exhibit/read:** context + shared rule → grouped candidates; detector uses that rule to check chosen tokens. Continue the S11 example for one context only.
- **Evidence:** E04, E20; C14.
- **Main / note:** same-rule grouping and context scope; note distinguishes public/secret-rule variants without cryptographic guarantees.
- **Layout/time:** diagram-flow; 90 sec.
- **Acceptance:** labels make what the generator/detector receive clear; no fixed food-word green list implied.

### S13 — 조금 바꾼 선택에 흔적이 남는다
- **Must / point:** slightly favoring the marked choices creates an aggregate signal rather than an explicit label.
- **Required:** before/after selection probabilities, not “always choose green”; same grouping/context as S12. Do not promise perfectly unchanged quality or a fixed observed fraction.
- **Exhibit/read:** one paired probability comparison from E20; green total 50% → 60% in this constructed context. The main statement is a preference, not a hard prohibition.
- **Evidence:** E04, E20; C14.
- **Main / note:** toy comparison and signal takeaway; note gives verbal normalization and detectability/quality tradeoff, no logit derivation.
- **Layout/time:** slides decides; 100 sec.
- **Acceptance:** before/after sums 100%; other candidates remain possible; fabricated data never presented as an experiment.

### S14 — 동전 100번, 앞면 70번?
- **Must / point:** an observation should be compared with a model of chance, not judged only by its raw percentage.
- **Required:** short audience vote/thought; 100 independent fair flips as the null model; expected 50, observed 70. Explicit reveal: unusual under this model, not logically impossible.
- **Exhibit/read:** count display or clear marked sample; if 100 marks shown, exactly 70 must match the observation.
- **Evidence:** E05; C15.
- **Main / note:** question, model and brief answer; note includes pause/reveal cue and transition to testing.
- **Layout/time:** slides decides; 80 sec including participation.
- **Acceptance:** fair/independent conditions stated; doesn't declare “the coin is certainly biased.”

### S15 — 우연이라면 얼마나 드문가?
- **Must / point:** detection asks how surprising a count is under a specified chance model.
- **Required:** Binomial(100,0.5) teaching example; mark 50 and 70, tail means “70번 이상.” Approx. 0.0039% may appear with its event/conditions, but never “AI일 확률.” Real text dependence is not assumed away.
- **Exhibit/read:** generated exact discrete probabilities; x = head count, y = probability at that count. Mean and shaded upper tail identified; don't pretend a smooth density is an exact PMF.
- **Evidence:** E05; C16.
- **Main / note:** model/tail interpretation/limitation; note explains calculation in words and cites E05 derivation source, not a z-score tutorial. No mandatory formal equation.
- **Layout/time:** slides decides; 100 sec.
- **Acceptance:** correct tail starts at 70; not exact-70 or two-sided; tail number not confused with posterior authorship probability. Plot regenerated from recorded inputs.

### S16 — 흔적은 단서, 판결은 아니다
- **Must / point:** a supported statistical signal has limits and must not become an automatic accusation.
- **Required:** detector looks for its supported scheme; short/edited text can weaken evidence; no mark does not imply human origin. Do not claim all editing destroys marks.
- **Exhibit/read:** marked generation → transformation → conditional detector evidence, including an inconclusive outcome.
- **Evidence:** E06–E07; C22.
- **Main / note:** visible boundaries; note can name SynthID as a distinct historical application, never the same algorithm. No extra method/results slide.
- **Layout/time:** diagram-flow; 60 sec.
- **Acceptance:** avoids both perfect-detector and hopeless-detector narratives; no real person accused.

### S17 — 출처의 질문이 확률의 질문으로
- **Must / point:** the central intellectual move was changing the question into one we can model and test.
- **Required:** origin concern → biased choices → chance comparison, using the same terms and order as the example.
- **Exhibit/read:** local three-step conceptual map, not a global recap of the whole lecture.
- **Evidence:** E04–E06, E10; C17.
- **Main / note:** abstraction takeaway; note credits engineering and assumptions too, not a claim that the toy model solves provenance completely.
- **Layout/time:** diagram-flow; 60 sec.
- **Acceptance:** audience can tell how the math view changed the problem; not just repeated green-token mechanics.

### S18 — 03 직관과 함께 커지는 가능성
- **Must / point:** return from the concrete example to the opportunities for the students.
- **Required/exhibit:** matching divider, forward-looking but not exaggerated.
- **Evidence:** E10; C04.
- **Main / note:** short transition.
- **Layout/time:** section-slide.left; 10 sec.
- **Acceptance:** name matches S02; no prediction about guaranteed careers.

### S19 — 좋은 질문을 더 많이 시험하기
- **Must / point:** understanding guides the questions, tools and checks in an AI-assisted experiment.
- **Required:** change a count/sample-size question → ask AI to help implement → independently check → revise question. AI can also propose ideas; not an exclusive human/AI split.
- **Exhibit/read:** one small experimental loop based on the coin example, not a live chatbot or invented productivity result.
- **Evidence:** E10; C18.
- **Main / note:** loop and verification step; note gives one concrete “what if” prompt as an illustration, no pretense it was run.
- **Layout/time:** diagram-flow; 70 sec.
- **Acceptance:** offline narrative complete; verification is explicit; no quantified speedup.

### S20 — 오래 남은 것은 수학의 의미
- **Must / point:** Albert's personal message is about learning to understand mathematics in words, not just procedural performance.
- **Required:** truthful paraphrase of C24: problem-solving practice helped, but intuition and meaning mattered especially, across his life including the program. Do not dismiss practice.
- **Exhibit/read:** formula/technique → verbal meaning → a new perspective as a conceptual personal reflection, not an invented life timeline.
- **Evidence:** E01, E13; C19/C24.
- **Main / note:** short personal statement on main; note supplies natural first-person wording faithful to C24 and transitions to a teaching illustration. Do not assert he specifically discovered AM–GM this way as a child.
- **Layout/time:** slides decides; 60 sec.
- **Acceptance:** every autobiographical statement traceable to Albert; no placeholder for an anecdote.

### S23 — 같은 합이라면, 균형 잡힐수록 곱이 크다
- **Must / point:** AM–GM expresses a usable idea about positive factors with a fixed sum, not only a contest manipulation.
- **Required:** positive a,b; fixed a+b=10 worked case (2,8) vs (5,5), products 16 vs 25. Introduce “산술·기하평균 부등식(AM–GM)” and at most its compact two-variable inequality. Equality at equal factors.
- **Exhibit/read:** a single fixed-perimeter rectangle comparison, correctly scaled if area/shape is quantitative; read same side-sum, different product, maximum at the square. Or an equally precise original product-vs-balance exhibit.
- **Evidence:** E18–E19; C26–C27.
- **Main / note:** mathematical meaning, numerical comparison and short inequality; note explains fixed-sum qualification and equality, no algebraic proof chain. Tech: none.
- **Layout/time:** slides decides; 90 sec.
- **Acceptance:** fixed sum/positivity visible; does not imply equalization universally maximizes every objective. This is an illustration, not claimed as Albert's personal historical episode.

### S24 — 평균과 함수, 순서가 중요하다
- **Must / point:** Jensen organizes the example through curvature: for concave log, value at the average is at least the average of values.
- **Required:** same a=2,b=8; graph y=log x, chord between endpoints; at x=5 compare curve height log5 with chord height log4. Label this as the log case of Jensen's inequality. One compact inequality is sufficient; note explains that convex functions reverse direction.
- **Exhibit/read:** exact log graph from E19, with clear input-average and output-average points at the same x. Curve lies above chord; not a parabola mislabeled log. Key names axes and the two routes, not merely two colored dots.
- **Evidence:** E18–E19; C26–C27.
- **Main / note:** picture + “오목한 log에서는 평균을 넣은 값 ≥ 함수값의 평균”, a,b>0, optional single log inequality. Note verbally connects increasing log/product rule back to AM–GM and describes generality without a formal theorem/proof lecture.
- **Layout/time:** slides decides; 100 sec.
- **Acceptance:** inequality direction, curve shape and log4/log5 locations correct; exact invariant checked; same phrase order in prose and figure. No “all functions” claim. Can split for readability while retaining this time budget.

### S21 — 이 식은 어떤 이야기를 할까?
- **Must / point:** turn the reflection into one practical habit, with an explicit answer to the talk's opening question.
- **Required:** after solving, explain meaning → question assumptions → try another setting. Mathematics helps expand the questions one can ask with AI; not a guarantee of immunity from change.
- **Exhibit/read:** one compact three-question prompt sequence; use the just-taught inequality only as a verbal callback, not another proof or full summary table.
- **Evidence:** E10, E13; C20/C24–C27.
- **Main / note:** the single global takeaway; note gives a short encouraging closing script in Albert's voice, within supported personal facts.
- **Layout/time:** diagram-flow or slides decides; 50 sec.
- **Acceptance:** no repeated agenda or second global recap; practical rather than preachy.

### S22 — 여러분의 다음 질문을 응원합니다
- **Must / point:** finish as a senior alumnus congratulating the graduates and opening possibilities.
- **Required/exhibit:** clean closer, congratulations and one forward-looking line; no additional content table, QR/link dependency or unrequested invitation.
- **Evidence:** E01, E10; C20.
- **Main / note:** short closer; note final spoken thought. No invented personal milestone.
- **Layout/time:** end-slide; 40 sec.
- **Acceptance:** warm final landing, legible, one ending.

## Packages and allowed surfaces

Slides owns implementation and integration. These are content boundaries, not a requirement to create worker agents. If slides delegates, no worker changes another package's content or shared surfaces.

| Package | IDs / physical range target | Files / sections permitted | Dependencies |
|---|---|---|---|
| P1 | S04–S08 / pages 4–8 | Main and note sections for these IDs; local assets with P1-specific names | E01–E03/E10; no dependency on later package prose |
| P2 | S10–S17 / pages 10–17 | Main and note sections for these IDs; local watermark/coin assets | E04–E09/E20; use one shared toy example within package |
| P3 | S19,S20,S23,S24,S21 / pages 19–23 | Main and note sections for these IDs; local AM–GM/Jensen assets | E10/E13/E17–E19; S19 refers to E05's coin setup, not a moving page number |
| Shared / integrator | S01–S03,S09,S18,S22; all ordering/consistency | Main/note shell; IDs; TOC/dividers; citations and totals; local figure generator; leaf/root outline; job record | Integrate after packages; retain phrase/ID consistency |

Authorized created/edited paths:
- `talks/261128yonseimath/261128yonseimath.html`
- `talks/261128yonseimath/261128yonseimath-note.html`
- `talks/261128yonseimath/OUTLINE.md`
- `talks/261128yonseimath/figs/` assets; `figs/generate-figures.py` for reproducible original plots (owned/written by slides)
- root `OUTLINE.md`: add this talk's entry only; update `talks/OUTLINE.md` only if it already exists and needs a pointer. Do not create a broad outline reorganization.
- `log/2026-11-24-261128yonseimath-draft/`: unchanged copies of planner files and slides-owned work report.

No changes to shared `reference/`, global scripts, unrelated decks, existing course outlines or source notes. Reuse canonical shared assets, not private duplicates. Any additional asset licensing unresolved must be flagged; do not silently copy restricted photos. Generated figures have inputs, algebra/parameters and generator path in the work report so the evidence register can be appended.

## Shared integration and handoff

1. Create branch from the recorded baseline. Copy the complete planner record unchanged; refresh living `job.md`, `requests.md`, `evidence.md` at push. Copy both plan versions for history; v2 governs.
2. Create target leaf outline stub first. Produce main and one matching note article per slide, including structural slides. For the contract's ID-only step, introduce stable slide/note IDs in a dedicated commit once the new draft exists, changing only IDs; report its SHA. Never renumber reserved IDs. New split S24a/S24b is reported as a split; new IDs start S25.
3. Keep display order S01…S20, S23, S24, S21, S22. Report actual old/new map (old page = new deck / brief reference as appropriate). Correct all outline counts and pointers after any split.
4. Validate source statements, group membership and numerical examples; sum the timing including audience response. No bare source placeholders or “personal story pending” text.
5. Run repository lint and outline checks. Render every draft page at final size and inspect Korean wrapping, plot labels, cites/footer, curves and notes. Check notes at a narrow viewport. Report precisely what was checked; lint alone is not visual review.
6. Commit/push and hand back `work-r1.md` with exact SHA, branch, ID-only SHA, mappings, deviations, source gaps, figure-generator path and checks. Changes of required content, facts, argument or time are plan issues, not silent deviations. No PR creation/merge by slides for this pipeline job; slides-review reviews then opens PR.

Only blocking findings start a revision round; large-job maximum is three rounds. Albert remains the final check, and his draft authorization is not a merge order. No PDF delivery unless he asks.
