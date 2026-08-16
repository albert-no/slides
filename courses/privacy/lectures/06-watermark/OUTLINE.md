# privacy/lectures/06-watermark/ — LLM watermarking

Single deck plus speaker note on watermarking for large language models. **Full math detail (exam material):** detection framed as a hypothesis test throughout, with rigorous statements *and* on-slide proofs for the green-list entropy bound, the Gumbel-max trick, distortion-freeness, edit-distance robustness, CGZ undetectability, and the impossibility results. Sections 06–07 stay survey-shaped but every entry names what is *provable*.

## Files

| Deck | Topic |
|---|---|
| `watermark.html` | Hypothesis test · green-list · Gumbel/Aaronson/Kuditipudi · undetectability (CGZ) · limits · robustness · radioactivity/SynthID/dgMARK |
| `watermark-note.html` | Speaker script, one entry per slide (`#s1`…`#s122`), linked TOC, timings to ~3:55 |

---

## watermark.html — 122 slides

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
| **02** — The green-list watermark | δ-tilt, z-test, spike entropy, power bound, quality cost | `:245-592` |
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
| | **Theorem 5 — the quality cost** | `:563` |
| | Green-list is *not* distortion-free | `:576` |
| | The one knob δ (figure) | `:586` |
| **03** — Distortion-free sampling | Gumbel-max, Aaronson, Kuditipudi ITS, Hu reweighting | `:594-1012` |
| | What would "free" mean? | `:604` |
| | Recall — the Gumbel distribution | `:616` |
| | **Theorem 6 — the Gumbel-max trick** | `:629` · outline `:643` · steps `:659`, `:670` |
| | Corollary — the max carries no information | `:680` |
| | Three faces of one sampler (recap chain) | `:691` |
| | The picture (SVG argmax) | `:701` |
| | Alternative proof — exponential minimum | `:732` |
| | Aaronson's rule | `:743` · **Proposition 7 — Aaronson ≡ Gumbel-max** `:754` |
| | **Definition 8 — distortion-free** | `:765` |
| | **Theorem 9 — exponential minimum is distortion-free** | `:778` |
| | **What distortion-free does *not* say** (SVG, two quantifiers) | `:791` |
| | The fine print: one key, many calls (Lemma 2.1) | `:811` |
| | Kuditipudi — inverse transform sampling | `:824` · **Theorem 10** `:835` |
| | Detection without the model | `:849` · permutation-test p-value `:860` |
| | **Lemma 11 — why the cost separates** | `:876` |
| | **Definition 12 — watermark potential** | `:890` |
| | **Lemma 13 — the clean p-value bound** | `:905` |
| | **Definition 14 — cost under edits** (Levenshtein) | `:918` |
| | **Lemma 15 — edit-distance robustness** | `:932` · honest reading `:945` |
| | What actually survives (figure) | `:958` |
| | **Definition 16 — unbiased reweighting** | `:968` · two reweightings + **Theorem 17** `:982` |
| | **Theorem 18 — from one token to a sequence** | `:1002` |
| **04** — Undetectability (CGZ) | computational indistinguishability, PRF construction | `:1014-1268` |
| | **Recall — indistinguishability and post-processing** | `:1024` |
| | **Definition 19 — a watermarking scheme** | `:1037` |
| | **Definition 20 — empirical entropy** | `:1054` |
| | **Definitions 21–22 — sound and complete** | `:1068` · **Definition 23** (substring-complete) `:1082` |
| | **Definition 24 — undetectable** | `:1095` |
| | **Distortion-free ≠ undetectable** (SVG) | `:1109` · separation `:1130` |
| | Warm-up construction | `:1140` · min-entropy necessity `:1157` · 6λ split `:1169` |
| | **Theorem 25 — the warm-up, with a PRF** | `:1185` |
| | The efficient scheme, one bit at a time | `:1198` · **detection score** `:1209` |
| | **Proposition 26 — the score gap is entropy** | `:1219` · proof `:1234` |
| | From one response to many (nonce) | `:1245` |
| | **Theorems 27–28 — the main results** | `:1258` |
| **05** — Limits and impossibility | entropy floors, generic removal, tradeoff | `:1270-1422` |
| | **Lemma 29 — model entropy is the wrong quantity** | `:1280` |
| | **Theorem 30 — low entropy cannot be watermarked** | `:1293` |
| | **Lemma 31 — undetectability is only computational** | `:1308` |
| | **Lemma 32 — the distortion-free impossibility** | `:1321` · measured `:1335` |
| | **Proposition 33 — detection costs distortion** (derived here) | `:1345` · proof `:1359` · curve `:1370` |
| | **Theorem 34 — undetectable implies removable** | `:1391` |
| | The three-way tension (SVG triangle) | `:1404` |
| **06** — Robustness and semantics | paraphrase, Unigram-Watermark, adaptive δ | `:1424-1635` |
| | The attack surface (SVG pipeline) | `:1434` |
| | **What paraphrase actually costs** (verbatim ICLR 2024 result) | `:1468` |
| | Fix the green list (Unigram-Watermark algorithm) | `:1487` |
| | **Theorem 35 — the tilt is a DP-style perturbation** (Rényi) | `:1506` |
| | **Theorem 36 — power, and the assumption it hides** (homophily) | `:1521` |
| | **Theorem 37 — surviving η edits** | `:1542` · proof `:1557` |
| | Three ways to make the signal survive | `:1574` |
| | **Spend δ where the entropy is** (adaptive δ_t) | `:1603` |
| | Reading a robustness table honestly | `:1621` |
| **07** — Beyond standard LLMs | radioactivity, SynthID-Text, dgMARK | `:1637-1806` |
| | **Definitions 38–39 — radioactivity** | `:1647` |
| | **Proposition 40 — de-duplication buys back the null** | `:1663` |
| | Why this is a membership-inference result | `:1677` |
| | How little watermarked data is enough (figure) | `:1694` |
| | Production scale: tournament sampling (figure) | `:1705` |
| | Detection + three grades of "non-distortionary" | `:1716` |
| | When there is no "previous token" (dgMARK figure) | `:1734` |
| | **dgMARK — steer the order, not the probabilities** | `:1745` |
| | **dgMARK detection — the same z-test, new indicator** | `:1762` |
| | Open problems | `:1775` · Takeaways `:1789` · Closer `:1802` |

