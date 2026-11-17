#!/usr/bin/env python3
"""Small KL, huge weight second moment (evidence E14) for prob09 slide S105.

Deterministic two-state calculation, natural logs (nats); no random numbers.
Roles: pi_theta = p (current/target), pi_b = pi_ref = q (sampler and reference coincide here).
Prints D_KL(p||q), E_q[w^2] with w = p/q, and the Jensen lower bound exp(D_KL).
Also prints a finite-difference check of the reward-plus-KL score gradient (evidence E21)
on a fixed three-outcome softmax example, so the note's derivation has a numeric check.
"""
import math

p = (0.9999, 0.0001)
q = (1 - 1e-12, 1e-12)
kl = sum(pi * math.log(pi / qi) for pi, qi in zip(p, q))
m2 = sum(pi * pi / qi for pi, qi in zip(p, q))
print("p (pi_theta)          =", p)
print("q (pi_b = pi_ref)     =", q)
print("D_KL(p||q) [nats]     = %.14f" % kl)
print("E_q[w^2] = sum p^2/q  = %.8f" % m2)
print("Jensen lower bound exp(KL) = %.6f  (lower bound on E_q[w^2], not an upper bound)" % math.exp(kl))
print("terms of E_q[w^2]: %.8f + %.8f" % (p[0] ** 2 / q[0], p[1] ** 2 / q[1]))

# ---- E21 numeric check: J(th) = sum p r - beta sum p ln(p/ref), p = softmax(th) ----
r = (1.0, 0.0, 2.0)          # fixed reward (illustrative)
ref = (0.5, 0.3, 0.2)        # fixed positive reference
beta = 0.7
th = [0.2, -0.4, 0.1]

def softmax(t):
    m = max(t); e = [math.exp(x - m) for x in t]; z = sum(e)
    return [x / z for x in e]

def J(t):
    pr = softmax(t)
    return sum(a * b for a, b in zip(pr, r)) - beta * sum(a * math.log(a / c) for a, c in zip(pr, ref))

pr = softmax(th)
# score of softmax: d/dth_k ln p_x = 1[x=k] - p_k
score_form = []
for k in range(3):
    score_form.append(sum(pr[x] * (r[x] - beta * math.log(pr[x] / ref[x])) * ((1 if x == k else 0) - pr[k])
                          for x in range(3)))
h = 1e-6
fd = []
for k in range(3):
    tp = th[:]; tm = th[:]; tp[k] += h; tm[k] -= h
    fd.append((J(tp) - J(tm)) / (2 * h))
print("E21 check  score form   =", ["%.8f" % v for v in score_form])
print("E21 check  finite diff  =", ["%.8f" % v for v in fd])
print("max abs difference      = %.2e" % max(abs(a - b) for a, b in zip(score_form, fd)))
