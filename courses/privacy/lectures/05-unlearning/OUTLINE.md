# privacy/lectures/05-unlearning/ — Machine unlearning

Two-part lecture on machine unlearning, split at the LLM boundary. **Part I** (`unlearning1-foundations.html`) — definitions, certified deletion (full derivation with proofs), and classical/classification unlearning + metrics. **Part II** (`unlearning2-llm.html`) — why the Part-I certificate does not transfer to LLMs, the objective family that replaces it, what benchmarks actually measure, and the deletion-vs-suppression open problem. Theory covered: Part I — three nested definitions, Newton-step certified deletion (Theorem 1 with two proved lemmas), Gaussian certification (Theorem 2), Sekhari capacity (Theorem 3), SISA cost model (Proposition 3), the certification-caps-every-metric bound (Proposition 4), plus the classification methods + metrics thread; Part II — 17 further numbered results, all proved on slide (Props 1/4/5/8/9/10/13/14/16, Lemmas 2–3, Theorems 6/7/11, Cor 12/17, Def 15). Source: `privacy/slide.pdf` and `privacy/privacy.md` reference table.

The folder's `hw4sol.pdf` is the 5-problem homework (P1 Neyman–Pearson, P2 DP⇒MIA, P3 Yeom gap, P4 influence unlearning, P5 certified Gaussian). Its hints/roadmaps are taught **inside the Part I slides** with **no "Homework 4 / Problem N" labels** (2026-06 decision, preserved): the influence→Newton→certification block is the P4/P5 walk-through, and the MIA recall/Proposition-4 block carries P1–P3. (Do not edit `hw4sol.pdf`; the hints live in the deck.)

## Files

| Deck | Topic |
|---|---|
| `unlearning1-foundations.html` | **Part I** (109 slides) — motivation · three definitions · certified/Newton (proved) · SISA · classification algorithms · metrics-as-hypothesis-test |
| `unlearning2-llm.html` | **Part II** (100 slides) — why the certificate does not transfer (proved) · objectives GA/NPO/SimNPO/ME/ELM/RMU (proved) · benchmarks: main figure + measurement claim (proved) · relearning, suppression, the open problem |

---

## unlearning1-foundations.html (Part I — before LLMs) — 109 slides

| Part | Topic | Slide | Line |
|---|---|---|---|
| | Title · Contents — Part I | 1–2 | `:55`, `:66` |
| **01** — Motivation, definition | RTBF, three definitions, relations, assumptions, influence→Newton (proved), Gaussian certification, Sekhari capacity, SISA | 3–66 | `:99-1154` |
| | §01 divider | 3 | `:99` |
| | The Central Question | 4 | `:107` |
| | Why This Became Urgent (lawsuits / GDPR Art. 17 / Carlini·Cooper cite) | 5 | `:123` |
| | Three Definitions That Do Not Work | 6 | `:145` |
| | Roadmap — Section 01 | 7 | `:159` |
| | The Gold Standard: Retrain From Scratch | 8 | `:178` |
| | **Definition 1 — Data Deletion Operation** (Ginart 2019) | 9 | `:194` |
| | Deletion as a Commuting Diagram (SVG) | 10 | `:206` |
| | **Definition 2 — Exact Unlearning** | 11 | `:244` |
| | **Definition 3 — $(\varepsilon,\delta)$-Certified Unlearning** | 12 | `:259` |
| | How the Three Definitions Sit (nested-sets SVG) | 13 | `:273` |
| | **Proposition 1 — exact ⟹ certified** (+ proof) | 14 | `:295` |
| | **Proposition 2 — DP gives certification for free** (+ proof) | 15 | `:309` |
| | Counterexample — certified and useless | 16 | `:323` |
| | What a Certificate Does and Does Not Buy | 17 | `:338` |
| | Certified Unlearning Is **Not** Differential Privacy | 18 | `:361` |
| | Corollary — certification needs a utility partner | 19 | `:382` |
| | Standing Convention · the $1/n$ vs $1/(n-1)$ choice | 20–21 | `:398`, `:413` |
| | Assumptions A1–A3 · what $\lambda$-strong convexity buys | 22–23 | `:430`, `:445` |
| | Newton derivation — LOO target, continuous path $L_t$, IFT, term-by-term, sign | 24–28 | `:463-541` |
| | Influence Unlearning: the update · read as Newton's method | 29–30 | `:542`, `:557` |
| | **Theorem 1 — one Newton step suffices**, residual $MG^2/(2\lambda^3n^2)$ (Guo 2020) | 31 | `:572` |
| | Proof of Theorem 1 — outline · **Lemma 1** · **Lemma 2** (2-slide proof) · combining | 32–37 | `:587-676` |
| | The Picture in Parameter Space (SVG) · which Hessian · never form $H^{-1}$ | 38–40 | `:677`, `:704`, `:718` |
| | **Lemma 3 — $\ell_2$ sensitivity $\le 2G/(\lambda n)$** (+ proof) · reading it · why over pairs | 41–43 | `:731`, `:746`, `:767` |
| | Recall — the Gaussian mechanism | 44 | `:782` |
| | **Theorem 2 — certified deletion by output noise** (+ proof) | 45 | `:796` |
| | What Guo et al. *actually* prove (objective perturbation) | 46 | `:810` |
| | The punchline $1/n^2$ vs $1/n$ · noise-vs-$n$ log-log (SVG) · why not just DP | 47–49 | `:823`, `:840`, `:862` |
| | Deletions arrive in a sequence | 50 | `:883` |
| | **Theorem 3 — deletion capacity** (Sekhari 2021, Thm. 2) · where it comes from · proof sketch · budget SVG · separation from DP | 51–55 | `:898-983` |
| | When Influence Functions Fail (Basu 2021) · can certification reach deep nets | 56–57 | `:984`, `:998` |
| | The other route: change how you train · Shards and Slices (SVG) | 58–59 | `:1014`, `:1031` |
| | **Proposition 3 — the SISA cost model** (+ 3-slide proof) | 60–63 | `:1059-1111` |
| | Reading the cost model · what sharding really costs | 64–65 | `:1112`, `:1127` |
| | Section 01 — what we proved | 66 | `:1141` |
| **02** — Classification algorithms | catalog, geometries, SCRUB, SalUn, $\ell_1$, RURK, verification | 67–84 | `:1155-1434` |
| | §02 divider · what breaks outside convexity | 67–68 | `:1155`, `:1163` |
| | Catalog — retraining-style · structured (tables, "certified?" column) | 69–70 | `:1184`, `:1198` |
| | FT, GA, RL — three geometries · FF and IU — one-shot moves | 71–72 | `:1212`, `:1226` |
| | **SCRUB** — two signs · why it does not blow up | 73–74 | `:1241`, `:1258` |
| | What happens without the min-step (**real figure**, SCRUB Fig. 6a/6d) | 75 | `:1274` |
| | **SalUn** — saliency mask · reading the mask (SVG) | 76–77 | `:1292`, `:1307` |
| | How much of the network to touch (**real figure**, SalUn Fig. A1a/A1b) | 78 | `:1333` |
| | **$\ell_1$-sparse** · why sparsity would help | 79–80 | `:1342`, `:1357` |
| | Residual knowledge under perturbation | 81 | `:1371` |
| | Where residual knowledge lives (**real figure**, RURK Fig. 1) | 82 | `:1386` |
| | **RURK** — objective and target $r_\tau(S_f)\le 1$ | 83 | `:1399` |
| | The Verification Problem (bridge into §03) | 84 | `:1413` |
| **03** — Classification metrics | metric-as-test, MIA recall, Proposition 4, converse, two-sided, IDI, COLA, benchmark | 85–109 | `:1435-1805` |
| | §03 divider · an unlearning metric is a hypothesis test | 85–86 | `:1435`, `:1443` |
| | The chain every metric follows (SVG) · the standard suite | 87–88 | `:1460`, `:1490` |
| | MIA as an unlearning probe | 89 | `:1507` |
| | **Recall — three facts about membership tests** (NP optimal test, Yeom $\Delta/B$ floor, DP cap) | 90 | `:1522` |
| | **Proposition 4 — certification caps every metric** (+ proof) · corollary: a passing score is not evidence | 91–93 | `:1535`, `:1547`, `:1559` |
| | The converse fails — head distillation (table) | 94 | `:1573` |
| | The test is two-sided · both sides of the target (SVG) | 95–96 | `:1588`, `:1609` |
| | **IDI** (lab, AAAI 2026) · IDI in one picture (**real figure**, IDI Fig. 4a) · reading the index · what it sees that outputs do not (table) | 97–100 | `:1641`, `:1657`, `:1666`, `:1681` |
| | Over-unlearning is not hypothetical | 101 | `:1698` |
| | **COLA** — collapse + align (lab) · what collapse does to the features (**real figure**, COLA Fig. 7) · COLA in numbers | 102–104 | `:1713`, `:1726`, `:1735` |
| | SalUn benchmark table (CIFAR-10 / ResNet-18, 10% random) · reading it correctly | 105–106 | `:1749`, `:1764` |
| | What a defensible evaluation looks like | 107 | `:1779` |
| | Takeaways — Part I · closer → Part II | 108–109 | `:1792`, `:1805` |

