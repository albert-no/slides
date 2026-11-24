# Evidence register — 2026-11-24-261128yonseimath-draft

Append-only. Literature selection cutoff: 2026-11-24 (the supplied brief). Primary-source checks performed during the Nov 24–25 planning turn. This is a focused evidence map for a ceremony talk, not a comprehensive watermarking survey. Check time-sensitive statements again before the final review for the Nov 28 talk. Labels use the pipeline taxonomy; a published announcement is not a certified theorem.

## E01 — Speaker and purpose
- Claim: Albert is a graduate of this program and a current Yonsei professor; occasion is the graduation ceremony, about 25 minutes.
- Source/version/locator: Albert's direct request C01, 2026-11-24; lab home https://ai-isl.yonsei.ac.kr/ , introduction and People/Albert No (accessed Nov 24–25).
- Label: illustrative example (speaker-supplied biographical context).
- Scope: user is authoritative for his own program attendance. Website confirms faculty/lab context, not an individual childhood memory. No invented alumni year, anecdotes, mentors, emotions or career causation.

## E02 — A dated competition result, not all AI
- Claim: an advanced Gemini Deep Think system obtained 35/42, solving 5/6 IMO 2025 problems; assessed at gold-medal standard.
- Source: Luong and Lockhart, Google DeepMind, 2025-07-21, “Breakthrough Performance at IMO 2025 with Gemini Deep Think”: https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/
- Label: published result (official developer report, with IMO president's confirmation).
- Setup: special advanced system, official problem set and grading criteria; distinguish this from ordinary public chatbot performance.
- Does not establish: a human contestant's medal was awarded to AI; all mathematics is solved; speed/rank superiority over every student.

## E03 — Navier–Stokes: announcement and recognition are distinct
- Claim: OpenAI announced an AI-produced Navier–Stokes proof on 2026-09-08; Clay issued a response on 2026-09-11 referring to a separate evaluation process.
- Sources/locators: OpenAI, introduction and “The result,” https://openai.com/index/navier-stokes-solution/ ; Clay, concluding paragraphs, https://www.claymath.org/news/navier-stokes-announcement/ .
- Label: published result (dated proof announcement only).
- Setup: OpenAI describes the forced breakdown alternatives C/D, not a blanket proof about all unforced fluids. No equation or technical claim is needed for this audience.
- Does not establish: this reviewer audited the proof, independent acceptance, a prize award, or current consensus. Main wording must be “AI를 활용한 해법 발표,” with “발표와 최종 인정은 별개.” Keep the dates. Do not convert a dated announcement into “완전히 해결됐다.”

## E04 — Text generation and green-list mechanism
- Claim: next-token sampling supplies a distribution; context-seeded candidate groups and a soft preference for one group leave a countable signal. Detection reuses the assignment rule.
- Source: Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein, “A Watermark for Large Language Models,” ICML 2023, §§1.1, 2–3, Algorithm 2, Eqs. (3)–(4); https://proceedings.mlr.press/v202/kirchenbauer23a.html and https://proceedings.mlr.press/v202/kirchenbauer23a/kirchenbauer23a.pdf .
- Label: published result.
- Scope: teaching example concerns autoregressive sampling and this watermark family. Tokens need not be words. Groups change with context, not fixed Korean word categories. Color denotes membership, not visible text ink. A secret-key variant should be identified as such; Algorithm 2 itself uses a previous-token hash.
- Does not establish: every AI uses this scheme, undetectable edits, perfect quality preservation, guaranteed fraction of green tokens, or a universal authorship detector.
- Canonical visual: Fig. 1 is a published mechanism/output illustration; use if it serves the specific panel. The proposed Korean lunch and coin examples are explicitly different, original teaching examples, not repainted paper results.

## E05 — Independent fair coins: exact calculation
- Claim: for K ~ Binomial(100, 0.5), mean 50 and standard deviation 5; K=70 is four standard deviations above the mean. P(K >= 70) = 0.00003925069822796835 = 0.003925069822796835%.
- Label: our calculation.
- Reproduction: Python 3 standard library, `sum(math.comb(100,k) for k in range(70,101))/2**100`; exact integer numerator before division. Computed during this planning turn.
- Setup: independent fair flips; one-sided event “70 or more,” not exactly 70 and not a two-sided tail.
- Does not establish: posterior probability of fairness or AI authorship; calibrated false-positive probability for real dependent text. Do not reuse the normal-tail approximation as the exact binomial value.
- Figure status: not generated. Planned plot inputs n=100, p=0.5, k=0…100; highlight k>=70, mark mean 50 and observation 70. Builder must retain the repo-local generator and report its path before review; append that actual path here after handoff. Main slide may omit the tiny numerical tail; notes retain exact calculation and z expression.

## E06 — Robustness is conditional
- Claim: editing can dilute watermark evidence, while some sufficiently long paraphrases remain detectable under evaluated conditions.
- Source: Kirchenbauer et al., “On the Reliability of Watermarks for Large Language Models,” ICLR 2024, abstract; https://proceedings.iclr.cc/paper_files/paper/2024/hash/d78e9e4316e1714fbb0f20be66f8044c-Abstract-Conference.html .
- Label: published result.
- Setup: human/machine paraphrase and mixing experiments. Do not import the paper's token/FPR numbers into the ceremony talk; they require a separate protocol explanation.
- Does not establish: robustness to every edit, guaranteed detection from short text, or a license to accuse an individual. A missing mark does not prove human authorship.

## E07 — SynthID is an application, not the same algorithm
- Claim: Google announced text watermarking integration in Gemini in May 2024. Substantial rewriting/translation can weaken the signal.
- Source: Google DeepMind, 2024-05-14, introduction and “The benefits and limitations of this technique,” https://deepmind.google/blog/watermarking-ai-generated-text-and-video-with-synthid/ .
- Label: published result (developer announcement).
- Setup: historical deployed-system motivation, not a claim about every current Gemini output. Do not copy the marketing diagram's probability label into the coin test.
- Does not establish: SynthID equals KGW green-list, all text can be detected, or all model configurations currently watermark. Optional one-line note only; not another method lesson.

## E08 — Social motivation, not a compliance lecture
- Claim: EU Article 50(2) specifies machine-readable marking/detectability for covered generated content; Korea Article 31(2) requires indication of generated origin by covered providers. Neither text mandates this green-list algorithm.
- Sources/locators: official Commission Article 50 text, paragraph 2, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50 ; Korean statute Article 31, version effective 2026-07-21, https://www.law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031810723 .
- Label: published result (primary legal text, narrowly summarized).
- Limits: scope, exceptions and technical feasibility matter. Main deck only says origin transparency is a social concern. Do not claim “모든 AI 글에 이 워터마크 의무.”
- Optional note source for EU dates: official FAQ “When do the transparency obligations of Article 50 become applicable?”, https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act ; it describes Aug 2, 2026 applicability and a limited Dec 2, 2026 transition. These dates are unnecessary on the main slide.
- Retrieval: supplied EUR-Lex URL yielded an anti-bot page; used the Commission's official text instead. Supplied Korea policy article R07 timed out twice; no claim relies on it.

## E09 — Explanatory illustrations, not observations
- Claim/content: “오늘 점심은…” with illustrative choices 40/30/20/10%; two group assignments; an imagined marked sequence. Labels must say “설명용 가상 예시.”
- Label: illustrative example.
- Source: attachment slides 09–10 (C13–C14); probabilities sum to 100 by construction. For mechanism correctness use E04.
- Limits: these are not measured model probabilities or tokenizer outputs. Do not assert the Korean food words are single tokens in a real tokenizer. Any before/after probabilities must normalize and come from the stated toy rule; do not imply a 50% vocabulary split forces 50% probability mass in every context.

## E10 — The talk's thesis is a viewpoint
- Claim/content: understanding assumptions, choosing questions and testing ideas remain useful with powerful AI. AI can also help with insight and formulation; no permanent human monopoly is claimed.
- Source: supplied brief C02, C10–C11, C17–C20; presented as the speaker's educational argument, not an experimentally established law.
- Label: illustrative example.
- Exhibit: question → toy experiment → check → next question, using the same coin example. No invented productivity percentage or “AI never understands” assertion. Any calculator/computer/AI sequence is an analogy of expanding tools, not a dated causal history.

## E11 — Audience caution
- Claim: Yonsei's regulation Article 4 primarily targets middle-school pupils and permits high-school pupils in the mentorship course.
- Source/version/locator: 과학영재교육원규정, revision 2026-09-18, Article 4, https://rules.yonsei.ac.kr/regulations/540df075-c271-43ed-a69e-7470589b62c2 .
- Label: published result (institutional rule).
- Does not establish: the exact guest composition at this ceremony. Middle-school-accessible design is our cautious inference, subject to Albert's confirmation. Do not print a school-grade claim on the title slide.

## E12 — Remaining brief references and reuse
- R08 https://www.3blue1brown.com/lessons/gpt/ was accessible (Grant Sanderson, 2024-04-01; “What is a GPT model?” and “Tokens”). It is a visual teaching reference only, not needed as scientific authority; E04 supports the mechanism. No frame/assets licensed or downloaded for reuse yet.
- Repository reuse at frozen baseline: `courses/trustworthy-ai/lec11-synthetic-media.html`, S15–S20 (token sampling, grouping, count, threshold); `courses/privacy/lectures/06-watermark/OUTLINE.md`, §§02 and 06. Adapt the concepts to Korean and this new audience; do not copy a 90-minute lecture or its “no activities” constraint. New local slide IDs are independent of lecture IDs.
- Label: unresolved for external visual licensing and final figure selection. Resolve in stage 4 / builder handoff; no missing figure becomes a factual placeholder in the shipped talk.

## E13 — Personal reflection now directly supplied
- Source: C24, Albert, 2026-11-25 00:08 Asia/Seoul.
- Claim: throughout his life, including the gifted program, training to understand mathematics verbally was valuable; techniques and solving exercises helped, but intuition about mathematical meaning was especially important.
- Label: illustrative example (speaker's own autobiographical reflection).
- Scope: this supplies a truthful personal ending, not a specific childhood incident. Candidate math examples below are teaching illustrations, not events Albert says he experienced. This updates E01's previous absence of personal reflection.
- C25 removes the need for detailed formulas, including mandatory formula appendices in notes. Keep verbal explanations and factual caveats; audit calculations remain in this evidence register, not required lecture content.

## E14 — Candidate A: area growth as a boundary strip (preferred)
- Label: our calculation / illustrative example.
- Claim: for a circle, the rate of change of area with radius is its circumference. Intuition: a small increase in radius adds a thin annulus, approximately a strip whose length is the old circumference and width is the radial increase.
- Verification: for r>0, h>0, A(r+h)-A(r)=2*pi*r*h+pi*h*h. The first-order term is circumference times h; the error is pi*h*h and vanishes relative to 2*pi*r*h as h/r tends to zero.
- Proposed main wording: “아주 조금 키울 때: 넓이 증가 ≈ 둘레 × 반지름 증가.” No derivative notation or derivation needed. Do not depict an annulus as an exactly rectangular strip at finite thickness. The example illustrates why two familiar formulas connect; it is not an autobiography.
- Figure status: proposed only, not generated. Inputs and generator path will be registered if selected. One circle → thin outer band → approximately unrolled strip, as a controlled sequence or one conceptual exhibit.

## E15 — Candidate B: mean as a balance point
- Label: our calculation / illustrative example.
- Data: equal masses at 2, 4, 9 on a number line; arithmetic mean 5. At fulcrum 5 the left moments are 3+1 and the right moment is 4, so net moment is zero. General statement requires equal weights, or a weighted mean when weights differ.
- Proposed main point: “평균은 더해서 나누는 값이면서, 같은 무게의 점들이 균형을 이루는 위치다.” Values need not be symmetrically paired; mean is not the median or the midpoint of extremes.
- Extension: moving the point at 9 further right shifts the balance point right, explaining outlier sensitivity without a separate formula.
- Figure status: proposed only, not generated.

## E16 — Candidate C: equal proportions, unequal evidence
- Label: our calculation / illustrative example.
- Setup: independent fair flips, one-sided upper-tail comparison. Seven heads out of ten and seventy out of one hundred have the same observed proportion but different tail probabilities under the null.
- Exact calculation: P(Binomial(10,.5)>=7)=176/1024=0.171875; E05 gives P(Binomial(100,.5)>=70)=0.00003925069822796835. Reproduce with sum(comb(n,k) for k in range(ceil(.7*n),n+1))/2**n for n=10,100.
- Proposed main point: “같은 70%여도, 관찰 횟수가 다르면 증거의 힘은 다르다.” This is a specific example, not a claim that every larger sample must provide stronger evidence regardless of its outcomes/dependence.
- Use only if choosing a callback to the watermark core; do not add all three candidates to a 25-minute ending. No tail numbers needed on the slide.

## E17 — Audience and execution authorization, superseding E11's inference
- Source: Albert C27, 2026-11-25 00:23 Asia/Seoul.
- Label: illustrative example (author-supplied audience brief).
- Audience is middle-school students capable of understanding university-level mathematics. Do not equate their age with a low conceptual ceiling. Albert requests a higher-level example such as AM–GM or Jensen and explicitly orders drafting first, discussing examples after the draft.
- Decision: proceed with the 25-minute structure, using two linked AM–GM/Jensen pages as a revisable example. Do not ask for another example-selection approval. E14–E16 remain candidate history, not build requirements. C25 still rules out detailed derivations; a meaningful compact inequality is appropriate.

## E18 — Jensen and the AM–GM connection
- Label: published result.
- Source: Boyd and Vandenberghe, Convex Optimization, 2004, §§3.1.8 “Jensen's inequality and extensions” and 3.1.9 “Inequalities,” pp. 77–78; https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf . Also authors' revised slides, “Jensen's inequality,” PDF page 58 (zero-index 57): https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf .
- Claim: convex functions lie below their chords; concave functions reverse the inequality. Applying the concave form to log on positive arguments yields two-variable AM–GM. Positive a,b suffice; equality occurs at a=b because log is strictly concave.
- Limits: not every function is convex/concave on the domain of interest; not a universal claim that equal allocation is best for every objective. The two-point log example is the chosen illustration, not a proof of the full random-variable theorem.

## E19 — Fixed-sum numerical example and exact graph
- Label: our calculation / illustrative example.
- Inputs: two positive quantities with a+b=10. Compare (a,b)=(2,8) and (5,5): products 16 and 25; arithmetic means both 5, geometric means 4 and 5.
- Invariant: ab=25-(a-5)^2 for b=10-a, 0<a<10. Equalizing increases the product toward its unique maximum 25. Main slide need not show this identity.
- Log graph: f(x)=ln(x), domain [1,9]. Chord endpoints (2,ln2),(8,ln8). At x=5 its midpoint height is (ln2+ln8)/2=ln4, below the curve value ln5. f''(x)=-1/x^2<0 proves the curve remains above the chord on [2,8], not just at sampled points. Transform and endpoints must be retained in the generator; both axes use the same mapping for curve and chord.
- The log inequality is one compact statement with a,b>0; no multi-line derivation is required. Connecting it verbally to AM–GM uses the monotonicity of log and its product rule.
- Generated-figure status: not generated. Planned repo-local generator: talks/261128yonseimath/figs/generate-figures.py, owned/written by slides, for these figures and the E05 coin plot. Append actual path/commit after handoff. Rectangles may be original teaching exhibits; do not relabel published data. Chord geometry here is our exact log example, not the existing prob01 parabolic illustration.

## E20 — Reproducible four-choice probability illustration
- Label: our calculation / illustrative example. Refines E09's unspecified before/after values for a complete first draft.
- One context only: “오늘 점심은…” with candidate word-labels 김밥, 라면, 국수, 샐러드. These are conceptual choices, not outputs of an actual tokenizer/model. Original probabilities: 0.40, 0.30, 0.20, 0.10. Mark 김밥 and 샐러드 for this context.
- Multiply marked probabilities by 1.5, then normalize all four by 1.25: resulting probabilities 0.48, 0.24, 0.16, 0.12. Marked mass changes from 0.50 to 0.60. Counts are not promised to equal these proportions in a finite sample.
- Half of the candidate list being marked does not generally imply half of the probability mass; this toy setup deliberately has both. At another context the assignment changes. Do not mark aggregate “other” as if it were a single token.
- Mechanism source remains E04; the specific numbers and Korean labels are ours. No sampling or model query was conducted. Generator path planned as in E19; exact parameters must stay with the generated comparison figure.
