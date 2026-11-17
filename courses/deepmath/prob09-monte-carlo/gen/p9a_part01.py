"""prob09 Part 01 (P1): every number and plotted coordinate on slides S26-S116.

Deterministic formula data only: no random numbers are drawn, so no seed is needed.
Run:  python3 gen/p9a_part01.py
Sources for the inputs: evidence.md E17 (six hand-chosen darts, darts bounds) and
E11 (running rare event p = Exp(1), f = 1{x > 10}).
"""
import math
from statistics import NormalDist

PI = math.pi

# ---------- S26: six hand-chosen darts (E17) ----------
darts = [(0.5, 0.5), (-0.9, 0.8), (0.2, -0.6), (-0.4, 0.1), (0.8, -0.7), (0.3, 0.9)]
hits = 0
print("S26 darts ledger (x, y, x^2+y^2, in?)")
for x, y in darts:
    r2 = x * x + y * y
    inside = r2 <= 1
    hits += inside
    # SVG (viewBox 400x440): square [-1,1]^2 -> centre (200,200), half-side 180
    print(f"  ({x:+.1f},{y:+.1f})  r2={r2:.2f}  {'in ' if inside else 'out'}  svg=({200+180*x:.1f},{200-180*y:.1f})")
print(f"  hits={hits}/6  estimate 4*hits/6 = {4*hits/6:.6f}  (8/3 = {8/3:.6f})")

# ---------- darts population quantities: f(x) = 4 * 1{|x| <= 1}, X ~ Unif[-1,1]^2 ----------
rho_d = PI / 4
var_f = PI * (4 - PI)                 # Var(4 * Bernoulli(pi/4)) = 16 rho (1 - rho)
sd_f = math.sqrt(var_f)
print(f"\nDarts: rho=pi/4={rho_d:.6f}  sigma_f^2=pi(4-pi)={var_f:.10f}  sigma_f={sd_f:.6f}")

# ---------- S19: exact distribution of the n = 6 darts estimate ----------
print("\nS19 exact pmf of hat mu_6 = 4K/6, K ~ Bin(6, pi/4); SVG x=120+190*v, y=300-650*P")
mean = 0.0
for k in range(7):
    pk = math.comb(6, k) * rho_d**k * (1 - rho_d)**(6 - k)
    v = 4 * k / 6
    mean += v * pk
    print(f"  k={k} value={v:.4f} P={pk:.4f}  bar x={120+190*v:.1f} top y={300-650*pk:.1f}")
print(f"  mean={mean:.6f} (pi={PI:.6f}); mu line x={120+190*PI:.1f}; P(hat mu_6 = pi) = 0")
print(f"  P(|hat mu_6 - pi| >= 0.5) = {sum(math.comb(6,k)*rho_d**k*(1-rho_d)**(6-k) for k in range(7) if abs(4*k/6-PI) >= 0.5):.4f}")
print(f"  RMSE at n=6 = {sd_f/math.sqrt(6):.4f}")

# ---------- S22: exact RMSE curve sigma_f / sqrt(n) ----------
print("\nS22 RMSE = sigma_f/sqrt(n); SVG x=150+156*(log10 n - 1), y=20+75*(-log10 RMSE)")
for n in [10, 100, 10**4, 10**6]:
    r = sd_f / math.sqrt(n)
    print(f"  n={n:>8}  RMSE={r:.6f}  svg=({150+156*(math.log10(n)-1):.1f},{20+75*(-math.log10(r)):.1f})")

# ---------- S115: CLT quantile and Chebyshev (known variance) ----------
z = NormalDist().inv_cdf(0.975)
eps, delta = 0.01, 0.05
n_cheb = var_f / (delta * eps**2)
print(f"\nS115 z_0.975={z:.5f}; Chebyshev n >= pi(4-pi)/(delta eps^2) = {n_cheb:.2f} -> {math.ceil(n_cheb)}")

# ---------- S24: Hoeffding, range [0,4] ----------
a, b = 0.0, 4.0
n_hoef = (b - a)**2 * math.log(2 / delta) / (2 * eps**2)
print(f"S24 ln(2/delta)=ln 40={math.log(40):.6f}; Hoeffding n >= {n_hoef:.2f} -> {math.ceil(n_hoef)}")
nh = math.ceil(n_hoef)
print(f"  check bound at n={nh}: 2exp(-2 n eps^2/16) = {2*math.exp(-2*nh*eps**2/16):.6f}")
print(f"  ratio Chebyshev/Hoeffding = {math.ceil(n_cheb)/nh:.3f}")
print(f"  RMSE at n={nh}: {sd_f/math.sqrt(nh):.5f}")

# ---------- S37: schematic error vs evaluations, all constants = 1 ----------
print("\nS37 error = N^(-2/d) (grid) and N^(-1/2) (MC); SVG x=150+100*log10 N, y=25+65*(-log10 err), clipped at err=1e-4")
for name, slope in [("grid d=2", -1.0), ("MC", -0.5), ("grid d=8", -0.25), ("grid d=20", -0.1)]:
    # end point at log10 N = 8 or where log10 err = -4
    lx = min(8.0, 4.0 / -slope)
    ly = slope * lx
    print(f"  {name:10s} slope={slope:+.2f}  end log10N={lx:.2f} log10err={ly:.2f}  svg end=({150+100*lx:.1f},{25+65*(-ly):.1f})")
for d in [2, 8, 20]:
    print(f"  grid d={d}: points per axis for N=10^8: m = N^(1/d) = {10**(8/d):.3g}")

# ---------- S116: rare event (E11 setup: p=Exp(1), f=1{x>10}) ----------
rho = math.exp(-10)
print(f"\nS116 rho = P(X>10) = e^-10 = {rho:.6e}")
print(f"  per-draw variance rho(1-rho) = {rho*(1-rho):.6e}; SD = {math.sqrt(rho*(1-rho)):.6f}")
print(f"  per-draw relative variance (1-rho)/rho = e^10 - 1 = {(1-rho)/rho:.7f}; relative SD = {math.sqrt((1-rho)/rho):.4f}")
nrel = (1 - rho) / rho / 0.1**2
print(f"  relative RMSE <= 0.1 needs n >= {nrel:.2f} -> {math.ceil(nrel)}")
print(f"  expected hits in 1/rho draws = 1; 1/rho = {1/rho:.2f}")
print(f"  P(no hit in n=10^4 draws) = (1-rho)^10000 = {(1-rho)**10000:.4f}")
print("  curves: x=150+135*(log10 rho + 6) for rho in [1e-6, 0.5]; y=20+40*(3 - log10 value)")
def pts(fn):
    out = []
    for i in range(0, 31):
        lr = -6 + i * (math.log10(0.5) + 6) / 30
        r = 10**lr
        out.append(f"{150+135*(lr+6):.1f},{20+40*(3-math.log10(fn(r))):.1f}")
    return " ".join(out)
print("  absolute SD sqrt(rho(1-rho)):", pts(lambda r: math.sqrt(r*(1-r))))
print("  relative SD sqrt((1-rho)/rho):", pts(lambda r: math.sqrt((1-r)/r)))
lr = math.log10(rho)
print(f"  marker x={150+135*(lr+6):.1f}; abs y={20+40*(3-math.log10(math.sqrt(rho*(1-rho)))):.1f}; rel y={20+40*(3-math.log10(math.sqrt((1-rho)/rho))):.1f}")
