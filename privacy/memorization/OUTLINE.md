# privacy/memorization/ — LLM memorization

Single deck on memorization in language models. Theory-focused: canary entropy / exposure null distribution, $k$-extractable, Feldman counterfactual memorization (long-tail theorem), repetition scaling law, Min-K%++ probe.

## Files

| Deck | Topic |
|---|---|
| `memorization.html` | Definition · extraction · scaling · books · copyright |

---

## memorization.html

| Part | Topic | Line |
|---|---|---|
| **01** — Why memorization matters | central question, lawsuits, GDPR | `:77-153` |
| | Central question | `:87` |
| | Three stakeholders | `:99` |
| | NYT / Authors / Getty / Disney lawsuits | `:122` |
| | GDPR + EU AI Act framing | `:136` |
| **02** — Defining memorization | Zhang generalization, Carlini canary, Feldman | `:155-304` |
| | Zhang 2017 — random labels | `:163` |
| | **Canaries** (Secret Sharer) | `:179` |
| | **Canary entropy / threat model** $H(s) = \log_2|\mathcal{R}|$ | `:194` |
| | **Exposure metric** | `:210` |
| | **Exposure null distribution** $\Pr_{H_0}[\text{exp} \ge t] \le 2^{-t}$ | `:226` |
| | **$k$-extractable** definition (Carlini 2021) | `:241` |
| | Three regimes — counterfactual / verbatim / probabilistic | `:254` |
| | **Counterfactual memorization** (Feldman / Zhang) | `:277` |
| | **Theorem: long-tail** — memorization is necessary | `:291` |
| **03** — Extraction attacks | GPT-2, scaling, dedup, Min-K%++ | `:306-427` |
| | Carlini 2021 GPT-2 extraction | `:314` |
| | Extraction pipeline (generate → rank → verify) | `:330` |
| | **Three scaling laws** (Carlini 2022) | `:353` |
| | **Repetition scaling formal law** $\log p_0$ | `:369` |
| | **Deduplication** (Lee 2021) | `:384` |
| | Aligned-ChatGPT divergence attack (Nasr 2023) | `:398` |
| | **Min-K%++ probe** (Zhang 2025) | `:412` |
| **04** — Books, production, non-adversarial | probabilistic extraction at scale | `:429-494` |
| | **Probabilistic extraction** (Hayes 2024) | `:437` |
| | Open-weight book extraction (Cooper 2025) | `:453` |
| | Production model extraction | `:469` |
| | Non-adversarial reproduction | `:482` |
| **05** — Copyright and defenses | NYT, dedup, DP, unlearning | `:496-588` |
| | Copyright as verbatim test | `:504` |
| | Defenses (dedup / DP / unlearning) | `:517` |
| | Memorization vs MIA | `:543` |
| | Open problems | `:564` |
| | Takeaways | `:577` |

**Key formulas:** Canary entropy `:198`; exposure formula `:215`; null distribution tail `:235`; $k$-extractable `:246`; counterfactual memorization `:282`; long-tail theorem `:296`; repetition scaling `:373-378`; Min-K%++ z-score `:417`.

**Key theorems:** Long-tail (Feldman 2020) `:296`; null-distribution tail bound for exposure `:235`.

---

## Cross-references

- **Carlini 2021** extraction also referenced in `privacy/mia/mia5-llm.html:166` (perplexity baseline).
- **Cooper 2025** book extraction motivates the unlearning lectures — see `privacy/unlearning/unlearning.html:108`.
- **Memorization vs MIA** comparison links to `privacy/mia/mia1-foundations.html` (membership inference foundations); Min-K%++ slide is an explicit bridge.
- **Defenses → unlearning** flows directly into `privacy/unlearning/unlearning.html`.
