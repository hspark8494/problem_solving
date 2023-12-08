def solution(a, b, c):
    t = len(set([a,b,c]))
    if t == 1:
        return a*3 * a**2*3 * a**3*3
    elif t == 2:
        return (a+b+c) * (a**2+b**2+c**2)
    else:
        return a+b+c