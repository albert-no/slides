#!/usr/bin/env python3
"""Small KL, huge weight second moment (evidence E14) for prob09 slide S105.

Deterministic two-state calculation, natural logs (nats); no random numbers.
Roles: pi_theta = p (current/target), pi_b = pi_ref = q (sampler and reference coincide here).
Prints D_KL(p||q), E_q[w^2] with w = p/q, and the Jensen lower bound exp(D_KL).
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
