import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(1.92,2.080,161)

p1 = x**9 - 18 * x**8 + 144 * x**7 - 672 * x**6 + 2016 * x**5 - 4032 * x**4 + 5376 * x**3 - 4608 * x**2 + 2304 * x - 512
p2 = (x-2)**9

plt.plot(x,p1)
plt.plot(x,p2)

plt.xlabel("x")
plt.ylabel("p(x)")

plt.show()

