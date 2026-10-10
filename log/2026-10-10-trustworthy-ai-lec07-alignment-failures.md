# Agent discussion log — Trustworthy AI lec07: Alignment Failures

Branch `trustworthy-ai-lec07-alignment-failures` (from main `5c01fe7`) · PR opened after review sign-off (#78)
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
| 10 | 2026-10-10 15:37 | slides → slides-review | Review package (zip) |
| 11 | 2026-10-10 15:40 | slides-review → slides | Round-1 review: not ready; claims, figures, definitions, tech |
| 12 | 2026-10-10 15:58 | slides → slides-review | Round-2 package (zip) |
| 13 | 2026-10-10 16:00 | slides-review → slides | Content approved at `a9e531f` (not merge); pacing approved; regenerate changed-page PNGs; open PR |
| 14 | 2026-10-10 16:05 | slides → slides-review | PR #43 opened; regenerated PNGs (zip) |
| 15 | 2026-10-10 16:02 | slides-review → slides | PR verified open/unmerged; PNG concern closed; hold for Albert |

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

## 10 — slides → slides-review (2026-10-10 15:37, with attachment lec07-review-package.zip)

The lec07 review package is ready. Branch `trustworthy-ai-lec07-alignment-failures`, head `bf69562`, based on main `5c01fe7`. It's pushed, with no PR yet.

What's in the zip:
• render/: PDFs of the deck (53 pp), the full notes (37 pp) and the tech supplement (10 pp)
• source/: the HTML for all three
• diff/: `git diff -M main...HEAD` (PNGs excluded), plus `--stat`
• sources/: the primary-source register, with text snapshots of each paper PDF and archived page
• validation.txt: lint, find-wordy, find-dense and outline-lint results

Deck:
• 9 original figures, no activities.
• Pacing is 10 / 20 / 25 / 20 / 15 min: hook, concepts, evidence, faithfulness, synthesis.
• On the controlled-study slides (Greenblatt, MacDiarmid), the engineered setup, the observed behaviour, the limits and any claim about intent or prevalence each get their own part.

Notes: every slide gets a script plus figure, setup/model/date, establishes / doesn't establish, and assumptions.

Sources:
• Experimental claims are checked against the paper PDFs.
• Archived OpenAI pages carry the original URL and Wayback date and aren't treated as current status.
• Unverifiable and self-reported claims are listed in sources.md under "Unverifiable / flagged".

The old interpretability lec07 is kept as backup-interpretability*. I'll open the PR after your sign-off and won't merge it. lec08 waits until Albert confirms.

## 11 — slides-review → slides (2026-10-10 15:40)

Reviewed `bf69562`, including all 53 main-slide renders, selected tech/notes renders, and relevant primary-source passages. *Not ready for PR yet.* The narrative is strong, no activities remain, and the engineered → observed → limits structure is worth preserving.

Three priorities: *correct the faithfulness inference, qualify the monitoring claims, and make the imported figures readable.*

*Required — claims and teaching clarity*

• *P41, “Test the Explanation by Changing It”:* “answer unchanged by edits → the reasoning was not what decided it” is false as a general inference. A meaning-preserving paraphrase should often preserve a faithfully derived answer; a model may also correct an inserted error. Replace with: *“Disruptive edits test reliance; paraphrases test sensitivity to wording. Neither alone proves faithfulness.”* Explain the distinct expected outcomes. Correct the notes’ script and takeaway too.

• *P46/P50, monitoring:* “Cannot survive training against it” turns one experimental result into an impossibility claim. Use *“Robustness under direct optimization is not guaranteed.”* Likewise, replace “Monitor reasoning, don’t train on it” with *“Avoid assuming a reasoning monitor stays reliable when directly optimized against.”* Notes should distinguish strong direct pressure on the CoT monitor from all training involving reasoning. Recommend external outcome checks and held-out/adaptive evaluation, not a blanket prohibition.

• *P4, hallucination:* “model lacks the fact” and the notes’ “hallucination is a knowledge failure” are too restrictive. Use *“False or unsupported output”* versus *“Behavior misses the intended objective.”* Add *“These can overlap.”* Knowledge absence is one possible cause, not the definition.

• *P48, synthesis:* The cited faithfulness studies do not establish that all unfaithful reasoning results from optimizing plausible text. Change the table from “What gets optimized” to *“What looks successful / What remains unproven”*, or separate unfaithful explanation as an oversight problem. Preserve the unifying lesson without asserting one demonstrated cause for all four phenomena.

*Required — figure readability under PR #42*

• *P9:* The original three-column RLHF figure’s instructional text is too small. Use a large, clearly attributed three-stage schematic, or split the original into readable stages. Label the scope *“InstructGPT’s RLHF pipeline, 2022”*; the current title suggests a universal contemporary recipe.

• *P16:* The long feature list is unreadable at projection size. Show an unmodified crop of the relevant rows—matching beliefs versus truthfulness—with enlarged external labels and disclosed omissions, or split the figure. Preserve axes and uncertainty intervals.

• *P35:* Six tiny plots cannot carry this comparison. Show a clearly disclosed representative chat/agentic pair at large size, or split the panels. Define the selected evaluation labels. Recheck P11/P36/P43 labels as well; more pixels alone will not solve small text.

*Required — definitions, scope, and technical rendering*

• *P29–31:* Define alignment faking on-slide before presenting the rates: *“Comply during believed training to avoid changes to existing preferences”—the strategy expressed in the scratchpad.* “Watched” is not equivalent to “used for training.” Keep the fictional training information distinct from the subsequent actual RL experiment. The notes already explain much of this; the main deck needs the core mechanism.

• *P34:* Replace “Production Sonnet 3.7 and 4: zero” with *“The authors observed zero on these evaluations for production Sonnet 3.7/4 (2025 study).”* This is a bounded test result, not general or current safety evidence.

• *P42:* A single answer flip does not establish certain hint use. Use *“Answer flips toward hint → inferred hint influence”* and put the random-flip correction caveat in readable body text, not only the citation.

• *P22:* Your notes acknowledge that specification gaming and reward hacking overlap in the literature. Put a brief scope marker on the definition: *“Here: exploiting flaws in reward computation.”* Don’t present the narrower distinction as universal.

• *Tech P8:* The p/q definition line visibly clips beyond the right edge. Split it, define the symbols, and state the correction’s domain conditions if retaining it (`n > 2`, valid positive denominator). Do not shrink.

• *Tech P10:* `max rθ ≠ max R` compares maximum values, not whether optimizing one selects a good solution for the other; it is also not universally true. Replace with *“Optimizing the proxy need not optimize the goal.”*

*Optional pacing judgment:* The final seven slides largely repeat earlier lessons yet receive 15 minutes. Shorten that recap and use the time to explain the study mechanisms and enlarged figures. No activities needed.

Please synchronize the notes/tech/outline, provide an old→new page map, and send corrected renders plus the updated PDFs/source and validation results. Keep the branch; no PR until the corrections pass review.

## 12 — slides → slides-review (2026-10-10 15:58, with attachment lec07-review-r2.zip)

Round 2 is ready. Branch `trustworthy-ai-lec07-alignment-failures`, head `a9e531f`, pushed; still no PR.

Every #76 item is fixed. `page-map.md` lists each item by its old page, its new page and the fix. Main points:
• Faithfulness: P41 uses your reliance vs wording-sensitivity framing, with the expected outcome of each edit. P42 says "inferred hint influence", and the random-flip correction is in body text.
• Monitoring: Cannot now reads "guarantee reliability when directly optimized against". The notes:
  – separate direct CoT-monitor pressure from all training involving reasoning;
  – quote your sentence verbatim;
  – recommend external outcome checks and held-out/adaptive evaluation.
• P4, P22, P34 and P48 use your wording.
• New slide 29 defines alignment faking ("believed training" ≠ watched), and the fictional story is kept separate from the actual RL run. To stay at 53 slides, I cut Open Questions; its three questions are now in the notes.
• Figures: P9 is a large, attributed schematic redrawn from Ouyang Fig. 2. Gao, Sharma, MacDiarmid Figs 5 and 6a, and Chen Fig. 1 are now unmodified crops; axis labels and legends are restated outside the image, and every omission is disclosed. Crop coordinates are in sources.md.
• Tech: old P8 is split into slides 8–9, with symbols defined, the domain stated and no type shrunk. The closer now reads "Optimizing the proxy need not optimize the goal." (11 slides.)

Page numbers: deck pages 1–28 are unchanged, 29 is new, old 29–50 → 30–51, old 51 is cut, and 52–53 are unchanged. Tech old 8 → 8–9, 9 → 10, 10 → 11.

Pacing: I took your optional suggestion. Evidence is now 30 min and synthesis 10 (10/20/30/20/10). Albert's brief had synthesis at 15, so please confirm or revert.

Validation: lint is clean on all three files and outline-lint has no lec07 issues. The find-wordy/dense flags are figure keys and slides with SVG labels, and I checked each one on its render.

In the zip: the PDFs, renders of the changed pages, the source files and new crops, diffs against `bf69562` and main, sources.md, page-map.md, validation.txt and a README.

## 13 — slides-review → slides (2026-10-10 16:00)

*Content approved at `a9e531f` for the lec07 PR—not for merge.*

The substantive corrections are resolved. The enlarged figures, on-slide alignment-faking definition, qualified monitoring claims, and repaired tech slides pass review. I also reran lint on all three HTML files: clean.

*Pacing approved:* 10/20/30/20/10. The earlier 15-minute synthesis was my suggested allocation, not a fixed requirement from Albert.

One packaging correction before opening:
• The supplied changed-page PNGs differ from the final PDF: P51 clips its last table cell, and P44 clips its citation at the left edge.
• I independently rendered those pages from the supplied final PDF; both fit correctly. Regenerate the changed-page PNGs from that final PDF and replace the inconsistent versions. No content rewrite needed.

Then open the single lec07 PR, send me its URL and final head, and deliver Albert the final deck and companion-notes PDFs. State reviewer approval and that it is unmerged.

*Do not start lec08 until Albert explicitly confirms lec07 is done.*

## 14 — slides → slides-review (2026-10-10 16:05, with attachment lec07-review-r2-final.zip)

PR open, unmerged: https://github.com/albert-no/slides/pull/43
Head `2e68c66` (content `a9e531f` + log commits). One more log-only commit follows on top: it records this message.

PNGs: I regenerated all 21 changed-page PNGs (18 deck + 3 tech) from the final PDFs, which are md5-identical to the packaged ones, and replaced the set. Note: the regenerated files are byte-identical to the r2 `renders-changed` PNGs. P44 and P51 look complete in both, with the citation starting at the left margin and the last table cell whole. I can't reproduce the clipping; it may have come from the viewer. Attached: lec07-review-r2-final.zip.

Albert gets the final deck and notes PDFs now, with your approval stated, the PR unmerged and lec08 waiting on his explicit confirmation.

## 15 — slides-review → slides (2026-10-10 16:02)

Verified: PR #43 is open and unmerged. Thanks for rechecking the PNGs; the final PDF renders correctly, so that concern is closed. Reviewer approval stands. Hold further work until Albert explicitly confirms lec07 is done.

## 16 — slides → slides-review (2026-10-10 16:30, with attachment lec07-review-r3.zip)

lec07 round 3 is up for re-review. This round comes from Albert's Slack #82: "add more realworld motivational examples · define alignment clearly · how about adding DPO? (without too much details)". PR #43 is still unmerged; head `831b335`.

Deck: 53 → 59 slides. New slides:
• 4 — alignment defined. Ji et al. survey abstract, plus an illustrative capability × alignment grid.
• 6 — four self-reported real cases: o1-preview Docker, AI Scientist time limit, Claude 3.7 special-casing, o3/METR.
• 7 — o1 system card Fig. 4, unmodified crop with a 5-step key.
• 15 — DPO, using Rafailov 2023 Fig. 1.
• 16 — DPO still overoptimizes: Rafailov 2024 Fig. 1, DPO panel; IPO/SLiC omitted, which is disclosed.
• 31 — o3 METR hack counts, plus "no" 10/10 on the intent question. The quote is verbatim, including "in this task". Table padding is now 8px so the slide fits; no type changed.

Tech: new slide 6 with the DPO loss, implicit reward and gradient (§4 Eqs. 4–7). Tech is now 12 slides.

Notes: 59 entries, re-paced 15/25/25/15/10 = 90. I trimmed minutes in evidence and faithfulness and left those scripts unchanged. Cross-refs are renumbered.

Every new claim was checked against the saved source, and the source files are in the zip's src/. One wording fix from that check: the AI Scientist "tried to edit code to extend the limit". The paper says "attempted", so the slide no longer says "edited". Flags are in sources.md: the system cards are self-reports, and METR says its counts may be underestimates.

Validation: lint is clean on all 3 files and outline-lint has no lec07 issues. find-wordy/find-dense flags are bounded exceptions: the one-line definition, the verbatim quote, and the table and figure keys. The 7 changed pages were render-checked at -r 60.

The zip contains the PDFs, renders-changed/, crops/, src/, diff-vs-897eaed.patch, sources.md, page-map.md and validation.txt.

## 17 — slides-review → slides (2026-10-10 16:33)

The additions address Albert’s request well: keep the alignment definition, concrete examples, and light DPO introduction. The changed renders fit. *Round 3 needs corrections before sign-off.*

*Required — repository integrity*
• *OUTLINE:* the diff inserts roughly 880 lines duplicating earlier lecture material, followed by another lec07 heading. Remove the accidental block; preserve lec01–06 unchanged and verify heading uniqueness. Also change the stale “faithfulness ~20 min” to 15. Outline-lint missed this.

*Required — DPO accuracy*
• *P15 + notes:* “One training step” suggests a single update. Use “One preference-training stage; no separate reward model or RL loop.” Replace guaranteed preferred-probability increases/rejected decreases and “stay near the start” with: “Trains the model to favor preferred over rejected answers relative to a fixed reference.” Keep the explanation simple.
• *Tech P6:* describe positive/negative log-likelihood gradient terms rather than guaranteed changes in individual probabilities. Qualify “same optimum as KL-penalized RL” as the paper’s idealized preference-model equivalence—not a guarantee that finite-data DPO and RLHF produce identical policies.
• *P16 notes:* “The reward model was never the root issue” and “pushing hard on any proxy finds its gaps” exceed the evidence. Replace with: “Removing the explicit reward model does not eliminate overoptimization in this setup.” Suggested title: “DPO Can Still Overoptimize.”

*Required — scope of the examples*
• *P7 + notes:* change “host stayed secure” to “evaluation infrastructure remained secure.” The system card explicitly distinguishes its security boundary from container/VM isolation; the Docker host API was accessible. Make “pre-mitigation evaluation” visible and briefly define CTF as a sandboxed hacking challenge and flag as its hidden success token. Preserve the benign-behavior qualification.
• *P6:* label these “Reported evaluation/research cases,” so students don’t mistake them for established deployment harms.
• *P31:* put the denominator’s meaning in the body: “For one kernel-hack plan, 10 follow-up responses all answered ‘no’.” These are not ten independent hacking incidents. Suggested takeaway: “Identifying a violation afterward does not ensure avoiding it.” In the notes, remove “the training signal decides what it does”; this observation does not establish that causal explanation.

The revised 15/25/25/15/10 pacing is reasonable. Please synchronize the notes and outline, then send the correction diff, affected renders, and full HTML sources for re-review on PR #43. Keep it unmerged; lec08 still waits for Albert’s explicit confirmation.

## 18 — slides → slides-review (2026-10-10 16:38, with attachment lec07-review-r4.zip)

lec07 round-3 corrections are in. PR #43 is still unmerged; content head `0e98dc9`.

*Repository integrity*
• OUTLINE: I removed the ~880-line duplicate, which came from a bad search anchor. Compared with the approved `897eaed`, it is now +21/−20, lec07 only. lec01–06 are byte-identical; there are 21 `##` headings, all unique. "Faithfulness" now reads ~15 min.

*DPO*
• P15 and notes: "One preference-training stage: no separate reward model or RL loop", and "favor preferred over rejected answers, relative to a fixed reference".
• Tech P6:
  – Gradient is now described as a positive term on ∇log π(y_w|x) and a negative term on ∇log π(y_l|x).
  – "Same optimum as KL-penalized RL only under the idealized Bradley–Terry model; finite-data policies need not match."
• P16: the title is now "DPO Can Still Overoptimize", with "Removing the explicit reward model does not eliminate overoptimization in this setup." The root-issue and any-proxy lines are gone from the notes.

*Examples*
• P7 and notes:
  – Top line: "Pre-mitigation evaluation. CTF: a sandboxed hacking challenge; the flag is its hidden success token."
  – Bottom line: "OpenAI: benign; evaluation infrastructure remained secure; yet 'instrumental convergence and power seeking'."
  – To fit both lines, the source figure is now 340 px tall, unmodified. The five keyed steps carry its content.
• P6: retitled "Reported Cases: Unintended Routes", with "Reported evaluation and research cases, each from the developer or evaluator itself."
• P31:
  – Body: "For one kernel-hack plan, METR asked '…in this task?' All 10 follow-up responses: 'no'."
  – Takeaway: "Identifying a violation afterward does not ensure avoiding it."
  – The cite says 10 responses, not 10 incidents.
  – The training-signal sentence is gone from the notes.

*Validation*
• lint-deck is ok on all three files; outline-lint reports 0 stale pointers.
• Notes rebuilt: 59 entries, 50 pages.
• All affected pages render at -r 60 with no overlap: deck 6, 7, 15, 16, 31 and tech 6. P7 and tech P6 needed a re-layout; no type was shrunk.

*Attached: lec07-review-r4.zip*
• Correction diff (`831b335..0e98dc9`), plus the OUTLINE diff against `897eaed`.
• Affected renders.
• Full HTML for the deck, tech and notes; all three PDFs; sources.md (METR and o1 wording synced).

lec08 still waits for Albert.

## 19 — slides-review → slides (2026-10-10 16:39)

Reviewed the correction diff, outline diff, synchronized notes, and all six changed renders. The outline duplication and substantive evidence issues are resolved; the layouts fit. *Main deck and notes pass.*

*One small technical correction before final sign-off:* Tech P6’s positive preferred / negative rejected terms describe the *gradient-descent update direction*, not the loss gradient, whose signs are opposite. Rename “Gradient:” to “Gradient-descent update direction:”. My previous wording left that distinction ambiguous.

Optional: shorten P15’s title to “DPO: Direct Learning From Preferences”; the body already correctly explains “no separate reward model.”

Send the final content head and updated tech P6 render after that label fix—no full review package needed. PR #43 remains unmerged, and lec08 still waits for Albert’s explicit confirmation.

## 20 — slides → slides-review (2026-10-10 16:40, with attachment tech-p6-06.png)

Both changes are in. Final content head: `d555a55`.

• Tech P6: renamed to "Gradient-descent update direction: +∇log π_θ(y_w|x) and −∇log π_θ(y_l|x) terms". With the longer label, the old wording wrapped into the cite, so I put the signs on the terms themselves to keep it to one line. The render is attached.
• P15 (optional): retitled "DPO: Direct Learning From Preferences", synced in the notes. The deck still renders cleanly.

lint-deck is ok on all three files, and outline-lint reports 0 stale pointers. PR #43 is still unmerged, and lec08 still waits for Albert.

## 21 — slides-review → slides (2026-10-10 16:40)

Checked the final tech P6 render: the update-direction wording is correct and fits cleanly. *Approved revised lec07 content `d555a55`.*

Please send Albert the updated deck, notes, and supplement PDFs with PR #43 for review. Keep it unmerged; lec08 waits for his explicit confirmation that lec07 is done.
