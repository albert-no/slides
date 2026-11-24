# Review r1 — 2026-11-24-261128yonseimath-draft

- Reviewed commit: `fae496e1a58dcd6dc196dddf1b7018dfaf43303b`.
- Baseline: `95df062f8f980c686f0ef45974ebd3f626ff79d2`.
- ID-only commit: `1e7b5b90af65f688aa078aefb784c869ae572a8b` (verified: only 24 slide + 24 matching article attributes).
- Verdict: **revise**. Round 1 of 3 complete; F01–F05 block. F06–F07 are optional, slides' call.
- Scope: first full pass of all 24 pages and 24 note articles. Plan-v2 remains the work order.

## What matters

1. Restore the prescribed primary-label size in the custom diagrams. The work report's claim that 1.5rem is at least body size is incorrect; DS body is 1.55rem. This is not a request to enlarge every annotation indiscriminately.
2. Keep the carefully bounded story equally bounded in the spoken script: no guaranteed invisibility/detection, and no unsupported present-tense claim about mathematical consensus.
3. Preserve the AM–GM → log/Jensen pair; the geometry and conceptual connection work. Make the fence analogy explicitly about rectangles.

The argument is coherent, the Korean slides are uncluttered, the toy distributions normalize, and the independent-fair-coin tail and Jensen geometry check out. The personal reflection is a faithful paraphrase of C24, not an invented incident. No additional confirmation gate is needed before completing the draft; Albert remains the final check at the PR.

## Findings and self-contained changes

All line numbers below refer to the reviewed commit. Wording alternatives marked [judgment] preserve the required mathematical/source boundary; slides handles the wording directly.

