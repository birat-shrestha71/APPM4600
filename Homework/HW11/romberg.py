"""
 This script tests Romberg integration for approximating integrals.
 The first column of the Romberg table is built with the composite
 trapezoidal rule and the remaining columns come from Richardson
 extrapolation.  The error in the diagonal entries is plotted as the
 number of panels is increased.
"""

#############################################
"""
Copyright (C) 2026  Adrianna M. Gillman

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
#############################################




import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma
from scipy.integrate import quad


def driver():

    f = lambda x: np.sin(x)
    a = 0
    b = np.pi

    # exact integral
    I_ex = 2

    nrefine = 5


    f2 = lambda t: t * np.cos(1/t) if t > 0 else 0




    xval = [2,4,6,8,10]

    T = 60
    N = 6000

    for x in xval:
        f3 = lambda t: t**(x-1) * np.exp(-t)

        g = gamma(x)

    
# number of panels: 1, 2, 4, ..., 2^nrefine
    ntest = 2**np.arange(0,nrefine+1)

    Rom = rombergTrap(a,b,nrefine,f)
    Rom2 = rombergSimp(a,b,nrefine,f)


    Simps = CompSimp(0,1,4,f2)

    #print("simp 5 nodes = ", Simps)

    trap = CompTrap(0,T,N,f3)

    errtrap = abs(trap - g) / g

    print('x =', x, ' Gamma =', g)
    print('trap err =', errtrap, ' evals =', N+1)

    count = [0]

    def fc(t):
        count[0] += 1
        return f3(t)

    quadv = quad(fc,0,T,epsrel=1e-12,epsabs=1e-12)[0]

    errquad = abs(quadv-g)/g

    print('quad err =', errquad, 'evals = ', count[0])


    n = 5

    pts, wts = np.polynomial.laguerre.laggauss(n)
    gl = np.sum(wts*pts**(x-1))
    errgl = abs(gl-g)/g

    print('gl err =', errgl, ' evals =', n)



# column j is only filled from row j down
    #for j in range(0,nrefine+1):
    #    print('absolute error in column', j, '= ', abs(I_ex-Rom[j:,j]))
        
    #for j in range(0,nrefine+1):
    #        print('absolute error in column (Simpson)', j, '= ', abs(I_ex-Rom2[j:,j]))

    err = abs(I_ex-np.diag(Rom))
    err2 = abs(I_ex - np.diag(Rom2))

    #print('absolute error of best approximation at each order = ', err)
    #print('absolute error of best approximation at each order (Simpson) = ', err2)

    #plt.semilogy(ntest,err,'o-')
    #plt.xlabel('n')
    #plt.ylabel('absolute error')
    #plt.show()


def rombergTrap(a,b,nrefine,f):
# number of panels: 1, 2, 4, ..., 2^nrefine
    ntest = 2**np.arange(0,nrefine+1)

    nn = len(ntest)

    Rom = np.zeros((nn,nn))

# first column: composite trapezoidal rule with n panels
    for j in range(0,nn):
        Rom[j,0] = CompTrap(a,b,ntest[j],f)

# remaining columns: Richardson extrapolation
    for j in range(1,nn):
        for i in range(j,nn):
            Rom[i,j] = Rom[i,j-1] + (Rom[i,j-1]-Rom[i-1,j-1])/(4**j-1)

    return Rom


def rombergSimp(a,b,nrefine,f):
    ntest = 2*2**np.arange(0,nrefine+1)
    nn = len(ntest)
    Rom = np.zeros((nn,nn))

    for j in range(0,nn):
        Rom[j,0] = CompSimp(a,b,ntest[j],f)


    for j in range(1,nn):
        for i in range(j,nn):
            Rom[i,j] = Rom[i,j-1] + (Rom[i,j-1]-Rom[i-1,j-1])/(4**(j+1)-1)
    return Rom

def CompTrap(a,b,n,f):
    h = (b-a)/n
    xnode = a+np.arange(0,n+1)*h

    I_trap = h*f(xnode[0])*1/2

    for j in range(1,n):
         I_trap = I_trap+h*f(xnode[j])
    I_trap= I_trap + 1/2*h*f(xnode[n])

    return I_trap

def CompSimp(a,b,n,f):
    h = (b-a)/n
    xnode = a+np.arange(0,n+1)*h

    I_simp = f(xnode[0]) + f(xnode[n])
    for j in range(1,n):
        if j % 2 == 1:
            I_simp = I_simp + 4*f(xnode[j])
        else:
            I_simp = I_simp + 2*f(xnode[j])
    return h/3*I_simp



driver()
