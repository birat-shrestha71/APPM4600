import numpy as np


def driver():

    f = lambda x: np.exp(x**2 + 7*x - 30) - 1
    fp = lambda x: np.exp(x**2 + 7*x - 30) * ((2 * x) + 7)
    fp2 = lambda x: np.exp(x**2 + 7*x - 30) * ((4 * x**2)+ (28*x) + 51)

    tol = 1e-9
    Nmax = 500
    [astar,ier] = bisection2(f,2,4.5,tol)
    [p2, pstar2,a,b] = newton(f,fp,4.5,tol,Nmax)
    [p,pstar,info,int] = hybrid(f,fp,fp2,2,4.5,tol,Nmax)

    print('root bisection: ' , astar)
    print ('ier', ier)

    print ('root newton:', pstar2)
    print('ier', info)
    print('count', b)

    print('root hybrid', pstar)
    print('ier', info)
    print(int)


def basin(f,fp,fp2,x):
    
    return np.abs(f(x) * fp2(x) / (fp(x)**2))

def bisection2(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier = 0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        print('count', count)
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    print('count', count)
    return [astar, ier]

def bisection(f,fp,fp2,a,b,tol):

    fa = f(a)
    fb = f(b)
    c = 0
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier,c]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier = 0
      return [astar, ier,c]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier,c]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      
      fd = f(d)
      if (basin(f,fp,fp2,d) < 1):
        
        astar = d
        ier = 0
        c = count
        return [astar,ier,c]
      
      if (fd == 0):
        astar = d
        ier = 0
        c = count
        return [astar, ier,c]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1

      
    astar = d
    ier = 0
    c = count
    return [astar, ier, c]

def newton(f,fp,p0,tol,Nmax):
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

def hybrid(f,fp,fp2,a,b,tol,Nmax):

   [astar,ier,c] = bisection(f,fp,fp2,a,b,tol)

   [p,pstar,info,it] = newton(f,fp,astar,tol,Nmax)

   return([p,pstar,info,it+c])

driver()