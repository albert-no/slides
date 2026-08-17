# privacy/lectures/06-watermark/ — LLM watermarking

Single deck plus speaker note on watermarking for large language models. **Full math detail (exam material):** detection framed as a hypothesis test throughout, with rigorous statements *and* on-slide proofs for the green-list entropy bound, the Gumbel-max trick, distortion-freeness, edit-distance robustness, CGZ undetectability, and the impossibility results. Sections 06–07 stay survey-shaped but every entry names what is *provable*.

## Files

| Deck | Topic |
|---|---|
| `watermark.html` | Hypothesis test · green-list · Gumbel/Aaronson/Kuditipudi · undetectability (CGZ) · limits · robustness · radioactivity/SynthID/dgMARK |
| `watermark-note.html` | Speaker script, one entry per slide (`#s1`…`#s123`), linked TOC, timings to ~3:55 |

---

## watermark.html — 123 slides

| Part | Topic | Line |
|---|---|---|
| — | Title · Contents | `:41-113` |
| **01** — Detection is a hypothesis test | frame, adversaries, goals, Neyman–Pearson recall | `:116-243` |
| | The central question | `:127` |
| | Why anyone wants this | `:140` |
| | Two adversaries, two errors (removal vs spoofing) | `:154` |
| | Three design goals | `:166` |
| | **Recall — optimal detection** (TV, Neyman–Pearson, LRT) | `:179` |
| | **The frame for the whole lecture** (SVG: two nulls, threshold, TPR/FPR) | `:193` |
| | What a detector must report (TPR@low-FPR, ROC critique) | `:217` |
| | Roadmap | `:230` |
| **02** — The green-list watermark | δ-tilt, z-test, spike entropy, power bound, quality cost | `:245-604` |
| | Core idea — tilt toward green (`.token-safe`/`.token-eos` chips) | `:255` |
| | Setup and notation | `:268` |
| | **Watermarked sampling — the δ-tilt** | `:285` |
| | What the tilt does (SVG logit-shift bars) | `:295` |
| | **Proposition 1 — exact green mass** | `:326` · proof `:340` |
| | The detection statistic | `:351` |
| | **The null hypothesis, stated precisely** | `:361` |
| | **Theorem 2 — why z is standard normal** (CLT) | `:375` · proof `:389` |
| | When the null fails (repeated contexts, low entropy) | `:405` |
| | **The z-test is not optimal** (what the LRT would need) | `:419` |
| | **Definition 3 — spike entropy** | `:432` · extremes `:445` |
| | **Theorem 4 — detection power from entropy** | `:456` · outline `:469` · steps `:486`, `:497`, `:508` |
| | Reading the bound | `:519` |
| | Measured power vs length (figure) | `:532` |
| | **Low-entropy text is unwatermarkable** (SVG) | `:542` |
| | **Theorem 5 — the quality cost** (corrected direction) | `:563` · proof `:577` |
| | Green-list is *not* distortion-free | `:588` |
| | The one knob δ (figure) | `:598` |
| **03** — Distortion-free sampling | Gumbel-max, Aaronson, Kuditipudi ITS, Hu reweighting | `:606-1024` |
| | What would "free" mean? | `:616` |
| | Recall — the Gumbel distribution | `:628` |
| | **Theorem 6 — the Gumbel-max trick** | `:641` · outline `:655` · steps `:683`, `:694` |
| | Corollary — the max carries no information | `:692` |
| | Three faces of one sampler (recap chain) | `:703` |
| | The picture (SVG argmax) | `:713` |
| | Alternative proof — exponential minimum | `:744` |
| | Aaronson's rule | `:755` · **Proposition 7 — Aaronson ≡ Gumbel-max** `:766` |
| | **Definition 8 — distortion-free** | `:777` |
| | **Theorem 9 — exponential minimum is distortion-free** | `:790` |
| | **What distortion-free does *not* say** (SVG, two quantifiers) | `:803` |
| | The fine print: one key, many calls (Lemma 2.1) | `:823` |
| | Kuditipudi — inverse transform sampling | `:836` · **Theorem 10** `:847` |
| | Detection without the model | `:861` · permutation-test p-value `:872` |
| | **Lemma 11 — why the cost separates** | `:888` |
| | **Definition 12 — watermark potential** | `:902` |
| | **Lemma 13 — the clean p-value bound** | `:917` |
| | **Definition 14 — cost under edits** (Levenshtein) | `:930` |
| | **Lemma 15 — edit-distance robustness** | `:944` · honest reading `:957` |
| | What actually survives (figure) | `:970` |
| | **Definition 16 — unbiased reweighting** | `:980` · two reweightings + **Theorem 17** `:994` |
| | **Theorem 18 — from one token to a sequence** | `:1014` |
| **04** — Undetectability (CGZ) | computational indistinguishability, PRF construction | `:1026-1280` |
| | **Recall — indistinguishability and post-processing** | `:1036` |
| | **Definition 19 — a watermarking scheme** | `:1049` |
| | **Definition 20 — empirical entropy** | `:1066` |
| | **Definitions 21–22 — sound and complete** | `:1080` · **Definition 23** (substring-complete) `:1094` |
| | **Definition 24 — undetectable** | `:1107` |
| | **Distortion-free ≠ undetectable** (SVG) | `:1121` · separation `:1142` |
| | Warm-up construction | `:1152` · min-entropy necessity `:1169` · 6λ split `:1181` |
| | **Theorem 25 — the warm-up, with a PRF** | `:1197` |
| | The efficient scheme, one bit at a time | `:1210` · **detection score** `:1221` |
| | **Proposition 26 — the score gap is entropy** | `:1231` · proof `:1246` |
| | From one response to many (nonce) | `:1257` |
| | **Theorems 27–28 — the main results** | `:1270` |
| **05** — Limits and impossibility | entropy floors, generic removal, tradeoff | `:1282-1435` |
| | **Lemma 29 — model entropy is the wrong quantity** | `:1292` |
| | **Theorem 30 — low entropy cannot be watermarked** | `:1305` |
| | **Lemma 31 — undetectability is only computational** | `:1320` |
| | **Lemma 32 — the distortion-free impossibility** | `:1333` · measured `:1347` |
| | **Proposition 33 — detection costs distortion** (derived by Claude) | `:1357` · proof `:1372` · curve `:1383` |
| | **Theorem 34 — undetectable implies removable** | `:1404` |
| | The three-way tension (SVG triangle) | `:1417` |
| **06** — Robustness and semantics | paraphrase, Unigram-Watermark, adaptive δ | `:1437-1648` |
| | The attack surface (SVG pipeline) | `:1447` |
| | **What paraphrase actually costs** (verbatim ICLR 2024 result) | `:1481` |
| | Fix the green list (Unigram-Watermark algorithm) | `:1500` |
| | **Theorem 35 — the tilt is a DP-style perturbation** (Rényi) | `:1519` |
| | **Theorem 36 — power, and the assumption it hides** (homophily) | `:1534` |
| | **Theorem 37 — surviving η edits** | `:1555` · proof `:1570` |
| | Three ways to make the signal survive | `:1587` |
| | **Spend δ where the entropy is** (adaptive δ_t) | `:1616` |
| | Reading a robustness table honestly | `:1634` |
| **07** — Beyond standard LLMs | radioactivity, SynthID-Text, dgMARK | `:1650-1819` |
| | **Definitions 38–39 — radioactivity** | `:1660` |
| | **Proposition 40 — de-duplication buys back the null** | `:1676` |
| | Why this is a membership-inference result | `:1690` |
| | How little watermarked data is enough (figure) | `:1707` |
| | Production scale: tournament sampling (figure) | `:1718` |
| | Detection + three grades of "non-distortionary" | `:1729` |
| | When there is no "previous token" (dgMARK figure) | `:1747` |
| | **dgMARK — steer the order, not the probabilities** | `:1758` |
| | **dgMARK detection — the same z-test, new indicator** | `:1775` |
| | Open problems | `:1788` · Takeaways `:1802` · Closer `:1815` |