## unlearning2-llm.html (Part II — LLM unlearning) — 100 slides

| Part | Topic | Slide | Line |
|---|---|---|---|
| | Title · Contents — Part II | 1–2 | `:56`, `:67` |
| **01** — Why the guarantee does not transfer | four properties P1–P4 of LLM training, each turned into a proved obstruction; Prop 1, Lemma 2, Lemma 3, Prop 4 | 3–23 | `:107-460` |
| | §01 divider · What the Certificate Bought Us | 3–4 | `:107`, `:115` |
| | Recall — certified unlearning · what made it provable | 5–6 | `:134`, `:149` |
| | Two Hypotheses Nobody States (row-shaped request, unique minimiser) | 7 | `:165` |
| | Four Properties of LLM Training (P1–P4) · the assumption map (SVG) | 8–9 | `:186`, `:202` |
| | P1 non-convexity — permutation symmetry `:241` · the Newton step can point uphill `:255` | 10–11 | `:237`, `:251` |
| | P2 the request names a concept (Harry Potter) | 12 | `:264` |
| | **Proposition 1 — exact deletion misses the concept** (+ proof) · reading it | 13–14 | `:283`, `:294` |
| | P3 one pass, one gradient — **Lemma 2** (displacement budget $\eta_j G c^{T-j}$) `:316` · proof `:324` · the dichotomy hidden in $c$ ($c=1$ convex vs $c=1+\eta\beta$) | 15–17 | `:309`, `:324`, `:335` |
| | P4 judged on text — **Lemma 3** (TV data-processing, one-way) · the direction that fails (SVG) | 18–19 | `:355`, `:367` |
| | **Proposition 4 — the certificate does not transfer** (clauses i–iv) + proof | 20–21 | `:396`, `:412` |
| | What Survives · Section 01 — where we stand | 22–23 | `:427`, `:445` |
| **02** — Objectives | GA → NPO → SimNPO → ME → ELM → RMU as one weighted-gradient family, with divergence rates and a proved containment | 24–53 | `:461-911` |
| | §02 divider · the design problem (forget + retain decomposition `:473`) | 24–25 | `:461`, `:469` |
| | Gradient ascent `:488` · **Proposition 5 — GA has no optimum** · why that matters | 26–28 | `:483`, `:498`, `:509` |
| | **Theorem 6 — divergence rates** (GA linear $-t$, NPO logarithmic $-\tfrac1\beta\log t$) | 29 | `:527` |
| | Recall — DPO `:544` · **NPO — delete the positive branch** `:556` | 30–31 | `:540`, `:552` |
| | **Theorem 7 — NPO is self-limiting** (weight $2\sigma(\beta r_\theta)$) + proof `:585` | 32–33 | `:565`, `:580` |
| | The whole difference in one line ($w^{\mathrm{GA}}\equiv 1$ vs $w^{\mathrm{NPO}}=2\sigma(\beta r_\theta)$) `:596` · the brake, drawn (SVG) | 34–35 | `:592`, `:608` |
| | Catastrophic collapse, measured (**real figure** `figs/npo-ga-collapse.png`) | 36 | `:630` |
| | **Proposition 8 — NPO contains GA** ($\beta\to 0$, correction $\tfrac\beta4\mathbb{E}[r_\theta^2]$ `:645`) + proof | 37–38 | `:639`, `:653` |
| | What $\beta$ buys · the dial, measured (**real figure** `figs/npo-beta-pareto.png`) | 39–40 | `:664`, `:682` |
| | Two complaints about NPO · **Proposition 9 — NPO is length-biased** `:717` · reading it | 41–43 | `:691`, `:711`, `:725` |
| | **SimNPO** — normalise and drop the reference `:750` · four other places to intervene | 44–45 | `:745`, `:759` |
| | Entropy maximisation has an optimum `:787` | 46 | `:783` |
| | **ELM** — main figure (`elm.png`) · what the target buys (erased target law `:813`, bounded below by $H(\pi^\star)$) | 47–48 | `:798`, `:809` |
| | **RMU** — intervene on activations `:828` | 49 | `:824` |
| | **Proposition 10 — one family** (GA is the unique constant-weight member) · the design space (SVG) | 50–51 | `:836`, `:847` |
| | Objectives side by side (table, incl. ELM row) · Section 02 — where we stand | 52–53 | `:877`, `:897` |
| **03** — Benchmarks | each of TOFU / WMDP / RWKU / MUSE as **main figure + measurement claim**, and the proved gaps between score and claim | 54–78 | `:912-1304` |
| | §03 divider · how success gets declared | 54–55 | `:912`, `:920` |
| | **TOFU** — main figure (`tofu.png`) · fictitious authors · forget quality (KS test) | 56–58 | `:935`, `:946`, `:964` |
| | **Theorem 11 — a $p$-value is not a score** (uniform under the null) + proof · selection inflates the score (max of $k$ iid uniforms `:996`, table) · reading it | 59–62 | `:976`, `:991`, `:1008`, `:1029` |
| | **WMDP** — main figure (`WMDP.png`) · hazardous knowledge · **Corollary 12 — accuracy is prompt-relative** | 63–65 | `:1043`, `:1054`, `:1075` |
| | **RWKU** — main figure (`RWKU.png`) · real knowledge, adversarial probes | 66–67 | `:1090`, `:1100` |
| | **MUSE** — main figure (`MUSE.png`) · six axes · the four suites (table) | 68–70 | `:1121`, `:1132`, `:1150` |
| | Recall — a validity failure (mia5 Prop 7) · **Proposition 13 — the split confound** `:1174` · which designs escape it | 71–73 | `:1168`, `:1183`, `:1194` |
| | **Proposition 14 — output metrics are blind** · is it vacuous? · what the benchmark sees (SVG) | 74–76 | `:1213`, `:1228`, `:1249` |
| | Cooper — the word is doing too much work · Section 03 — where we stand | 77–78 | `:1278`, `:1291` |
| **04** — Relearning, suppression, the open problem | closure under a fine-tuning budget; benign relearning; lab decks; what remains open | 79–100 | `:1305-1613` |
| | §04 divider · two hypotheses (deletion vs suppression) | 79–80 | `:1305`, `:1313` |
| | **Definition 15 — closure under adaptation** · **Proposition 16 — strictly stronger** + proof (the gate) · **Corollary 17 — attacks are one-sided** · closure, drawn (SVG) | 81–85 | `:1333`, `:1348`, `:1359`, `:1374`, `:1386` |
| | Benign relearning (**real figure** `figs/benign-relearn-pipeline.png`) · why that is damning | 86–87 | `:1407`, `:1416` |
| | What property triggers recovery? · recovery tracks syntactic similarity (lab, **real figure** `figs/syntax-similarity.png`) · a mechanism and a fix | 88–90 | `:1432`, `:1452`, `:1464` |
| | **DUSK** (lab, `DUSK.png`) · the partition DUSK enforces (`:1491` two-condition target) | 91–92 | `:1479`, `:1487` |
| | **R-TOFU** (lab, `r-tofu.png`) · what the chain of thought reveals | 93–94 | `:1499`, `:1507` |
| | Are we making progress? (Triantafillou) · five things one word (table) · why the naming is a safety measure (lab position paper) | 95–97 | `:1521`, `:1535`, `:1553` |
| | The open problem · Takeaways · Questions | 98–100 | `:1569`, `:1586`, `:1601` |

