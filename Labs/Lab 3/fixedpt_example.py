"""
 This script explores the use of the fixed point method.  
 Two functions are considered that have different properties.
 I like to use this code before I talk about convergence analysis
 for the fixed point method as motivation.
"""

############################################# 
"""
Copyright (C) 2025  Adrianna M. Gillman

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



# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: 1+0.5*np.sin(x)
# fixed point is alpha1 = 1.4987....

     f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-6

# test f1 '''
     x0 = 0.0
     [xstar,ier, count] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar[count])
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
    
#test f2 '''
     x0 = 0.0
     [xstar,ier,count] = fixedpt(f2,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar[count])
     print('f2(xstar):',f2(xstar))
     print('Error message reads:',ier)



# define routines
def fixedpt(f, x0, tol, Nmax):
    x = np.zeros(1)
    count = 0
    while count < Nmax:
        x[count] = f(x0)
        if abs(x[count] - x0) < tol:
            ier = 0
            return [x, ier, count]
        x0 = x[count]
        count = count + 1
        if count < Nmax:          
            x = np.append(x, 0)
    ier = 1
    return [x, ier, count - 1]
    

driver()
