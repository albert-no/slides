# privacy/unlearning/ — Machine unlearning

Single comprehensive deck on machine unlearning. ~57-slide pass with theory (Newton-step certified, Sekhari deletion capacity, influence function, GA collapse, NPO bounded-loss, Pawelczyk verification hardness) plus full classification + LLM + benchmark + lab thread. Source: `privacy/slide.pdf` and `privacy/privacy.md` reference table.

## Files

| Deck | Topic |
|---|---|
| `unlearning.html` | Foundations · classification · metrics · LLM · benchmarks · lab |

---

## unlearning.html

| Part | Topic | Line |
|---|---|---|
| **01** — Motivation, definition | RTBF, Ginart, certified, Newton, Sekhari, SISA | `:86-243` |
| | Central question | `:96` |
| | Why now (lawsuits + GDPR + memorization) | `:108` |
| | Retraining baseline | `:131` |
| | **Ginart data deletion** $A(\mathcal{D}_{-i}) =_d R_A(\cdot)$ | `:144` |
| | Exact vs approximate | `:157` |
| | **$(\varepsilon,\delta)$-certified unlearning** | `:175` |
| | **Theorem — Newton-step unlearning** (Guo 2020), split: setup `:189`, noise `:202` |
| | **Theorem — deletion capacity** (Sekhari 2021) | `:214` |
| | SISA (sharded, isolated, sliced, aggregated) | `:228` |
| **02** — Classification algorithms | catalog, IU, SCRUB, SalUn, $\ell_1$, RURK | `:245-349` |
| | Method catalog table | `:253` |
| | **Influence function — closed form** (IU) | `:269` |
| | **SCRUB** contrastive distillation | `:286` |
| | **SalUn** weight-saliency mask | `:302` |
| | **$\ell_1$-sparse** unlearning | `:320` |
| | RURK — residual under perturbation | `:336` |
| **03** — Classification metrics | UA/RA/TA/MIA/RTE, IDI, COLA | `:351-448` |
| | Full-stack evaluation | `:359` |
| | MIA loss/entropy probes | `:376` |
| | SalUn benchmark table | `:391` |
| | **IDI** (lab, AAAI 2026) | `:406` |
| | COLA — collapse + align (lab) | `:422` |
| | Over-unlearning (negative IDI) | `:437` |
| **04** — LLM unlearning | GA collapse, NPO, SimNPO, ME+GD, IDK, ECO, ELM, LUNAR | `:450-647` |
| | Why LLMs are different | `:458` |
| | **GA / Knowledge Unlearning** | `:473` |
| | **Why GA collapses** — gradient blow-up | `:489` |
| | **NPO** (DPO-style negative branch) | `:504` |
| | **NPO bounded loss** — sigmoid saturation | `:520` |
| | **SimNPO** (reference-free, length-normalized) | `:536` |
| | **ME+GD** (uniform KL) | `:552` |
| | Who's Harry Potter (Eldan) | `:567` |
| | TOFU IDK refusal | `:582` |
| | Guardrail / ECO | `:599` |
| | ELM concept erasure | `:620` |
| | LUNAR activation redirection (consolidated math) | `:634` |
| **05** — Benchmarks and failures | TOFU/WMDP/RWKU/MUSE, Pawelczyk, position, lab | `:649-858` |
| | TOFU | `:657` |
| | WMDP | `:671` |
| | RWKU | `:684` |
| | MUSE six-way | `:698` |
| | Benign relearning (Hu) | `:714` |
| | Syntactic relearning (lab) | `:727` |
| | Cooper "doesn't do what you think" — 5 mismatches | `:740` |
| | **Theorem — verification hardness** (Pawelczyk 2024) | `:757` |
| | Are we making progress? (Triantafillou 2024 NeurIPS competition) | `:771` |
| | Position (lab) — term overused | `:787` |
| | DUSK — shared knowledge (lab) | `:806` |
| | R-TOFU — reasoning models (lab) | `:819` |
| | SEPS — multi-query separability (lab) | `:832` |
| | Random thoughts | `:845` |

**Key formulas:** Certified $(\varepsilon,\delta)$ `:179`; Newton step `:194`; Newton noise `:206`; Sekhari capacity `:219`; influence function `:272`; SCRUB KL `:288`; SalUn mask `:307-310`; $\ell_1$-sparse `:323`; RURK `:339`; IDI `:410`; GA gradient blow-up `:493`; NPO `:507`; NPO bounded gradient `:524`; SimNPO `:540`; ME+GD `:558`; LUNAR redirection (aligned) `:638`; Pawelczyk hardness `:761`.

**Key theorems:** Newton-step certified (Guo 2020), 2-slide statement `:189, :202`; deletion capacity (Sekhari 2021) `:214`; NPO bounded-divergence `:528`; black-box verification hardness (Pawelczyk 2024) `:757`.

**Lab papers cited:** IDI/COLA (AAAI 2026); R-TOFU (EMNLP 2025); SEPS (EMNLP 2025); DUSK; syntactic relearning (ICLR 2026); position paper (ICML 2026 under review).

**Audit history.** 2026-05 visual audit: split Newton-Step theorem from 1 slide into 2 (was overflowing at bottom); consolidated LUNAR's two math blocks into one `aligned` env (citation was colliding with trailing prose). Total slide count 56 → 57.

---

## Cross-references

- **Memorization** is the motivating signal — see `privacy/memorization/memorization.html`. Lawsuits and Cooper's framing reused.
- **MIA-Efficacy** as evaluation reuses the threshold attacks defined in `privacy/mia/mia1-foundations.html` and the LiRA-style calibration from `privacy/mia/mia4-modern.html`.
- **DP** as the parent of certified unlearning — see `privacy/dp/dp8-fl.html:375` (or the $(\varepsilon,\delta)$-DP definition in `privacy/dp/dp4-approximate-dp.html:81`). Newton-step theorem reuses DP-Gaussian noise calibration.
- **Influence function** also referenced in unlearning literature beyond IU — Sekhari capacity follows from same first-order analysis.
- **Diffusion-LLM watermarking (dgMARK)** is a sibling lab thread — see `dllm/dllm.html:524-569`. Watermark deck `privacy/watermark/watermark.html` is the broader context.