**Key formulas (Part I):** Certified $(\varepsilon,\delta)$ two-sided inequality `1:264-267`; leave-one-out target `1:406`; continuous path $L_t$ `1:485`; influence via IFT, $\theta'(0)=\tfrac1n H^{-1}\nabla\ell$ `1:521`; the plus sign, explained `1:531`; influence-unlearning update `1:547`; same update as a Newton step `1:567`; Theorem 1 residual $MG^2/(2\lambda^3n^2)$ `1:577`; Newton error identity (Lemma 2) `1:636`; Hessian-choice discrepancy $G\kappa/(\lambda^2n^2)$ `1:711`; $\ell_2$-sensitivity $2G/(\lambda n)$ `1:735`; recall Gaussian mechanism `1:787`; certified $\sigma \ge \eta\sqrt{2\ln(1.25/\delta)}/\varepsilon$ `1:804`; unlearning noise $\propto 1/n^2$ `1:830`; Sekhari deletion capacity `1:904`; SISA cost $n(R+1)(2R+1)/(6SR)$ `1:1107`; SCRUB KL `1:1244`; SalUn mask `1:1297-1300`; $\ell_1$-sparse `1:1347`; RURK objective `1:1404`; Proposition 4 TV cap `1:1541`; IDI `1:1646`.

**Key figures (Part I) — nine inline `u1-` SVG:** commuting diagram `1:206`; three definitions as nested sets `1:273`; LOO path + Newton step + residual gap `1:677`; noise-vs-$n$ log-log ($1/n^2$ against $1/n$) `1:840`; deletion capacity as a consumed budget `1:942`; SISA shard/slice grid `1:1031`; SalUn mask `1:1307`; metrics-as-test-statistics chain `1:1460`; two-sided target number line `1:1609`.

**Real paper figures (Part I) — captured from the source PDFs, stored in `figs/`:**

