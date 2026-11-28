# Review r2 — final content approval

- Reviewed commit: `19bec6de1d382ed7648887d434a649c2ab439323`.
- Baseline: `3dd5a996afc0c89f47573cf9bbb330336a097948`; comparison for this round: `6d067ac53c346d0cc7c6a4441cc0ca69537c371f`.
- Branch / existing PR: `2026-11-27-lec14-focused-overview` / #84.
- Verdict: **approved**, round 2 of 2. All blocking findings closed. No further content round or plan change.

## Outcome

The new title and both Korean companions are ready: 59 main-slide explanations plus 52 optional backup explanations, and a separate connected guide with the prerequisite background. The local corrections now preserve the intended argument and inference limits. Main/backup slide counts, IDs, timing, English content and styling remain unchanged from the approved title revision.

| Comment | Status | Verified outcome |
|---|---|---|
| C01 better title | done | Trust Beyond Capability / 유능한 AI, 믿고 맡겨도 될까?; title/metadata/index consistency retained. |
| C02 complete Korean notes | done | All 111 entries and their sources/exhibit readings remain; no substantive reduction. |
| C03 slide-by-slide explanation | done | Exact main59 + backup52 ID/order mapping, main/backup page labels, working navigation. |
| C04 flow and backgrounds | done | G0–G7 independently readable; local definitions and transitions corrected, optional B1–B6 separate. |

## Finding disposition

| ID | Where | Type | Blocking remaining | Result |
|---|---|---|---|---|
| F01 | guide G1 / main 13–15 | fact | no | Informed approval can inspect proposed pricing; spending cap and purchase-gate coverage are distinct. Closed. |
| F02 | main 31 / S71, guide G2 | fact | no | Context reading distinguished from weight updates, with explicit retained-record/action caveat. Cloud's tested-setting qualification retained. Closed. |
| F03 | main 42 / S36a, guide G2 | fact | no | Active trained controls included; “통제” scoped to this AI-control section. Closed. |
| F04 | guide B3 / backup 28 | fact | no | Hammond taxonomy and the appendix's evidence grouping explicitly separated. Closed. |
| F05 | main 16 / S60, main 41 / S35, guide G7 | unmet request | no | Betley–Cloud–Askin roadmap and v2 citation present; recap describes authorized shop mistakes; closing refers to the five course areas actually given. Closed. |
| F06 | main 49 / S39a | fact | no | Heuristic not conclusive proof, rather than not evidence; message and explanation agree. Closed. |
| F07 | both standalone exports | unmet request | no | Shared files accessible; exact hashes, complete content, assets, offline reading and cross-document section navigation independently verified. Closed. Minor plain-link packaging issue separately noted as F09. |
| F08 | local Korean wording | preference | no | All suggested polish taken, without changing numbers or claims. Closed. |
| F09 | standalone plain companion links only | fact | no | Four no-fragment companion links were unnecessarily unwrapped and marked unavailable. Minor packaging defect; content and the numerous cross-document section links remain available and work. Optional correction below. |

## F09 — optional export navigation polish, not another content round

1. Files: `log/2026-11-28-lec14-korean-notes/standalone/lec14-agentic-threats-note-ko.standalone.html` (opening “두 한국어 문서의 역할”, counterpart of source note line 59) and `.../lec14-agentic-threats-guide-ko.standalone.html` (opening paragraph, G0 usage paragraph, end of reading list; counterparts of source guide lines 55, 85, 431). These are untracked exports; line positions shift when CSS/assets are embedded.
2. Current: the no-fragment link to the **other Korean standalone file** is replaced with text plus `<span class="offnote">(저장소 파일 …-ko.standalone.html, 오프라인 사본에는 없음)</span>`. This occurs once in the note and three times in the guide. Those files actually are supplied together. Fragment links to the same counterpart correctly remain links.
3. Optional precise fix: retain/restore these four ordinary links to the corresponding `…-ko.standalone.html` and remove only their incorrect unavailable annotations. Continue annotating the genuinely unavailable English files. Do not change tracked Korean prose, assets or any other link.
4. Reason: the packaging annotation is misleading, but it does not remove content or block cross-reading: tested per-article/chapter links reach the other file offline. It is **not an approval condition and does not start another round**. If taken during final artifact handoff, report the replacement hashes and this export-only delta; no source-content commit is needed.

## Verification

- Exact r1→r2 diff: only requested local wording in the two Korean documents plus this job's records. No deck, English note, reference, figure, script or OUTLINE changes. Read all changed text and its surrounding explanation; unchanged neighbors retain the r1-reviewed content. All r1 source-boundary decisions still apply.
- Tracked copies of review-r1, plan-v1, requests and evidence are byte-identical to the reviewer files. The 111-article mapping still equals the two decks' concatenated ID sequences.
- Both shared exports copied into an otherwise empty scratch folder. Their body text equals the exact-commit source text after removal of explicit offline-unavailable annotations. All IDs/anchors match. All embedded images decode byte-identically to the source assets: 32 note images and 17 guide images. No external or relative rendering dependencies remain, including CSS font URLs.
- All retained local/internal/cross-document link targets exist. The only local target file in each document is the other Korean standalone file. Verified live navigation in both directions, including target anchors, with networking disabled.
- Independent Chromium offline test (cache disabled, CDP offline mode): zero HTTP(S) requests, zero broken images, loaded Korean fonts, zero horizontal overflow at 430×900 and 1280×900 (client widths415/1265 due to scrollbar). Figure enlargement and Escape dismissal work. Screenshots inspected for changed main16/31/42/49/51, the changed flow, guideG1/G2/G7/B3 and approval-to-learning transition. Long notes scroll normally; no clipping or font shrink introduced.
- Main/backup/tech title renders, whole-document coverage and outline integrity passed r1 and are unchanged.

## Verified exports at this review

Shared directory: `/workspace/extra/slides/log/2026-11-28-lec14-korean-notes/standalone/`.

| File | SHA-256 |
|---|---|
| `lec14-agentic-threats-note-ko.standalone.html` | `f6cf41e0bd9d3fa02d4b5c1eb0a27a5d7d7e6509f01f7d5badb6d2b17046f5be` |
| `lec14-agentic-threats-guide-ko.standalone.html` | `9f49c28a7fa013f850e706843140148e46608af64006f72228c2797a858a0ab7` |

## Final record handoff

Copy this frozen review unchanged and refresh living job.md/evidence.md, then push the record. Every commit after `19bec6de1d382ed7648887d434a649c2ab439323` must touch only `log/2026-11-28-lec14-korean-notes/`. Send the exact pushed record SHA; if optional F09 is taken, include fresh artifact hashes/paths in that final log record. slides-review will verify the log-only chain, refresh existing PR #84 and deliver the two HTML files to Albert. No duplicate PR, no PDF, and **no merge authorization**.