**Key formulas:** z-statistic `:355`; δ-tilt `:289`; spike entropy `:435`; power bound `:461`; Gumbel construction `:632`; Aaronson rule `:759`; ITS decoder `:840`; alignment cost `:865`; Levenshtein cost `:936`; CGZ empirical entropy `:1069`; **CGZ detection score** `:1225`; tradeoff proposition `:1363`; Rényi bound `:1524`; **survive-edits bound** `:1560`; **adaptive δ_t** `:1622`; SynthID score `:1731`; dgMARK parity + z `:1775`, `:1792`.

**Key theorems with proofs on the slides.** Prop 1 `:326`/`:340` · Thm 2 `:375`/`:389` · **Thm 4** `:456`/`:469`-`:508` · **Thm 5** `:563`/`:577` · **Thm 6 Gumbel-max** `:641`/`:655`-`:688`, alt proof `:744` · Prop 7 `:766` · Thm 9 `:790` · Thm 10 `:847` · Lemmas 11/13/15 `:888`/`:917`/`:944` · Thms 17–18 `:1008`/`:1014` · Thm 25 `:1197` · **Prop 26** `:1231`/`:1246` · Thms 27–28 `:1270` · Lemma 29 `:1292` · Thm 30 `:1305` · Lemmas 31–32 `:1320`/`:1333` · **Prop 33 (derived by Claude)** `:1357`/`:1372` · Thm 34 `:1404` · Thms 35–36 `:1519`/`:1534` · **Thm 37** `:1555`/`:1570` · Prop 40 `:1676`.