| File | Source | Slide · line |
|---|---|---|
| `figs/scrub-maxsteps-only.png` + `figs/scrub-alternating.png` | Kurmanji et al., *Towards Unbounded Machine Unlearning*, NeurIPS 2023 (arXiv:2302.09880) — Figure 6(a) and 6(d) | 75 · `1:1274` |
| `figs/salun-saliency-sparsity.png` | Fan et al., *SalUn*, ICLR 2024 (arXiv:2310.12508) — Figure A1(a) and A1(b) | 78 · `1:1333` |
| `figs/rurk-residual-knowledge.png` | Hsu et al., *The Unseen Threat*, NeurIPS 2025 (arXiv:2601.22359) — Figure 1 | 82 · `1:1386` |
| `figs/idi-conceptual.png` | Jeon, Jeung, Kim, No, Choi, *An Information Theoretic Evaluation Metric for Strong Unlearning*, AAAI 2026 — Figure 4(a), conceptual illustration of IDI | 98 · `1:1657` |
| `figs/cola-collapse.png` | Jeon et al., arXiv:2405.17878 (extended version of the AAAI 2026 paper) — Figure 7, the collapse phase of COLA | 103 · `1:1726` |

No `<!-- TODO real figure: … -->` markers remain in Part I. The two former markers (IDI, COLA) were filled on 2026-08-17 from the AAAI 2026 camera-ready Albert supplied and its arXiv extended version; the COLA schematic is not in the camera-ready, which defers to Appendix C.7 of the arXiv paper.

**Key formulas (Part II):** permutation symmetry $F(\theta)=F(P\theta)$ `2:241`; Newton step in the eigenbasis (sign fails off convexity) `2:255`; Lemma 2 displacement budget $\lVert\theta_T-\theta_T'\rVert\le \eta_j G c^{T-j}$ `2:316`, one-step gap `2:328`; forget + retain decomposition `2:473`; GA objective and gradient `2:488`; DPO `2:544`; **NPO** $\tfrac2\beta\mathbb{E}\log(1+e^{\beta r_\theta})$ `2:556`; NPO gradient weight $2\sigma(\beta r_\theta)$ `2:585`; GA-vs-NPO weights in one line `2:596`; small-$\beta$ expansion with $\tfrac\beta4\mathbb{E}[r_\theta^2]$ `2:645`, scalar expansion `2:657`; length-bias weight ratio `2:717`; **SimNPO** `2:750`; entropy maximisation $\log\lvert V\rvert - H(\pi_\theta)$ `2:787`; **ELM** erased target law $\pi^\star \propto \pi_{\mathrm{nov}}(\pi_{\mathrm{nov}}/\pi_{\mathrm{exp}})^\lambda$ and its cross-entropy fit `2:813`; **RMU** `2:828`; max of $k$ iid uniforms, $\Pr[p_{\max}\le t]=t^k$, $\mathbb{E}=k/(k+1)$ `2:996`; split-confound advantage $=\mathrm{TV}(Q_1,Q_0)$ `2:1174`; DUSK two-condition target `2:1491`.

**Key figures (Part II) — six inline SVG:** the assumption map (which Part-I hypothesis each LLM property breaks) `2:206`; the direction that fails (one-way TV transfer) `2:371`; the brake, drawn (GA constant weight vs NPO saturating weight) `2:612`; the design space (where each objective intervenes) `2:851`; what the benchmark sees (two parameter vectors, one score) `2:1253`; closure under a fine-tuning budget `2:1390`.

**Real paper figures (Part II) — five main-figure PNGs alongside the deck, plus four captures in `figs/`. Every one is that paper's own Figure 1/2/3/5, not a screenshot of prose.**

| File | Source | Slide · line |
|---|---|---|
| `figs/npo-ga-collapse.png` | Zhang, Lin, Bai, Mei, *Negative Preference Optimization*, COLM 2024 — Figure 2 | 36 · `2:630` |
| `figs/npo-beta-pareto.png` | same paper — Figure 3 | 40 · `2:682` |
| `elm.png` | Gandikota, Feucht, Marks, Bau, *Erasing Conceptual Knowledge from Language Models*, NeurIPS 2025 — Figure 1 | 47 · `2:798` |
| `tofu.png` | Maini, Feng, Schwarzschild, Lipton, Kolter, *TOFU: A Task of Fictitious Unlearning for LLMs*, COLM 2024 — Figure 1 | 56 · `2:935` |
| `WMDP.png` | Li, Pan, Gopal, et al., *The WMDP Benchmark*, ICML 2024 — Figure 1 | 63 · `2:1043` |
| `RWKU.png` | Jin, Wang, Zhang, et al., *RWKU: Benchmarking Real-World Knowledge Unlearning for LLMs*, NeurIPS 2024 D&B — Figure 1 | 66 · `2:1090` |
| `MUSE.png` | Shi, Wang, Li, et al., *MUSE: Machine Unlearning Six-Way Evaluation for Language Models*, ICLR 2025 — Figure 1 | 68 · `2:1121` |
| `figs/benign-relearn-pipeline.png` | Hu, Fu, Wu, Smith, *Unlearning or Obfuscating? Jogging the Memory of Unlearned LLMs via Benign Relearning*, ICLR 2025 (arXiv:2406.13356) — Figure 2 (left) | 86 · `2:1407` |
| `figs/syntax-similarity.png` | Yoon, Hong, Jeung, No (Yonsei), *Rethinking Benign Relearning: Syntax as the Hidden Driver of Unlearning Failures*, ICLR 2026 (arXiv:2602.03379) — Figure 5 | 89 · `2:1452` |
| `DUSK.png` | Jeung, Yoon, Hong, Kim, Han, Yu, No (Yonsei), *DUSK: Do Not Unlearn Shared Knowledge*, ACL 2026 Findings — Figure 1 | 91 · `2:1479` |
| `r-tofu.png` | Yoon, Jeung, No (Yonsei), *R-TOFU: Unlearning in Large Reasoning Models*, EMNLP 2025 (oral) — Figure 1 | 93 · `2:1499` |

