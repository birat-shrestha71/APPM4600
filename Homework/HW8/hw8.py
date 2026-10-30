import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import math
from numpy.linalg import inv 
from numpy.linalg import norm


def driver():
    
    f  = lambda x: 1.0 / (1.0 + x**2)
    fp = lambda x: -2*x/(1.+x**2)**2
    a = -5
    b = 5

    
    ''' number of intervals'''
    Nint = 20
    j = np.arange(Nint+1)
    xint = np.sort(5*np.cos(np.pi*j/Nint))
    #xint = np.linspace(a,b,Nint+1) 
    yint = f(xint)

    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(xint[0],xint[Nint],Neval+1)
    
    
    (M,C,D) = create_natural_spline(yint,xint,Nint)
    (M2,C2,D2) = create_clamped_spline(yint,xint,Nint, fp(a), fp(b))

    yeval = eval_cubic_spline(xeval,Neval,xint,Nint,M,C,D)
    yeval2 = eval_cubic_spline(xeval,Neval,xint,Nint,M2,C2,D2)
#    print('yeval = ', yeval)
    
    ''' evaluate f at the evaluation points'''
    fex = f(xeval)
        
    nerr = norm(fex-yeval)
    print('nerr = ', nerr)
    
    plt.figure()
    plt.plot(xeval,fex,'ro-',label='exact function')
    plt.plot(xeval,yeval,'bs--',label='natural spline')
    plt.plot(xeval,yeval2,'gs--',label='clamped spline') 
    plt.legend()
    plt.show()
     
    #err = abs(yeval-fex)
    #plt.figure() 
    #plt.semilogy(xeval,err,'ro--',label='absolute error')
    #plt.legend()
    #plt.show()

    N = 20

    a = -5
    b = 5
       
    ''' create equispaced interpolation nodes'''
    #xint = np.linspace(a,b,N+1)
     
    j = np.arange(N+1)
    xint = np.sort(5*np.cos(np.pi*j/N))   
    ''' create interpolation data'''
    yint = np.zeros(N+1)
    ypint = np.zeros(N+1)
    for jj in range(N+1):
        yint[jj] = f(xint[jj])
        ypint[jj] = fp(xint[jj])
        
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yevalL = np.zeros(Neval+1)
    yevalH = np.zeros(Neval+1)
    for kk in range(Neval+1):
      yevalL[kk] = eval_lagrange(xeval[kk],xint,yint,N)
      yevalH[kk] = eval_hermite(xeval[kk],xint,yint,ypint,N)
    
    ''' create vector with exact values'''
    fex = np.zeros(Neval+1)
    for kk in range(Neval+1):
        fex[kk] = f(xeval[kk])
        
        
    plt.figure()
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yevalL,'bs--',label='Lagrange') 
    plt.plot(xeval,yevalH,'g.--',label='Hermite')
    plt.semilogy()
    plt.legend()
    plt.show()
             
    #errL = abs(yevalL-fex)
    #errH = abs(yevalH-fex)
    #plt.figure()
    #plt.semilogy(xeval,errL,'bs--',label='Lagrange')
    #plt.semilogy(xeval,errH,'c.--',label='Hermite')
    #plt.show()            
    





def eval_hermite(xeval,xint,yint,ypint,N):

    ''' Evaluate all Lagrange polynomials'''

    lj = np.ones(N+1)
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    ''' Construct the l_j'(x_j)'''
    lpj = np.zeros(N+1)
#    lpj2 = np.ones(N+1)
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
#              lpj2[count] = lpj2[count]*(xint[count] - xint[jj])
              lpj[count] = lpj[count]+ 1./(xint[count] - xint[jj])
              

    yeval = 0.
    
    for jj in range(N+1):
       Qj = (1.-2.*(xeval-xint[jj])*lpj[jj])*lj[jj]**2
       Rj = (xeval-xint[jj])*lj[jj]**2
       yeval = yeval + yint[jj]*Qj+ypint[jj]*Rj
       
    return(yeval)
       


def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)
  
def create_clamped_spline(yint,xint,N,fp_a,fp_b):
    h = np.diff(xint)
    b = np.zeros(N+1)
    A = np.zeros((N+1, N+1))
  
    A[0][0] = h[0]/3;  A[0][1] = h[0]/6
    b[0] = (yint[1]-yint[0])/h[0] - fp_a
   
    for j in range(1, N):
        A[j][j-1] = h[j-1]/6
        A[j][j]   = (h[j-1]+h[j])/3
        A[j][j+1] = h[j]/6
        b[j] = (yint[j+1]-yint[j])/h[j] - (yint[j]-yint[j-1])/h[j-1]
   
    A[N][N-1] = h[N-1]/6;  A[N][N] = h[N-1]/3
    b[N] = fp_b - (yint[N]-yint[N-1])/h[N-1]
    M = np.linalg.solve(A, b)
    C = yint[:-1]/h - h*M[:-1]/6
    D = yint[1:]/h  - h*M[1:]/6
    return M, C, D
    

def create_natural_spline(yint,xint,N):

#    create the right  hand side for the linear system
    b = np.zeros(N+1)
#  vector values
    h = np.zeros(N+1)  
    for i in range(1,N):
       hi = xint[i]-xint[i-1]
       hip = xint[i+1] - xint[i]
       b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
       h[i-1] = hi
       h[i] = hip

#  create matrix so you can solve for the M values
# This is made by filling one row at a time 
    A = np.zeros((N+1,N+1))
    A[0][0] = 1.0
    for j in range(1,N):
       A[j][j-1] = h[j-1]/6
       A[j][j] = (h[j]+h[j-1])/3 
       A[j][j+1] = h[j]/6
    A[N][N] = 1

    Ainv = inv(A)
    
    M  = Ainv.dot(b)

#  Create the linear coefficients
    C = np.zeros(N)
    D = np.zeros(N)
    for j in range(N):
       C[j] = yint[j]/h[j]-h[j]*M[j]/6
       D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
    return(M,C,D)
       
def eval_local_spline(xeval,xi,xip,Mi,Mip,C,D):
# Evaluates the local spline as defined in class
# xip = x_{i+1}; xi = x_i
# Mip = M_{i+1}; Mi = M_i

    hi = xip-xi
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
            + C*(xip-xeval) + D*(xeval-xi)
    return yeval 
    
    
def  eval_cubic_spline(xeval,Neval,xint,Nint,M,C,D):
    
    yeval = np.zeros(Neval+1)
    
    for j in range(Nint):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        atmp = xint[j]
        btmp= xint[j+1]
        
#   find indices of values of xeval in the interval
        ind= np.where((xeval >= atmp) & (xeval <= btmp))
        xloc = xeval[ind]

# evaluate the spline
        yloc = eval_local_spline(xloc,atmp,btmp,M[j],M[j+1],C[j],D[j])
#        print('yloc = ', yloc)
#   copy into yeval
        yeval[ind] = yloc

    return(yeval)

driver()               

