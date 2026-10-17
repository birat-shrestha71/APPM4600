import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (1 + (10*x)**2)

def eval(c, x):
    
    n = len(c)
    p = np.zeros_like(x)
    for j in range(n):
        p += c[j] * x**(n-1-j)
    return p

def weights(x):
    n = len(x)
    w = np.ones(n)
    for j in range(n):
        for i in range(n):
            if i != j:
                w[j] /= 2*(x[j] - x[i])
    return w

def bary1(x, y, w, xe):
    p = np.zeros_like(xe)
    for k, t in enumerate(xe):
        d = t - x
        if np.any(d == 0):
            p[k] = y[np.argmin(abs(d))]
        else:
            p[k] = np.prod(2*d) / 2 * np.sum(w/d * y)
    return p

xfine = np.linspace(-1, 1, 1001)          


for N in range(2, 26):
    h = 2/(N-1)
    x = -1 + np.arange(N)*h
    y = f(x)

    V = np.vander(x)
    c = np.linalg.inv(V) @ y

    p = eval(c, xfine)

    #plt.figure()
    #plt.plot(x, y, 'o')                   
    #plt.plot(xfine, p, label='p(x)')      
    #plt.plot(xfine, f(xfine), label='f(x)')
    #plt.ylim(-2, 2)                       
    #plt.title(f'N = {N}')
    #plt.legend()

    if np.abs(p).max() > 100:
        break

for N in [500]:
    j = np.arange(1,N+1)
    x = np.cos(((2*j - 1) * np.pi) / (2 * N))    
    y = f(x)
    w = weights(x)
    p = bary1(x, y, w, xfine)
    plt.figure()
    plt.plot(xfine, f(xfine), 'k--', label='f')
    plt.plot(xfine, p, label='p')
    plt.plot(x, y, 'o')
    plt.ylim(-1, 2)
    plt.title(f'N = {N}')
    plt.legend()

plt.show()
