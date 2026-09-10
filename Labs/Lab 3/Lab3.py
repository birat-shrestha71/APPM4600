import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: 1+0.5*np.sin(x)

     Nmax = 100
     tol = 10e-10

# test
     x0 = 0.0
     [xstar,ier, count] = fixedpt(f1,x0,tol,Nmax)
     #print('the approximate fixed point is:',xstar[count])
     #print('f1(xstar):',f1(xstar))
     #print('Error message reads:',ier)

     f2 = lambda x: np.sqrt(10 / (x + 4))       
     p = 1.3652300134140976 
     x0 = 1.5
     [x,ier,count] = fixedpt(f2,x0,tol,Nmax)
     [alpha,const] = order_conv(p,x)
     [p_new,ier] = aitkens(x,x0,tol,count)
     #print(alpha[-1])
     #print(const[-1])
     #print('used aitkens')
     [alpha2,const2] = order_conv(p,p_new)
     #print(p)
     #print(alpha2[-1],const2[-1])
     [stef,ier] = steffenson(f2,x0,tol,Nmax)
     print('stef')
     print(stef)
     print(ier)
     [alpha3,const3] = order_conv(p,stef)
     print(alpha3,const3)

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
    
def order_conv(p,p2):
    N = len(p2)
    errors = np.abs(p2 - p)

    alpha = np.zeros((N,1))
    constant = np.zeros((N,1))

    for n in range(1, N-1):
        alpha[n] = np.log(errors[n+1] / errors[n]) / np.log(errors[n] / errors[n-1])
    for n in range(1, N-1):
        constant[n] = errors[n+1] / errors[n]    

    return alpha[1:-1] , constant[1:-1]

def aitkens(p,p0,tol,Nmax):

    n = 0
    p_new = np.zeros(1)

    while n < Nmax-2:

        p_new[n] = p[n] - (p[n+1] - p[n])**2 / (p[n+2] - 2*p[n+1] + p[n])

        if abs(p_new[n] - p0) < tol:
            ier = 0
            return [p_new,ier]
        
        p0 = p_new[n]
        n = n+1

        p_new = np.append(p_new,0)
    ier=1
    return [p_new,ier]

def steffenson(f,p0,tol,Nmax):
        p = np.zeros(1)
        p[0] = p0

        n = 0

        a = p[n]
        b = f(p[n])
        c = f(b)

        while n < Nmax-1:
            p = np.append(p,0)
            p[n+1] = a - ((b-a)**2 / (c - 2 * b + a))

            if abs (p[n+1] - p[n]) < tol:
                ier = 0
                return [p,ier]

            n = n+1

        ier = 1
        return [p,ier]
driver()
