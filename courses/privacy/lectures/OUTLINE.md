# privacy/lectures/ — Privacy lecture series

Master-level series on privacy, copyright, and provenance in generative models. Folders are numbered in reading order (`01-`…`06-`); deck filenames keep their intra-topic numbering (`dp1-…`, `diffusion1-…`, `mia1-…`). Several decks have a paired `<deck>-note.html` companion (notes hold full derivations and proof detail; decks hold rigorous statements + intuition).

Exams live one level up in `../exam/`.

## Subfolders

- **`01-dp/`** — Differential privacy (8 decks). `dp1`–`dp7` build foundations: reconstruction attacks → pure DP → properties → approximate DP → DP-SGD → RDP → DP in ML / PATE. `dp8-fl.html` is the capstone applied talk (NeurIPS 2023). Source LaTeX in `tex/dp.tex`. See `01-dp/OUTLINE.md`.
- **`02-generative/`** — Generative-model review. **Diffusion** (5 lectures, from-scratch Bayes-route, SDE, DDIM, guidance, discrete) and **LLM** (1 brief deck: tokens, decoder-only transformer, NLL pretraining, sampling, privacy hooks). Companion notes: `diffusion3-sde-score-note.html` and `note/2_difffusion.tex` (LaTeX). See `02-generative/OUTLINE.md`.
- **`03-memorization/`** — Memorization in generative models. **Two decks (split 2026-05)**: `memorization-diffusion.html` (intro + lawsuits + Bartz/Anthropic, three formal definitions, diffusion detection, SAIL, CLIP-pad, LLM bridge; math-detail revision 2026-08 — 101 slides, theorem/lemma cards with on-slide proofs, companion `memorization-diffusion-note.html`) and `memorization-llm.html` (math-detail revision 2026-08 — 55 → 128 slides: exposure theory, Feldman, extraction/scaling/alignment, Min-K%/++, ACR, Cooper books, defenses with proofs; companion `memorization-llm-note.html`). Captured paper figures in `figs/`. See `03-memorization/OUTLINE.md`.
- **`04-mia/`** — Membership inference attacks (5 lectures, paired notes). Plus legacy `old/MIA.html`. See `04-mia/OUTLINE.md`.
- **`05-unlearning/`** — Machine unlearning. **Two decks, both math-detail revised 2026-08 with paired notes**: `unlearning1-foundations.html` (107 slides — three nested definitions, certified deletion with full proofs, SISA cost model, classification methods, metrics-as-hypothesis-test) and `unlearning2-llm.html` (29 → 100 slides — why the certificate does not transfer to LLMs, the GA/NPO/SimNPO/ME/ELM/RMU objective family, each benchmark as its own main figure plus a measurement claim, closure under a fine-tuning budget; 17 numbered results, all proved on slide). Captured paper figures in `figs/`. See `05-unlearning/OUTLINE.md`.
- **`06-watermark/`** — LLM watermarking (single deck). Green-list, distortion-free, undetectable, robustness, radioactivity. See `06-watermark/OUTLINE.md`.

## Reading order

1. **`01-dp/`** — differential privacy: the formal privacy backbone (reconstruction → ε-DP → (ε,δ)-DP → DP-SGD → RDP → PATE → DP-FL capstone).
2. **`02-generative/`** — generative-model review (diffusion + LLM); pins down the score, sampling, and per-token loss that every downstream attack plugs into.
3. **`03-memorization/`** — what generative models retain; the *signal* unlearning removes and MIA detects.
4. **`04-mia/`** — membership inference; the detection lens, with DP as its formal bound.
5. **`05-unlearning/`** — machine unlearning; certified/Newton theory reuses DP, evaluation reuses MIA.
6. **`06-watermark/`** — provenance by construction; the opposite direction from memorization.

## Theme connections

