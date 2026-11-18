#!/usr/bin/env python3
"""prob09 Part 04 (job 2026-11-18-prob09-oracle-tails-softmax): three-outcome softmax toy (S132, S73, S133, S76).

Our toy, exact arithmetic, no random draws (softmax definition: Goodfellow, Bengio & Courville,
Deep Learning, Sec. 6.2.2.3, eq. (6.29)):
    outcomes A, B, C; logits z = (0, ln 2, ln 4); masses a_k = exp(z_k) = (1, 2, 4)
    Z = sum_k a_k = 7;  p(k) = a_k / Z = (1/7, 2/7, 4/7)
    target mu = p(C) = E_p[f], f(k) = 1{k = C}
SNIS with q = Uniform{A, B, C}: tilde w(k) = a_k / q(k) = 3 a_k; the common 3 cancels.
Illustrative batch (A, C, C): a hand-picked possible batch, not a simulation.
Run:  python3 gen/p9f_unknown_z.py
"""
import math
from fractions import Fraction as F

K = ('A', 'B', 'C')
z = {'A': 0.0, 'B': math.log(2), 'C': math.log(4)}
a = {k: F(round(math.exp(z[k]))) for k in K}
for k in K:
    assert abs(math.exp(z[k]) - float(a[k])) < 1e-12
Z = sum(a.values())
p = {k: a[k] / Z for k in K}
f = {k: 1 if k == 'C' else 0 for k in K}
mu = sum(p[k] * f[k] for k in K)
print("== Softmax (S132) ==")
print(f"masses a = exp(z) = {[str(a[k]) for k in K]};  Z = {Z};  p = {[str(p[k]) for k in K]};  sum p = {sum(p.values())}")
print(f"mu = p(C) = {mu} = {float(mu):.6f}")

print("== Sums replace integrals (S76) ==")
print(f"sum_k a_k f(k) = {sum(a[k]*f[k] for k in K)} = Z mu = {Z*mu};  sum_k a_k = {Z}")
q = {k: F(1, 3) for k in K}
wt = {k: a[k] / q[k] for k in K}
print(f"q uniform 1/3; tilde w = a/q = {[str(wt[k]) for k in K]} = 3a;  E_q[tilde w] = {sum(q[k]*wt[k] for k in K)} = Z;"
      f"  E_q[tilde w f] = {sum(q[k]*wt[k]*f[k] for k in K)} = Z mu")

print("== Illustrative batch A, C, C (S133) ==")
batch = ('A', 'C', 'C')
num = sum(wt[x] * f[x] for x in batch)
den = sum(wt[x] for x in batch)
num_a = sum(a[x] * f[x] for x in batch)
den_a = sum(a[x] for x in batch)
est = num / den
assert est == F(num_a, den_a)
print(f"tilde w = {[str(wt[x]) for x in batch]};  ratio {num}/{den} = {num_a}/{den_a} = {est} = {float(est):.6f}")
print(f"true mu = {mu} = {float(mu):.6f};  error {est - mu} = {float(est - mu):.6f};  P_q(ordered batch) = {F(1, 3)**3}")
