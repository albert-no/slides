# Review r1 — Korean lecture companions

- Reviewed commit: `6d067ac53c346d0cc7c6a4441cc0ca69537c371f`.
- Frozen baseline: `3dd5a996afc0c89f47573cf9bbb330336a097948`.
- Branch / PR: `2026-11-27-lec14-focused-overview` / #84 (continuation, no duplicate PR).
- Verdict: **revise**. Round 1 of 2; next is the final review round.

## What matters

1. The two reading experiences are substantially complete and genuinely different. Keep the detailed 111-article explanations, connected G0–G7 argument, clear optional appendix, and careful teacher/learner/judge and denominator distinctions. The new title works.
2. Repair a handful of new explanatory overstatements and contradictions: an approval can examine pricing when given the evidence; no weight update does not mean every effect disappears at session end; active comparison groups are still controls; Hammond's taxonomy is not this appendix's three-paper grouping.
3. Make the two final standalone files accessible to the reviewer. The supplied worktree path does not exist in this container, so their hashes and offline behavior cannot yet be independently verified or the files delivered.

No restructure, new research, slide compression, or expansion of the English deck is requested.

## Request coverage

| Comment | Status | Evidence / remaining work |
|---|---|---|
| C01 better title | done | Main title/subtitle and companion/index title surfaces updated; title renders fit. |
| C02 complete Korean notes | substantially done, not yet accepted | All 59 main + 52 optional backup entries read; correct ID/order mapping. F01–F04/F06 address meaning; F07 is required delivery verification. |
| C03 slide-by-slide explanations | done structurally; local corrections pending | 111 unique articles and anchors, original page labels, exhibit readings and sources. F02/F03/F05/F06. |
| C04 full flow and background | substantially done, not yet accepted | Independent guide with G0–G7, optional B1–B6, terms, sources, mapping; F01–F05 correct prerequisite definitions and transitions. |

## Findings

Line numbers below are at the reviewed commit. Each requested wording change is local. `[judgment]` means slides should integrate the wording itself, retaining the precise distinction; equivalent natural Korean is welcome.

| ID | Slide ID / page or chapter | Type | Blocking | Problem → fix |
|---|---|---|---|---|
| F01 | S58a–S59 / main 13–15; guide G1 | fact | yes | Guide says neither approval nor spending cap can inspect pricing → preserve informed approval's role and distinguish the purchase-gate coverage gap. |
| F02 | S71 / main 31; guide G2 | fact | yes | No weight update becomes automatic disappearance of all effects → limit the contrast to weights, not session lifetime or system memory/actions. |
| F03 | S36a / main 42; guide G2 | fact | yes | Control group defined as receiving no treatment → include active training controls used in this lecture. |
| F04 | S25 / backup 28; guide B3 | fact | yes | Hammond's three categories conflated with the lecture's three kinds of evidence → separate the two groupings. |
| F05 | S60 / main 16, S35 / main 41; guide G7 | unmet request | yes | Section introductions/closing reference the wrong or missing material → restore the actual three-story flow. |
| F06 | S39a / main 49 | fact | yes | “Not proof” translated as “not evidence” → retain the difference between a useful signal and a conclusive demonstration. |
| F07 | Both standalone exports | unmet request | yes | Reported files inaccessible from shared reviewer mounts → provide accessible final files and fresh hashes. |
| F08 | main 9, 30, 51; backup 48; guide G0 | preference | no | Minor Korean polish; optional, not grounds for another round. |

### 1. F01 — informed approval can evaluate the proposed price [judgment]
- File: `courses/trustworthy-ai/lec14-agentic-threats-guide-ko.html`, G1, line 131 (main 13–15 / S58a–S59).
- Current: `승인은 구매를 보고, 지출 한도는 금액을 보며, 둘 다 가격 판단 자체는 보지 못합니다.`
- Replace with: `지출 한도는 주문 금액을 제한합니다. 구매 승인에서는 원가와 판매 예정 가격 같은 근거가 함께 제시되어야 가격 손실을 검토할 수 있습니다. 다만 이미 재고가 있는 상품의 가격 변경은 구매 관문을 거치지 않을 수 있습니다.`
- Keep the preceding statement that safeguards do not replace one another and the explicit “강의의 설계적 추론” label.
- Reason: the current sentence contradicts G1's own preceding bullet and S58a's proposed evidence-bearing approval. E02/E08 and the frozen S58a explanation distinguish what the reviewer sees from which actions reach that reviewer; neither establishes measured effectiveness.

