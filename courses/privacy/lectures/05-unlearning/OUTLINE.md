# privacy/lectures/05-unlearning/ — Machine unlearning

Two-part lecture on machine unlearning, split at the LLM boundary. **Part I** (`unlearning1-foundations.html`) — definitions, certified deletion (full derivation with proofs), and classical/classification unlearning + metrics. **Part II** (`unlearning2-llm.html`) — LLM unlearning methods and benchmarks/failures. Theory covered: three nested definitions, Newton-step certified deletion (Theorem 1 with two proved lemmas), Gaussian certification (Theorem 2), Sekhari capacity (Theorem 3), SISA cost model (Proposition 3), the certification-caps-every-metric bound (Proposition 4), GA collapse, NPO bounded-loss, plus the full classification + LLM + benchmark + lab thread. Source: `privacy/slide.pdf` and `privacy/privacy.md` reference table.

The folder's `hw4sol.pdf` is the 5-problem homework (P1 Neyman–Pearson, P2 DP⇒MIA, P3 Yeom gap, P4 influence unlearning, P5 certified Gaussian). Its hints/roadmaps are taught **inside the Part I slides** with **no "Homework 4 / Problem N" labels** (2026-06 decision, preserved): the influence→Newton→certification block is the P4/P5 walk-through, and the MIA recall/Proposition-4 block carries P1–P3. (Do not edit `hw4sol.pdf`; the hints live in the deck.)

## Files

| Deck | Topic |
|---|---|
| `unlearning1-foundations.html` | **Part I** (107 slides) — motivation · three definitions · certified/Newton (proved) · SISA · classification algorithms · metrics-as-hypothesis-test |
| `unlearning2-llm.html` | **Part II** (29 slides) — LLM methods · benchmarks · failures · lab |

---

## unlearning1-foundations.html (Part I — before LLMs) — 107 slides

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
| **03** — Classification metrics | metric-as-test, MIA recall, Proposition 4, converse, two-sided, IDI, COLA, benchmark | 85–107 | `:1435-1800` |
| | §03 divider · an unlearning metric is a hypothesis test | 85–86 | `:1435`, `:1443` |
| | The chain every metric follows (SVG) · the standard suite | 87–88 | `:1460`, `:1490` |
| | MIA as an unlearning probe | 89 | `:1507` |
| | **Recall — three facts about membership tests** (NP optimal test, Yeom $\Delta/B$ floor, DP cap) | 90 | `:1522` |
| | **Proposition 4 — certification caps every metric** (+ proof) · corollary: a passing score is not evidence | 91–93 | `:1535`, `:1547`, `:1559` |
| | The converse fails — head distillation (table) | 94 | `:1573` |
| | The test is two-sided · both sides of the target (SVG) | 95–96 | `:1588`, `:1609` |
| | **IDI** (lab, AAAI 2026) · reading the index · what it sees that outputs do not (table) | 97–99 | `:1642`, `:1658`, `:1673` |
| | Over-unlearning is not hypothetical | 100 | `:1690` |
| | **COLA** — collapse + align (lab) · COLA in numbers | 101–102 | `:1706`, `:1719` |
| | SalUn benchmark table (CIFAR-10 / ResNet-18, 10% random) · reading it correctly | 103–104 | `:1733`, `:1748` |
| | What a defensible evaluation looks like | 105 | `:1763` |
| | Takeaways — Part I · closer → Part II | 106–107 | `:1776`, `:1789` |

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

**Key formulas (Part I):** Certified $(\varepsilon,\delta)$ two-sided inequality `1:264-267`; leave-one-out target `1:406`; continuous path $L_t$ `1:485`; influence via IFT, $\theta'(0)=\tfrac1n H^{-1}\nabla\ell$ `1:521`; the plus sign, explained `1:531`; influence-unlearning update `1:547`; same update as a Newton step `1:567`; Theorem 1 residual $MG^2/(2\lambda^3n^2)$ `1:577`; Newton error identity (Lemma 2) `1:636`; Hessian-choice discrepancy $G\kappa/(\lambda^2n^2)$ `1:711`; $\ell_2$-sensitivity $2G/(\lambda n)$ `1:735`; recall Gaussian mechanism `1:787`; certified $\sigma \ge \eta\sqrt{2\ln(1.25/\delta)}/\varepsilon$ `1:804`; unlearning noise $\propto 1/n^2$ `1:830`; Sekhari deletion capacity `1:904`; SISA cost $n(R+1)(2R+1)/(6SR)$ `1:1107`; SCRUB KL `1:1244`; SalUn mask `1:1297-1300`; $\ell_1$-sparse `1:1347`; RURK objective `1:1404`; Proposition 4 TV cap `1:1541`; IDI `1:1647`.

