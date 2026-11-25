# Yonsei graduation talk — author-feedback revision

## 1. Summary and controls

Medium job, two review rounds maximum. Build from **37757bb365a74b434a65a0ec0f6d86d40c9b253a**, not moving main. Main file **M = talks/261128yonseimath/261128yonseimath.html**; companion **N = talks/261128yonseimath/261128yonseimath-note.html**. Main/notes/assets are written only by slides.

Keep the 25-minute Korean talk and the advanced middle-school audience. Preserve the argument: AI is changing mathematical work; understanding mathematics helps turn real engineering needs into tractable questions; intuition and AI together expand what students can try. This is not a lecture on AI's shortcomings. Replace explanatory clutter with the requested images, a clearly motivated watermark example and a simple autoregressive animation. Finish with multiplicative-growth intuition for AM–GM, then the direct log/Jensen comparison and real-world application.

**Must:** implement all C01–C19, including literal deletions; remove the TOC and limitation slide, not just hide them. **[judgment]** Natural Korean and visual editing across the whole deck belong to slides directly. Replace awkward slogan-like summaries, repetitive “A · B · C” conclusions and policing caveats with ordinary spoken Korean, or delete them when the exhibit already says the point. Do not mechanically erase useful short labels, mathematical assumptions or citations. Do not reinstall deleted text under a synonym.

**Resolved tensions:**
1. C01 overrides the three-section Contents rule for this talk. Section dividers remain; no replacement roadmap.
2. C11 expressly requests looping playback. This narrow exception applies to the S12 demo only; preserve speaker control, pause/restart and a complete static fallback. No shared engine/design-rule changes.
3. C13 asks for a question, no explanation. S14 may omit the usual answer/Point line; S15 explicitly answers the question. The user will narrate.
4. “Gold Medal” is the requested heading; “금메달 수준 · Gemini Deep Think” and the score keep its meaning accurate. Navier–Stokes slide says “해법 발표” and uses the original source image, not a diagram of recognition procedures.
5. C10's worldwide-text shorthand becomes truthful large-corpus/contextual learning wording. C09's all-odd image is a teaching construction, not a theorem of impossibility or a secure watermark. E05/E08 provide exact scope without a caveat-heavy slide.
6. The dgMARK animation is a **visual reference**; the mechanism taught is ordinary left-to-right, soft green-list watermarking. It is not dgMARK or diffusion decoding. Random-looking groups must be reproducible from the prefix/rule for detection.
7. Pure mathematics need not justify itself only through engineering. S06 includes curiosity, conceptual organization and unknowns; S08 explicitly turns to applications. No “AI cannot do research” or “AI only calculates” contrast.

## 2. Coverage and frozen page trail

All line locations below are baseline starts in **M** and are lookup anchors, not implementation prescriptions. Revised pages are targets; work-r1 supplies actual pages.

| Comment | Baseline page / title / line | Stable ID → target page | Package |
|---|---|---|---|
| C01 | p2 오늘의 세 가지 질문 :113 | S02 retired | Shared |
| C02 | p4 AI도 올림피아드 문제를 증명한다 :157 | S04 →3 | P1 |
| C03 | p5 연구의 최전선에도 등장한 AI :179 | S05 →4 | P1 |
| C04 | p6 정답 다음의 질문 :197 | S06 →5 | P1 |
| C05 | p7 도구가 바꾸는 질문 :217 | S07 →6 | P1 |
| C06 | p8 현상을 질문으로 바꾸는 힘 :234; whole deck | S08 →7; all wording | P1/P2/P3 + Shared |
| C07 | p9 글에 숨긴 확률 :251 | S09 →8 | Shared |
| C08 | p10 글에 출처를 남길 수 있을까? :261 | split S10a →9, S10b →10 | P2 |
| C09 | new image bridge after original p10 | new S25 →11, after S10b | P2 |
| C10 | p11 다음 조각을 고르는 확률 :284 | S11 →12 | P2 |
| C11 | p12 같은 규칙으로 묶고 세기 :304 | S12 →13 | P2 |
| C12 | p13 조금 바꾼 선택에 흔적이 남는다 :335 | S12/S13 →13/14 | P2 |
| C13 | p14 동전 100번, 앞면 70번? :360 | S14 →15; S15 →16 answers | P2 |
| C14 | p16 흔적은 단서, 판결은 아니다 :400 | S16 retired | P2 |
| C15 | p17 출처의 질문이 확률의 질문으로 :421 | S17 →17 | P2 |
| C16 | p19 좋은 질문을 더 많이 시험하기 :449 | S19 →19 | P3 |
| C17 | p20 오래 남은 것은 수학의 의미 :469 | S20 →20 | P3 |
| C18 | p21 같은 합이라면, 균형 잡힐수록 곱이 크다 :486; p22 평균과 함수, 순서가 중요하다 :514 | S23/S24 →21/22 | P3 |
| C19 | p23 이 식은 어떤 이야기를 할까? :535 | S21 →23 | P3 |

