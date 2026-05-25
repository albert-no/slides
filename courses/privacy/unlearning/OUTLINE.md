# privacy/unlearning/ — Machine unlearning

Single comprehensive deck on machine unlearning. ~50-slide pass with theory (Newton-step certified, Sekhari deletion capacity, influence function, GA collapse, NPO bounded-loss, Pawelczyk verification hardness) plus full classification + LLM + benchmark + lab thread. Source: `privacy/slide.pdf` and `privacy/privacy.md` reference table.

## Files

| Deck | Topic |
|---|---|
| `unlearning.html` | Foundations · classification · metrics · LLM · benchmarks · lab |

---

## unlearning.html

| Part | Topic | Line |
|---|---|---|
| **01** — Motivation, definition | RTBF, Ginart, certified, Newton, Sekhari, SISA | `:86-233` |
| | Central question | `:96` |
| | Why now (lawsuits + GDPR + memorization) | `:108` |
| | Retraining baseline | `:131` |
| | **Ginart data deletion** $A(\mathcal{D}_{-i}) =_d R_A(\cdot)$ | `:144` |
| | Exact vs approximate | `:157` |
| | **$(\varepsilon,\delta)$-certified unlearning** | `:175` |
| | **Theorem — Newton-step unlearning** (Guo 2020) | `:189` |
| | **Theorem — deletion capacity** (Sekhari 2021) | `:204` |
| | SISA (sharded, isolated, sliced, aggregated) | `:218` |
| **02** — Classification algorithms | catalog, IU, SCRUB, SalUn, $\ell_1$, RURK | `:235-339` |
| | Method catalog table | `:243` |
| | **Influence function — closed form** (IU) | `:259` |
| | **SCRUB** contrastive distillation | `:276` |
| | **SalUn** weight-saliency mask | `:292` |
| | **$\ell_1$-sparse** unlearning | `:310` |
| | RURK — residual under perturbation | `:326` |
| **03** — Classification metrics | UA/RA/TA/MIA/RTE, IDI, COLA | `:341-438` |
| | Full-stack evaluation | `:349` |
| | MIA loss/entropy probes | `:366` |
| | SALUN benchmark table | `:381` |
| | **IDI** (lab, AAAI 2026) | `:396` |
| | COLA — collapse + align (lab) | `:412` |
| | Over-unlearning (negative IDI) | `:427` |
| **04** — LLM unlearning | GA collapse, NPO, SimNPO, ME+GD, IDK, ECO, ELM, LUNAR | `:440-639` |
| | Why LLMs are different | `:448` |
| | **GA / Knowledge Unlearning** | `:463` |
| | **Why GA collapses** — gradient blow-up | `:479` |
| | **NPO** (DPO-style negative branch) | `:494` |
| | **NPO bounded loss** — sigmoid saturation | `:510` |
| | **SimNPO** (reference-free, length-normalized) | `:526` |
| | **ME+GD** (uniform KL) | `:542` |
| | Who's Harry Potter (Eldan) | `:557` |
| | TOFU IDK refusal | `:572` |
| | Guardrail / ECO | `:589` |
| | ELM concept erasure | `:610` |
| | LUNAR activation redirection | `:624` |
| **05** — Benchmarks and failures | TOFU/WMDP/RWKU/MUSE, Pawelczyk, position, lab | `:640-849` |
| | TOFU | `:648` |
| | WMDP | `:662` |
| | RWKU | `:675` |
| | MUSE six-way | `:689` |
| | Benign relearning (Hu) | `:705` |
| | Syntactic relearning (lab) | `:718` |
| | Cooper "doesn't do what you think" — 5 mismatches | `:731` |
| | **Theorem — verification hardness** (Pawelczyk 2024) | `:748` |
| | Are we making progress? (Triantafillou 2024 NeurIPS competition) | `:762` |
| | Position (lab) — term overused | `:778` |
| | DUSK — shared knowledge (lab) | `:797` |
| | R-TOFU — reasoning models (lab) | `:810` |
| | SEPS — multi-query separability (lab) | `:823` |
| | Random thoughts | `:836` |
| | Takeaways | `:850` |

**Key formulas:** Certified $(\varepsilon,\delta)$ `:179`; Newton step + noise `:193-201`; Sekhari capacity `:209-211`; influence function `:262`; SCRUB KL `:278`; SalUn mask `:297-300`; $\ell_1$-sparse `:313`; RURK `:329`; IDI `:400`; GA gradient blow-up `:483`; NPO `:497`; NPO bounded gradient `:514`; SimNPO `:530`; ME+GD `:548`; LUNAR redirection `:628-632`; Pawelczyk hardness `:752`.

**Key theorems:** Newton-step certified (Guo 2020) `:191`; deletion capacity (Sekhari 2021) `:206`; NPO bounded-divergence `:518`; black-box verification hardness (Pawelczyk 2024) `:750`.

**Lab papers cited:** IDI/COLA (AAAI 2026); R-TOFU (EMNLP 2025); SEPS (EMNLP 2025); DUSK; syntactic relearning (ICLR 2026); position paper (ICML 2026 under review).

---

## Cross-references

- **Memorization** is the motivating signal — see `privacy/memorization/memorization.html`. Lawsuits and Cooper's framing reused.
- **MIA-Efficacy** as evaluation reuses the threshold attacks defined in `privacy/mia/mia1-foundations.html` and the LiRA-style calibration from `privacy/mia/mia4-modern.html`.
- **DP** as the parent of certified unlearning — see `privacy/dp/dp8-fl.html:375` (or the $(\varepsilon,\delta)$-DP definition in `privacy/dp/dp4-approximate-dp.html:81`). Newton-step theorem reuses DP-Gaussian noise calibration.
- **Influence function** also referenced in unlearning literature beyond IU — Sekhari capacity follows from same first-order analysis.
- **Diffusion-LLM watermarking (dgMARK)** is a sibling lab thread — see `dllm/dllm.html:524-569`. Watermark deck `privacy/watermark/watermark.html` is the broader context.
