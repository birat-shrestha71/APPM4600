import numpy as np

def f(p):
    x, y, z = p
    return x**2 + 4*y**2 + 4*z**2 - 16

def grad_f(p):
    x, y, z = p
    return np.array([2*x, 8*y, 8*z])

def step(p):
    g = grad_f(p)
    d = f(p) / np.dot(g, g)      
    return p - d * g             

p = np.array([1.0, 1.0, 1.0])   
history = [p]

for n in range(6):
    p = step(p)
    history.append(p)
    print(f"n={n+1}  p={p}  f={f(p):.3e}")