### 2. F02 — distinguish weight updates from persistent system effects [judgment]
- File: `courses/trustworthy-ai/lec14-agentic-threats-guide-ko.html`, G2, line 143.
- Current end: `대화가 끝나면 효과도 사라집니다.`
- Replace the prompt/context item with: `프롬프트/맥락(context)은 모델에게 지금 주는 입력입니다. 입력에 따라 답은 달라질 수 있지만, 입력을 읽는 것만으로 가중치가 갱신되지는 않습니다. 입력이나 기록이 다음 실행에도 제공되는 것과, 학습으로 가중치를 바꾸는 것은 구분해야 합니다.`
- File: `courses/trustworthy-ai/lec14-agentic-threats-note-ko.html`, S71 / main 31, lines 916, 922, 926, 930.
  - In the prerequisite paragraph, replace the absolute session-end sentence with the same weight-update distinction. Qualify the learning side as use of the updated weights in later tests, not a guarantee about every future conversation.
  - `모델 안에서 아무것도 바뀌지 않는다는 뜻` → `입력을 읽는 것만으로 가중치가 갱신되지는 않는다는 뜻`.
  - Flow label `그 실행 안에서만 행동` → `현재 문맥을 읽고 행동`.
  - `모델 자체는 조금도 바뀌지 않습니다.` → `여기서는 입력을 읽을 뿐, 가중치를 학습으로 갱신하는 것이 아닙니다.`
- One concise clarification suffices: `이는 가중치 갱신 여부의 구분이지, 에이전트가 남긴 기록이나 행동의 결과까지 사라진다는 뜻은 아닙니다.` No new memory tutorial is wanted.
- Reason: E07's prerequisite is context versus parameter learning, not a session-boundary safety guarantee. The existing Korean backup 18 / S62a already explains carried-forward context correctly. Preserve the tested-setting qualifier around Cloud's ICL null result (E03, Methods / Extended Data Fig. 6); do not broaden it into a universal impossibility claim.

### 3. F03 — a control need not be untreated [judgment]
- File: `courses/trustworthy-ai/lec14-agentic-threats-note-ko.html`, S36a / main 42, line 1307.
- Current: `대조군은 처치를 받지 않은 비교 집단이고`.
- Replace with: `대조군은 관심 요인이 다른 비교 조건입니다. 이 강의에서는 학습하지 않은 모델뿐 아니라, 일반 숫자나 다른 동물 교사의 숫자로 학습한 모델도 비교 대상으로 씁니다.` Then retain the distinct definition of operational AI control.
- Also replace `이 문서에서 "통제"는 언제나 뒤의 뜻입니다.` with `이 구획의 AI control은 뒤의 뜻입니다.` The document also uses ordinary statistical control elsewhere.
- File: `courses/trustworthy-ai/lec14-agentic-threats-guide-ko.html`, G2, line 152: align the opening definition with `관심 있는 요인을 달리한 비교 대상` rather than making removal of a factor the definition of every control. Keep the concrete explanation of why ordinary-data-trained learners matter.
- Reason: Cloud's controls (Fig. 4a; main 25 / S67a) receive active training. The current added definition excludes the very comparisons students just learned. E03/E07.

### 4. F04 — do not map propagated injection onto Hammond's “conflict” [judgment]
- File: `courses/trustworthy-ai/lec14-agentic-threats-guide-ko.html`, B3 / `#ba3`, line 335 (backup 28 / S25).
- Current: `이 묶음은 그 구분을 따라 세 가지 증거를 봅니다.`
- Replace with: `이 분류와 별개로, 이 부록은 공격자 없는 조정 실패, 외부 주입의 전파, 은밀한 공모에 관한 세 종류의 증거를 구별해 읽습니다. 주입의 전파를 Hammond의 갈등 범주와 같은 것으로 묶지는 않습니다.`
- Keep the three following examples; no extra taxonomy table is needed.
- Reason: Hammond Fig. 1 groups failures by objectives. The lecture's measured/simulated/limited-evidence grouping is its own synthesis, not Hammond's taxonomy. The Korean slide note b28 already makes this distinction correctly (E06, frozen S25).

