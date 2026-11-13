# Plan v3 — round-1 corrections and a sourced CEO example

## Changes since v2

1. **S78 source route changes**, not its teaching purpose: image generation produced no output, so use a verified published CEO-generation example instead. This is the historical-source contingency, not a credential change. Do not drop S78 or fabricate a fresh run.
2. **S21b's scope is corrected:** randomization is used by the illustrated profit-optimal equalized-odds rule, not required by equalized odds in all feasible rules. “Not 50/50” becomes “not necessarily 50/50”.
3. **The review controls readability repairs:** F03/F04 require figure-first chart readings and canonical prose rhythm. Counts/layouts remain flexible. No new argument or literature-survey block is added.

This is an amendment to plan-v2's complete work order; all unreplaced specs, package boundaries and preservation rules still apply. `review-r1.md` is the full numbered round-2 change list. Address blocking F01–F04; F05 is discretionary. Review remains medium, round 2 of 2 next.

## 1. Replacement S78 spec [judgment]

- **Position:** new S78 after S77 and before S74. Main and matching note paths unchanged from v2.
- **Point / proposed title:** “A CEO Prompt Leaves Appearance Unspecified.” The input specifies an occupation; a concrete image adds details absent from it.
- **Must exhibit:** Wan and Chang, ACL 2025, Figure 1, PDF p1 / printed p9174, top-row **CEO** image only, from the single-subject examples. Source PDF: https://aclanthology.org/2025.acl-long.449.pdf . This actual DALL-E 3 generated image is embedded at 1024×1024; extract the source bitmap rather than upscaling a small page screenshot. Visually match it to the CEO panel before shipping (the PDF's first page-image object 273 is that panel; extraction indices are a hint, not a substitute for the match).
- **Main prompt:** “Generate a picture of one CEO.” Use the paper's actual instantiated prompt, not the unexecuted “Generate a photo…” prompt. Define CEO as chief executive officer.
- **Interpretation:** “The prompt specifies a role, not appearance.” Necessary visible qualifier: “Published example, not a new run.” Also make clear that a single example does not establish a bias rate, in either direction. Do not label inferred race/gender or turn this selected image into a claim about actual CEOs.
- **Attribution:** Wan and Chang, ACL 2025 — Figure 1, CEO example; DALL-E 3. Say other panels are omitted. 2025 is the publication year, not a claimed generation date.
- **Note:** source URL/figure/panel, exact user prompt, historical model name, extraction/repo path, and selection status (authors' illustrative example, not an independently sampled audit). Explain that repeated outputs and a defined comparison would be needed for distributional conclusions. Do not bring in the paper's paired-subject 74% result or teach a new method here.
- **Tech:** unchanged.
- **Evidence:** E14 supersedes E10's unexecuted route; E11 remains separate historical context, not the CEO-image attribution.
- **Layout/time:** figure-first; target 0.75 min. Restore v2's explicit 10-minute opening pacing using the additional quarter-minute adjustments to S06/S08/S09. Keep the total 90 minutes.
- **Acceptance:** actual high-quality source bitmap, prompt/picture match, honest published-output label, no fabricated test, no replacement of the author's example with a more stereotypical one. The opening then has both of Albert's suggested visual ideas.

## 2. Other packages

- **P1:** implement F02 and F04. Source E13 is authoritative for the correction; the old plan wording does not override it. Keep the truthful five-rule explanation, faithful crops and criterion distinctions. If title changes to emphasize the optimum, synchronize the note.
- **P2:** S23a/b approved in content; only integration/reference changes unless a split elsewhere affects their neighbours.
- **P3:** implement F03, preserving definitions, focal pair, approximate values and limitations. Crop, larger external labels, or staged overview/zoom are allowed. If splitting S26a/b further, retain stable hierarchical suffix mapping and update notes; do not renumber earlier IDs. Any new ID takes the next free number.
- **P0:** add S78 as above; keep S77, optionally F05 cite cleanup, and repair opening note transitions so they describe both examples.

## 3. Shared surfaces / delivery

Update counts, note IDs/headings/pacing/references and only lec12 OUTLINE entries. Preserve all unrelated content and the existing technical supplement. Record every new split's old→new page trail, source extraction path and tests in work-r2. Review only changes and their neighbours; do not redo unrelated lecture material.

Copy review-r1.md and plan-v3.md unchanged, refresh living job/requests/evidence files, and push the named round-2 commit. The review verdict is still revise; no PR or merge yet.
