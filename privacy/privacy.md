# Data Privacy

# MIA

| 논문제목 | 논문 요약 | 링크 |
| --- | --- | --- |
| Membership Inference Attacks against Machine Learning Models | *Shokri - black-box 분류모델에서 샘플이 훈련셋에 있었는지 맞히는 공격 - MIA 첫 논문 | [https://arxiv.org/pdf/1610.05820](https://arxiv.org/pdf/1610.05820) |
| Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting | MIA가 왜 가능한지 DP 기반 이론으로 증명한 논문 - loss 기반 threshold 논문 | [https://arxiv.org/abs/1709.01604](https://arxiv.org/abs/1709.01604) |
| Understanding Membership Inferences on Well-Generalized Learning Models | Generalized MIA 제시 - 일반화가 잘 되어 있어도 취약한 샘플이 있고 그 샘플들에 대해 MIA 적용 | [https://arxiv.org/pdf/1802.04889](https://arxiv.org/pdf/1802.04889) |
| ML-Leaks: Model and Data Independent Membership Inference Attacks and Defenses on
Machine Learning Models | Shadow model이 1개밖에 없는 상황이 있을 수 있는 공격 상황을 가정하여 이 세팅에서도 shokri 논문과 비슷한 성능을 보임
Shadow model이 같은 분포의 데이터로 학습되지 않아도 됨 - 각 샘플의 상위 3개의 feature만 사용해서 signal로 사용 (심지어 refer 모델이 없어도 가능) | [https://arxiv.org/abs/1806.01246](https://arxiv.org/abs/1806.01246) |
| Comprehensive Privacy Analysis of Deep Learning: Passive and Active White-box Inference Attacks against Centralized and Federated Learning | shokri 논문 - white box MIA gradient paprmeter 업데이트 등을 모두 확인 가능하면 더 강한 MIA를 적용할 수 있음 /activation/output~~만~~ 보는 black-box식 확장은 white-box에서 충분히 강하지 않고, 대신 SGD가 남기는 gradient/update 신호를 활용해야 더 잘 맞음 | [https://arxiv.org/abs/1812.00910](https://arxiv.org/abs/1812.00910) |
| White-box vs Black-box: Bayes Optimal Strategies for Membership Inference | MIA의 대부분 신호는 loss에 있어서 white box setting이 꼭 black box보다 세다고 할 수는 없음 | [https://arxiv.org/abs/1908.11229](https://arxiv.org/abs/1908.11229) |
| LOGAN: Membership Inference Attacks Against Generative Models | 최초의 생성 모델 MIA 논문 GAN에서 dicriminator가 member와 non member의 미세한 차이를 학습할 수 있어서 이 signal로 MIA를 적용할 수 있음 - Jamie Hayes | [https://arxiv.org/abs/1705.07663](https://arxiv.org/abs/1705.07663) |
| Membership Inference Attacks on Sequence-to-Sequence Models: Is My Data In Your Machine Translation System? | Sequence to sequence 모델에 대해 MIA 적용을 한 첫 논문. shokri 식 MIA 적용을 하면 language model에 대해서는 거의 성공을 하지 못 하지만 OOD or OOV(vocabulary)에 대해서는 0.8 이상의 성능을 보임
또한 문장 단위로 MIA를 적용하는 것보다 문장 모음 단위로 공격을 적용했을 때 더 높은 성능을 보임 | [https://arxiv.org/abs/1904.05506](https://arxiv.org/abs/1904.05506) |
| Systematic Evaluation of Privacy Risks of Machine Learning Models | MIA가 privacy 관점에서 과소평가 되고 있기 때문에 MIA를 AUC 관점으로 보지 말고 샘플별 위험도까지 함께 봐야 함 - privacy risk score 제시 sample이 member일 posterior probability 측정 | [https://arxiv.org/pdf/2003.10595](https://arxiv.org/pdf/2003.10595) |
| Label-Only Membership Inference Attacks | *Carlini 논문 - data augmentation attack :  원본 샘플에 변형을 가해서 예측값이 바뀌는지 확인 / boundary distance attack : 샘플이 decision boundary에서 얼마나 떨어져 있는지 측정
  • member인 경우는 공격에 더 robust 하고 non member의 경우는 더 쉽게 예측값이 바뀜 (confidence를 보지 않아도 됨) | [https://arxiv.org/pdf/2007.14321](https://arxiv.org/pdf/2007.14321) |
| Membership Inference Attacks From First Principles | carlini (LiRA) - 프라이버시의 경우 낮은 FPR에서의 성능이 중요하다고 주장하며 member와 non member간에 likelihood ratio로 해당 값을 attack metric으로 사용해서 해당 값을 보정 | [https://arxiv.org/pdf/2112.03570](https://arxiv.org/pdf/2112.03570) |
| Enhanced Membership Inference Attacks against Machine Learning Models | *Shokri - MIA를 hypothesis testing으로 표현 reference model attack | [https://arxiv.org/abs/2111.09679](https://arxiv.org/abs/2111.09679) |
| Membership Inference Attacks against Language Models via Neighbourhood Comparison | LM MIA - sample 하나만 볼 때 reference base attack에서 sample의 품질이 안 좋아지면 문제가 발생, 따라서 neighbourhood attack 제시. sample의 synthetic neighbor 문장도 봐야 한다고 주장  | [https://arxiv.org/pdf/2305.18462](https://arxiv.org/pdf/2305.18462) |
| Membership Inference Attacks against Diffusion Models | diffusion MIA - diffusion의 denoising 단계와 sampling 설정에서 membership leakage가 커질 수 있음 (sample에 대한 denoising loss 차이로 확인) | [https://arxiv.org/pdf/2302.03262](https://arxiv.org/pdf/2302.03262) |
| Low-Cost High-Power Membership Inference Attacks | RMIA *Shokri - LiRA의 개선 버전, LiRA에서 reference model을 학습하는 cost를 줄이기 위해 reference를 줄일 수 있게 target vs reference model이 아니라 sample vs 다른 sample 로 비교 
  • 이렇게 해도 reference에서 비교하는 것과 비슷한 성능을 보임 | [https://arxiv.org/abs/2312.03262](https://arxiv.org/abs/2312.03262) |
| Membership Inference Attacks against Fine-tuned Large Language Models via Self-prompt Calibration | LLM MIA는 reference dataset을 shokri 논문처럼 구현할 수 없음 - 따라서 member들의 확률 분포에서 근처에 있는지 확인 즉, neighbor dataset을 만들고, 원문과 이웃 샘플 사이의 차이를 계산하면 멤버는 뾰족한 점의 형태를 띌 것이라 주장. 또한 reference 모델을 얻기 힘든 문제를 해결하기 위해 target에 대해 비슷한 분포의 텍스트를 생성해서 reference model을 fine tuning. | [https://arxiv.org/pdf/2311.06062](https://arxiv.org/pdf/2311.06062) |
| Context-Aware Membership Inference Attacks against Pre-trained Large Language Models | LLM MIA를 문장 전체의 평균 loss나 perplexity를 보는 게 아니라 각 토큰의 prefix 문맥에서 어떻게 signal이 나타나는지 확인해야 한다고 주장
  • per token loss를 보고 초반 토큰만 잘라서 loss를 확인/ loss가 얼마나 빨리 감소하는지, 낮은 loss 토큰이 얼마나 안정적으로 이어지는지, entropy 확인, 문장을 한 번 더 반복했을 때 loss가 얼마나 줄어드는지 확인 | [https://arxiv.org/pdf/2409.13745](https://arxiv.org/pdf/2409.13745) |
| InfoRMIA: Stronger Membership Inference and Memorization Assessment for LLMs | InfoRMIA *Shokri - RMIA에서 문장 단위의 비교와 discrete 한 비교의 단점을 보안하기 위해 제시. 문장 단위를 token 단위로 비교하고 이기는 횟수 count 하는 방식을 얼마나 이기는지 log 확률값으로 바꿔서 연속으로 바꿈 | [https://arxiv.org/abs/2510.05582](https://arxiv.org/abs/2510.05582) |
|  |  |  |
|  |  |  |
|  |  |  |

# Unlearning

| 논문제목 | 논문 요약 | 링크 |
| --- | --- | --- |
| Towards Making Systems Forget with Machine Unlearning | right to be forgotten을 기반으로 Machine Unlearning의 개념을 제시한 최초의 논문 | [https://www.ieee-security.org/TC/SP2015/papers-archived/6949a463.pdf](https://www.ieee-security.org/TC/SP2015/papers-archived/6949a463.pdf) |
| Machine Unlearning | SISA(Sharded, Isolated, Sliced, Aggregated) - 데이터를 분리해서 학습을 하여 재학습 없이 unlearning 수행 | [https://arxiv.org/abs/1912.03817](https://arxiv.org/abs/1912.03817) |
| Certified Data Removal from Machine Learning Models | Certified Unlaerning 첫 논문 - DP 관점에서 unlearning을 보장할 수 있어야 한다고 주장 | [https://arxiv.org/pdf/1911.03030](https://arxiv.org/pdf/1911.03030) |
| Approximate Data Deletion from Machine Learning Models | James Zou* Unlearning을 Data deletion을 관점으로 unlearning의 정의를 제시 | [https://arxiv.org/pdf/2002.10077](https://arxiv.org/pdf/2002.10077) |
| Eternal Sunshine of the Spotless Net: Selective Forgetting in Deep Networks | retain set에는 Fine tuning하고 forget set에 대해서는 random labeling을 하는 방식으로 unlearning | [https://arxiv.org/pdf/1911.04933](https://arxiv.org/pdf/1911.04933) |
| Unrolling SGD: Understanding Factors Influencing Machine Unlearning | Papernot* GA loss 사용 | [https://arxiv.org/pdf/2109.13398](https://arxiv.org/pdf/2109.13398) |
| Can Bad Teaching Induce Forgetting? Unlearning in Deep Networks Using an Incompetent Teacher | Distillation을 활용하여 Unlearning retain data와 forget  data를 분리하도록 distillation | [https://arxiv.org/pdf/2205.08096](https://arxiv.org/pdf/2205.08096) |
| Descent-to-Delete: Gradient-Based Methods for Machine Unlearning | strong unlearning. Parameter level에서 indistinguishability 해야함을 주장 | [https://arxiv.org/abs/2007.02923](https://arxiv.org/abs/2007.02923) |
| Towards Adversarial Evaluations for Inexact Machine Unlearning | IC test (Interclass Confusion test) 제안/ 모델이 정말 unlearning 됐는지 확인하는 test class를 바꿨을 때 생기는 confusion으로 잊혀지는지 확인 | [https://arxiv.org/pdf/2201.06640](https://arxiv.org/pdf/2201.06640) |
| Towards Unbounded Machine Unlearning | SCRUB. 원래 모델을 teacher, unlearned model을 student로 두고, student가 retain set에서는 teacher를 따르되, forget set에서는 teacher와 일부러 멀어지게 학습 | [https://arxiv.org/pdf/2302.09880](https://arxiv.org/pdf/2302.09880) |
| SALUN: Empowering Machine Unlearning via Gradient-Based Weight Saliency in Both Image Classification and Generation | SALUN 지워야할 가중치만 지우는 방법 제시. forget loss에 대해 gradient의 절대값이 큰 weight를  선택해서 제거 | [https://arxiv.org/pdf/2310.12508](https://arxiv.org/pdf/2310.12508) |
| Model Sparsity Can Simplify Machine Unlearning | ℓ1 기반 sparsity regularization을 objective에 넣어서, 지우는 과정 자체가 sparse 방향으로 가도록 만들고 unlearning | [https://arxiv.org/pdf/2304.04934](https://arxiv.org/pdf/2304.04934) |
| An Information Theoretic Evaluation Metric for Strong Unlearning | our paper* 출력만 보는 기존 평가 대신 중간표현에 남아 있는 forget-label 상호정보를 IDI로 측정하고, 이를 줄이기 위해 forget representation을 collapse한 뒤 retain representation을 다시 맞추는 COLA를 제안 | [https://arxiv.org/pdf/2405.17878](https://arxiv.org/pdf/2405.17878) |
| What makes unlearning hard and what to do about it | unlearning이 어려워지는 핵심 원인을 forget–retain entanglement와 forget-set memorization으로 분석하고, forget set을 이런 난이도별로 쪼개 각 부분에 기존 알고리즘을 순차 적용해 성능을 높이는 RUM 제시 | [https://arxiv.org/pdf/2406.01257](https://arxiv.org/pdf/2406.01257) |
| LLM unlearning |  |  |
| Knowledge Unlearning for Mitigating Privacy Risks in Language Models | Joel Jang* LLM unlearning GA 방식 제안 | [https://arxiv.org/abs/2210.01504](https://arxiv.org/abs/2210.01504) |
| Simplicity Prevails: Rethinking Negative Preference Optimization for LLM Unlearning | NPO, GA의 catastrophic forgetting 문제를 보안하기 위해 RL에서 사용하는 DPO 방식에서 착안한 NPO 방식 제안 | [https://arxiv.org/abs/2410.07163](https://arxiv.org/abs/2410.07163) |
| Large language model unlearning | Gradiff GA 방식의 unlearning | [https://arxiv.org/pdf/2310.10683](https://arxiv.org/pdf/2310.10683) |
| The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning | RMU hidden state를 uniform 하게 만듦 / 위험한 지식 생성에 대한 unlearning benchmark WMDP 제시. | [https://arxiv.org/pdf/2403.03218](https://arxiv.org/pdf/2403.03218) |
| TOFU: A Task of Fictitious Unlearning for LLMs | IDK refusal 방법 제시 / TOFU benchmark 제시 | [https://arxiv.org/abs/2401.06121](https://arxiv.org/abs/2401.06121) |
| Direct Preference Optimization: Your Language Model is Secretly a Reward Model | DPO/ refusal 기반 방식으로 unlearning 학습할 때 언급 | [https://arxiv.org/abs/2305.18290](https://arxiv.org/abs/2305.18290) |
| A Closer Look at Machine Unlearning for Large Language Models | forget data에 대해 Maximal Entropy를 따르도록 학습하는 방식으로 unlearning | [https://arxiv.org/abs/2410.08109](https://arxiv.org/abs/2410.08109) |
| Meow: Memory Supervised LLM Unlearning via Inverted Facts | 원래 기억의 반대 사실을 주입해 특정 지식을 상쇄시키려는 memory-supervised editing 방식 | [https://arxiv.org/abs/2409.11844](https://arxiv.org/abs/2409.11844) |
| Model Collapse Is Not a Bug but a Feature in Machine Unlearning for LLMs | 일부 editing/unlearning에서 나타나는 model collapse를 오히려 강한 망각 수단으로 해석하는 논문 | [https://arxiv.org/abs/2507.04219](https://arxiv.org/abs/2507.04219) |
| RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models | RWKU 실제 세계 지식 삭제를 대상으로 한 LLM unlearning 벤치마크 | [https://arxiv.org/abs/2406.10890](https://arxiv.org/abs/2406.10890) |
| Large Language Model Unlearning via Embedding-Corrupted Prompts | ECO 모델 가중치는 건드리지 않고, forget 관련 프롬프트만 분류기로 찾아 그 입력 임베딩에 미리 학습한 corruption을 넣어 추론 시점에만 안 배운 모델처럼 행동하게 만드는 ECO 프레임워크 | [https://arxiv.org/abs/2412.06966](https://arxiv.org/abs/2412.06966) |
| DUSK: Do Not Unlearn Shared Knowledge | DUSK forget·retain 데이터가 사실 일부 지식을 공유한다는 현실적 설정을 반영해, 공유 지식은 남기고 forget 데이터 고유 표현만 지워야 함 | [https://arxiv.org/abs/2505.15209](https://arxiv.org/abs/2505.15209) |
| Rethinking Benign Relearning: Syntax as the Hidden Driver of Unlearning Failures | benign relearning의 진짜 원인이 topic 유사성보다 syntax 유사성이라고 보고, forget 질의를 다양한 문장 구조로 패러프레이즈한 뒤 unlearning하는 syntactic diversification으로 재학습에 의한 기억 복구를 줄이자는 논문 | [https://arxiv.org/abs/2602.03379](https://arxiv.org/abs/2602.03379) |
| Machine Unlearning Doesn’t Do What You Think: Lessons for Generative AI Policy and Research | 단순 suppression을 unlearning으로 착각하면 안 된다고 비판하는 정책·개념 정리 논문 | [https://arxiv.org/abs/2412.06966](https://arxiv.org/abs/2412.06966) |
| [**SEPS: A Separability Measure for Robust Unlearning in LLMs**](https://aclanthology.org/2025.emnlp-main.283/) | SEPS forget/retain 분리가 얼마나 잘 됐는지를 separability로 재는 평가 지표 논문 | [https://arxiv.org/abs/2505.14832](https://arxiv.org/abs/2505.14832) |
| Position: The Term “Machine Unlearning” Is Overused in LLMs | 정확히 정의된 forget set을 제거했을 때 재학습한 D∖F 모델과 (근사적으로) 구분되지 않는 경우에만 써야 하고, 나머지는 suppression·editing·alignment·obfuscation 같은 다른 이름으로 구분하자고 주장 |  |

# Memorization

| 논문제목 | 논문 요약 | 링크 |
| --- | --- | --- |
| Understanding Deep Learning Requires Rethinking Generalization | 딥러닝 모델이 랜덤 라벨까지 외울 수 있음을 보여주며, “일반화와 암기” 논의를 촉발한 원조격 논문 | [https://arxiv.org/pdf/1611.03530](https://arxiv.org/pdf/1611.03530) |
| The Secret Sharer: Evaluating and Testing Unintended Memorization in Neural Networks | canary와 exposure metric을 통해 신경망이 민감한 문자열을 의도치 않게 암기·유출할 수 있음을 정량화 | [https://arxiv.org/pdf/1802.08232](https://arxiv.org/pdf/1802.08232) |
| Extracting Training Data from Large Language Models | GPT-2에서 실제 학습데이터 조각, 개인정보, 코드 등을 블랙박스 쿼리로 추출할 수 있음을 보여준 LLM memorization 논문 | [https://arxiv.org/pdf/2012.07805](https://arxiv.org/pdf/2012.07805) |
| Deduplicating Training Data Makes Language Models Better | 중복 데이터가 memorization을 크게 증가시키며, 데이터 deduplication만으로도 암기된 텍스트 방출을 줄일 수 있음을 보임 | [https://arxiv.org/pdf/2107.06499](https://arxiv.org/pdf/2107.06499) |
| Quantifying Memorization Across Neural Language Models | 모델 크기, 데이터 반복, 문맥 길이 등이 memorization에 미치는 영향을 체계적으로 분석 | [https://arxiv.org/pdf/2202.07646](https://arxiv.org/pdf/2202.07646) |
| Copyright Violations and Large Language Models | LLM이 책과 코드 문제를 verbatim으로 재현하는 현상을 저작권 침해 가능성과 연결 | [https://arxiv.org/pdf/2310.13771](https://arxiv.org/pdf/2310.13771) |
| Scalable Extraction of Training Data from Aligned, Production Language Models | 정렬된 상용 LLM에서도 대규모 학습데이터 추출 위험이 남아 있음을 보임 | [https://arxiv.org/pdf/2311.17035](https://arxiv.org/pdf/2311.17035) |
| Measuring Memorization in Language Models via Probabilistic Extraction | 기존 greedy suffix matching보다 현실적인 probabilistic extraction 관점에서 memorization 측정법을 제안 | [https://arxiv.org/pdf/2410.19482](https://arxiv.org/pdf/2410.19482) |
| Extracting Memorized Pieces of (Copyrighted) Books from Open-Weight Language Models | open-weight LLM에서 저작권 도서 일부가 모델별·도서별로 얼마나 추출되는지 분석 | [https://arxiv.org/pdf/2505.12546](https://arxiv.org/pdf/2505.12546) |
| Extracting Books from Production Language Models | Claude, GPT-4.1, Gemini, Grok 같은 production LLM에서 책 단위 추출 가능성을 비교 | [https://arxiv.org/pdf/2601.02671](https://arxiv.org/pdf/2601.02671) |
| Measuring Non-Adversarial Reproduction of Training Data in Large Language Models | 공격적 프롬프트가 아니라 자연스러운 사용자 프롬프트에서도 학습데이터와 겹치는 출력이 얼마나 나오는지 측정 | [https://arxiv.org/pdf/2411.10242](https://arxiv.org/pdf/2411.10242) |

# LLM Watermarking

| 논문제목 | 논문 요약 | 링크 |
| --- | --- | --- |
| A Watermark for Large Language Models | “green-list token”을 약하게 선호하도록 샘플링을 바꿔 LLM 출력에 통계적 watermark를 심음 | [https://arxiv.org/pdf/2301.10226](https://arxiv.org/pdf/2301.10226) |
| On the Reliability of Watermarks for Large Language Models | 사람이 고치거나 LLM이 paraphrase한 뒤에도 watermark가 얼마나 남는지 평가 | [https://arxiv.org/pdf/2306.04634](https://arxiv.org/pdf/2306.04634) |
| Undetectable Watermarks for Language Models | 비밀키 없이는 watermarked output과 일반 output을 구별하기 어렵게 만드는 암호학적 watermark 개념을 제안 | [https://arxiv.org/pdf/2306.09194](https://arxiv.org/pdf/2306.09194) |
| Provable Robust Watermarking for AI-Generated Text | paraphrasing 공격을 염두에 두고, AI 생성 텍스트 watermark의 강건성을 이론적으로 다룸 | [https://arxiv.org/pdf/2306.17439](https://arxiv.org/pdf/2306.17439) |
| Robust Distortion-free Watermarks for Language Models | 텍스트 분포를 왜곡하지 않으면서도 키 기반으로 검출 가능한 “distortion-free” watermark를 제안 | [https://arxiv.org/pdf/2307.15593](https://arxiv.org/pdf/2307.15593) |
| Unbiased Watermark for Large Language Models | watermark가 출력 확률분포와 품질을 얼마나 바꾸는가라는 문제를 다룸 | [https://arxiv.org/pdf/2310.10669](https://arxiv.org/pdf/2310.10669) |
| A Semantic Invariant Robust Watermark for Large Language Models | 단순 토큰 패턴이 아니라 앞선 문맥의 의미 표현을 이용해 paraphrase·동의어 치환에 더 강한 watermark를 만들려함 | [https://arxiv.org/pdf/2310.06356](https://arxiv.org/pdf/2310.06356) |
| Watermarking Makes Language Models Radioactive | **Models Radioactive”**, NeurIPS 2024watermarked text가 후속 모델 학습 데이터로 들어갔는지까지 추적할 수 있다는 “radioactivity” 관점을 제시 | [https://arxiv.org/pdf/2402.14904](https://arxiv.org/pdf/2402.14904) |
| Permute-and-Flip: An Optimally Robust and Watermarkable Decoder for LLMs | decoding 자체를 watermark에 유리하고 robust하게 설계하려함 | [https://arxiv.org/pdf/2402.05864](https://arxiv.org/pdf/2402.05864) |
| Scalable watermarking for identifying large language model outputs | 대규모 실제 서비스 환경에서 text watermarking을 평가한 production-level 사례 | [https://www.nature.com/articles/s41586-024-08025-4](https://www.nature.com/articles/s41586-024-08025-4) |