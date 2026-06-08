# privacy/lectures/06-watermark/ — LLM watermarking

Single deck on watermarking for large language models. Detection, distortion-free, undetectable, robustness. **High-level overview** (not exam material): theorem *statements* kept (Gumbel-max, edit-distance robustness, entropy bound) with intuition rather than full proofs; method survey consolidated.

## Files

| Deck | Topic |
|---|---|
| `watermark.html` | Green-list · Gumbel-max · Aaronson/Kuditipudi · undetectable · robust · radioactivity |

---

## watermark.html

| Part | Topic | Line |
|---|---|---|
| **01** — Why watermark text | central question, three goals | `:77-149` |
| | Central question (one-line framing) | `:87` |
| | Use cases (provenance / disinfo / data hygiene) | `:97` |
| | **Three design goals** (detect / quality / robust) | `:117` |
| | Two kinds of attack (removal vs spoofing) | `:131` |
| **02** — Green-list (Kirchenbauer) | tilt-toward-green, z-test, entropy bound | `:150-255` |
| | **Core idea — tilt toward green** (token visual) | `:160` |
| | Setup ($\gamma, \delta$) | `:178` |
| | **Watermarked sampling** $\hat p_\theta$ | `:191` |
| | **Detection z-test** | `:205` |
| | **Detection power — entropy bound** (statement + intuition) | `:220` |
| | Core tradeoff — one knob $\delta$ | `:237` |
| **03** — Distortion-free / undetectable | Gumbel-max, Aaronson, edit-distance, CGZ | `:256-422` |
| | Recall — Gumbel distribution | `:266` |
| | **Theorem — Gumbel-max trick** (statement + idea) | `:281` |
| | **Why it works — proof sketch** (rough proof) | `:296` |
| | **Distortion-free definition** | `:311` |
| | Aaronson Gumbel rule | `:323` |
| | Why it is distortion-free (intuition) | `:338` |
| | Kuditipudi inverse-transform + edit distance | `:352` |
| | **Theorem — edit-distance robustness** (statement) | `:368` |
| | Unbiased family (Hu) | `:383` |
| | **Undetectable** definition (CGZ) | `:396` |
| | **CGZ construction** — PRF-based (no equation) | `:411` |
| **04** — Robustness and semantics | paraphrase, fixed-list/semantic/PF, quality-first | `:423-487` |
| | Paraphrase attack | `:433` |
| | Making the signal survive edits (fixed-list · semantic · permute-flip) | `:449` |
| | Quality-first decoding (adaptive · WaterMax) | `:471` |
| **05** — Beyond standard LLMs | radioactivity, SynthID, dgMARK | `:488-564` |
| | **Radioactive** watermarks (training tracer) | `:498` |
| | SynthID-Text (Nature 2024) | `:513` |
| | dgMARK — diffusion-LLM (lab) | `:528` |
| | Open problems | `:541` |
| | Takeaways | `:553` |

**Key formulas:** Watermarked sampling `:193`; z-test `:209`; entropy bound on power `:224`; Gumbel construction `:270`; proof-sketch steps `:300`; Aaronson rule `:328`; Gumbel disguise identity `:343`; edit-distance bound `:372`.

**Key theorems (statements kept, proofs as intuition):** Gumbel-max trick `:284` + exponential-min proof sketch `:296`; Edit-distance robustness (Kuditipudi) `:370`; Undetectable definition (CGZ) `:399`.

**Audit history.** 2026-06 high-level overview pass: deleted full Gumbel-max proof and Aaronson derivation (replaced with intuition); added a green/red-list **token-visual** slide (`.token-safe`/`.token-eos` chips) before Setup and a **proof sketch** for Gumbel-max (exponential-min argument); restructured the δ/γ tradeoff into a single-knob (δ) two-card slide; reframed adversary slide (clearer spoofing); clarified "disinformation" on the use-cases slide; removed equations after the undetectable slide (CGZ score, survive-edits TPR, adaptive δ_t); shortened every citation to a single line; broad minimalism trim. Deck now 37 slides (incl. title, dividers, closer). Theorem *statements* retained.

---

## Cross-references

- **dgMARK** is the lab's diffusion-LLM watermark — broader dLLM context lives in `dllm/dllm.html:524-569`.
- **Radioactivity** connects watermarking to MIA-style training-data detection — see `privacy/lectures/04-mia/mia5-llm.html` for the LLM MIA context.
- **Memorization** motivates the broader provenance pipeline — `privacy/lectures/03-memorization/memorization.html`.