**Key formulas:** z-statistic `:355`; δ-tilt `:289`; spike entropy `:435`; power bound `:461`; Gumbel construction `:620`; Aaronson rule `:747`; ITS decoder `:828`; alignment cost `:853`; Levenshtein cost `:924`; CGZ empirical entropy `:1057`; **CGZ detection score** `:1213`; tradeoff proposition `:1351`; Rényi bound `:1511`; **survive-edits bound** `:1547`; **adaptive δ_t** `:1609`; SynthID score `:1718`; dgMARK parity + z `:1749`, `:1766`.

**Key theorems with proofs on the slides.** Prop 1 `:326`/`:340` · Thm 2 `:375`/`:389` · **Thm 4** `:456`/`:469`-`:508` · Thm 5 `:563` · **Thm 6 Gumbel-max** `:629`/`:643`-`:676`, alt proof `:732` · Prop 7 `:754` · Thm 9 `:778` · Thm 10 `:835` · Lemmas 11/13/15 `:876`/`:905`/`:932` · Thms 17–18 `:996`/`:1002` · Thm 25 `:1185` · **Prop 26** `:1219`/`:1234` · Thms 27–28 `:1258` · Lemma 29 `:1280` · Thm 30 `:1293` · Lemmas 31–32 `:1308`/`:1321` · **Prop 33 (derived here)** `:1345`/`:1359` · Thm 34 `:1391` · Thms 35–36 `:1506`/`:1521` · **Thm 37** `:1542`/`:1557` · Prop 40 `:1663`.

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

**Audit history.**

- **2026-08 math-detail revision (reverses the 2026-06 pass).** 30 → 122 slides. Detection is now framed as a hypothesis test from slide 9 and reused throughout. **Restored in full:** the Gumbel-max proof (Thm 6, four steps + an exponential-minimum alternative), the Aaronson derivation (Prop 7), the **CGZ detection score** equation, the **survive-edits bound** (Zhao Thm 3.7) with its Taylor-step proof, and the **adaptive δ_t** equations (Liu & Bu Eqs. 3 and 5). **New:** Section 01 (hypothesis-test frame, Neyman–Pearson recall) and Section 05 (limits and impossibility, including a tradeoff proposition derived for this deck). Kirchenbauer Thm 4.2 now carries a four-step proof; CGZ undetectability is developed from Definitions 19–24 to Theorems 27–28. 11 deck-local SVG figures plus 7 captured paper figures. Companion `watermark-note.html` added. Deck is no longer a high-level overview.
- **2026-06 high-level overview pass (superseded).** Deleted the full Gumbel-max proof and Aaronson derivation (replaced with intuition); added the green/red token-visual slide; removed equations after the undetectable slide (CGZ score, survive-edits TPR, adaptive δ_t); consolidated the method survey. Deck was 30 slides.

---

## Cross-references

- **Hypothesis testing, Neyman–Pearson, TPR@low-FPR, ROC critique** are owned by `privacy/lectures/04-mia/mia4-modern.html`; this deck recalls them in self-contained cards (`:179`, `:217`) rather than restating.
- **Per-example calibration and the blind baseline** (`04-mia/mia5-llm.html`) are the reference point for the radioactivity/MIA comparison at `:1677`.
- **(ε,δ)-DP, indistinguishability, post-processing** are owned by `privacy/lectures/01-dp/`; recalled at `:1024` and reused in Theorem 35 (`:1506`).
- **Autoregressive factorization, temperature/softmax sampling, next-token entropy** come from `privacy/lectures/02-generative/llm.html`; assumed in the Section 02 setup (`:268`).
- **Measurement-validity discipline** follows `privacy/lectures/05-unlearning/` §03; applied at `:1621`.
- **Extractable vs discoverable memorization** (`privacy/lectures/03-memorization/memorization-llm.html`) is the provenance motivation for radioactivity (`:1647`).
- **dgMARK** is the lab's diffusion-LLM watermark — broader dLLM context lives in `talks/kics260521dllm/kics260521dllm.html:707`.
