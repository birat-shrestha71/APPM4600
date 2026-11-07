import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt


def trapezoid(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = f(x)
    return h * (y.sum() - 0.5 * (y[0] + y[-1]))

def simpson(f, a, b, n):          
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = f(x)
    return h / 3 * (y[0] + y[-1] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum())



f = lambda x: np.exp(x) * np.cos(x)
I = -12.070346316389632

results = {}
for name, rule in [("Trapezoid", trapezoid), ("Simpson", simpson)]:
    n = 2
    hs, errs = [], []
    while True:
        err = abs(rule(f, 0, np.pi, n) - I)
        hs.append(np.pi / n)
        errs.append(err)
        if err / abs(I) < 1e-10:
            break
        n *= 2                
    results[name] = (hs, errs)
    print(name, "n =", n, "h =", np.pi / n)

    slope = np.polyfit(np.log(hs), np.log(errs), 1)[0]
    print(name, "slope =", slope)

plt.figure()
for name, (hs, errs) in results.items():
    plt.loglog(hs, errs, 'o-', label=name)
plt.xlabel("h")
plt.ylabel("absolute error")
plt.legend()
plt.show()


g = lambda s: 1 / (1 + s**2)
exact = 2 * np.arctan(5)

nT, nS = 1291, 108          
print("Trapezoid:", trapezoid(g, -5, 5, nT), "error", abs(trapezoid(g, -5, 5, nT) - exact))
print("Simpson:  ", simpson(g, -5, 5, nS), "error", abs(simpson(g, -5, 5, nS) - exact))

for tol in [1e-6, 1e-4]:
    count = [0]
    def counted(x):
        count[0] += 1
        return g(x)
    val, _ = quad(counted, -5, 5, epsabs=tol, epsrel=tol)
    print("quad tol", tol, ":", val, "error", abs(val - exact), "evals", count[0])