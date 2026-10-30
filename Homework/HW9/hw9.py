import numpy as np
import matplotlib.pyplot as plt
f   = np.sin
T  = lambda x: x - x**3/6 + x**5/120
r33 = lambda x: (x - 7*x**3/60) / (1 + x**2/20)      
r24 = lambda x: x / (1 + x**2/6 + 7*x**4/360)         
 
x = np.linspace(0.02, 5, 4000)
plt.semilogy(x, abs(f(x)-T(x)),  label="Maclaurin T6")
plt.semilogy(x, abs(f(x)-r33(x)), label="Pade [3/3]=[4/2]")
plt.semilogy(x, abs(f(x)-r24(x)), label="Pade [2/4]")
plt.xlabel("x")
plt.ylabel("|sin x - approx|")
plt.legend()
plt.show()