**Figures** (`figs/`, captured from source PDFs):

| File | Source |
|---|---|
| `kgw-tradeoff.png` | Kirchenbauer et al., ICML 2023 — Figure 2 (left) |
| `kgw-power.png` | Kirchenbauer et al., ICML 2023 — Figure 3(b) |
| `kud-substitution.png` | Kuditipudi et al., TMLR 2024 — Figure 4(b) |
| `kud-potential.png` | Kuditipudi et al., TMLR 2024 — Figure 11(a) |
| `radioactivity-pvalue.png` | Sander et al., NeurIPS 2024 — Figure 5 |
| `synthid-tournament.png` | Dathathri et al., Nature 634 (2024) — Figure 2 (bottom) |
| `dgmark-overview.png` | Hong & No, ICML 2026 — Figure 1 |

**Corrections carried by this deck.**

- **Kirchenbauer et al. Theorem 4.3 is stated here with its inequality reversed relative to the published version.** The paper prints $\mathbb{E}\sum_k \hat p_k \ln p_k \le \beta P^\star$ with $P^\star = \sum_k p_k \ln p_k \le 0$ and $\beta \ge 1$, which asserts a *lower* bound on the perplexity damage. Their Appendix F establishes $\mathbb{E}[\hat p_k] \le \beta p_k$ correctly, then multiplies through by the negative $\ln p_k$ without flipping the sense. The deck states the corrected upper bound $\mathbb{E}[-\sum_k \hat p_k \ln p_k] \le \beta H(p)$ and proves it in two steps at `:577`; the full erratum, including two smaller slips in the same appendix, is `watermark-note.html#s36`.
- **Proposition 33 (`:1357`) is not from the literature** — written and derived by Claude for this deck by algebra on Theorems 4 and 5. Both the slide and note `#s95` say so.

**Audit history.**

- **2026-08-17 Theorem 4.3 correction.** 122 → 123 slides. Theorem 5 restated in the correct direction with a two-step proof slide added (`:577`); Proposition 33 labelled as Claude-derived on the slide and in the note. Note file realigned to 123 entries.
- **2026-08 math-detail revision (reverses the 2026-06 pass).** 30 → 122 slides. Detection is now framed as a hypothesis test from slide 9 and reused throughout. **Restored in full:** the Gumbel-max proof (Thm 6, four steps + an exponential-minimum alternative), the Aaronson derivation (Prop 7), the **CGZ detection score** equation, the **survive-edits bound** (Zhao Thm 3.7) with its Taylor-step proof, and the **adaptive δ_t** equations (Liu & Bu Eqs. 3 and 5). **New:** Section 01 (hypothesis-test frame, Neyman–Pearson recall) and Section 05 (limits and impossibility, including a tradeoff proposition derived for this deck). Kirchenbauer Thm 4.2 now carries a four-step proof; CGZ undetectability is developed from Definitions 19–24 to Theorems 27–28. 11 deck-local SVG figures plus 7 captured paper figures. Companion `watermark-note.html` added. Deck is no longer a high-level overview.
- **2026-06 high-level overview pass (superseded).** Deleted the full Gumbel-max proof and Aaronson derivation (replaced with intuition); added the green/red token-visual slide; removed equations after the undetectable slide (CGZ score, survive-edits TPR, adaptive δ_t); consolidated the method survey. Deck was 30 slides.

---

## Cross-references

- **Hypothesis testing, Neyman–Pearson, TPR@low-FPR, ROC critique** are owned by `privacy/lectures/04-mia/mia4-modern.html`; this deck recalls them in self-contained cards (`:179`, `:217`) rather than restating.
- **Per-example calibration and the blind baseline** (`04-mia/mia5-llm.html`) are the reference point for the radioactivity/MIA comparison at `:1690`.
- **(ε,δ)-DP, indistinguishability, post-processing** are owned by `privacy/lectures/01-dp/`; recalled at `:1036` and reused in Theorem 35 (`:1519`).
- **Autoregressive factorization, temperature/softmax sampling, next-token entropy** come from `privacy/lectures/02-generative/llm.html`; assumed in the Section 02 setup (`:268`).
- **Measurement-validity discipline** follows `privacy/lectures/05-unlearning/` §03; applied at `:1634`.
- **Extractable vs discoverable memorization** (`privacy/lectures/03-memorization/memorization-llm.html`) is the provenance motivation for radioactivity (`:1660`).
- **dgMARK** is the lab's diffusion-LLM watermark — broader dLLM context lives in `talks/kics260521dllm/kics260521dllm.html:707`.