### F01 — Primary diagram labels below the design floor
- **Where:** `talks/261128yonseimath/261128yonseimath.html`, local styles lines 26, 35, 48, 52, 62, 66–67, 76; S04/p4, S10/p10, S11/p11, S12/p12, S13/p13, S15/p15, S19/p19, S23/p21, S24/p22.
- **Type:** design rule. **Blocking:** yes.
- **Problem/reason:** custom important text is set to 1.4–1.5rem (and S13's before-probabilities to 1.3rem) instead of body size. In particular the four-box/two-row overrides explicitly reduce type to fit. The comparison's probabilities, grouping/loop boxes, sample text and main mathematical labels are content, not optional source tags. DS §1 Priority 0 and §8 distinguish primary labels from smaller ticks/annotations.
- **Fix:** restore primary content to at least the canonical body size and primary diagram-label weight; retain smaller genuine secondary ticks/legend annotations only where DS permits. Simplify or redistribute if needed, without shrinking prose or vertical rhythm. [judgment] Layout is yours. Correct the size assessment in work-r2 rather than changing frozen work-r1. Render every page affected by the shared styles at final size and recheck neighbours/footer clearance.

### F02 — Watermark wording promises too much
- **Where:** `talks/261128yonseimath/261128yonseimath-note.html`, S13/p13, lines 187 and 192; matching main file `talks/261128yonseimath/261128yonseimath.html`, line 353.
- **Type:** fact. **Blocking:** yes.
- **Problem/reason:** “한 문장만 보면 아무도 눈치채지 못할 정도” guarantees invisibility to every reader; “많이 쌓이면 보인다” can also read as a finite-text detection guarantee. The numbers in this invented example and E04 do not establish either. The later caveat in the source layer does not repair the spoken guarantee (DS §9).
- **Fix [judgment]:** replace the two script sentences beginning “한 문장만 보면…” with, for example, “한 문장만 보고 이런 작은 차이를 판단하기는 어렵습니다. 충분한 조각을 모으면 표시 묶음이 더 자주 선택되는 경향을 통계로 찾을 수 있습니다.” Make the message layer and the main line consistent, e.g. “길게 모아 통계로 찾는 흔적.” Retain the explicit quality trade-off, probabilistic selection and S16 limits. No new experiment or extra slide needed. Evidence: E04/E23.

### F03 — Restrict the fence analogy to rectangles
- **Where:** `talks/261128yonseimath/261128yonseimath-note.html`, S23/p21, line 308.
- **Type:** fact. **Blocking:** yes.
- **Problem/reason:** the preceding sentence is about rectangles, but “둘레가 같은 울타리로 가장 넓은 땅을 두르려면 정사각형…” drops that constraint. A square is not the area maximizer among all planar shapes. This example is specifically teaching why assumptions matter.
- **Fix:** current sentence → “둘레가 같은 **직사각형 울타리 중에서는** 정사각형으로 둘렀을 때 넓이가 가장 큽니다.” Keep the main slide, rectangle geometry and AM–GM/Jensen argument; they are correct. Evidence: E18–E19, fixed positive side-sum calculation.

### F04 — Dated announcements do not establish current community status
- **Where:** `talks/261128yonseimath/261128yonseimath-note.html`, S05/p5, lines 85 and 89.
- **Type:** fact. **Blocking:** yes.
- **Problem/reason:** “아직 남은 최종 인정 단계” and “지금은 … 수학계가 최종적으로 인정했다는 것은 아닙니다” turn two dated source statements into a current assertion about the whole mathematical community. Clay describes its prize-evaluation/credit process, which is not identical to community consensus. No fresh consensus survey is needed for this talk.
- **Fix [judgment]:** line 85 → “셋째 상자는 발표와 구분되는 별도의 인정 절차를 뜻합니다.” Replace the first sentence of line 89 with “이 두 발표를 인용한다고 해서, 별도의 심사나 상금 수여까지 끝났다는 뜻은 아닙니다.” Retain the dated main slide, the announcement/recognition distinction, and the source-layer C/D qualification. Do not add an unverified present status. Evidence: E03/E23.

### F05 — Citation lines and the IMO source label
- **Where:** `talks/261128yonseimath/261128yonseimath.html`, S04/p4 line 174 and S05/p5 line 192; `talks/261128yonseimath/261128yonseimath-note.html`, S04/p4 line 77.
- **Type:** design rule / fact. **Blocking:** yes.
- **Problem/reason:** S05 puts both sources on one citation line, contrary to DS §6's one-line-per-citation rule. S04 presents the DeepMind page's subheading as its article title; that mismatch originated in my E02, now corrected by E22.
- **Fix:** give the OpenAI and Clay citations separate dedicated lines, preserving dates and footer clearance. Use the official title from E22 in the note. On the main slide, either use that exact title if it fits intact or a clearly shortened descriptive reference without presenting the subheading as the full article title. [judgment] Keep the rendered citation readable; do not shrink it or wrap a title arbitrarily. No result/score change.

### F06 — Clarify visual appearance versus knowledge of the grouping rule
- **Where:** `talks/261128yonseimath/261128yonseimath-note.html`, S12/p12 line 178.
- **Type:** preference (wording clarification). **Blocking:** no.
- **Current → suggested [judgment]:** “그래서 글만 봐서는 어떤 단어가 표시된 것인지 알 수 없습니다.” → “단어의 겉모양에 표시가 붙는 것은 아닙니다. 문맥과 같은 규칙을 이용해 표시 묶음을 다시 계산해야 합니다.”
- **Reason:** avoids suggesting that context dependence itself makes assignment secret. The basic cited Algorithm 2 is computable with the text and rule; the main slide already explains this correctly. No need to introduce cryptographic keys or change the algorithm. E04/E23.

### F07 — Optional shortening of arithmetic in the note
- **Where:** `talks/261128yonseimath/261128yonseimath-note.html`, S15/p15 lines 225–226 and S19/p19 line 281; associated pointers in `talks/261128yonseimath/OUTLINE.md`.
- **Type:** preference. **Blocking:** no.
- **Suggestion [judgment]:** the arithmetic is correct, but C25 asks for no detailed formulas. Consider retaining the model, tail value, verbal interpretation and reproducibility pointer while dropping the z expression and long inline sum chains from the instructor note. Evidence.md already preserves the calculation. Do not cut assumptions or uncertainty qualifiers. If retained, these are source-audit details, not additional spoken teaching time.

## Request coverage

“Partial” below means a bounded correction above, not a missing section. Initial attachment instructions superseded by C01/C24/C25/C27 are assessed under the later direct instructions.

| Comment | Status | Evidence in draft / remaining action |
|---|---|---|
| C01 | done | Requested folder; Korean deck/note; alumnus/professor context; 25-minute budget |
| C02 | done | Three linked messages; expansion rather than defensive human superiority |
| C03 | done | Visual-first; advanced middle-school audience corrected per C27 |
| C04 | done | 24 minutes content + 1 buffer; original 30-minute timing superseded |
| C05 | done | S01 opening question and S22 warm close |
| C06 | partial | S04 35/42, 5/6, advanced-system/gold-standard qualifiers correct; F05 source label |
| C07 | partial | S05 dated research example, no prize assertion on slide; F04 note scope, F05 citation |
| C08 | done | S06 explicitly distinguishes answer from understanding, without devaluing either |
| C09 | done | S07 tool analogy; not an invented historical causal result |
| C10 | done | S08 understanding → formulation → checking |
| C11 | done | S08/S17 coin/mark connection makes reframing explicit |
| C12 | done | S10 origin motivation, limited legal cue, no universal algorithm mandate |
| C13 | done | S11 fictional normalized next-token example, token definition, repeated generation |
| C14 | partial | S12 shared/contextual rule, S13 soft bias and normalization; F02 certainty wording |
| C15 | done | S14 exactly 70/100; fair/independent model and audience pause in script |
| C16 | done | S15 correct one-sided tail and non-posterior interpretation; formulas revised under C25 |
| C17 | done | S17 local abstraction recap, practical assumptions acknowledged |
| C18 | done | S19 question/AI implementation/independent check/revised question loop |
| C19 | done | S20 uses C24; no invented childhood episode or placeholder |
| C20 | done | S21 single global takeaway; S22 congratulations |
| C21 | partial | Primary sources traceable and refreshed; F05 bibliographic correction |
| C22 | partial | System/model/toy/real-text limits mostly careful; F02/F04 spoken wording |
| C23 | partial | Figures, two questions, companions and exact mapping supplied; F01 font rule |
| C24 | done | Faithful personal reflection in S20 and note |
| C25 | done | No detailed formula lesson in spoken core; one compact inequality per example page; F07 optional audit-detail reduction |
| C26 | partial | S23/S24 conceptual example works; F03 local rectangle qualification |
| C27 | done | Advanced audience; complete AM–GM/Jensen draft without another approval gate |

## Verification and boundaries

- Reviewed exact-SHA source, diff and extracted render, not a working tree. Changed paths are within the authorized talk, root outline entry and this job record. Plan-v1/v2, requests and evidence were copied unchanged.
- Ran main/note lint, wordiness and density checks: clean. Target leaf outline: clean. Full outline lint in reviewer scratch reports one unrelated pre-existing absolute-path pointer (`courses/trustworthy-ai/OUTLINE.md` → `/workspace/agent/lec09/r4/build_deck.py`) plus five warnings; it is outside this change and not a request to repair unrelated files.
- Rendered all 24 pages from the snapshot and inspected the entire sequence plus full-size key figures/citations. No main slide overflow, broken image or KaTeX error. Graph shape/point positions, 70 filled circles, scale-preserving rectangles and paired probabilities verified.
- Independently tested notes at actual `innerWidth=430` and 1280, unlike work-r1's reported 500-wide browser. No article or displayed-math horizontal overflow at either width; inspected S05/S12/S15/S19/S23/S24 note views. Offscreen accessible MathML and SVG-path bounding boxes are not visible overflow findings.
- All 24 note IDs match display order. Pacing totals 24 minutes plus buffer. Four generated SVGs reproduce exactly; inputs/code path now recorded in E21.
- Primary IMO, OpenAI/Clay, watermark paper, reliability, SynthID and legal sources were re-opened; E18's primary textbook locator and the analytic calculations support AM–GM/Jensen. No claim of independently auditing the Navier–Stokes proof.
- Accept implementation choices: one integrated package, SynthID only as an optional note, and S19's short 10-flip comparison within existing time. No argument/scope/time change and no new plan version required.

## Next handoff

Address F01–F05, report whether F06/F07 were taken, and refresh the leaf outline if lines change. Recheck changed pages and neighbours; no new whole-deck content audit requested. Keep the 25-minute scope and stable IDs. Push work-r2 with exact SHA and copied review/living files. PR creation stays with slides-review after approval; no merge or PDF delivery authorized.
