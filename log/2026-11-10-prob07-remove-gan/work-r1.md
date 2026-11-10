# work-r1 — 2026-11-10-prob07-remove-gan

- Branch: `2026-11-10-prob07-remove-gan` (from baseline `cdc2949`)
- ID-only commit: `9f2273b`. It adds `data-slide-id` S01–S137 to the main deck in baseline order and changes nothing else (137 attribute-only line edits, no line shifts).
- Content commit: `61a2337`. Head commit: named in the pointer message (the commit that adds this file).
- Result: main deck 137 → 130 slides (seven deleted, no splits, no new slides). `1 / 130` set.

## Per item

Done inline; no subagents (the scope is one contiguous deletion plus four small edits).

- **1–7, S128–S134 deleted.** Whole block from the GAN framework slide through "Dropping a Mode" removed. The deck-local rule `.p7-red`, used only by S134, removed from the deck's `<style>` block (dead CSS; no shared file touched).
- **8, S120.** Title "Two Families You Have Already Used"; `grid-3` → `grid-2` with the LLM and diffusion cards unchanged; GAN card removed. Highlight: "Same goal: q_θ ≈ p_data. **Different routes** — LLM cross-entropy training is exact MLE of q_θ(x); diffusion training generally is not."
- **9, shared surfaces.**
  - S02 Contents §11 sub: "LLMs and diffusion through likelihood".
  - S118 divider subtitle: "LLMs and diffusion — through the likelihood lens".
  - S135 scorecard: GAN row removed; conclusion "Of these two training setups, **only LLM cross-entropy training is exact MLE of q_θ(x)**." Title kept.
  - Note §11.1 (both formats): "All three families" → "Both example families"; discrete/continuous text unchanged.
  - Note §§11.4–11.6 deleted in both formats; §11.7 renumbered §11.4; GAN row and the final GAN/JS sentence removed; "Among these three" → "Of these two".
- **10, references and outline.**
  - Note refs 7 (Goodfellow) and 12 (Karras/StyleGAN) removed in both formats. Markdown list renumbered (old 8–11 → 7–10, old 13–14 → 11–12); the HTML `<ol>` renumbers itself. "cited by reference 8" → "cited by reference 7" (Ho et al.) in both formats, twice each. No other in-text reference numbers exist in either note.
  - `courses/deepmath/OUTLINE.md`: folder table row and prob07 header 130 slides; §11 row rewritten (GAN/JS entries removed, pages 118–128); bridge/closer 129–130; Markdown edition line count 1983 → 1843; Figures/numerics paragraph drops the GAN diagram, p/q/D* curves, two-mode fits, KL/JS nats, FFHQ and GAN Thm 1, and its note-reference numbers are updated (refs 8–9, 7, 11–12). All prob07 line pointers re-derived (−1 for the CSS line; −6 after S120; new S135/S136 lines). Root `OUTLINE.md` has no prob07 GAN text; untouched.
  - Standalone bundles of deck and note rebuilt locally (gitignored, not committed).

## Slide mapping

| Slide ID | Old page | New page | Change |
|---|---|---|---|
| S01–S127 | 1–127 | 1–127 | unchanged pages; S02, S118, S120 edited |
| S128–S134 | 128–134 | — | deleted (IDs retired) |
| S135 | 135 | 128 | edited |
| S136 | 136 | 129 | moved |
| S137 | 137 | 130 | moved |

## Deviations from the plan

- **Note IDs not added.** Both note editions are organized by section (§1–§12), with no per-slide `<article>` elements. Giving them slide IDs would mean restructuring the notes, so the ID-only commit covers the main deck only. See plan issue 1.
- **S120 title.** I kept "Two Families You Have Already Used" (old title with the count changed) rather than "Two Generative Model Families". The "you have already used" framing keeps the slide clearly non-exhaustive, which is the E03 guardrail.
- **Orphan CSS removed** (`.p7-red`, S134 only). That line deletion shifts every later deck line by one; the outline pointers account for it.

## Plan issues

1. Notes have no per-slide articles, so `PIPELINE.md`'s "matching `<article>` in the note carries the same ID" cannot be met without restructuring them. Proposal: record this job's `id commit` as deck-only. If per-slide note IDs are wanted, make them a separate job.

## Unsourced facts

None introduced. The new S120 clause "diffusion training generally is not [exact MLE of q_θ(x)]" restates the existing S127/S135 qualifier (E03).

## Checks run

- `lint-deck.py` on the deck: ok. `outline-lint.py`: 0 stale/missing pointers (5 pre-existing warnings in infotheory/privacy outlines). Every prob07 outline pointer was also checked by script against the baseline line contents (IDs stripped); all match.
- Term search (case-insensitive: GAN/GANs, generative adversarial, discriminator, Jensen–Shannon / Jensen-Shannon, `\text{JS}`, JS divergence, StyleGAN, Goodfellow, FFHQ) over the deck, both notes and both refreshed standalones. The only hits are "slo**gan**" (note §2) and base64 font data in the standalones. JavaScript links are intact.
- Retained: Jensen's inequality in note §11.3 (both formats); KL/CE in §11.1 and S119; S121–S127 untouched apart from IDs; S123 CE-SFT/RLHF and S127 path-MLE qualifiers unchanged.
- Rendered the 130-page PDF with headless Chromium; read at `-r 60` pp1–3, 117–121, 126–130 (plan's neighbour set; I looked closely at pp2, 118, 119, 120, 121, 127, 128, 129, 130). No overflow, overlap, bad wraps or type reduction. The seam p127 → p128 (scorecard) → p129 (bridge) reads coherently. S120 has two balanced cards and no empty third slot. The lower ~40% of S120 is blank, as it was with the baseline card layout; per the plan, I did not pad it.
