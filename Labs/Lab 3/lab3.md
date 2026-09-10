3.1 - wrote code for aitkens

3.2 - the convergence alpha is the same between the methods of fixed point and aitkens however the convergance const shows that aitkens does indeed convergence much faster as we compare them fixed point gave .127 and aitkens gave 0.016. As we can see the aitkens method shows much faster

3.3 - inputs (f, p0, tol, Nmax)

        p = np.zeros(1)
        p = p0

        n = 0

        a = p[n]
        b = f(p[n])
        c = f(b)

        p append 0

        while n < Nmax:

        p[n+1] = a - ((b-a)**2 / (c - 2 * b + a))

        abs (p[n+1] - p[n]) < tol
            ier = 0
            return p,ier


        ier = 1
        return p,ier

3.3.4 - steffensons worked but the order of convergence function i wrote does not work