`figs/rurk-residual-knowledge.png` is **Part I only** (Hsu et al., *The Unseen Threat*, RURK). It was briefly used on a Part II RWKU slide in the 2026-08 rewrite — a misattribution (RURK ≠ RWKU) as well as a cross-deck duplicate; that slide is gone and RWKU now carries its own `RWKU.png`.

**Key theorems (Part II — 17 numbered results, every one stated *and* proved on slides):**

| Result | Statement | Proof |
|---|---|---|
| **Proposition 1** — exact deletion misses the concept | `2:283` | same slide; reading `2:294` |
| **Lemma 2** — one-pass displacement budget $\eta_j G c^{T-j}$ | `2:309` | `2:324`; the $c$ dichotomy `2:335` |
| **Lemma 3** — one-way transfer, $\mathrm{TV}(\Gamma_{\theta_u},\Gamma_{\theta_r})\le\mathrm{TV}(P_u,P_r)$ | `2:355` | same slide; figure `2:367` |
| **Proposition 4** — the certificate does not transfer (clauses i–iv) | `2:396` | `2:412` |
| **Proposition 5** — GA has no optimum | `2:498` | same slide; practice `2:509` |
| **Theorem 6** — divergence rates, GA $-t(1+o(1))$ vs NPO $-\tfrac1\beta\log t(1+o(1))$ | `2:527` | same slide (Zhang et al. Thm 1–2) |
| **Theorem 7** — NPO is self-limiting | `2:565` | `2:580` |
| **Proposition 8** — NPO contains GA as $\beta\to0$ | `2:639` | `2:653` |
| **Proposition 9** — NPO is length-biased | `2:711` | same slide; reading `2:725` |
| **Proposition 10** — one family; GA the unique constant-weight member | `2:836` | same slide; design space `2:847` |
| **Theorem 11** — a $p$-value is not a score | `2:976` | `2:991`; selection table `2:1008`; reading `2:1029` |
| **Corollary 12** — accuracy is prompt-relative | `2:1075` | same slide |
| **Proposition 13** — the split confound | `2:1183` | same slide; which designs escape `2:1194` |
| **Proposition 14** — output metrics are blind | `2:1213` | same slide; vacuity check `2:1228` |
| **Definition 15** — closure under adaptation (fine-tuning budget) | `2:1333` | — |
| **Proposition 16** — closure strictly stronger than output-indistinguishability | `2:1348` | `2:1359` (gate construction) |
| **Corollary 17** — relearning attacks are one-sided evidence | `2:1374` | same slide; figure `2:1386` |


**Key theorems (Part I — every one stated *and* proved on slides):**

| Result | Statement | Proof |
|---|---|---|
| Definition 1 — deletion operation (Ginart 2019) | `1:194` | — |
| Definition 2 — exact unlearning | `1:244` | — |
| Definition 3 — $(\varepsilon,\delta)$-certified | `1:259` | — |
| Proposition 1 — exact ⟹ certified | `1:295` | same slide |
| Proposition 2 — DP ⟹ certified (identity map) | `1:309` | same slide; counterexample `1:323` |
| **Theorem 1** — one Newton step, residual $MG^2/(2\lambda^3n^2)$ (Guo 2020) | `1:572` | `1:587-676` (outline, Lemma 1, Lemma 2 ×2, combine) |
| Lemma 1 — $\lVert\theta_o-\theta_{-z}\rVert \le G/(\lambda n)$ | `1:602` | same slide |
| Lemma 2 — Newton squares the error, $(M/2\lambda)\lVert e\rVert^2$ | `1:617` | `1:631`, `1:646` |
| Lemma 3 — $\ell_2$ sensitivity $\le 2G/(\lambda n)$ | `1:731` | same slide |
| **Theorem 2** — certified deletion by output noise | `1:796` | same slide; honesty note `1:810` |
| **Theorem 3** — deletion capacity (Sekhari 2021, Thm. 2) | `1:898` | sketch `1:926`; DP separation `1:966` |
| **Proposition 3** — SISA expected cost model | `1:1059` | `1:1072`, `1:1087`, `1:1098` |
| **Proposition 4** — certification caps every bounded metric | `1:1535` | `1:1547`; corollary `1:1559` |

**Homework-4 in-deck (woven, not labeled):** the influence→Newton→certification block `1:463-822` is the long-form walkthrough of the influence-unlearning (P4) and certified-Gaussian (P5) problems; the MIA problems (P1 Neyman–Pearson optimal test, P2 DP⇒MIA cap, P3 Yeom gap floor) live on the recall card **"Recall — Three Facts About Membership Tests"** `1:1522` and the Proposition-4 block that follows. No "Homework 4 / Problem N" labels appear on slides — the outline flows inside the lecture content.

**Lab papers cited:** IDI/COLA — Jeon, Jeung, Kim, No, Choi, *An Information Theoretic Evaluation Metric for Strong Unlearning*, AAAI 2026 (Part I `1:1642`, `1:1706`); R-TOFU (Yoon, Jeung, No; EMNLP 2025 oral, `2:1499`); DUSK (Jeung, Yoon, Hong, Kim, Han, Yu, No; ACL 2026 Findings, `2:1479`); syntactic relearning (Yoon, Hong, Jeung, No; *Rethinking Benign Relearning*, ICLR 2026, `2:1452`); position paper (Yoon, Jun, No; ICML 2026, `2:1553`). (SEPS slide dropped 2026-06.)

**Every image asset in this folder is referenced.** `elm.png`, `tofu.png`, `WMDP.png`, `RWKU.png`, `MUSE.png`, `DUSK.png`, `r-tofu.png` are all live in Part II (see the **Real paper figures (Part II)** table); `figs/` holds the four captures plus Part I's three.

**Companion note — `unlearning1-notes.html`** (non-standard plural filename; do **not** rename). 46 entries covering all 107 slides, each badged with the slide or slide range it serves. Structure: `.toc` two-column index with slide-range badges, then one `.slide-note` block per teaching beat (`.snum` / `.stag` / `.timing` / `<h3>`, body of `.say` spoken lines, `.board` derivations, `.ask` anticipated questions, `.key` highlights, `.sec-label` on the three section dividers). Total spoken budget ≈ 110 min. Board-work entries worth knowing about: the $1/n$ vs $1/(n-1)$ identity; assumptions A1–A3 and the two jobs of strong convexity; the Lemma-2 integral identity; the Guo objective-perturbation caveat; the Sekhari risk decomposition; the SISA double sum; the Proposition-4 signed-measure proof.

