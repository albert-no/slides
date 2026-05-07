# privacy/memorization/ — Memorization in generative models

Single deck covering memorization across **diffusion** and **LLM** generation. Diffusion comes first: prior detection metrics (Carlini, Somepalli, Webster, Wen, Ross), then **SAIL** (our ICML 2025 work) developed from full Hessian sharpness theory, then the CLIP-embeddings paper (Kim & No, CVPR 2026 Findings). LLM half: Secret Sharer / exposure / Feldman long-tail, scaling laws, Min-K%/Min-K%++, then **ACR** (Schwarzschild 2024 NeurIPS) as the audit-grade definition.

## Files

| Deck | Topic |
|---|---|
| `memorization.html` | Diffusion (Carlini→Wen→SAIL→CLIP-pad) · LLM (canary→ACR) |

---

## memorization.html

| Part | Topic | Line |
|---|---|---|
| Title / Contents | | `:18-75` |
| **01** — Why memorization matters | central question, lawsuits | `:78-135` |
| | Central question | `:88` |
| | Three stakeholders | `:100` |
| | Live lawsuits 2023–2026 | `:123` |
| **02** — Memorization in diffusion | Carlini 2023, Somepalli, Webster, Wen, LID, **SAIL**, **CLIP-pad** | `:137-484` |
| | Diffusion recap (forward, reverse SDE, score) | `:147` |
| | Carlini 2023 — extracting training images | `:158` |
| | Somepalli 2023 — replication via SSCD | `:174` |
| | Webster 2023 — reproducible extraction (500 prompts) | `:188` |
| | **Wen 2024** — score-norm metric $\|s_\theta^\Delta\|$ | `:201` |
| | Ross 2024 — LID geometric view | `:215` |
| | **Our Method: SAIL** (section divider) | `:240` |
| | **Sharpness setup** — $H(x_t) = \nabla^2 \log p_t$ | `:248` |
| | Memorization $\Leftrightarrow$ sharp peaks (validation) | `:264` |
| | **Lemma 4.1** — score norm = $-\mathrm{tr}(H)$ | `:279` |
| | **Lemma 4.2** — Wen's metric = squared eigenvalue gap | `:292` |
| | **Lemma 4.3** — Hessian-score product = $-\mathrm{tr}(H^3)$ | `:305` |
| | **Proposed metric** $\|H^\Delta s^\Delta\|^2$ — quartic gap | `:318` |
| | Detection results (SD v1.4 / v2.0) | `:329` |
| | SAIL — mitigation by initialization | `:349` |
| | Taylor approximation (avoid 2nd-order autograd) | `:361` |
| | **Final SAIL objective** + algorithm | `:371` |
| | Mitigation results (Pareto SSCD vs CLIP) | `:385` |
| | **CLIP Embeddings Drive Memorization** (section divider) | `:409` |
| | SD text conditioning — four slots | `:417` |
| | **Padding embedding $\approx$ EoT embedding** | `:442` |
| | Mitigation I — replace pad + mask EoT | `:458` |
| | Mitigation II — partial padding mask | `:472` |
| **03** — Defining LLM memorization | Zhang, Carlini 2019, exposure, Feldman | `:485-562` |
| | Zhang 2017 — random labels | `:495` |
| | **Carlini 2019** — Secret Sharer (canary) | `:510` |
| | Exposure — calibrated memorization score | `:524` |
| | Null distribution tail $\Pr[\mathrm{exp}\ge t]\le 2^{-t}$ | `:537` |
| | **Feldman 2020** — long-tail theorem | `:549` |
| **04** — Extraction attacks | Carlini 2021, scaling, dedup, Nasr, Min-K | `:563-693` |
| | **Carlini 2021** — $k$-extractable, GPT-2 | `:573` |
| | Extraction pipeline | `:586` |
| | **Carlini 2022** — three scaling laws | `:609` |
| | Repetition empirical law | `:625` |
| | Lee 2022 — deduplication | `:635` |
| | Nasr 2023 — divergence attack | `:649` |
| | **Min-K% Prob** (Shi 2024) | `:663` |
| | **Min-K%++** (Zhang 2025) | `:678` |
| **05** — Adversarial compression and beyond | ACR, books, defenses | `:694-892` |
| | Why a new definition (gaps in Discoverable / Extractable / CF / MIA) | `:703` |
| | **ACR formal definition** (Schwarzschild 2024) | `:717` |
| | MiniPrompt — search by GCG | `:731` |
| | ACR — what it reveals (compliance theatre) | `:759` |
| | Hayes 2024 — probabilistic extraction | `:774` |
| | Cooper 2025 — books from open-weight LLMs | `:788` |
| | Aerni 2024 — non-adversarial reproduction | `:804` |
| | Defenses (dedup / DP / unlearning) | `:818` |
| | Memorization vs MIA | `:844` |
| | Open problems | `:865` |
| | Takeaways | `:879` |

**Key formulas:** Sharpness Hessian `:252`; Lemma 4.1 score-norm `:284`; Lemma 4.2 squared gap `:298`; Lemma 4.3 cubic trace `:311`; Proposed $\|H^\Delta s^\Delta\|^2$ + quartic gap `:322`; SAIL objective `:354`; Taylor approximation `:365`; final $\mathcal{L}_{\text{SAIL}}$ `:374`; Padding $\approx$ EoT `:447`; Exposure `:529`; Null tail bound `:541`; Long-tail mem `:554`; $k$-extractable `:578`; Repetition law `:629`; Min-K% `:670`; Min-K%++ `:684`; ACR `:723`.

**Key theorems / lemmas:** Long-tail (Feldman 2020) `:554`; Lemmas 4.1 / 4.2 / 4.3 (Jeon-Kim-No 2025) `:284, :298, :311`; ACR definition (Schwarzschild 2024) `:723`.

---

## Cross-references

- **Diffusion preliminaries** at `:147` reuse score-based notation from `privacy/generative/diffusion3-sde-score.html` (forward SDE, reverse SDE via score, classifier-free guidance). No re-derivation here — pointer only.
- **SAIL** (Jeon, Kim, No 2025) is the lab's main contribution and motivates the diffusion sharpness framing. Detection metric extends Wen 2024 via the Hessian-score product (Lemma 4.3 cubic amplification). Mitigation is inference-time noise optimization, leaving prompt and weights untouched.
- **CLIP-pad mitigation** (Kim, No 2026 CVPR Findings) is a complementary inference-time fix — different mechanism, same target prompt set.
- **Carlini 2021** extraction also appears in `privacy/mia/mia5-llm.html:166` (perplexity baseline).
- **Cooper 2025** book extraction motivates the unlearning lectures — see `privacy/unlearning/unlearning.html:108`.
- **ACR** is referenced as the audit benchmark in `privacy/unlearning/unlearning.html` (compliance theatre slide).
- **Memorization vs MIA** comparison links to `privacy/mia/mia1-foundations.html` (membership inference foundations); Min-K%/Min-K%++ are explicit bridges.
- **Defenses → unlearning** flows directly into `privacy/unlearning/unlearning.html`.
