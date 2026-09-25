import numpy as np
import matplotlib.pyplot as plt        
def driver():
#f = lambda x: (x-2)**3
#fp = lambda x: 3*(x-2)**2
#p0 = 1.2

  f = lambda x: x**6 - x - 1
  fp = lambda x: 6 * x **5 - 1
  p0 = 2
  p1 = 1

  Nmax = 100
  tol = 1.e-14

  (p,pstar,info,it) = secant(f,p0, p1, tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)
  


def secant(f,p0,p1,tol,Nmax):
  """
  Secant iteration.
  
  Inputs:
    f        - function
    p0,p1    - two initial guesses for root
    tol      - iteration stops when p_n,p_{n+1} are within tol
    Nmax     - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """
  p = np.zeros(Nmax+1);
  p[0] = p0
  p[1] = p1
  for it in range(1,Nmax):
      if (f(p1)-f(p0) == 0):
          pstar = p1
          info = 1
          return [p,pstar,info,it]
      p2 = p1-f(p1)*(p1-p0)/(f(p1)-f(p0))
      p[it+1] = p2

      if (abs(p2-p1) < tol):
          pstar = p2
          info = 0
          return [p,pstar,info,it]
      p0 = p1
      p1 = p2
  pstar = p2
  info = 1
  return [p,pstar,info,it]

def newton(f,fp,p0,tol,Nmax):
  """
  Newton iteration.
  
  Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """
  p = np.zeros(Nmax+1);
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]

driver()

f = lambda x: x**6 - x - 1
fp = lambda x: 6 * x **5 - 1
p0 = 2
p1 = 1

Nmax = 100
tol = 1.e-14
alpha = 1.1347241384015195

pN, pstarN, infoN, itN = newton(f,fp,p0,tol,Nmax)
pS, pstarS, infoS, itS = secant(f,p0,p1,tol,Nmax)

# only keep the iterates that were actually used, error, alpha)
pN = pN[0:itN+2]
pS = pS[0:itS+2]

errN = abs(pN - alpha)
errS = abs(pS - alpha)

# plot |x_k - alpha| vs |x_{k+1} - alpha|
plt.figure()
plt.loglog(errN[0:-1], errN[1:], 'o-', label='Newton')
plt.loglog(errS[0:-1], errS[1:], 's-', label='Secant')
plt.xlabel('|x_k - alpha|')
plt.ylabel('|x_k+1 - alpha|')
plt.title('log-log error plot')
plt.legend()
plt.show()