Unaffected structural baseline anchors: p1 S01 :100; p3 S03 :147; p18 S18 :439; p24 S22 :552. Preserve these IDs. S10 is retired by the split; S10a/S10b pair with matching note articles. S02/S16 are not reused. New numbering starts S25; if further splitting helps legibility, report the mapping.

## 3. Title sequence and timing targets

24 pages remain a useful target, not a cap. Replacements remove two pages and add two. No extra technical appendix. Planned content24minutes +1minute pacing buffer; no timed-rehearsal claim.

| ID | Proposed title | Seconds |
|---|---|---:|
| S01 | existing opening question, simplified subtitle if redundant | 30 |
| S03 | AI 이후의 수학 | 10 |
| S04 | IMO 2025 Gold Medal | 50 |
| S05 | Navier–Stokes: 밀레니엄 문제 | 50 |
| S06 | 문제를 푸는 것 vs 수학을 연구하는 것 | 80 |
| S07 | 도구가 바꾸는 질문 | 40 |
| S08 | 현실 문제를 풀려면 수학을 이해해야 한다 | 70 |
| S09 | AI가 쓴 글에 보이지 않는 표식 남기기 | 10 |
| S10a | AI가 썼다는 걸 알아야 할 때 | 50 |
| S10b | 지우기 쉬운 표시 대신 | 40 |
| S25 | 눈에는 비슷해도, 숫자에는 흔적이 있다 | 90 |
| S11 | ChatGPT는 다음 단어의 분포를 예측한다 | 80 |
| S12 | 초록 단어를 조금 더 자주 | 120 |
| S13 | 초록만 고르지는 않는다 | 60 |
| S14 | 앞면 확률이 1/2인 동전을 100번 던져서 앞면이 70번 나올 수 있을까? | 40 |
| S15 | 가능하지만, 매우 드물다 | 100 |
| S17 | AI 작성글의 표식을 통계 문제로 | 70 |
| S18 | 직관과 함께 커지는 가능성 | 10 |
| S19 | AI와 함께 더 많은 아이디어 시험하기 | 60 |
| S20 | 오래 남은 것은 수학의 의미 | 70 |
| S23 | 평균 성장배율이 같아도, 들쭉날쭉하면 덜 성장한다 | 100 |
| S24 | Jensen’s inequality: log는 concave | 110 |
| S21 | 수학을 직관으로 이해하고, 현실에 적용하기 | 70 |
| S22 | 수료를 축하합니다 | 30 |

P1/opening5:30; P2/section2 11:00; P3/closing7:30. All titles except explicit author replacements are **[judgment] proposals**; simplify naturally, preserving the point. Long Korean titles may wrap at meaning boundaries; never reduce type to force one line.

## 4. Slide-level specifications

