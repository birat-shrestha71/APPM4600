import numpy as np
 
 
def comp_trap(a, b, f, N):
    
    x = np.linspace(a, b, N)
    h = (b - a) / (N - 1)
    y = f(x)
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])
 
 
def comp_simpson(a, b, f, N):
    
    x = np.linspace(a, b, N)
    h = (b - a) / (N - 1)
    y = f(x)
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]) + y[-1])
 