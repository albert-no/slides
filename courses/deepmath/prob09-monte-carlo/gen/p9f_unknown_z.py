#!/usr/bin/env python3
"""prob09 Part 04 (P3, job 2026-11-18): unknown-Z logistic-normal toy (S132, S133).

Model (our toy, not a published experiment; framework: Stan User's Guide, see E07):
    theta ~ N(0,1), prior density phi(theta)
    y1, y2 | theta  independent Bernoulli(s(theta)),  s(t) = 1/(1+exp(-t))
    observed y1 = y2 = 1  ->  likelihood s(theta)^2
    unnormalized posterior  ptilde(theta) = phi(theta) s(theta)^2
    Z = int phi s^2,   mu = E_post[s(theta)] = int phi s^3 / Z   (posterior predictive P(y3=1))
SNIS with proposal q = phi (the prior): weights ptilde/q = s^2, so
    mu_hat = sum s(theta_i)^3 / sum s(theta_i)^2,   theta_i IID N(0,1).

Outputs
  1. Deterministic quadrature reference (composite Simpson on [-12,12], 12,000 and
     24,000 panels). Validation only: never an input to the estimator.
  2. One seeded SNIS batch (random.Random(SEED).gauss, n = N_DRAWS) for the notes.
  3. fig/p9f-bayes.svg: prior phi, likelihood s^2, unnormalized posterior phi s^2
     (area shaded = Z). Curves are exact closed forms on a fine grid; panels 1 and 3
     share one vertical scale (density), panel 2 is a probability on [0,1].
     Math labels are HTML overlays in the deck; positions printed below.
Run:  python3 gen/p9f_unknown_z.py
"""
import math, os, random

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'fig')
BLUE, RED, GREY, BAND = '#003876', '#c0392b', '#666666', '#dbe5f1'
FONT = 'font-family="Noto Sans, Arial, sans-serif"'

SEED, N_DRAWS = 20261118, 10_000


def log_s(t):
    """Stable log of the logistic function."""
    return -math.log1p(math.exp(-t)) if t >= 0 else t - math.log1p(math.exp(t))


def s_pow(t, k):
    return math.exp(k * log_s(t))


def phi(t):
    return math.exp(-0.5 * t * t) / math.sqrt(2 * math.pi)


def simpson(fn, a, b, m):
    h = (b - a) / m
    tot = fn(a) + fn(b)
    for i in range(1, m):
        tot += (4 if i % 2 else 2) * fn(a + i * h)
    return tot * h / 3


def quadrature():
    res = {}
    for m in (12_000, 24_000):
        Z = simpson(lambda t: phi(t) * s_pow(t, 2), -12, 12, m)
        num = simpson(lambda t: phi(t) * s_pow(t, 3), -12, 12, m)
        res[m] = (Z, num, num / Z)
        print(f"Simpson [-12,12], {m} panels: Z = {Z:.14f}  num = {num:.14f}  mu = {num/Z:.14f}")
    (Z1, n1, m1), (Z2, n2, m2) = res[12_000], res[24_000]
    print(f"  panel-doubling differences: Z {abs(Z1-Z2):.1e}, num {abs(n1-n2):.1e}, mu {abs(m1-m2):.1e}")
    return res[24_000]


def snis_batch():
    rng = random.Random(SEED)
    num = den = 0.0
    sq = 0.0
    for _ in range(N_DRAWS):
        t = rng.gauss(0.0, 1.0)
        w = s_pow(t, 2)
        num += w * s_pow(t, 1)
        den += w
        sq += w * w
    est = num / den
    ess = den * den / sq
    print(f"SNIS batch: seed {SEED}, n = {N_DRAWS}, theta_i IID N(0,1) via random.Random(seed).gauss")
    print(f"  mu_hat = sum s^3 / sum s^2 = {est:.4f}   ESS = {ess:.0f}")
    return est, ess


# ---------- figure ----------
W, H = 1040, 285
PANELS = [(60, 320), (390, 650), (720, 980)]   # x-ranges of the three plot boxes
Y0, Y1 = 60, 235                                 # plot box top / bottom (px)
XR = (-4.0, 4.0)
DENS_MAX = 0.42                                  # shared density scale, panels 1 and 3