### 01 — S01, opening (baseline p1)
- **Must:** retain occasion, alumnus/current-professor identity and the question about learning mathematics in the AI era. Evidence E01/E11. No fabricated autobiographical detail.
- **[judgment] Prefer:** remove overlapping subtitle slogans; one opening question is enough. Exhibit/title-slide,30sec. Note remains a brief opening, not an extra outline.
- Acceptance: title and final S21 answer still connect; no TOC replacement creeps in.

### 02 — S02, delete (baseline p2)
- **Must:** delete main slide and matching note article; update navigation/counts. Retire ID. No replacement roadmap or mandatory spoken three-part list.

### 03 — S03, section1 (baseline p3)
- **Must:** preserve section number01 and name. **Slides decides:** minimal subtitle polish. Section-slide,10sec; note short. E01.

### 04 — S04, IMO (baseline p4)
- **Must, C02:** “AI도 올림피아드 문제를 증명한다” → **“IMO 2025 Gold Medal”**. Delete solved/unsolved six-box diagram. Keep score35/42 as the sole result exhibit and identify advanced Gemini Deep Think / 금메달 수준, E02.
- **[judgment] Prefer:** remove the defensive “모든 챗봇이 아니라…” sentence; name the evaluated system directly instead. Five of six may be spoken/notes, not another visual.
- Main: heading, score, short context, citation. Note: exact evaluation scope/source. Suggested layout: single finding/exhibit;50sec. Acceptance: no award overclaim, no six-status diagram, readable and uncluttered.

### 05 — S05, Navier–Stokes (baseline p5)
- **Must, C03:** English **Navier–Stokes**, explicit **밀레니엄 문제**, and the large original OpenAI vortex image from E03. Remove the fluid-definition sentence, verification timeline, final-recognition highlight and all extra schematics.
- Main: title, image, concise “OpenAI의 해법 발표 · 2026.9.8” context/citation. No fluid mechanics lesson. Note: dated source and optional exact result/prize-process context, not a mandatory caution speech.
- Figure-first,50sec. **Slides decides:** fit/crop only if it preserves the original image meaning and provenance. Acceptance: no invented rotating animation, no verification diagram, aspect ratio intact; source image dominates.

### 06 — S06, solving versus researching (baseline p6)
- **Must, C04:** left “정답 구하기” / “주어진 문제를 해결한다”; right “수학을 연구하는 것” with (1)어떤 문제를 풀 것인가? (2)우리가 아는 것을 어떻게 더 효율적으로 표현할 것인가? (3)무엇을 모르는가? Remove both quoted conclusion lines from C04.
- **[judgment] Prefer:** clean two-column comparison as the exhibit, not a flow that makes research exclusively a later stage. Credit **Terence Tao, Math2.0,2026, 관점 요약** (E04). The three questions are Albert's framing; do not put them in quotation marks as Tao's exact words.
- Main: comparison/citation; note: concise Tao paraphrase with PDFpp16/25 and the complementarity of solving/research. No claim AI can only do the left side. Grid-2,80sec. Acceptance: all three research questions present, not “problem understanding” substituted for research.

### 07 — S07, tools (baseline p7)
- **Must, C05:** AI label “코딩 · 추론 · 탐색을 돕는다” → **“코딩 · 추론 · 탐색”**; delete “역사의 단계가 아니라 비유 · 이해는 여전히 질문을 고른다”.
- **[judgment]:** retain the calculator/computer/AI exhibit as capabilities, not a claimed historical replacement sequence. Remove/rephrase redundant highlight if the image says it. E01/E05, diagram-flow,40sec. Note can clarify coexistence without reintroducing a caveat paragraph.

