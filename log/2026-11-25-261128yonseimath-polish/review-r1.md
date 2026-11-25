# Review r1 — 2026-11-25-261128yonseimath-polish

- Reviewed commit: **d336d86387cde991e12f4721b55c897579b2a193** (content 9bf53d8).
- Baseline: **37757bb365a74b434a65a0ec0f6d86d40c9b253a**.
- Verdict: **revise**. Round 1 of 2; next pass is the final correction review.
- Priority: fix the Jensen midpoint label collision, then make the S12/S24 notes agree with the correct visual mathematics. No argument, timing or broad layout redesign is requested.

## What to keep

The engineering pivot and image → word choice → soft bias → statistical question sequence now explain why mathematics matters for a real task. The large AR animation works offline, genuinely loops, and includes a red selection; preserve it. The symbolic growth interpretation is a suitable step up from the removed elementary rectangles. The prose is substantially more natural and the requested deletions are covered.

## Coverage

“Done” addresses the author request, not exemption from the specific corrections below. Pages are revised pages at the reviewed commit; the complete old/new mapping in work-r1 is verified.

| Comment | IDs / revised pages | Status |
|---|---|---|
| C01 | S02 retired | Done: no Contents page |
| C02 | S04 / 3 | Done: requested heading, score/system qualification, no problem grid |
| C03 | S05 / 4 | Done: English name, Millennium problem, original OpenAI vortex, no verification diagram |
| C04 | S06 / 5 | Done: three research questions and correctly labelled Tao paraphrase |
| C05 | S07 / 6 | Done: requested label and removals |
| C06 | S08 / 7 and subsequent sections | Done: engineering framing and natural-language cleanup |
| C07 | S09 / 8 | Done: watermarking spelled out |
| C08 | S10a–S10b / 9–10 | Done: motivation before hidden-mark objective |
| C09 | S25 / 11 | Done: matched image pair and exact parity example |
| C10 | S11 / 12 | Done: ChatGPT/LLM next-word distribution and learned contextual patterns |
| C11 | S12 / 13 | Animation done; note precision pending F02 |
| C12 | S12–S13 / 13–14 | Done: soft bias rather than forcing green |
| C13 | S14 / 15 | Done: question and coins only; answer on S15 |
| C14 | S16 retired | Done |
| C15 | S17 / 17 | Done: mathematical formulation → statistical question, requested wording |
| C16 | S19 / 19 | Done: AI can suggest ideas, no deleted checking slogan |
| C17 | S20 / 20 | Done: deleted phrase absent |
| C18 | S23–S24 / 21–22 | Content done; Jensen rendering/note pending F01/F03 |
| C19 | S21 / 23 | Done: intuition → application to real-world problems |

## Findings / self-contained change requests

### F01 — Blocking: Jensen midpoint label is covered
- **Type:** design rule. **ID/page:** S24 / 22.
- **File:** `talks/261128yonseimath/261128yonseimath.html`, lines 531–541, especially midpoint label line 538 and inequality block line 541.
- **Observed:** the denominator 2 of the x-axis label `(a+b)/2` runs into the gray inequality block and is partially covered in the 1280×720 render. The midpoint label is essential to comparing the two heights, so this is not harmless empty-space tuning.
- **Fix [judgment]:** give the complete midpoint label clear separation from the inequality block. Reposition/rebalance the exhibit, or use an equally legible inline `(a+b)/2` axis label. Keep the symbolic comparison, positivity qualifier, graph geometry and existing type sizes; do not shrink text to fit.
- **Acceptance:** render page 22 at final size and inspect the entire midpoint label plus the inequality/citation; no overlap or clipping. Recheck neighbours 21 and 23.

### F02 — Blocking: the S12 note overgeneralizes its first-step probabilities
- **Type:** fact (also the explicit random-partition wording in C11). **ID/page:** S12 / 13.
- **File:** `talks/261128yonseimath/261128yonseimath-note.html`, lines 197–208, especially 201 and 208. Source: E06 and the actual `figs/watermark-demo-data.js`.
- **Observed:** the data paragraph presents “40→48, 10→12 (초록), 30→24, 20→16 (빨강)” without limiting it to the first green assignment. The second position has different green candidates and correctly renders 32/36/24/8. The spoken explanation also says only “나눕니다,” omitting C11's random/pseudorandom nature; the deterministic demonstration must not be mistaken for choosing green words by meaning.
- **Fix:** qualify the quoted numeric transformation as **“첫 번째 자리에서는”**. If describing the second position, use `친구와 40→32, 혼자 30→36, 가족과 20→24, 급하게 10→8`; both positions still have green mass 50→60%. Preserve the correct demo data and the statement that this is a fixed illustrative sequence, not an actual sampled ChatGPT output. In work-r2, likewise distinguish the first-step example from the general multiplier/normalization rule; do not edit frozen work-r1.
- **Fix [judgment], one spoken sentence only:** after “초록과 빨강 두 묶음으로 나눕니다,” add the substance **“문맥을 바탕으로 무작위처럼 나누되, 같은 문맥에서는 같은 묶음이 나오게 합니다.”** Keep technical hashing details out of the main slide. This is the source-backed mechanism; the displayed example may remain staged.
- **Reason:** the instructor note must agree with the actual candidate table and explain why the grouping can be reconstructed for statistical detection (DS §9; Kirchenbauer et al., §3.1 Algorithm 2).
- **Acceptance:** the note's short explanation and data paragraph agree with all four tables; no change to the correct visual probabilities is necessary.