**Companion note — `unlearning2-notes.html`** (same plural convention). **One entry per slide: 100 `.slide-note` blocks**, ids `#s1`–`#s100`, preceded by a 100-item `.toc` ordered list linking to each. Ids track deck slide numbers exactly, verified by a 1–100 sweep over `id=`, `href="#s"` and the `.snum` labels, plus a deck-`<h2>`-to-note-`<h3>` title diff (only two intentional differences: slide 1, whose deck title carries a `<br>`, and the §01 divider, where the note leads with the sub-heading). In-note cross-references of the form "slide N" were remapped with the ids. Same component vocabulary as the Part I notes (`.snum` / `.stag` / `.timing` / `<h3>`, then `.say` spoken lines, `.board` derivations, `.ask` anticipated questions), with `<hr class="sec">` + `.sec-label` at each of the four section boundaries. Board-work entries worth knowing about: the permutation-symmetry argument for non-unique minimisers; the expansiveness constant $c$ and where $1+\eta\beta$ comes from; the TV data-processing step in Lemma 3; the NPO gradient weight $2\sigma(\beta r_\theta)$ and its $\beta\to0$ expansion; the uniformity of a $p$-value under the null and the max-of-$k$ selection effect; the gate construction in Proposition 16. Rewritten 2026-08 from scratch — the previous version documented the retired 29-slide deck.

**Audit history.** 2026-05 visual audit: split Newton-Step theorem 1→2 slides; consolidated LUNAR math. 2026-06 revision: every `.cite` shortened to one rendered line; "Why Now" GDPR **Art. 17** confirmed + lawsuits one-per-line + Carlini·Cooper cite; Newton block expanded 2→8 slides; **fixed sign error** on influence-function slide ($+\tfrac1n H^{-1}\nabla\ell$). 2026-06 split: single 63-slide `unlearning.html` retired and split into Part I (`unlearning1-foundations.html`) and Part II (`unlearning2-llm.html`); Part II sections renumbered 01/02. 2026-06 reorder: moved the influence-function slide from §02 up to lead into the Newton block (so the Newton step no longer feels sudden); folded the homework hints into the natural flow (removed the explicit "Homework 4" roadmap slides; the MIA problems became "MIA: Optimal Test and Its Limits"). Part I now 36 slides, Part II 32. 2026-06 benchmark figures: embedded each benchmark's **actual main-figure image** — `tofu.png` (pretrained→finetuned→unlearned pipeline), `WMDP.png` (bio/chem/cyber three-domain pie, 3,668 Q), `RWKU.png` (forget/neighbor/MIA/utility framework), `MUSE.png` (six-way data-owner/deployer grid), `DUSK.png` (forget-all vs forget-unique Venn partitions) — figure dominant + one-line caption (`cite cite-left` added locally); glossed each of Cooper's 5 mismatches; sharpened the Triantafillou "progress" takeaway; **removed the Pawelczyk verification-hardness slide**; venues updated — DUSK → ACL 2026 Findings, position paper → ICML 2026 accepted (Position Track) with an "Accepted · ICML 2026" pill. Part II now 31 slides. (Image PNGs live alongside the deck; `bundle.py` base64-inlines them for the standalone build.) 2026-06 trim: **removed the Guardrail/ECO slide**; replaced ELM's bullet explanation with its main-figure image (`elm.png`). Part II now 30 slides. 2026-06 trim 2: **removed the SEPS slide**; added R-TOFU main-figure image (`r-tofu.png`); on the position slide removed the "Accepted · ICML 2026" pill, corrected authors to **Yoon, Jun, No**, and tightened the proposal wording. Part II now 29 slides.

**2026-08 math-detail revision (Part I only; Part II untouched).** Part I **36 → 107 slides**, `unlearning1-notes.html` **36 → 46 entries**. Added: three numbered definitions with a nested-set figure; Propositions 1–2 with proofs, a certified-and-useless counterexample, and an explicit "certified ≠ DP" slide; a standing-convention slide and the $1/n$ vs $1/(n-1)$ note; assumptions A1–A3 stated before use; the influence derivation carried through the IFT term by term with the sign explained; Theorem 1 proved in full via Lemma 1 and a two-slide Lemma 2 (Newton error identity, curvature-gap bound); the which-Hessian discrepancy and a "you never form $H^{-1}$" (CG / LiSSA) slide; Lemma 3 proved; Theorem 2 proved by reduction to the Gaussian mechanism, with a separate slide on what Guo et al. *actually* prove (objective perturbation, not output noise); Theorem 3 restated in the paper's correct form with a proof sketch, a budget figure and the DP separation; an honest "when influence functions fail" pair (Basu 2021); SISA made quantitative by Proposition 3 with a three-slide proof; §02 given per-method geometry and a "certified? no" column plus a verification-problem bridge; §03 reframed so that every metric is a **test statistic** for $H_0:\theta_u \sim \mathcal{A}(\mathcal{D}_r)$, with Proposition 4 (certification caps every bounded metric) proved, its vacuity corollary, the head-distillation converse, and the two-sided target made explicit. **Corrections made during the audit** (all previously on slides or in the notes): Sekhari capacity mis-stated as linear in $\varepsilon$ with $\sqrt d$ → $c\,n\sqrt{\varepsilon}/(d\log(1/\delta))^{1/4}$; Guo certification mis-attributed to output perturbation; COLA's two stages described wrongly on both counts; IDI citation had wrong authors/title/venue; RURK citation wrong; an unverifiable IDI baseline value $-0.110$ removed (the verified pair is $-0.349$ / $-0.060$). The old "MIA: Optimal Test and Its Limits" slide became a recall card plus Proposition 4. Verified by full 104-page headless-Chrome render at `-r 60`; nine layout defects found and fixed (one slide split, one unfilled Bézier, six label-overlap groups, one clipped label).