### 08 — S08, engineering pivot (baseline p8)
- **Must, C06:** replace abstract coin-method preview and “계산 기법도 여전히 필요 · 무엇을 남길지 고르는 것이 핵심” with the point **“현실 문제를 풀기 위해서는 수학적인 이해가 중요하다.”** This is the bridge to the engineering case, not a claim all pure mathematics is utilitarian.
- **[judgment] Exhibit:** a simple problem→mathematical model→usable design relationship, concretely anchored by “AI가 쓴 글에 표식을 남기려면?” Do not explain the full watermark answer before the motivation. Natural labels such as “무엇을 만들고 싶은가 / 어떤 수학으로 표현할까 / 어떻게 구현할까” are preferable to a stack of thesis slogans.
- E01/E06/E11; main one visual/point, note one brief transition. Diagram-flow,70sec. Acceptance: engineering importance explicit; S17 later supplies the actual statistical reframing rather than repeating this slide verbatim.

### 09 — S09, section2 (baseline p9)
- **Must, C07:** “글에 숨긴 확률” → **“AI가 쓴 글에 보이지 않는 표식 남기기”**, or a shorter natural paraphrase with the same meaning. Optional subtitle “LLM watermarking”; watermarking means embedding a mark, not hiding probability itself.
- Section-slide,10sec; E06. Synchronize name everywhere, no Contents to restore.

### 10 — S10a, misuse motivation (split baseline p10)
- **Must, C08:** first establish why origin can matter: e.g. a school assignment expected to show a student's own thinking, or a supposedly personal review. One hypothetical concrete writing situation as the exhibit; no fabricated real incident/percentage.
- **[judgment]:** title “AI가 썼다는 걸 알아야 할 때.” Message is undisclosed/uncritical use where provenance matters, not “all LLM use is wrong.” Keep visible versus invisible marking for S10b.
- E06; main one example and short question, note expands the motivation. Card/single exhibit,50sec. Remove the old legal aside from the main and do not replace it with policy detail.

### 11 — S10b, hidden marking objective (split baseline p10)
- **Must, C08:** “AI가 쓴 글에는 AI가 썼다는 표식을 남기고 싶다”; an obvious “[AI 생성]” label can simply be deleted, so seek a mark that does not stand out in the text. Exhibit: the same sentence with a removable visible tag versus the desired unchanged-looking text. This is a design goal, not a claim the two files/words are identical.
- E06/E08. Main picture plus goal; note explains generation-time embedding and no universal removal-resistance promise. Grid-2,40sec. Acceptance: clear why the next image example is relevant; no cryptography/secrecy lecture or verification diagram.

### 12 — S25, image parity bridge (new, after S10b)
- **Must, C09:** compare the same grayscale image before and after all intensities are made odd, using E08's lossless reproducible construction. “각 픽셀값을 최대1만 바꾸기” and “모두 홀수” give the visual its meaning; no dense pixel-number table.
- **[judgment] Main:** large before/after pair as one comparison exhibit, brief oddness label, then the bridge question **“그런데 글의 단어도 이렇게 조금씩 바꿀 수 있을까?”** Images should look nearly identical at presentation size. Do not state all-odd pixels are mathematically impossible without a watermark.
- Note:8-bit setup, actual computed odd fraction/max difference, fragility and the difference between a teaching construction and production watermark. Source/processing citation. Grid-2,90sec.
- Acceptance: inspect both generated images and file-level assertions; no JPEG/resizing damage after parity; visible original/marked labels; source credit; not claimed to prove AI authorship. Use the verified NASA source or report an equally traceable replacement.

### 13 — S11, LLM design principle (baseline p11)
- **Must, C10:** prominently identify **ChatGPT 같은 LLM의 기본 원리**: predict the distribution of plausible next words from context, learned from large amounts of text. Open-ended continuation has multiple valid possibilities.
- Exhibit: retain/adapt a simple context with candidate probability bars, explicitly illustrative rather than measured. Use E06 values if retained. Do not spend the headline defining “token”; a word-based simplification is fine with exact token granularity in notes.
- Replace literal “all texts in the world” with E05 wording. No count lookup, single-correct-next-word or mandatory-argmax implication. Main: prediction + learning point; note: actual token units and pretraining/post-training scope. Single distribution exhibit,80sec. Acceptance: both learning and generation are understandable without formulas.

