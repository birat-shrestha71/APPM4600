def line(f, x0, x1, alpha):

    if x0 == x1:
        return 0,0

    f0 = f(x0)
    f1 = f(x1)

    slope = (f1 - f0) / (x1 - x0)      # construct the line
    L_alpha = f0 + slope * (alpha - x0)  # evaluate it at alpha

    return L_alpha, slope