def fig():
    parts = []
    add = parts.append
    labels = []

    def X(px0, px1, x):
        return px0 + (x - XR[0]) / (XR[1] - XR[0]) * (px1 - px0)

    def Y(y, ymax):
        return Y1 - y / ymax * (Y1 - Y0)

    specs = [
        (lambda t: phi(t), DENS_MAX, GREY, None),
        (lambda t: s_pow(t, 2), 1.0, RED, None),
        (lambda t: phi(t) * s_pow(t, 2), DENS_MAX, BLUE, BAND),
    ]
    for (px0, px1), (fn, ymax, col, fill) in zip(PANELS, specs):
        n = 400
        pts = [(X(px0, px1, XR[0] + (XR[1] - XR[0]) * i / n), Y(fn(XR[0] + (XR[1] - XR[0]) * i / n), ymax))
               for i in range(n + 1)]
        d = ' '.join(f"{x:.1f},{y:.1f}" for x, y in pts)
        if fill:
            add(f'<polygon points="{pts[0][0]:.1f},{Y1} {d} {pts[-1][0]:.1f},{Y1}" fill="{fill}" stroke="none"/>')
        add(f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="4" stroke-linejoin="round"/>')
        add(f'<line x1="{px0}" y1="{Y1}" x2="{px1}" y2="{Y1}" stroke="#333" stroke-width="2"/>')
        add(f'<line x1="{px0}" y1="{Y0}" x2="{px0}" y2="{Y1}" stroke="#333" stroke-width="2"/>')
        for t in (-3, 0, 3):
            x = X(px0, px1, t)
            add(f'<line x1="{x:.1f}" y1="{Y1}" x2="{x:.1f}" y2="{Y1+8}" stroke="#333" stroke-width="2"/>')
            add(f'<text x="{x:.1f}" y="{Y1+34}" font-size="24" text-anchor="middle" fill="#333" {FONT}>{t}</text>')
        top = 0.4 if ymax == DENS_MAX else 1.0
        y = Y(top, ymax)
        add(f'<line x1="{px0-8}" y1="{y:.1f}" x2="{px0}" y2="{y:.1f}" stroke="#333" stroke-width="2"/>')
        add(f'<text x="{px0-12}" y="{y+8:.1f}" font-size="22" text-anchor="end" fill="#333" {FONT}>{top:g}</text>')
        add(f'<text x="{px0-12}" y="{Y1+8}" font-size="22" text-anchor="end" fill="#333" {FONT}>0</text>')
    # positions for the deck's HTML overlays (percent of viewBox)
    def pct(px, py):
        return f"left:{100*px/W:.2f}%;top:{100*py/H:.2f}%"
    labels.append(("times sign", pct((PANELS[0][1] + PANELS[1][0]) / 2, (Y0 + Y1) / 2)))
    labels.append(("equals sign", pct((PANELS[1][1] + PANELS[2][0]) / 2, (Y0 + Y1) / 2)))
    for k, (px0, px1) in enumerate(PANELS):
        labels.append((f"panel-{k+1} title (centred above box)", pct((px0 + px1) / 2, 22)))
    labels.append(("theta axis label right of panel 3", pct(PANELS[2][1] + 30, Y1)))
    body = '\n'.join(parts)
    comment = ("S132: prior phi (grey), likelihood s^2 (red), unnormalized posterior phi*s^2 (blue, area shaded = Z); "
               f"theta in [-4,4]; panels 1,3 Y={Y1}-{Y1-Y0}*y/{DENS_MAX}, panel 2 Y={Y1}-{Y1-Y0}*y")
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">\n'
           f'<!-- generated by gen/p9f_unknown_z.py. {comment} -->\n{body}\n</svg>\n')
    with open(os.path.join(OUT, 'p9f-bayes.svg'), 'w') as fh:
        fh.write(svg)
    print("wrote fig/p9f-bayes.svg")
    for name, pos in labels:
        print(f"  overlay {name}: {pos}")
    print(f"  peaks: phi {phi(0):.3f}; phi*s^2 max on grid "
          f"{max(phi(t/1000)*s_pow(t/1000,2) for t in range(-4000,4001)):.3f}")


if __name__ == '__main__':
    quadrature()
    snis_batch()
    fig()
