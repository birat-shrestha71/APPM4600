import numpy as np

def eval_leg(n, x):
    p = np.zeros(n + 1)
    p[0] = 1.0
    if n >= 1:
        p[1] = x
    for k in range(1, n):
        p[k + 1] = ((2 * k + 1) * x * p[k] - k * p[k - 1]) / (k + 1)
    return p