- **generative review ↔ everything downstream**: `02-generative/` pins down score, sampling, discrete-space generation; `llm.html` pins down $p_\theta(\cdot\mid x_{<t})$, per-token loss $\ell_t$, the sampling step. MIA / memorization / watermarking / unlearning each plug into one of those pieces (LLM 4-card map at `02-generative/llm.html:1101`).
- **diffusion ↔ llm (within `02-generative/`)**: parallel reviews. Diffusion = continuous score-based generation; LLM = discrete autoregressive counterpart. Privacy attacks differ in mechanism but share targets (training-data leakage, provenance, removal).
- **diffusion ↔ MIA**: diffusion-model MIA is a research frontier — `04-mia/mia4-modern.html:1717-1874` covers it (per-timestep statistic at `:1747`, measured AUC-vs-$t$ peak at `:1811`). The diffusion-models theory in `02-generative/` provides the substrate; the deck carries a self-contained Recall card for the denoising objective at `:1735`.
- **DP ↔ MIA**: `04-mia/mia1-foundations.html:1237-1341` proves the hypothesis-testing region (`α + e^ε β ≥ 1−δ`), the ROC cap (`TPR ≤ e^ε FPR + δ`) and the advantage bound (`Adv ≤ e^ε−1+δ`); `01-dp/dp8-fl.html` builds the DP machinery. DP-SGD is defined and pushed through the ROC cap numerically at `04-mia/mia4-modern.html:1518, :1581`, and the post-processing bound that kills output-side defenses is proved at `:1609, :1632`.
- **DP ↔ unlearning**: certified $(\varepsilon,\delta)$-unlearning reuses the DP definition from `01-dp/dp8-fl.html:375` — same bound, different distribution comparison.
- **memorization ↔ unlearning ↔ MIA**: memorization is the *signal* unlearning aims to remove and MIA aims to detect. `03-memorization/memorization-diffusion.html` + `memorization-llm.html` motivate the other two; defenses slide flows directly into `05-unlearning/`. `05-unlearning/unlearning1-foundations.html:1733` reuses the SalUn MIA-Efficacy column, and Proposition 4 `:1535` bounds what any such column can show.
- **memorization ↔ watermark**: both about provenance under copyright pressure, but opposite directions — memorization detects unintended retention, watermarking adds intended traceability. Same lawsuits motivate both.
- **dgMARK ↔ watermark**: lab thread for diffusion LLMs — full context in `talks/kics260521dllm/kics260521dllm.html:524-569`, broader watermark survey in `06-watermark/`.
- **Theoretical diffusion (`courses/infotheory/lectures/07-diffusion/`) vs from-scratch (`02-generative/`)**: same math, different presentation. The infotheory series uses information-theoretic / hierarchical-VAE framing (cleaner for theory students); the privacy series uses the Bayes-+-Taylor route and goes further (5 lectures including SDE, DDIM, CFG, discrete).

## Quick lookup — cross-deck pointers

