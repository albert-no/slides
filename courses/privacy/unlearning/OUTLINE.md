# privacy/unlearning/ — Machine unlearning

Two-part lecture on machine unlearning, split at the LLM boundary. **Part I** (`unlearning1-foundations.html`) — definitions, certified deletion (full 8-slide Newton derivation), and classical/classification unlearning + metrics. **Part II** (`unlearning2-llm.html`) — LLM unlearning methods and benchmarks/failures. Theory covered: Newton-step certified deletion, Sekhari capacity, influence function, GA collapse, NPO bounded-loss, plus the full classification + LLM + benchmark + lab thread. Source: `privacy/slide.pdf` and `privacy/privacy.md` reference table.

The folder's `hw4sol.pdf` is the 5-problem homework (P1 Neyman–Pearson, P2 DP⇒MIA, P3 Yeom gap, P4 influence unlearning, P5 certified Gaussian). Its hints/roadmaps are taught **inside the Part I slides** — two dedicated "Homework 4" roadmap slides plus the 8-slide Newton derivation that is itself the P4/P5 walk-through. (Do not edit `hw4sol.pdf`; the hints live in the deck.)

## Files

| Deck | Topic |
|---|---|
| `unlearning1-foundations.html` | **Part I** — motivation · definition · certified/Newton · classification algorithms · metrics |
| `unlearning2-llm.html` | **Part II** — LLM methods · benchmarks · failures · lab |

---

## unlearning1-foundations.html (Part I — before LLMs)

| Part | Topic | Line |
|---|---|---|
| | Title (`for a Model to Forget?`) · Contents | `:28`, `:39` |
| **01** — Motivation, definition | RTBF, Ginart, certified, influence→Newton (8-slide), Sekhari, SISA | `:70-341` |
| | Central question | `:80` |
| | Why now (lawsuits / GDPR Art. 17 / memorization + Carlini·Cooper cite) | `:92` |
| | Retraining baseline | `:116` |
| | **Ginart data deletion** $A(\mathcal{D}_{-i}) =_d R_A(\cdot)$ | `:129` |
| | Exact vs approximate | `:142` |
| | **$(\varepsilon,\delta)$-certified unlearning** | `:160` |
| | **Influence function — closed form** (IU, sign $+\tfrac1n H^{-1}\nabla\ell$) — Newton lead-in | `:174` |
| | Newton — why / target (leave-one-out $\theta_{-z}$) | `:191` |
| | Newton — continuous path $L_t$ | `:207` |
| | Newton — differentiating optimality (IFT → influence) | `:226` |
| | **Theorem — Newton-step unlearning** (Guo 2020) | `:237` |
| | Newton — why one step suffices ($O(1/n^2)$ residual) | `:251` |
| | Newton — $L_2$-sensitivity $\le 2G/(\lambda n)$ | `:267` |
| | **Theorem — certified deletion by Gaussian noise** (Guo 2020) | `:278` |
| | Newton — unlearning noise ($1/n^2$) vs DP noise ($1/n$) | `:291` |
| | **Theorem — deletion capacity** (Sekhari 2021) | `:312` |
| | SISA (sharded, isolated, sliced, aggregated) | `:326` |
| **02** — Classification algorithms | catalog, SCRUB, SalUn, $\ell_1$, RURK | `:342-431` |
| | Method catalog table | `:351` |
| | **SCRUB** contrastive distillation | `:367` |
| | **SalUn** weight-saliency mask | `:383` |
| | **$\ell_1$-sparse** unlearning | `:401` |
| | RURK — residual under perturbation | `:417` |
| **03** — Classification metrics | UA/RA/TA/MIA/RTE, IDI, COLA | `:432-546` |
| | Full-stack evaluation | `:440` |
| | MIA loss/entropy probes | `:457` |
| | **MIA: optimal test and its limits** (NP test, Yeom $\Delta/B$ floor, DP cap) | `:472` |
| | SalUn benchmark table | `:487` |
| | **IDI** (lab, AAAI 2026) | `:502` |
| | COLA — collapse + align (lab) | `:518` |
| | Over-unlearning (negative IDI) | `:533` |
| | Takeaways — Part I | `:547` |

