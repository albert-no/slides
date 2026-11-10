# Evidence register (append-only)

No new literature survey: this job removes material and preserves existing mathematical claims and qualifiers. The entries below establish the baseline and deletion boundary; they are not a fresh scientific validation of unchanged slides.

## E01 — Baseline inventory and removal boundary
- Claim: 137 slide-class elements; pages 128–134 are the seven GAN/JS teaching slides; GAN references also occur on pages 2, 118, 120 and 135.
- Source/version: [pinned deck](https://github.com/albert-no/slides/blob/cdc2949fd21af93b014994acb56a4c048a95becb/courses/deepmath/prob07-estimation/prob07-estimation.html), pages 2, 118–135; exact titles and line locators in the plan's baseline map.
- Setup: counted class tokens equal to `slide`, excluding `slide-num`; read corresponding slide bodies.
- Does not establish: final slide count or any GAN theorem's truth.
- Label: our calculation (repository inventory).

## E02 — Companion deletion boundary
- Claim: HTML and Markdown companions duplicate the removed lesson in §§11.4–11.6 and mention it in §§11.1, 11.7 and references 7/12.
- Sources/version: [HTML note](https://github.com/albert-no/slides/blob/cdc2949fd21af93b014994acb56a4c048a95becb/courses/deepmath/prob07-estimation/prob07-estimation-note.html) §§11.1, 11.4–11.7, 12; [Markdown note](https://github.com/albert-no/slides/blob/cdc2949fd21af93b014994acb56a4c048a95becb/courses/deepmath/prob07-estimation/prob07-estimation-note.md) same sections, baseline lines 1530–1983.
- Setup: direct source inspection; §11.7 retains both LLM and diffusion rows and therefore must be edited, not deleted.
- Does not establish: permission to delete unrelated KL material or Jensen's inequality.
- Label: our calculation (repository inventory).

## E03 — Retained mathematical qualifiers
- Claim: baseline p119 and note §11.1 limit the empirical-KL identity to discrete data/models. Pages 126–127 and note §11.3 distinguish fixed-variance Gaussian conditional training, the full bound/path objective, reweighted simple denoising loss, and image likelihood. Page 123 distinguishes ordinary cross-entropy training from RLHF.
- Sources/version: [pinned deck](https://github.com/albert-no/slides/blob/cdc2949fd21af93b014994acb56a4c048a95becb/courses/deepmath/prob07-estimation/prob07-estimation.html) pp119, 121–127, 135; [note](https://github.com/albert-no/slides/blob/cdc2949fd21af93b014994acb56a4c048a95becb/courses/deepmath/prob07-estimation/prob07-estimation-note.md) §§11.1–11.3, 11.7 and their existing references.
- Setup: preservation requirement; no changed model assumptions, new numbers or new results are proposed.
- Does not establish: that all LLM training is MLE, that every diffusion loss is exact image MLE, or that these are the only generative-model families.
- Label: published result (existing cited lesson; not independently re-audited for this deletion-only plan).

## E04 — Outline and continuity
- Claim: leaf outline describes 137 slides, section 11 on pp118–135 and bridge/closer on pp136–137; its prose includes the removed diagrams, divergence example and GAN-only citations. The surviving Gaussian bridge supports prob08; no dependency on GAN was found in the adjacent-deck descriptions.
- Source/version: [leaf OUTLINE](https://github.com/albert-no/slides/blob/cdc2949fd21af93b014994acb56a4c048a95becb/courses/deepmath/OUTLINE.md), prob07 section/table and prob08 introduction; [root OUTLINE](https://github.com/albert-no/slides/blob/cdc2949fd21af93b014994acb56a4c048a95becb/OUTLINE.md), Deep Learning Math track description.
- Setup: exact current descriptions, not a revised-page calculation. Straight deletion: 137 - 7 = 130; old135→128, old136→129, old137→130.
- Does not establish: that historical logs or independent GAN lessons elsewhere should be altered.
- Label: our calculation (repository inventory and page arithmetic).
