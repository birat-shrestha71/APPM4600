import numpy as np
import matplotlib.pyplot as plt

#exercises

x = np.linspace(0,9,10)
y = np.arange(0,10)

x2 = x[0:3]

print('the first three entries are of x are', x2)

w = 10**(-np.linspace(1,10,10))
#the entries of w are 10 ^ -1 through -10 power, which should be 0.1 growing to 1e-10

x3 = np.linspace(1,10,10) #sets up x axis with spacing as 1-10

s = 3 * w

plt.semilogy(x3,w)  #plots in semilog with respect to y
plt.semilogy(x3,s)

plt.xlabel('x')
plt.ylabel('y')

plt.show()


