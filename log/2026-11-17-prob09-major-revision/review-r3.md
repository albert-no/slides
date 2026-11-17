# Round 3 review

- Job: 2026-11-17-prob09-major-revision
- Reviewed commit: **839fdc4708624a9838804f2f45a6ef5fb87be52a**
- Content commit: 029fc7483264a8db0af7aee75573f2b152a6a5b8
- Previous reviewed commit: 79b3163b79487e35b4b46963cee232b231f50941
- Baseline: b20ab73ac7e74e9489d379cf9caad7565f17e31e
- Verdict: **approved**. No open blocking findings.

## Result

The final local repairs pass. Approve the 86-slide revision, paired HTML lecturer notes and accessible Markdown edition under the approved 150-minute plan. The practical-proposal-first argument, just-in-time prerequisite recalls, estimator distinctions and example-led gradient section are retained. No further changes requested.

## Request coverage

| Comment | Status | Result |
|---|---|---|
| C01 | Done | prob09 deck and both companion-note editions revised and reviewed. |
| C02 | Done | Continuity with the frozen prob01-prob08 baseline audited; stale attribution corrected and redundant reteaching/calculations removed. Earlier decks were not edited. |
| C03 | Done | Major narrative, exhibit and notes revision, with current design-rule and rendering checks. Final deck is 86 slides versus baseline 113. Model names were context, not a reconfiguration request. |
| C04 | Done | Albert's approved scope, rigorous junior-undergraduate audience, six parts and 150-minute pacing respected. |

## Findings closed in this round

| ID | Slide / page | Type | Blocking now | Verified result |
|---|---|---|---|---|
| F01 | S109a / p84 | Design rule | No | Redundant highlight removed; conditions retained. Five-element body budget, normal 4px divider, no slide overflow and clear footer reserve. Note descriptions match. |
| F09 | HTML note S19 / p8, S116 / p15, S90 / p66 | Design rule | No | Hiding/scroll workaround removed; displays split into logical steps, matching Markdown. Summation limits, fractions and radicals are visible at 430px without reducing type. |
| F15 | S116 / p15 and both notes | Fact | No | Rare-event and sample-size qualifications, domain 0<rho<=1/2, distribution-level RMSE distinction and correct curve endpoints are synchronized. The introduction remains generic. E31 supports the calculation. |
| F16 | HTML note S109b / p85 | Fact / internal reference | No | Misleading Gaussian variance-comparison backward reference removed. |

F02-F08 and F10-F14 remain closed from round 2. No new findings or preferences.

## Independent checks

- Read the complete round-3 source diff in all three target files and work-r3. Changes are confined to the requested repairs and their synchronization; no changes to argument, sources, slide mapping, earlier decks, generators or shared design assets.
- Archived the exact reviewed SHA. Inspected Chromium renders of changed slides 15/84 and neighbours 14/16/83/85 at 1280x720; additionally checked p84 in the actual 86-page print PDF. S109a's divider is restored and the capacity defect is gone. The all-slide print-layout measurement reports no width/height overflow and zero KaTeX errors.
- Independently used actual device emulation, not an iframe approximation: mobile 430px has layout width 430 and visual scale 1. Also tested narrow desktop 430px and desktop 1280px after fonts/math loaded. No displayed equation has horizontal overflow; no overflow-hiding rule remains. Inspected S19/S116/S90 mobile screenshots, S90 narrow-desktop and S109a desktop notes. Mathematical lower limits and radicals remain fully visible. All mobile and full-desktop articles fit. The already accepted S115 half-pixel KaTeX-vlist edge produces a one-pixel narrow-desktop metric only, not a clipped glyph.
- Deck and HTML-note lint pass. Accessible Markdown has zero lint ERROR and is ASCII. Deck/HTML/Markdown have 86 unique IDs in identical order. No content or font-size reduction beyond the requested redundant highlight removal.
- Frozen plans, requests, evidence through E31, review-r1 and review-r2 match their tracked copies exactly. The content 029fc74 to reviewed 839fdc4 tail touches only this job's tracked log. Final approval-record push is still required before opening the PR.

## Plan decisions and next action

No new plan version or escalation. The S109a/b split remains accepted; total 86 slides and 150 minutes are unchanged in this round.

Slides: copy this review unchanged, refresh the living job files, and push the job branch. Return the exact pushed head in the normal one-line pointer. No further source edits are authorized by this approval. Slides-review will verify that every subsequent commit touches only `log/2026-11-17-prob09-major-revision/`, then open the PR against `main`.

Approval is pinned to 839fdc4708624a9838804f2f45a6ef5fb87be52a. It is not merge authorization. No PDF delivery is requested.
