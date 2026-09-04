import numpy as np
import matplotlib.pyplot as plt 

#x = np.linspace(1.92,2.080,161)

#p1 = x**9 - 18 * x**8 + 144 * x**7 - 672 * x**6 + 2016 * x**5 - 4032 * x**4 + 5376 * x**3 - 4608 * x**2 + 2304 * x - 512
#p2 = (x-2)**9

#plt.plot(x,p1)
#plt.plot(x,p2)

#plt.xlabel("x")
#plt.ylabel("p(x)")

#plt.show()

#x = np.pi
#x2 = 10**6

#exp = np.arange(-16,1)
#phi = 10.0**exp

#f1 = np.cos(x + phi) - np.cos(x)
#f2 = np.sin(x + phi/2) * np.sin(phi/2) * -2

#f3 = np.cos(x2 + phi) - np.cos(x2)
#f4 = np.sin(x2 + phi/2) * np.sin(phi/2) * -2

#fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5)) 


#ax1.semilogx(phi, f1 - f2,label="x = pi")
#ax1.set_xlabel("delta")
#ax1.set_ylabel("difference")
#ax1.set_title("difference for x = pi")
#ax1.legend()

#ax2.semilogx(phi, f3 - f4, color = "r", label="x = 10e6")
#ax2.set_xlabel("delta")
#ax2.set_ylabel("difference")
#ax2.set_title("difference for x = 10e6")
#ax2.legend()

#plt.tight_layout()
#plt.show()

#solved the taylor formula and put it in here

x = np.pi
x2 = 10**6

exp = np.arange(-16,1)
phi = 10.0**exp

def taylor(x,phi):
    return -phi * np.sin(x) - (phi**2/2) * np.cos(x)

f1 = np.sin(x + phi/2) * np.sin(phi/2) * -2
f2 = np.sin(x2 + phi/2) * np.sin(phi/2) * -2

t1 = taylor(x,phi)
t2 = taylor(x2,phi)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5)) 


ax1.semilogx(phi, t1 - f1,label="x = pi")
ax1.set_xlabel("delta")
ax1.set_ylabel("difference")
ax1.set_title("difference for x = pi with taylor")
ax1.legend()

ax2.semilogx(phi, t2 - f2, color = "r", label="x = 10e6")
ax2.set_xlabel("delta")
ax2.set_ylabel("difference")
ax2.set_title("difference for x = 10e6 with taylor")
ax2.legend()

plt.tight_layout()
plt.show()