### 14 — S12, autoregressive loop (baseline p12)
- **Must, C11/C12:** replace the current two-lane generation/checking diagram completely. Follow E07's visual language, but animate **one short sentence from left to right**, with enough time to narrate each step.
- Observable sequence: existing prefix → next-word candidates split into green/red → green probabilities nudged upward → one candidate selected and appended → next position, new context-dependent grouping → finished sentence hold → repeat. No arbitrary-position filling. Candidate red probability never becomes zero; the staged complete sentence includes at least one red selection.
- **[judgment] Main:** large word chips/candidate bars and a small key; explanatory prose may be absent. Use “설명용 예시” in a minimal source/key slot. Avoid hash jargon boxes, math rules, dense percentages and multiple simultaneous explanatory lanes. The “조금 더 자주” idea must be visible, not only spoken.
- E06/E07. Note: plain-language narration, reproducible grouping/detection rule, source distinction, short-output limits; no algorithm derivation. Token-chip/single animated exhibit,120sec. Local implementation/media format **slides decides**; preserve existing engine and keyboard navigation.
- Acceptance: local/offline playback; two complete loops; stable typography/no jumping sentence; pause/restart operable; inactive slide stops/pause; re-entry sensible; reduced-motion/print representative static frame; no red/green-only meaning (labels/selection marker also distinguish states). Note article stands alone without playback. No live API required.

### 15 — S13, gentle bias protects language choices (baseline p13)
- **Must, C12:** explicit **“초록만 고르면 문장이 어색해질 수 있다. 그래서 조금 더 자주 고른다.”** Wording may be shortened naturally. Do not guarantee no quality loss.
- **[judgment] Exhibit:** a simple before/after probability comparison (e.g. illustrative green mass50%→60%, red remains40%). Prefer this single comparison over the old four-word paired table plus large second panel. It should reinforce, not repeat the entire animation.
- E06. Main: tradeoff and picture; note: probabilities/normalization if useful, not mandatory formulas. Single finding exhibit,60sec. Acceptance: no always-green rule, no added6-step mechanism diagram, demo and note values agree.

### 16 — S14, coin question (baseline p14)
- **Must, C13:** heading asks **“앞면 확률이1/2인 동전을100번 던져서 앞면이70번 나올 수 있을까?”** Spaces and semantic wrapping are slides' judgment. Delete the current explanation, expectation, answer highlight and caution paragraph.
- **Prefer:** retain only the100-coin/70-head visual, enlarged as room permits; minimal encoding key if needed. Question + exhibit is complete. E09; note states fair independent setup and speaking pause. Single exhibit,40sec.
- Acceptance: no explanation restored to satisfy a template; S15 supplies the answer.

### 17 — S15, rare not impossible (baseline p15)
- **Must:** answer S14 plainly, then retain the exact Binomial(100,1/2) picture and70-or-more upper-tail value≈0.0039%. Main key states fair, independent100 tosses and labels axes/tail. E09.
- **[judgment]:** replace the slogan-like caveat footer with necessary setup in the key; put the distinction from “probability AI wrote it” in optional notes, since the main chart claims only a coin probability. No formula/long sum on slide.
- Figure-first,100sec. Acceptance: “70번 이상” stays distinct from “정확히70번”; chart not relabelled as real-watermark detection data.

### 18 — S16, delete (baseline p16)
- **Must, C14:** remove main and matching article. Do not create another limitations page. Any indispensable unique scope (scheme-specific detection, editing/length sensitivity) can become concise optional detail in S17's note; not a mandatory speech passage. E06/E09.