**2026-08 figure pass + errata (Part I).** arXiv turned out to be reachable from the container, so three of the five `TODO real figure` markers were filled with real captures (SCRUB Fig. 6a/6d, SalUn Fig. A1a/A1b, RURK Fig. 1 — see the **Real paper figures** table above); Part I **104 → 107 slides**. The SalUn capture uses **Figure A1**, not the paper's Figure 1: Figure 1 is a diffusion-model schematic whose examples are "Nudity"-concept generations, which is Part II's territory and unsuitable for a classroom slide, whereas A1 is the classification saliency-sparsity trade-off against the Retrain reference line and continues the "Reading the Mask" thread directly. Two markers remained (IDI, COLA) until 2026-08-17 — see the next entry.

**2026-08-17 IDI/COLA figures + note realignment (Part I).** Albert supplied the AAAI 2026 camera-ready (*An Information Theoretic Evaluation Metric for Strong Unlearning*, Jeon, Jeung, Kim, No, Choi), which also contains COLA, so both remaining markers were closed from it. **IDI**: Figure 4(a), the conceptual illustration (three layerwise-MI curves, blue area over red area), captured at `-r 450` and now slide 98. **COLA**: the collapse schematic is *not* in the camera-ready — that version defers to Appendix C.7 of the extended paper (arXiv:2405.17878), whose Figure 7 (Before / Collapse / After feature clouds) was captured at `-r 300` and is now slide 103. Part I **107 → 109 slides**. Every number on the IDI and COLA slides was re-verified line by line against the camera-ready's Table 1 and appendix — all correct, nothing changed.