**Key figures (Part I) — nine inline `u1-` SVG:** commuting diagram `1:206`; three definitions as nested sets `1:273`; LOO path + Newton step + residual gap `1:677`; noise-vs-$n$ log-log ($1/n^2$ against $1/n$) `1:840`; deletion capacity as a consumed budget `1:942`; SISA shard/slice grid `1:1031`; SalUn mask `1:1307`; metrics-as-test-statistics chain `1:1460`; two-sided target number line `1:1609`.

**Real paper figures (Part I) — captured from the arXiv PDFs, stored in `figs/`:**

| File | Source | Slide · line |
|---|---|---|
| `figs/scrub-maxsteps-only.png` + `figs/scrub-alternating.png` | Kurmanji et al., *Towards Unbounded Machine Unlearning*, NeurIPS 2023 (arXiv:2302.09880) — Figure 6(a) and 6(d) | 75 · `1:1274` |
| `figs/salun-saliency-sparsity.png` | Fan et al., *SalUn*, ICLR 2024 (arXiv:2310.12508) — Figure A1(a) and A1(b) | 78 · `1:1333` |
| `figs/rurk-residual-knowledge.png` | Hsu et al., *The Unseen Threat*, NeurIPS 2025 (arXiv:2601.22359) — Figure 1 | 82 · `1:1386` |

Two `<!-- TODO real figure: … -->` markers remain, both on lab papers not posted to arXiv: **IDI** `1:1642` and **COLA** `1:1706` — ask Albert for the AAAI 2026 source PDF.

**Key formulas (Part II):** GA gradient blow-up `2:107`; NPO `2:121`; NPO bounded gradient `2:138`; SimNPO `2:154`; ME+GD `2:172`; LUNAR redirection (aligned) `2:235`.

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
| NPO bounded-divergence (Part II) | `2:142` | — |

**Homework-4 in-deck (woven, not labeled):** the influence→Newton→certification block `1:463-822` is the long-form walkthrough of the influence-unlearning (P4) and certified-Gaussian (P5) problems; the MIA problems (P1 Neyman–Pearson optimal test, P2 DP⇒MIA cap, P3 Yeom gap floor) live on the recall card **"Recall — Three Facts About Membership Tests"** `1:1522` and the Proposition-4 block that follows. No "Homework 4 / Problem N" labels appear on slides — the outline flows inside the lecture content.

**Lab papers cited:** IDI/COLA — Jeon, Jeung, Kim, No, Choi, *An Information Theoretic Evaluation Metric for Strong Unlearning*, AAAI 2026 (Part I `1:1642`, `1:1706`); R-TOFU (EMNLP 2025, main-figure image); DUSK (ACL 2026 Findings, main-figure image); syntactic relearning (ICLR 2026); position paper (Yoon, Jun, No; ICML 2026) — all Part II. (SEPS slide dropped 2026-06.)

**Companion note — `unlearning1-notes.html`** (non-standard plural filename; do **not** rename). 46 entries covering all 107 slides, each badged with the slide or slide range it serves. Structure: `.toc` two-column index with slide-range badges, then one `.slide-note` block per teaching beat (`.snum` / `.stag` / `.timing` / `<h3>`, body of `.say` spoken lines, `.board` derivations, `.ask` anticipated questions, `.key` highlights, `.sec-label` on the three section dividers). Total spoken budget ≈ 110 min. Board-work entries worth knowing about: the $1/n$ vs $1/(n-1)$ identity; assumptions A1–A3 and the two jobs of strong convexity; the Lemma-2 integral identity; the Guo objective-perturbation caveat; the Sekhari risk decomposition; the SISA double sum; the Proposition-4 signed-measure proof.

