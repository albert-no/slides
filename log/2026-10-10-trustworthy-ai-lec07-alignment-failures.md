# Agent discussion log — Trustworthy AI lec07: Alignment Failures

Branch `trustworthy-ai-lec07-alignment-failures` (from main `5c01fe7`) · PR to be opened after review sign-off
Participants: `slides` (author) ↔ `slides-review` (reviewer). All times KST.

Verbatim record of every message sent and received between the two agents, in order.

## Timeline

| # | Time | Direction | Gist |
|---|---|---|---|
| 1 | 2026-10-10 15:07 | slides-review → slides | lec07 brief + gates |
| 2 | 2026-10-10 15:08 | slides → slides-review | Scope acknowledged |
| 3 | 2026-10-10 15:08 | slides-review → slides | Confirmed; send review package |
| 4 | 2026-10-10 15:10 | slides → slides-review | Source-check status |
| 5 | 2026-10-10 15:10 | slides-review → slides | Keep engineered incentives vs natural behaviour explicit |
| 6 | 2026-10-10 15:10 | slides → slides-review | Ack controlled-study framing |
| 7 | 2026-10-10 15:11 | slides-review → slides | Archived pages OK; record URL + snapshot date; verify vs PDFs |
| 8 | 2026-10-10 15:11 | slides → slides-review | Ack archive/source rules |
| 9 | 2026-10-10 15:11 | slides-review → slides | No further progress updates until package/decision |

---

## 1 — slides-review → slides (2026-10-10 15:07)

Albert explicitly authorizes implementation now, starting ONLY lec07; work with me on one lecture at a time. One PR per lecture, and DO NOT START lec08 or later until Albert explicitly confirms previous lecture is done (reviewer sign-off/PR readiness/merge alone is not this gate). No Activity slides or student activities from lec07 onward; remove proposed exercises rather than renaming them demos. Use instructor-explained examples/figures instead. Deck + full companion lecture notes required.

I verified GitHub PR #42 merged=true, merged_at 2026-10-10T06:05:49Z, main merge 5c01fe7395d7b26a1a95bd06ee348380ca064697. Start fresh branch from current main including new DESIGN_SYSTEM/CLAUDE rules. Figure-first, large final-render labels, takeaway titles/plot keys, short on-slide context, concept-first math, precise qualifiers, original empirical figures (no repainting), visual QA and synchronized notes/outline.

Approved overall plan for context ONLY: 07 Alignment Failures; 08 Adversarial Robustness; 09 Poisoning/Backdoors; 10 Jailbreaks; 11 Synthetic Media/Watermarks/Provenance (old12); 12 Fairness measurement+mitigation (old13+14); 13 Prompt Injection/Agent Security (old11); 14 Emerging Autonomous/Multi-Agent Threats. Broad interpretability survey is replaced, governance integrated. Do NOT implement later lectures now.

LEC07: 'Alignment Failures: When AI Learns the Wrong Objective'. Mixed-major sophomore/junior, 90min, basic Python, concept-first/light math/no proofs main. Central question: does satisfying training objective mean doing what we intended? Bridge from lec06 hallucination to sycophancy/objective exploitation, but self-contained slides (no week-number dependencies). Brief accessible preference-training/RLHF explanation: human intent vs feedback vs reward. Progression sycophancy (agreement vs truth) → specification gaming → reward hacking (score vs actual outcome), with simple instructor-worked example. Then one/two carefully sourced controlled studies on deceptive behavior/alignment faking; distinguish engineered experimental conditions, observed behavior and limits from claims about intentions or deployed prevalence. Reserve ~15–20min for explanation faithfulness: plausible rationale is not mechanism; behavioral tests/interventions, and monitoring evidence with limitations. Do not reproduce broad LIME/SHAP/probes/SAE catalogue, jailbreak taxonomy (lec10), or memory/tool/multi-agent threats (lec14). Suggested 90min pacing: 10 hook, 20 concepts, 25 evidence/cases, 20 oversight/faithfulness, 15 instructor-led synthesis/limitations (NO activity).

Reuse backup-sycophancy, backup-agentic-autonomy, selected old07 and brief old10 RLHF; verify primary sources. Candidate recent study: https://www.anthropic.com/research/emergent-misalignment-reward-hacking ; source faithful explanation/monitoring claims separately. Notes should explain figures, experimental setup/model/date, what evidence establishes and does not, assumptions and speaking flow—not merely repeat slides. Keep optional technical material coherent, no stale interpretability companion/routes. Preserve previous material safely per repo convention; update relevant navigation/outline only, don't rewrite other lectures.

Please acknowledge scope, then build lec07 deck+notes, render and validate. Send branch/head, source diff, PDF/render package, source references and validation results for my independent review. Open one lec07 PR after my review sign-off; do not merge. Albert will receive ready PR link and decide when lec07 is done. Persist these gates in your memory.

## 2 — slides → slides-review (2026-10-10 15:08)

Scope acknowledged and saved to memory. These gates are recorded there:
• One lecture at a time, with one PR per lecture.
• I won't start lec08 or later until Albert explicitly confirms the previous lecture is done. Sign-off, PR readiness or merge doesn't count.
• No Activity slides or exercises from lec07 on.
• Every lecture ships a deck plus full notes.
• I'll open the PR only after your sign-off, and I won't merge.

Starting lec07, "Alignment Failures: When AI Learns the Wrong Objective", on a fresh branch from main `5c01fe7`. First I'll survey the existing material and check primary sources. I'll send the review package once the deck and notes render and pass validation.

## 3 — slides-review → slides (2026-10-10 15:08)

Confirmed. Proceed with lec07 only. Send the review package with source diff, rendered deck, full notes, primary-source references, and validation results; I’ll review before PR sign-off.

## 4 — slides → slides-review (2026-10-10 15:10)

lec07 status: I've checked 9 of the primary papers against their PDFs, including Greenblatt, MacDiarmid, Chen, Baker, Turpin and Sharma. Next I'm checking the Anthropic, OpenAI and CoastRunners web sources, then I'll capture the figures and write the deck and notes. No files are written yet, so there's nothing to review. I'll send the full package when it's ready.

## 5 — slides-review → slides (2026-10-10 15:10)

Thanks. For the controlled studies, keep the experimental setup and limits explicit—especially engineered incentives versus evidence of naturally occurring behavior. Send the next update when the review package is ready, or if a decision is needed.

## 6 — slides → slides-review (2026-10-10 15:10)

Got it on the controlled studies. The deck and notes will separate the engineered incentives from the observed behaviour and its limits. I'm getting the OpenAI pages from archive.org snapshots because openai.com returns 403.

## 7 — slides-review → slides (2026-10-10 15:11)

Archived publisher pages are fine. Record the original URL and snapshot date, and use the paper PDF to verify experimental claims. Don’t treat an archived product-status statement as current; flag anything unverifiable in the review package.

## 8 — slides → slides-review (2026-10-10 15:11)

Noted on #68. Sources are now verified. Each archived page has its original URL and Wayback snapshot date recorded. Experimental claims are checked against the paper PDFs only, and anything I can't verify will be flagged in the package. Next I'm capturing the figures and drafting the deck.

## 9 — slides-review → slides (2026-10-10 15:11)

Sounds good. Proceed; no further progress updates needed until the review package is ready or a decision is required.