| Topic | Where | Lines |
|---|---|---|
| Reconstruction attack (Dinur–Nissim) | `01-dp/dp1-reconstruction.html` | `:181-244` |
| Randomized response + sample complexity | `01-dp/dp2-pure-dp.html` | `:78-148` |
| **$\varepsilon$-DP definition + Laplace mechanism + proof** | `01-dp/dp2-pure-dp.html` | `:172, :275-298` |
| Exponential mechanism + Noisy Max (with proofs) | `01-dp/dp2-pure-dp.html` | `:349-450` |
| Composition + post-processing + group privacy | `01-dp/dp3-properties.html` | `:84-194` |
| **Subsampling amplification proof** | `01-dp/dp3-properties.html` | `:205-273` |
| Why additive DP fails (counterexamples) | `01-dp/dp3-properties.html` | `:296-340` |
| DP $k$-means + privacy proof | `01-dp/dp3-properties.html` | `:354-415` |
| **$(\varepsilon,\delta)$-DP + privacy-loss RV** | `01-dp/dp4-approximate-dp.html` | `:84-128` |
| **Gaussian mechanism + 1-D / multi-D proofs** | `01-dp/dp4-approximate-dp.html` | `:172-244` |
| DP-ERM via exponential mechanism + utility proof | `01-dp/dp5-erm.html` | `:113-160` |
| Advanced composition ($\sqrt k$) | `01-dp/dp5-erm.html` | `:171-201` |
| **DP-SGD algorithm + privacy + utility** | `01-dp/dp5-erm.html` | `:254-315` |
| **Rényi DP definition + Gaussian via RDP proof** | `01-dp/dp6-rdp.html` | `:138-285` |
| Input / Inference / Model DP paradigms | `01-dp/dp7-ml-paradigms.html` | `:78-141` |
| **PATE three-phase architecture** | `01-dp/dp7-ml-paradigms.html` | `:151-220` |
| (ε,δ)-DP definition (capstone restatement) | `01-dp/dp8-fl.html` | `:375-395` |
| Local DP minimax rate | `01-dp/dp8-fl.html` | `:483` |
| PrivUnit mechanism | `01-dp/dp8-fl.html` | `:523` |
| **RRSC + k-closest exact-optimality (NeurIPS 2023)** | `01-dp/dp8-fl.html` | `:571-822` |
| DP-Diffusion / DP-RDM | `01-dp/dp8-fl.html` | `:852-1004` |
| Bayes-route reverse derivation | `02-generative/diffusion1-foundations.html` | `:377-663` |
| Inverse-transform sampling proposition | `02-generative/diffusion1-foundations.html` | `:164` |
| MMSE = conditional mean (+ proof) | `02-generative/diffusion1-foundations.html` | `:620-655` |
| Tweedie's formula (+ proof) | `02-generative/diffusion1-foundations.html` | `:692-753` |
| DDPM VP forward + VLB + ε-loss | `02-generative/diffusion2-ddpm.html` | `:123-915` |
| Fokker–Planck + Anderson reverse SDE | `02-generative/diffusion3-sde-score.html` | `:135-315` |
| Score-matching theorem | `02-generative/diffusion3-sde-score.html` | `:339` |
| DDIM (deterministic, ODE, inversion) | `02-generative/diffusion4-ddim.html` | `:134-281` |
| Classifier-free guidance | `02-generative/diffusion5-guidance-discrete.html` | `:202-282` |
| Discrete diffusion + score-entropy loss | `02-generative/diffusion5-guidance-discrete.html` | `:287-425` |
| LLM overview (tokens, transformer, NLL, post-training, sampling) | `02-generative/llm.html` | `:214, :329, :369` |
| Cross-entropy = entropy + KL; perplexity | `02-generative/llm.html` | `:564, :609, :621` |
| KL-regularized RLHF optimum → DPO (+ NPO preview) | `02-generative/llm.html` | `:822, :929, :951` |
| LLM privacy-hook map (per-token loss / verbatim / sampling / conditional) | `02-generative/llm.html` | `:1101` |
| **Bartz v. Anthropic $1.5B settlement** (Reuters) | `03-memorization/memorization-diffusion.html` | `:162` |
| **Three formal definitions** — extraction / SSCD similarity / Webster taxonomy | `03-memorization/memorization-diffusion.html` | `:269, :426, :518` |
| Diffusion memorization — Carlini 2023 / Somepalli / Webster / Wen / Ross | `03-memorization/memorization-diffusion.html` | `:215-891` |
| **Carlini 2023 — Fig 4 precision + Fig 5 duplicates** | `03-memorization/memorization-diffusion.html` | `:390` |
| **Somepalli 2023 — Fig 5 similarity histograms** | `03-memorization/memorization-diffusion.html` | `:475` |
| **Wen's statistic = implicit classifier gradient** (proposition + proof) | `03-memorization/memorization-diffusion.html` | `:647, :659` |
| **Wen 2024 — Fig 2 magnitude plots** | `03-memorization/memorization-diffusion.html` | `:761` |
| **LID — small-ball definition + Levina–Bickel MLE** | `03-memorization/memorization-diffusion.html` | `:815, :855` |
| **Ross 2024 — LID schematic (Fig 1)** | `03-memorization/memorization-diffusion.html` | `:868` |
| **Theorem — smoothed thin support ($D-k$ eigenvalues at $-\sigma^{-2}$)** | `03-memorization/memorization-diffusion.html` | `:941-1012` |
| **SAIL — sharpness Lemmas 4.1–4.3 + proofs + objective** | `03-memorization/memorization-diffusion.html` | `:892-1421` |
| **SAIL — eigenvalue distribution figure (Fig 3 left)** | `03-memorization/memorization-diffusion.html` | `:1076` |
| **SAIL — Pareto plot (Fig 6 left)** | `03-memorization/memorization-diffusion.html` | `:1398` |
| **CLIP padding-embedding memorization** (Kim & No, CVPR 2026 Findings) | `03-memorization/memorization-diffusion.html` | `:1423-1620` |
| **CLIP-pad attention drop bar chart (Fig 8)** | `03-memorization/memorization-diffusion.html` | `:1558` |
| Secret Sharer canary + exposure theory (Thm 1/2, Prop 2/3) | `03-memorization/memorization-llm.html` | `:196-460` |
| Counterfactual + long-tail (Feldman, Thm 3) | `03-memorization/memorization-llm.html` | `:511-660` |
| Carlini scaling laws + repetition formal + dedup | `03-memorization/memorization-llm.html` | `:856-924` |
| Min-K% / Min-K%++ probes (Prop 6/7) | `03-memorization/memorization-llm.html` | `:1052, :1162` |
| **Adversarial Compression Ratio (ACR)** + Thm 4 counting bound | `03-memorization/memorization-llm.html` | `:1268-1534` |
| Cooper book extraction | `03-memorization/memorization-llm.html` | `:1586-1666` |
| LLM memorization defenses (dedup / DP Thm 5 / $n$-gram blocking) | `03-memorization/memorization-llm.html` | `:1717-1895` |
| Yeom membership advantage (Thm 2, exact) + counterexamples | `04-mia/mia3-theory.html` | `:387, :584-679` |
| Yeom DP bound $e^{\varepsilon}-1$ (Thm 1, proved) | `04-mia/mia3-theory.html` | `:701-764` |
| Sablayrolles: loss is a sufficient statistic (Thm 6 + corollary) | `04-mia/mia3-theory.html` | `:1212-1298` |
| Salem three relaxations as TV perturbations | `04-mia/mia3-theory.html` | `:1655-1699` |
| Nasr rank-one last-layer gradient; trajectories $\succ$ snapshots (DPI) | `04-mia/mia3-theory.html` | `:1920, :2104` |
| LiRA closed form (Thm 1) + calibrated z-score (Cor 1) + calibration dominates (Prop 1) | `04-mia/mia4-modern.html` | `:385, :453, :548` |
| Offline LiRA as a one-sided UMP z-test (Prop 2) | `04-mia/mia4-modern.html` | `:680` |
| Ye conditioning hierarchy (Thm 2, partial order) | `04-mia/mia4-modern.html` | `:951, :1021` |
| RMIA pairwise ratio + rank score (Defs 7–8) | `04-mia/mia4-modern.html` | `:1162, :1200` |
| Label-only boundary distance = logit (Prop 4, Cor 2) | `04-mia/mia4-modern.html` | `:1357, :1381` |
| Post-processing cannot help a defense (Prop 5, Cor 3) | `04-mia/mia4-modern.html` | `:1609, :1632` |
| Calibrated LLM score $\log p_\theta(x)-\log q(x)$ (Def 1) + calibration helps iff (Prop 4) | `04-mia/mia5-llm.html` | `:545, :577` |
| Why pre-training MIA is hard — model-based SNR (Props 1–3, Cor 1) | `04-mia/mia5-llm.html` | `:260, :295, :331, :451` |
| InfoRMIA decomposition (Thm 1) + it is the calibrated score again (Cor 2) | `04-mia/mia5-llm.html` | `:1054, :1089` |
| Blind baselines as a validity failure (Prop 7); per-record instability (Prop 6) | `04-mia/mia5-llm.html` | `:1424, :1306` |
| Extraction implies inference, converse fails (Prop 8); DP AUC ceiling (Prop 9) | `04-mia/mia5-llm.html` | `:1733, :1840` |
| Certified $(\varepsilon,\delta)$ unlearning (Definition 3; Props 1–2, counterexample) | `05-unlearning/unlearning1-foundations.html` | `:259-337` |
| Influence function — derived from the IFT, leads into Newton | `05-unlearning/unlearning1-foundations.html` | `:463-571` |
| Theorems 1–3 (Newton step w/ proof, Gaussian certification, Sekhari capacity) | `05-unlearning/unlearning1-foundations.html` | `:572-983` |
| MIA recall (optimal test, DP cap, Yeom gap) + Proposition 4 (HW4 woven in) | `05-unlearning/unlearning1-foundations.html` | `:1522-1571` |
| SCRUB / SalUn / $\ell_1$-sparse / RURK | `05-unlearning/unlearning1-foundations.html` | `:1241-1412` |
| IDI / COLA (lab) | `05-unlearning/unlearning1-foundations.html` | `:1642-1732` |
| **Why the certificate does not transfer** (P1–P4; Prop 1, Lemmas 2–3, Prop 4, all proved) | `05-unlearning/unlearning2-llm.html` | `:107-460` |
| **GA / NPO / SimNPO / ME / ELM / RMU as one weighted-gradient family** (Props 5/8/9/10, Thms 6/7) | `05-unlearning/unlearning2-llm.html` | `:461-911` |
| TOFU / WMDP / RWKU / MUSE — main figure + measurement claim (Thm 11, Cor 12, Props 13–14) | `05-unlearning/unlearning2-llm.html` | `:912-1304` |
| **Closure under a fine-tuning budget** (Def 15, Prop 16, Cor 17) + benign/syntactic relearning, DUSK, R-TOFU | `05-unlearning/unlearning2-llm.html` | `:1305-1613` |
| Kirchenbauer green-list + entropy bound | `06-watermark/watermark.html` | `:164-222` |
| Gumbel-max trick + proof | `06-watermark/watermark.html` | `:252-295` |
| Aaronson distortion-free proof | `06-watermark/watermark.html` | `:325` |
| Edit-distance robustness theorem | `06-watermark/watermark.html` | `:356` |
| Christ–Gunn–Zamir undetectable + construction | `06-watermark/watermark.html` | `:386-419` |
| Adaptive / WaterMax | `06-watermark/watermark.html` | `:486-516` |
| SynthID-Text production | `06-watermark/watermark.html` | `:542` |

## Pairing convention

Decks in the DP, generative (diffusion), and MIA series have `-note.html` companions. The note generally contains full derivations of theorems stated in the deck, pitfalls / comparison tables, and forward/backward references to other lectures. When in doubt: deck = "what is true"; note = "why and how to apply".
