# privacy/watermark/ — LLM watermarking

Single deck on watermarking for large language models. Detection, distortion-free, undetectable, robustness. Theory-rigorous: Gumbel-max theorem with proof, Aaronson distortion-free proof, z-test entropy bound, CGZ construction, edit-distance robustness theorem.

## Files

| Deck | Topic |
|---|---|
| `watermark.html` | Green-list · Gumbel-max · Aaronson/Kuditipudi · undetectable · robust · radioactivity |

---

## watermark.html

| Part | Topic | Line |
|---|---|---|
| **01** — Why watermark text | central question, three goals | `:77-154` |
| | Central question | `:87` |
| | Use cases (provenance / disinfo / data hygiene) | `:99` |
| | **Three design goals** (detect / quality / robust) | `:122` |
| | Adversary model (removal vs spoofing) | `:137` |
| **02** — Green-list (Kirchenbauer) | sampling rule, z-test, entropy bound | `:156-242` |
| | Setup ($\gamma, \delta, h$) | `:164` |
| | **Watermarked sampling** $\hat p_\theta$ | `:178` |
| | **Detection z-test** | `:192` |
| | **Detection power — entropy bound** | `:207` |
| | Quality–detect tradeoff | `:224` |
| **03** — Distortion-free / undetectable | Gumbel, Aaronson proof, edit-distance, CGZ | `:244-419` |
| | **Recall — Gumbel distribution** | `:252` |
| | **Theorem — Gumbel-max trick** | `:268` |
| | **Proof — Gumbel-max** | `:283` |
| | **Distortion-free definition** | `:297` |
| | Aaronson Gumbel rule | `:309` |
| | **Aaronson is distortion-free** (proof) | `:325` |
| | Kuditipudi inverse-transform + edit distance | `:340` |
| | **Theorem — edit-distance robustness** | `:356` |
| | Hu unbiased family | `:372` |
| | **Undetectable** definition (CGZ) | `:386` |
| | **CGZ construction** — PRF-based | `:403` |
| **04** — Robustness and semantics | paraphrase, fixed-list, semantic, adaptive | `:421-516` |
| | Paraphrase attack | `:429` |
| | Provable robust (Zhao) | `:445` |
| | **Semantic-invariant** watermark (Liu) | `:459` |
| | Permute-and-flip | `:473` |
| | **Adaptive watermark** (Liu 2024) | `:486` |
| | **WaterMax** (Giboulot 2024) | `:502` |
| **05** — Beyond standard LLMs | radioactivity, SynthID, dgMARK | `:518-595` |
| | **Radioactive** watermarks (training tracer) | `:526` |
| | SynthID-Text (Nature 2024) | `:542` |
| | dgMARK — diffusion-LLM (lab) | `:556` |
| | Open problems | `:570` |
| | Takeaways | `:583` |

**Key formulas:** Watermarked sampling `:180`; z-test `:194`; entropy bound on power `:210`; Gumbel density / construction `:256`; Aaronson rule `:317`; Gumbel-max equivalence `:333`; CGZ score `:415`; adaptive bias `:490`.

**Key theorems:** Gumbel-max trick + proof `:271 + :286`; Aaronson distortion-free `:325`; Edit-distance robustness (Kuditipudi) `:359`; Undetectable definition (CGZ) `:389`.

---

## Cross-references

- **dgMARK** is the lab's diffusion-LLM watermark — broader dLLM context lives in `dllm/dllm.html:524-569`.
- **Radioactivity** connects watermarking to MIA-style training-data detection — see `privacy/mia/mia5-llm.html` for the LLM MIA context.
- **Memorization** motivates the broader provenance pipeline — `privacy/memorization/memorization.html`.