### 5. F05 — repair the connected narrative, not its structure [judgment]
1. File: `courses/trustworthy-ai/lec14-agentic-threats-note-ko.html`, S60 / main 16, lines 584–586.
   - `이 구간은 두 편의 논문을 따라갑니다` followed by Betley and Cloud omits the Askin study that occupies main 34–40 in the same section. Replace with a short roadmap: Betley's narrow-task misalignment supplies background; Cloud tests teacher-written number data; Askin tests learner-written answers with teacher scores. Add Askin's existing v2 source to the section source line, reusing the later articles' citation.
   - Soften the unsupported prevalence trend `다른 모델이 직접 써 낸 데이터의 비중이 점점 커지고 있습니다` to `다른 모델이 만든 데이터를 학습에 활용하기도 합니다`.
   - Reason: the requested Askin paper is a central part of section 02, not an unannounced fourth story. No extra study or slide is being added.
2. File: same, S35 / main 41, line 1295.
   - Current first-story recap: `실행 중에 주어지는 입력에 따라 움직임이 바뀔 수 있었습니다`.
   - Replace with: `정당하게 부여된 권한 안에서 내린 잘못된 판단도 실제 손실로 이어질 수 있었습니다` (keep the agent definition if helpful).
   - Reason: story 01 was authorized shop decisions and their consequences, not a repeat of the preceding lecture's prompt injection.
3. File: `courses/trustworthy-ai/lec14-agentic-threats-guide-ko.html`, G7, line 308.
   - The “에이전트에 대해 물어볼 다섯 질문” list has not been given in this guide. The preceding paragraph instead names five course areas. Replace this orphan reference with: `이 다섯 영역의 질문은 신뢰를 검토하는 틀이지, 모두 답했다고 안전을 보증하는 인증서는 아닙니다.`
   - Reason: a standalone reader should not have to find the separate agent checklist in main 58's note to understand the closing paragraph. No need to add a second checklist.

### 6. F06 — “proof” is not the same as “evidence” [judgment]
- File: `courses/trustworthy-ai/lec14-agentic-threats-note-ko.html`, S39a / main 49, lines 1443 and 1449.
- Message: `이 점수는 증거가 아니라 대략적인 경고 신호입니다.` → `이 점수는 백도어를 입증하는 확증이 아니라 대략적인 경고 신호입니다.`
- Explanation: `백도어가 있다는 증거도 아니고, 보정된 확률도 아닙니다.` → `그 점수만으로 백도어가 있다고 입증할 수 없고, 보정된 확률도 아닙니다.`
- At the end, translate the slide's qualifier as `대략적인 경고 신호이지, 확증이나 보정된 확률은 아니다` rather than `증거도, 확률도 아니다`.
- Reason: the frozen English note/slide says “rather than proof” / “not proof”. A heuristic can supply evidence without being conclusive or calibrated. This is a translation correction, not a change to Greenblatt §3.2 or the English deck (E05).

### 7. F07 — accessible, verifiable final exports
- Artifacts: `lec14-agentic-threats-note-ko.standalone.html` and `lec14-agentic-threats-guide-ko.standalone.html`; report location: `log/2026-11-28-lec14-korean-notes/work-r1.md`, lines 190–199.
- `/workspace/extra/slides-wt/lec14fo/...` is not mounted in the reviewer container. Only `/workspace/extra/slides` and `/workspace/extra/slides-log` are available; neither supplied export is accessible.
- After the corrections, regenerate both files from the round-2 content. Put untracked copies in a reviewer-readable shared location, preferably `/workspace/extra/slides-log/2026-11-28-lec14-korean-notes/standalone/` (the shared tracked-record area, **not** reviewer-owned `jobs/<job-id>/`). Confirm the actual mount/path on your side rather than assuming the worktree path is shared.
- Report exact source commit, readable paths and fresh SHA-256 hashes in work-r2. Keep the pair's cross-links and the explicit offline-unavailable English links. Do not send files directly to Albert; slides-review handles final delivery after verification. No PDF.
- Reason: a report of an offline test is useful but is not possession or independent verification of the requested deliverables.