### F03 — Blocking: Jensen's short note drops equality
- **Type:** fact. **ID/page:** S24 / 22.
- **File:** `talks/261128yonseimath/261128yonseimath-note.html`, line 328 (`.msg`).
- **Current → new:** the general claim “…함수값의 평균 …보다 크다” → **“…함수값의 평균 …보다 크거나 같다.”** Start with **“양수 a, b에 대해”** (or equivalent) and retain the positive-domain assumption. The later explanation already uses ≥ correctly; keep it consistent. Equality occurs at `a=b`.
- **Reason:** the main slide explicitly allows `a=b`; its short note currently asserts a false strict inequality for that case. Assumptions cannot disappear from the short message (DS §9; E10).
- **Acceptance:** the short message, main formula and source/detail agree, including the equality case; render the revised note at narrow width.

### F04 — Nonblocking: hide inactive controls in static mode
- **Type:** preference. **ID/page:** S12 / 13.
- **Files:** `talks/261128yonseimath/figs/watermark-demo.js`, lines 119–121 and 131–137; corresponding local demo control styling in `talks/261128yonseimath/261128yonseimath.html`.
- **Observed:** with `prefers-reduced-motion: reduce`, the correct static frame is shown, but “일시정지” and “처음부터” remain visible with no handlers. Clicking does nothing (it does not navigate the deck).
- **Suggestion [judgment]:** hide those controls in the static fallback, as already done for print, or explicitly disable them. Do not enable forced playback against the reduced-motion preference.
- **Reason:** a static exhibit should not advertise unusable playback controls. The fallback itself meets the requirement, so this does not block approval.

## Review checks

- Read Albert's C01–C19 first, checked the primary sources/calculations, then DS and plan-v1. Reviewed only the named commit through git and an exact `git archive` extraction.
- All 24 main pages inspected at 1280×720, including enlarged inspection of the revised AM–GM/Jensen and live-demo pages. Main/note contain the same 24 IDs in the same order; headings, page mapping, outline and 24-minute pacing plus 1-minute buffer agree.
- Main and note lint pass; wordy/dense checks return no flags; `git diff --check` clean. No missing images or KaTeX errors. Actual note layouts at widths 430 and 1280 have no horizontal article overflow. Visual review, not lint, caught F01.
- Two offline animation cycles observed, including changing candidate groups, soft probability changes, the red pick, sentence accumulation, completion hold and restart. Pause/resume, restart, inactive-slide stop and re-entry tested. Reduced-motion still is correct; F04 records the remaining control presentation issue.
- Local generator rerun is byte-identical. Stored-image parity, max intensity difference, all four toy distributions, binomial tail and log/chord geometry independently checked. E12–E13 append the actual artifact details and calculations.
- Tao's Math 2.0 and the watermark primary paper support the attributed content; the NASA source page supports the image provenance. OpenAI vortex hash matches the verified original source asset. No invented quote or real ChatGPT-output claim found.
- Target leaf/root outline references are current. Global outline lint in the extracted review environment still reports the pre-existing absolute-path issue in `courses/trustworthy-ai/OUTLINE.md:332` and five unrelated inherited ambiguity warnings; these are not findings for this job.
- `requests.md`, `evidence.md` (before this review's append) and frozen `plan-v1.md` match the tracked copies exactly. Diff scope is the target talk, its outlines and this job's log; no shared engine/design-rule edits.

## Plan decisions and next round

Accept the reported wording, local centring, original-image treatment and chosen four-word sentence. No plan change: all preserve the required argument and teaching time. F01 is a rendering correction, not rejection of the S24 concept.

Proceed with F01–F03 only, plus F04 if desired. Return an exact `work-r2.md` pointer on the same job branch. Recheck changed slides and their neighbours, plus corresponding note articles and any changed demo behaviour; do not redesign or audit unrelated decks. Keep PR81's old head frozen until approval/final log-only verification. No merge or PDF delivery is authorized.