**Audit history.** 2026-05 visual audit: split Newton-Step theorem 1→2 slides; consolidated LUNAR math. 2026-06 revision: every `.cite` shortened to one rendered line; "Why Now" GDPR **Art. 17** confirmed + lawsuits one-per-line + Carlini·Cooper cite; Newton block expanded 2→8 slides; **fixed sign error** on influence-function slide ($+\tfrac1n H^{-1}\nabla\ell$). 2026-06 split: single 63-slide `unlearning.html` retired and split into Part I (`unlearning1-foundations.html`) and Part II (`unlearning2-llm.html`); Part II sections renumbered 01/02. 2026-06 reorder: moved the influence-function slide from §02 up to lead into the Newton block (so the Newton step no longer feels sudden); folded the homework hints into the natural flow (removed the explicit "Homework 4" roadmap slides; the MIA problems became "MIA: Optimal Test and Its Limits"). Part I now 36 slides, Part II 32. 2026-06 benchmark figures: embedded each benchmark's **actual main-figure image** — `tofu.png` (pretrained→finetuned→unlearned pipeline), `WMDP.png` (bio/chem/cyber three-domain pie, 3,668 Q), `RWKU.png` (forget/neighbor/MIA/utility framework), `MUSE.png` (six-way data-owner/deployer grid), `DUSK.png` (forget-all vs forget-unique Venn partitions) — figure dominant + one-line caption (`cite cite-left` added locally); glossed each of Cooper's 5 mismatches; sharpened the Triantafillou "progress" takeaway; **removed the Pawelczyk verification-hardness slide**; venues updated — DUSK → ACL 2026 Findings, position paper → ICML 2026 accepted (Position Track) with an "Accepted · ICML 2026" pill. Part II now 31 slides. (Image PNGs live alongside the deck; `bundle.py` base64-inlines them for the standalone build.) 2026-06 trim: **removed the Guardrail/ECO slide**; replaced ELM's bullet explanation with its main-figure image (`elm.png`). Part II now 30 slides. 2026-06 trim 2: **removed the SEPS slide**; added R-TOFU main-figure image (`r-tofu.png`); on the position slide removed the "Accepted · ICML 2026" pill, corrected authors to **Yoon, Jun, No**, and tightened the proposal wording. Part II now 29 slides.

**2026-08 math-detail revision (Part I only; Part II untouched).** Part I **36 → 107 slides**, `unlearning1-notes.html` **36 → 46 entries**. Added: three numbered definitions with a nested-set figure; Propositions 1–2 with proofs, a certified-and-useless counterexample, and an explicit "certified ≠ DP" slide; a standing-convention slide and the $1/n$ vs $1/(n-1)$ note; assumptions A1–A3 stated before use; the influence derivation carried through the IFT term by term with the sign explained; Theorem 1 proved in full via Lemma 1 and a two-slide Lemma 2 (Newton error identity, curvature-gap bound); the which-Hessian discrepancy and a "you never form $H^{-1}$" (CG / LiSSA) slide; Lemma 3 proved; Theorem 2 proved by reduction to the Gaussian mechanism, with a separate slide on what Guo et al. *actually* prove (objective perturbation, not output noise); Theorem 3 restated in the paper's correct form with a proof sketch, a budget figure and the DP separation; an honest "when influence functions fail" pair (Basu 2021); SISA made quantitative by Proposition 3 with a three-slide proof; §02 given per-method geometry and a "certified? no" column plus a verification-problem bridge; §03 reframed so that every metric is a **test statistic** for $H_0:\theta_u \sim \mathcal{A}(\mathcal{D}_r)$, with Proposition 4 (certification caps every bounded metric) proved, its vacuity corollary, the head-distillation converse, and the two-sided target made explicit. **Corrections made during the audit** (all previously on slides or in the notes): Sekhari capacity mis-stated as linear in $\varepsilon$ with $\sqrt d$ → $c\,n\sqrt{\varepsilon}/(d\log(1/\delta))^{1/4}$; Guo certification mis-attributed to output perturbation; COLA's two stages described wrongly on both counts; IDI citation had wrong authors/title/venue; RURK citation wrong; an unverifiable IDI baseline value $-0.110$ removed (the verified pair is $-0.349$ / $-0.060$). The old "MIA: Optimal Test and Its Limits" slide became a recall card plus Proposition 4. Verified by full 104-page headless-Chrome render at `-r 60`; nine layout defects found and fixed (one slide split, one unfilled Bézier, six label-overlap groups, one clipped label).

