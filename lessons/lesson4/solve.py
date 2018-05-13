def get_roots(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b-D**0.5) / (2*a)
        x2 = (-b+D**0.5) / (2*a)
        return x2, x1
    elif D == 0:
        return (-b) / (2*a)
    else:
        return None