### 19 — S17, mathematical engineering payoff (baseline p17)
- **Must, C15:** start **“AI 작성글에 표식을 넣자”** and explicitly arrive at **“통계 문제”**. “정식화” → **“수학문제화”**. Replace “선택을 조금 기울이고” with **“확률에 bias를 추가하여 통계적 특성을 심는다”**, or naturally abbreviated equivalent preserving both bias and statistical property. Delete “실제 적용에는 공학과 가정 점검이 더 필요”.
- **[judgment] Exhibit:** one concrete chain: design goal → generation probabilities biased slightly → count green words / ask if that excess is unusual. Do not present an arbitrary-text detector or probabilities as posterior authorship. This is the earned answer to S08, not another abstract slogan.
- E06/E09; main short flow; note connects to null comparison and stores optional limits from retiredS16. Diagram-flow,70sec. Acceptance: source attribution, exact requested terminology, no deleted summary rephrased underneath.

### 20 — S18, section3 (baseline p18)
- **Must:** retain numbered divider03; **[judgment]:** simplify subtitle if needed to avoid another generic maxim. E01/E11. Section-slide,10sec.

### 21 — S19, AI helps test and propose ideas (baseline p19)
- **Must, C16:** title **“AI와 함께 더 많은 아이디어 시험하기”**; retain explicit **“AI도 아이디어를 낼 수 있다.”** Delete “확인은 반드시 따로”.
- **[judgment]:** revise the loop to “아이디어 → AI와 함께 구현·실험 → 결과를 보고 새 아이디어”, rather than keeping “독립적으로 확인” as the same policing message in a box. This does not say testing is unnecessary. Optional10-of10/7-of10 example may remain in notes, not clutter the main.
- E04/E11; main one loop and idea point, note source-backed viewpoint rather than exaggerated capability guarantee. Diagram-flow,60sec. Acceptance: AI participates in ideation, not only coding; deleted caution not resurrected.

### 22 — S20, personal meaning (baseline p20)
- **Must, C17:** delete **“이곳 영재원에서도, 그 뒤의 삶 전체에서도”**. Keep authentic contrast between useful techniques/problem practice and enduring meaning/intuition, E01/E11.
- **[judgment]:** fewer words and a personal voice; the existing formula→words→meaning exhibit may be simplified if redundant. No added childhood episode. Main one personal statement/exhibit; note concise reflection without requiring the deleted phrase.70sec.

### 23 — S23, AM–GM as growth intuition (baseline p21)
- **Must, C18:** remove the2×8/5×5 rectangle and numeric definition lesson. Assume AM–GM is known. Use the familiar multiplicative-growth interpretation in E10, not another elementary shape proof.
- **[judgment] Exhibit:** two symbolic growth paths from the same starting size: different positive factors a,b versus repeated mean factor m=(a+b)/2. Same two-period arithmetic mean, different final product; the steady path is at least as large. One compact inequality can anchor the idea; no numerical worked example.
- Natural point: **“평균 성장배율이 같아도, 들쭉날쭉하면 덜 성장한다.”** The two-step/positive/fixed-average setup must be visible, not a universal claim about life or investment. Growth factors, not ambiguous signed percentage rates. E10.
- Main one symbolic comparison and known inequality; note a short verbal explanation, optional identity only if genuinely useful, not a derivation lesson. Diagram-flow or math-block comparison,100sec. Acceptance: no rectangles/numeric plug-in, substantive intuitive interpretation, ready connection to log/Jensen.

### 24 — S24, direct log/Jensen comparison (baseline p22)
- **Must, C18:** directly compare **log((a+b)/2)** and **(1/2)log a+(1/2)log b**, with a,b>0 and ≥ in the correct direction. Use **concave**, not “오목”, for log. No general Jensen theorem/proof.
- **[judgment] Exhibit:** retain/adapt the large log curve and chord, labelled only a,b,(a+b)/2 and the two symbolic heights; delete visible2,8,log4,log5. Curve above chord; distinguish with line style as well as colour. E10 gives exact geometry.
- Main one curve/chord comparison plus the compact inequality; note verbal “average input versus average output,” one-sentence AM–GM link, source. Figure-first,110sec. Acceptance: the two expressions are immediately comparable, no crowding/overlapping long math labels, no extra proof or expectation notation.