## unlearning2-llm.html (Part II — LLM unlearning)

| Part | Topic | Line |
|---|---|---|
| | Title (`for an LLM to Forget?`) · Contents | `:28`, `:39` |
| **01** — LLM unlearning | GA collapse, NPO, SimNPO, ME+GD, IDK, ELM, LUNAR | `:63-241` |
| | Why LLMs are different | `:72` |
| | **GA / Knowledge Unlearning** | `:87` |
| | **Why GA collapses** — gradient blow-up | `:103` |
| | **NPO** (DPO-style negative branch) | `:118` |
| | **NPO bounded loss** — sigmoid saturation | `:134` |
| | **SimNPO** (reference-free, length-normalized) | `:150` |
| | **ME+GD** (uniform KL) | `:166` |
| | Who's Harry Potter (Eldan) | `:181` |
| | TOFU IDK refusal | `:197` |
| | ELM concept erasure (main-figure image `ELM.png`) | `:214` |
| | LUNAR activation redirection (consolidated math) | `:227` |
| **02** — Benchmarks and failures | TOFU/WMDP/RWKU/MUSE, position, lab | `:241-431` |
| | TOFU (main-figure image `tofu.png`) | `:250` |
| | WMDP (main-figure image `WMDP.png`) | `:264` |
| | RWKU (main-figure image `RWKU.png`) | `:277` |
| | MUSE six-way (main-figure image `MUSE.png`) | `:290` |
| | Benign relearning (Hu) | `:303` |
| | Syntactic relearning (lab) | `:316` |
| | Cooper "doesn't do what you think" — 5 mismatches (each glossed) | `:329` |
| | Are we making progress? (Triantafillou 2024 NeurIPS competition) | `:346` |
| | Position (lab) — term overused (Yoon, Jun, No; ICML 2026) | `:362` |
| | DUSK — shared knowledge (lab, main-figure image `DUSK.png`, ACL 2026 Findings) | `:382` |
| | R-TOFU — reasoning models (lab, main-figure image `r-tofu.png`) | `:393` |
| | Random thoughts | `:406` |
| | Takeaways | `:420` |

**Key formulas (Part I):** Certified $(\varepsilon,\delta)$ `1:165`; influence function closed form `1:178` (sign $+\tfrac1n H^{-1}\nabla\ell$, matches Newton step); leave-one-out target `1:196`; continuous path $L_t$ `1:210`; influence via IFT `1:230`; Newton step `1:243`; $L_2$-sensitivity $2G/(\lambda n)$ `1:272`; certified Gaussian-noise $\sigma$ `1:283`; Sekhari capacity `1:317`; SCRUB KL `1:369`; SalUn mask `1:388-391`; $\ell_1$-sparse `1:404`; RURK `1:420`; IDI `1:506`.

**Key formulas (Part II):** GA gradient blow-up `2:107`; NPO `2:121`; NPO bounded gradient `2:138`; SimNPO `2:154`; ME+GD `2:172`; LUNAR redirection (aligned) `2:235`.

**Key theorems:** Newton-step certified (Guo 2020), led in by the influence-function slide `1:174` then an 8-slide derivation `1:191-304` (statement `1:237`, Gaussian-noise certification `1:278`); deletion capacity (Sekhari 2021) `1:312`; NPO bounded-divergence `2:142`.

**Homework-4 in-deck (woven, not labeled):** the influence→Newton→certification block `1:174-304` is the long-form walkthrough of the influence-unlearning and certified-Gaussian problems; the MIA problems (Neyman–Pearson optimal test, DP⇒MIA cap, Yeom gap floor) live naturally on **"MIA: Optimal Test and Its Limits"** `1:472`. No "Homework 4 / Problem N" labels appear on slides — the outline flows inside the lecture content.

