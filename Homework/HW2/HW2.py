import math
import numpy as np
import matplotlib.pyplot as plt
x = 9.999999995000000e-10

y = math.exp(x)

g = x + (x**2) / 2

#print(y - 1)
#print(g)

x = np.linspace(-2,8,100)

f = x - 4 * np.sin(2 * x) - 3


plt.plot(x,f)

plt.axhline(0, color = "r")

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = x - 4sin(2x) - 3')
plt.show()