**2026-08 figure pass + errata (Part I).** arXiv turned out to be reachable from the container, so three of the five `TODO real figure` markers were filled with real captures (SCRUB Fig. 6a/6d, SalUn Fig. A1a/A1b, RURK Fig. 1 — see the **Real paper figures** table above); Part I **104 → 107 slides**. The SalUn capture uses **Figure A1**, not the paper's Figure 1: Figure 1 is a diffusion-model schematic whose examples are "Nudity"-concept generations, which is Part II's territory and unsuitable for a classroom slide, whereas A1 is the classification saliency-sparsity trade-off against the Retrain reference line and continues the "Reading the Mask" thread directly. Two markers remain (IDI `1:1642`, COLA `1:1706`) — lab papers, not on arXiv, need Albert's PDFs.

**Two errata from the same pass, both now fixed:**

1. **The SalUn benchmark row was never fabricated.** The mid-revision "correction" to `1.55/99.88/93.93/13.28/1.13` was itself the error. arXiv:2310.12508 Table 1 (p. 7, CIFAR-10 / ResNet-18, 10% random data forgetting) reads SalUn `2.85±0.43 / 99.62±0.12 / 93.93±0.29 / 14.39±0.82`, avg gap `1.15`, RTE `2.66` — i.e. the deck's **original** numbers were right. The table row, the "Reading That Table Correctly" bullet, and the notes entry have all been reverted to the paper's values, and the notes carry a sourced audit paragraph recording the round trip. The reading also changed: SalUn's MIA **overshoots** retrain's `12.88`; it wins on average closeness, not on any single axis.
2. **RURK Proposition 2 was mis-stated.** The slide said "a larger radius forces a larger $\varepsilon$." The paper says the opposite shape: for **fixed** $(\varepsilon,\delta)$ the disagreement probability depends solely on $\tau$ and rises as $\tau$ grows. Bullet rewritten.

---

## Cross-references

- **Homework `hw4sol.pdf`** (5-problem) is taught from the Part I slides, woven in without "Homework 4 / Problem N" labels: the influence→Newton→certification block `unlearning1-foundations.html:463-822` is the long-form walkthrough of the influence-unlearning + certified-Gaussian problems, and the MIA problems (NP optimal test, DP⇒MIA cap, Yeom gap floor) live on the recall card `1:1522` and Proposition 4 `1:1535`. The deck holds the hints; the PDF is left untouched (do not edit it).
- **Memorization** is the motivating signal — lawsuits in `privacy/lectures/03-memorization/memorization-diffusion.html:140`, Cooper's framing in `privacy/lectures/03-memorization/memorization-llm.html:384`. Both reused on Part I "Why This Became Urgent" `1:123`.
- **MIA-Efficacy** as evaluation reuses the threshold attacks defined in `privacy/lectures/04-mia/mia1-foundations.html` and the LiRA-style calibration from `privacy/lectures/04-mia/mia4-modern.html`. Part I does **not** restate that theory: slide `1:1522` is a recall card only, and the new content is Proposition 4 `1:1535` — the cap those results imply for *unlearning* metrics.
- **DP** as the parent of certified unlearning — see `privacy/lectures/01-dp/dp8-fl.html:375` (or the $(\varepsilon,\delta)$-DP definition in `privacy/lectures/01-dp/dp4-approximate-dp.html:81`). Theorem 2 `1:796` reduces to the Gaussian mechanism recalled at `1:782`; the "certified ≠ DP" slide `1:361` and the capacity separation `1:966` mark the boundary in the other direction.
- **Influence function** also referenced beyond IU — Sekhari capacity follows from the same first-order analysis.
- **Diffusion-LLM watermarking (dgMARK)** is a sibling lab thread — see `talks/kics260521dllm/kics260521dllm.html:707`. Watermark deck `privacy/lectures/06-watermark/watermark.html` is the broader context.
