import math

x = 9.999999995000000e-10

y = math.exp(x)

g = x + (x**2) / 2

print(y - 1)
print(g)