The same pass fixed a **pre-existing numbering drift in `unlearning1-notes.html`**: the 46 entries' `snum` labels, TOC ranges, and three inline "Slide N" prose references had fallen up to **3 slides behind** the deck (the note file labelled the IDI block 94–96 when it was 97–100). All 46 `snum` ranges and all 46 TOC ranges were rebuilt from the deck's own heading sequence, and the three stale prose references (`91`→`94`, `87`→`90`, `96`→`100`, plus COLA's `99`→`104`) were repointed. The note entries for IDI and COLA each gained a paragraph on how to walk the new figure.

**Two errata from the same pass, both now fixed:**

1. **The SalUn benchmark row was never fabricated.** The mid-revision "correction" to `1.55/99.88/93.93/13.28/1.13` was itself the error. arXiv:2310.12508 Table 1 (p. 7, CIFAR-10 / ResNet-18, 10% random data forgetting) reads SalUn `2.85±0.43 / 99.62±0.12 / 93.93±0.29 / 14.39±0.82`, avg gap `1.15`, RTE `2.66` — i.e. the deck's **original** numbers were right. The table row, the "Reading That Table Correctly" bullet, and the notes entry have all been reverted to the paper's values, and the notes carry a sourced audit paragraph recording the round trip. The reading also changed: SalUn's MIA **overshoots** retrain's `12.88`; it wins on average closeness, not on any single axis.
2. **RURK Proposition 2 was mis-stated.** The slide said "a larger radius forces a larger $\varepsilon$." The paper says the opposite shape: for **fixed** $(\varepsilon,\delta)$ the disagreement probability depends solely on $\tau$ and rises as $\tau$ grows. Bullet rewritten.

**2026-08 math-detail revision (Part II).** Part II **29 → 95 slides**; `unlearning2-notes.html` rewritten from scratch, **29-slide coverage → 95 per-slide entries**. The deck was restructured from a two-section survey (methods, then benchmarks) into **four argued sections, each ending in a "Where We Stand" card**, carrying **17 numbered results, every one proved on slide** (see the Part II theorem table above):

- **§01 — why the certificate does not transfer.** The old deck asserted "LLMs are different" in bullets. It now names four properties of LLM training (P1 non-convexity, P2 concept-shaped requests, P3 one-pass SGD, P4 text-level judgement), maps each onto the Part-I hypothesis it breaks (SVG `2:206`), and converts each into a proved obstruction: Proposition 1 (exact row deletion misses the concept), Lemma 2 (Hardt–Recht–Singer displacement budget, with the $c=1$ / $c=1+\eta\beta$ dichotomy), Lemma 3 (TV data-processing — transfer runs one way only), and Proposition 4 (four clauses, the certificate's hypotheses fail one by one).
- **§02 — objectives.** GA / NPO / SimNPO / entropy-maximisation / RMU are now presented as **one weighted-gradient family** (Proposition 10, with GA the unique constant-weight member) rather than a list. New: Proposition 5 (GA has no optimum), Theorem 6 (linear vs logarithmic divergence rates), Theorem 7 (NPO is self-limiting), Proposition 8 (NPO contains GA as $\beta\to0$, correction $\tfrac\beta4\mathbb{E}[r_\theta^2]$), Proposition 9 (NPO is length-biased — the failure SimNPO fixes). Two real NPO-paper figures replace the previous bullet claims about collapse and about $\beta$.
- **§03 — benchmarks.** TOFU / WMDP / RWKU / MUSE each keep their **main figure** and then get read as a **measurement claim**, with three proved gaps: Theorem 11 (a $p$-value is uniform under the null, so "forget quality" is not a score, and selecting the best of $k$ runs inflates it), Corollary 12 (WMDP accuracy is prompt-relative), Proposition 13 (the split confound, recalling `mia5` Prop 7), Proposition 14 (no black-box suite separates a model that forgot from one that learned to stay quiet).
- **§04 — relearning and suppression.** The deletion-vs-suppression question is made formal by **Definition 15 (closure under a fine-tuning budget)**, Proposition 16 (strictly stronger than output indistinguishability, proved by a gate construction) and Corollary 17 (relearning attacks are one-sided evidence). Benign relearning, the lab syntactic-similarity result, DUSK and R-TOFU then land as instances of that framework rather than as standalone anecdotes.

Verified by full headless-Chrome render at `-r 60` plus incremental re-renders of every edited slide; `lint-deck.py` clean, `find-dense.py` clean (80-word ceiling), zero overflow or overlap found. Only Priority-3 (empty space) defects surfaced; the four emptiest slides (7, 60, 69, 71) were filled with `.highlight` takeaway lines rather than padding.

**2026-08 figure restoration + citation errata (Part II).** The revision above had dropped five of the seven embedded main-figure PNGs (`tofu.png`, `WMDP.png`, `RWKU.png`, `MUSE.png`, `elm.png`) in favour of text — a regression against the standing **Visual richness** default and against the 2026-06 decision to embed each paper's own main figure. All five are restored as **figure-dominant slides with a one-line caption** (`cite cite-left`, `bottom: 48px`), each placed immediately before the analysis slide it belongs with; the measurement-claim theorems are untouched. ELM, which had been removed outright, is back as a two-slide pair (figure `2:798` + a new "What the Target Buys" slide `2:809` giving the erased target law and its $H(\pi^\star)$ lower bound), and an ELM row was added to the Objectives comparison table `2:877`. Part II **95 → 100 slides**.

**Three citation errata found and fixed in the same pass:**

1. **RWKU vs RURK.** The rewrite had illustrated the RWKU benchmark with `figs/rurk-residual-knowledge.png` — Part I's capture from Hsu et al., *The Unseen Threat* (**RURK**), captioned as Jin et al., *RWKU*. Wrong paper, and a cross-deck duplicate. Slide removed; RWKU now carries its own `RWKU.png` main figure `2:1090`.
2. **Four lab/paper author lists had drifted** from the pre-rewrite deck and are restored in full, each now ending in `— Figure N`: benign relearning → Hu, Fu, Wu, Smith (ICLR 2025, Fig. 2 left); syntactic relearning → Yoon, Hong, Jeung, No, *Rethinking Benign Relearning…* (ICLR 2026, Fig. 5); DUSK → Jeung, Yoon, Hong, Kim, Han, Yu, No (Fig. 1); R-TOFU → Yoon, Jeung, No (EMNLP 2025 oral, Fig. 1).
3. Both `figs/` captures were **verified against the source PDFs** (arXiv:2406.13356 p. 3 and arXiv:2602.03379) by caption text plus a page render, not from memory.

**Speaker notes realigned in the same pass.** `unlearning2-notes.html` **95 → 100 entries**: ids `#s47`–`#s95` re-keyed to their new slide numbers, the note for the retired RURK-figure slide deleted, and six new entries written (ELM figure 47, ELM analysis 48, TOFU 56, WMDP 63, RWKU 66, MUSE 68) in the existing `.say` / `.board` / `.ask` vocabulary, with the four `<hr class="sec">` + `.sec-label` boundaries re-placed at slides 1 / 24 / 54 / 79.

Verified by full 100-page headless render with the mandated `--virtual-time-budget=30000 --run-all-compositor-stages-before-draw` flags, then `-r 60` reads of every image slide (47, 48, 55, 56, 62, 63, 65, 66, 67, 68, 85, 86, 88, 89, 90, 92). One defect found and fixed: the first ELM draft carried the figure **and** two bullets, overrunning into the brand footer — split into the figure/analysis pair above and the image raised to `max-height: 430px`. `lint-deck.py` clean, `find-dense.py` clean.

---

## Cross-references

- **Homework `hw4sol.pdf`** (5-problem) is taught from the Part I slides, woven in without "Homework 4 / Problem N" labels: the influence→Newton→certification block `unlearning1-foundations.html:463-822` is the long-form walkthrough of the influence-unlearning + certified-Gaussian problems, and the MIA problems (NP optimal test, DP⇒MIA cap, Yeom gap floor) live on the recall card `1:1522` and Proposition 4 `1:1535`. The deck holds the hints; the PDF is left untouched (do not edit it).
- **Memorization** is the motivating signal — lawsuits in `privacy/lectures/03-memorization/memorization-diffusion.html:140`, Cooper's framing in `privacy/lectures/03-memorization/memorization-llm.html:384`. Both reused on Part I "Why This Became Urgent" `1:123`.
- **MIA-Efficacy** as evaluation reuses the threshold attacks defined in `privacy/lectures/04-mia/mia1-foundations.html` and the LiRA-style calibration from `privacy/lectures/04-mia/mia4-modern.html`. Part I does **not** restate that theory: slide `1:1522` is a recall card only, and the new content is Proposition 4 `1:1535` — the cap those results imply for *unlearning* metrics.
- **DP** as the parent of certified unlearning — see `privacy/lectures/01-dp/dp8-fl.html:375` (or the $(\varepsilon,\delta)$-DP definition in `privacy/lectures/01-dp/dp4-approximate-dp.html:81`). Theorem 2 `1:796` reduces to the Gaussian mechanism recalled at `1:782`; the "certified ≠ DP" slide `1:361` and the capacity separation `1:966` mark the boundary in the other direction.
- **Influence function** also referenced beyond IU — Sekhari capacity follows from the same first-order analysis.
- **DPO → NPO** — Part II does **not** re-derive the KL-regularized RLHF optimum. That derivation and the DPO corollary live in `privacy/lectures/02-generative/llm.html:822, :929`, and the NPO preview slide there (`:937`) is the hand-off. Part II slide `2:540` is a one-slide recall of DPO, and the new content starts at `2:552` (NPO as DPO with the positive branch deleted) with Theorems 6–7 and Propositions 8–10.
- **The split confound** — Part II slide `2:1107` is a recall card for `privacy/lectures/04-mia/mia5-llm.html:1424` (**Proposition 7**, a $\theta$-independent split measures text, not membership; proof `:1441`, reading `:1457`). The new content is Proposition 13 `2:1122`, which carries the same argument over to forget-vs-retain benchmark splits, plus `2:1133` on which designs escape it. Proposition 14 `2:1152` is the output-metric blindness result that follows.
- **Part I → Part II hand-off** — §01 of Part II is written against Part I's certificate: the two unstated hypotheses `2:165` are exactly Definition 3 `1:259` plus the unique-minimiser assumption behind Theorem 1 `1:572`, and the assumption map `2:206` names which Part-I result each LLM property invalidates. Proposition 4 `2:396` is the formal statement that the Part-I guarantee does not carry.
- **Diffusion-LLM watermarking (dgMARK)** is a sibling lab thread — see `talks/kics260521dllm/kics260521dllm.html:707`. Watermark deck `privacy/lectures/06-watermark/watermark.html` is the broader context.