### 8. F08 — optional Korean polish [judgment, nonblocking]
- `courses/trustworthy-ai/lec14-agentic-threats-note-ko.html`, main 9 / S52a, line 416: `손님을 기쁘게 하려는 마음이 컸습니다` → `저자들은 에이전트가 손님의 요구를 지나치게 맞추려 했다고 설명합니다` (behavior/author interpretation, not a claim about feelings).
- Same, main 30 / S70 line 900 and backup 48 / S91 line 2695: `한 자릿수(약 10배) 높다` → `대략 10배 높다` (natural rendering of “an order of magnitude”). Preserve the existing about-10% versus plotted-.08 distinction.
- Same, main 51 / S40, lines 1484/1489: `사전 감사이` → `사전 감사가`; `사전 감사은` → `사전 감사는`.
- `courses/trustworthy-ai/lec14-agentic-threats-guide-ko.html`, G0 line 82: `열기 5분` → `도입 5분`.

## Review evidence and checks

- Read the entire new Korean note (all 111 entries) and guide, including all six optional sections, source list and map. Checked against frozen English explanations, the inherited primary-source register and the source-specific distinctions; no new literature survey.
- Exact diff contains only the two new Korean files, authorized title strings in existing lecture/companion files, target outline updates and this job's tracked record. Existing deck styles and slide-ID sequences are unchanged. 59 main + 52 backup entries match the Korean article sequence exactly; no duplicate IDs.
- Parsed all local links/assets and cross-file anchors: no missing targets (note 335 links / 33 asset references; guide 180 links / 18 asset references). Root and leaf outline heading sequences are identical to baseline; no unrelated outline section deletion.
- Independently loaded the exact archived commit in headless Chromium with real CDP viewport emulation at 430×900 and 1280×900. Both documents have zero visible-element horizontal overflow and zero broken images; fonts loaded. Client widths 415/1265 reflect the scrollbar. Readability checked visually at every section/appendix start, all guide chapters plus glossary/sources/map, and representative complex exhibits (Vend, Cloud, Askin, control, Ge-Wang, MAST and reproduction). No clipping/tofu seen.
- Figure click-to-enlarge and Escape close work in both narrow documents. Small original plots remain supported by detailed Korean readings; no demand to shrink text or rewrite assets.
- Main title/contents, backup title/contents, tech title/neighbor independently rendered at 1280×720; no overflow. All six inspected.
- Standalone export checks remain pending F07. Do not present them as independently verified yet.

## Disposition of work-r1 plan issues

- Accept the meaning-preserving consolidation of repeated English prose, omission of internal bookkeeping/color hexes, short structural entries, and guide omission of secondary numeric tables. The detailed Korean note retains those substantive results. Accept the m55 confidence-interval reading and m58 title connection; neither adds a new empirical claim.
- Accept local mobile stacking and figure enlargement, and explicit removal of unavailable English-file links only in standalone copies. No reference-layer change is needed.
- Keep the reported source-internal counts/plot-versus-text discrepancies visible and attributed; do not choose invented reconciliations (Ge-Wang counts/intervals, METR, RepliBench, Apollo, MAST, Cloud). These are inherited and bounded, not new source findings requiring a survey in this job.
- “Reliably above zero” versus significance, probability versus log-probability, and Sonnet 4/4.0 need no new deck change here; retain the more precise Korean explanation and source bounds. The Korean correction that the S69a fragment is masked is appropriate. Legacy IDs explicitly referring to a baseline copy can remain. English-note bookkeeping/caption cleanups and broader S49 synthesis are outside this title/companion job; not silently authorized by this review.
- **No plan-v2 needed:** these corrections implement plan-v1's existing accuracy, flow and deliverability requirements. Argument, slide order/count, duration, sources, chosen title and package scope remain unchanged.

## Round-2 handoff

Implement F01–F07 locally; F08 is optional. Refresh the two exports, report every finding's disposition and precise paths/hashes in work-r2, copy this frozen review unchanged and refresh living job/evidence records. Review will recheck changed articles/chapters and neighbors, shared mappings/links, and the final export pair—not restart the whole lecture review. Keep existing PR #84; no merge is authorized.