**Lab papers cited:** IDI/COLA (AAAI 2026, Part I); R-TOFU (EMNLP 2025, main-figure image); DUSK (ACL 2026 Findings, main-figure image); syntactic relearning (ICLR 2026); position paper (Yoon, Jun, No; ICML 2026) — all Part II. (SEPS slide dropped 2026-06.)

**Audit history.** 2026-05 visual audit: split Newton-Step theorem 1→2 slides; consolidated LUNAR math. 2026-06 revision: every `.cite` shortened to one rendered line; "Why Now" GDPR **Art. 17** confirmed + lawsuits one-per-line + Carlini·Cooper cite; Newton block expanded 2→8 slides; **fixed sign error** on influence-function slide ($+\tfrac1n H^{-1}\nabla\ell$). 2026-06 split: single 63-slide `unlearning.html` retired and split into Part I (`unlearning1-foundations.html`) and Part II (`unlearning2-llm.html`); Part II sections renumbered 01/02. 2026-06 reorder: moved the influence-function slide from §02 up to lead into the Newton block (so the Newton step no longer feels sudden); folded the homework hints into the natural flow (removed the explicit "Homework 4" roadmap slides; the MIA problems became "MIA: Optimal Test and Its Limits"). Part I now 36 slides, Part II 32. 2026-06 benchmark figures: embedded each benchmark's **actual main-figure image** — `tofu.png` (pretrained→finetuned→unlearned pipeline), `WMDP.png` (bio/chem/cyber three-domain pie, 3,668 Q), `RWKU.png` (forget/neighbor/MIA/utility framework), `MUSE.png` (six-way data-owner/deployer grid), `DUSK.png` (forget-all vs forget-unique Venn partitions) — figure dominant + one-line caption (`cite cite-left` added locally); glossed each of Cooper's 5 mismatches; sharpened the Triantafillou "progress" takeaway; **removed the Pawelczyk verification-hardness slide**; venues updated — DUSK → ACL 2026 Findings, position paper → ICML 2026 accepted (Position Track) with an "Accepted · ICML 2026" pill. Part II now 31 slides. (Image PNGs live alongside the deck; `bundle.py` base64-inlines them for the standalone build.) 2026-06 trim: **removed the Guardrail/ECO slide**; replaced ELM's bullet explanation with its main-figure image (`elm.png`). Part II now 30 slides. 2026-06 trim 2: **removed the SEPS slide**; added R-TOFU main-figure image (`r-tofu.png`); on the position slide removed the "Accepted · ICML 2026" pill, corrected authors to **Yoon, Jun, No**, and tightened the proposal wording. Part II now 29 slides.

---

## Cross-references

- **Homework `hw4sol.pdf`** (5-problem) is taught from the Part I slides, woven in without "Homework 4 / Problem N" labels: the influence→Newton→certification block `unlearning1-foundations.html:174-304` is the long-form walkthrough of the influence-unlearning + certified-Gaussian problems, and the MIA problems (NP optimal test, DP⇒MIA cap, Yeom gap floor) live on "MIA: Optimal Test and Its Limits" `1:472`. The deck holds the hints; the PDF is left untouched (do not edit it).
- **Memorization** is the motivating signal — see `privacy/memorization/memorization.html`. Lawsuits and Cooper's framing reused on Part I "Why Now" `1:92`.
- **MIA-Efficacy** as evaluation reuses the threshold attacks defined in `privacy/mia/mia1-foundations.html` and the LiRA-style calibration from `privacy/mia/mia4-modern.html`. The "MIA: Optimal Test and Its Limits" slide `1:472` mirrors that MIA-deck theory.
- **DP** as the parent of certified unlearning — see `privacy/dp/dp8-fl.html:375` (or the $(\varepsilon,\delta)$-DP definition in `privacy/dp/dp4-approximate-dp.html:81`). Newton-step theorem reuses DP-Gaussian noise calibration.
- **Influence function** also referenced beyond IU — Sekhari capacity follows from the same first-order analysis.
- **Diffusion-LLM watermarking (dgMARK)** is a sibling lab thread — see `dllm/dllm.html:524-569`. Watermark deck `privacy/watermark/watermark.html` is the broader context.