### 25 — S21, closing takeaway (baseline p23)
- **Must, C19:** clearly close on **“수학을 직관으로 이해하기” → “그 직관을 현실 세계의 문제에 적용하기.”** Replace the old three-question checklist and “이해한 만큼, AI와 함께 더 많이 묻고 확인한다” summary.
- **[judgment] Exhibit:** one two-part relationship with an understated callback from watermark/AM–GM, not another full recap. E11. Main two actions, note answer to opening question in Albert's voice. Diagram-flow,70sec. Acceptance: understanding plus application, not only asking/verifying; no AI-exclusive-human intuition claim.

### 26 — S22, congratulations (baseline p24)
- **Must:** retain the warm congratulations/next-question closer; no contact/content appendix. E11. End-slide,30sec. Note brief, no invented story.

## 5. Work packages and shared surfaces

Packages define ownership, not a requirement to spawn workers. **[judgment] content/design/wording decisions are for slides itself**, not context-free implementation agents.

- **P1 — AI and engineering pivot:** S04–S08 in M and matching articles in N; E03 original vortex asset only. Depends on E02–E05 and shared S03/S09 transitions. May not edit P2/P3 slide sections.
- **P2 — Watermark case:** S10a/S10b/S25/S11–S15/S17, deletionS16, matching N sections, image parity inputs/outputs, local demo code/media; generator portions for image/coins/probabilities only. Depends on P1 S08 meaning, not its markup. Reuse E06 probability parameters consistently. Animation/assets are local to this deck; no reference/ or shared script edits.
- **P3 — Meaning and intuition:** S19/S20/S23/S24/S21 in M/N, log-figure portion of existing generator and its outputs. Depends on S17's real-problem connection. No elementary AM–GM teaching. Preserve factual personal source.
- **Shared, slides final integration only:** S01; deleteS02; S03/S09/S18/S22; all navigation/counts; all C06 wording; paired-note ordering/timing/heading consistency; talks/261128yonseimath/OUTLINE.md and relevant rootOUTLINE.md entries. Update renamed topics, lines and counts from actual output. Generator is shared between P2/P3: integrate changes once to avoid overwrites. Remove unused deck-local style/assets only if safe; no repository-wide cleanup.
- New local source files require provenance and regeneration instructions; no shared framework changes. If an asset or loop cannot be delivered as specified, report the concrete problem and alternative in work-r1 instead of silently shipping a static replacement for C11.

## 6. Acceptance and handoff

1. All C01–C19 covered with actual old→newpage/ID map; exact deletion strings absent from main. Structural deletions mirrored in N; matching unique IDs/order; no orphan article.
2. Verify source scope and captions: IMO standard, dated Navier–Stokes announcement, Tao paraphrase, hypothetical misuse, illustrative probabilities, source/modified image, AR≠dgMARK.
3. Render changed slides and neighbours at final presentation size; inspect image dominance, Korean line wraps, primary diagram labels, curve/chord math labels, footer clearance. No type shrinking, clipping, dense tables or added boilerplate.
4. Run lint/density/outline/whitespace checks; report inherited warnings separately. Notes readable at actual430 and1280 widths, including long log expressions. No KaTeX errors.
5. Reproduce image-parity tests and coin/log invariants. Record generated-input paths/values and source URLs. Animation test report covers two cycles, pause/restart, slide leave/re-entry, red selections, offline run, print/reduced-motion fallback and navigation. Inspect frames, not only source code.
6. Keep24-minute narration plan plus1minute buffer; target page count may change, but don't add technical depth or an extended safety/limitations section.
7. work-r1 names exact job-branch commit, mapping, deviations, source issues and checks. Copy planner files unchanged and refresh living files. Keep PR81 head frozen at baseline while unreviewed. After approval, final log-only push and conditional fast-forward delivery follow job.md. No new PR or merge.
