def line(f, x0, x1, alpha):

    if x0 == x1:
        return 0
   
    l0 = (alpha - x1) / (x0 - x1)   # basis polynomial for x0
    l1 = (alpha - x0) / (x1 - x0)   # basis polynomial for x1

    return f(x0) * l0 + f(x1) * l1


