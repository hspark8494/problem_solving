def solution(a, b):
    k = a%2 + b%2
    if k == 0:
        return abs(a-b)
    elif k == 1:
        return 2*(a+b)
    else:
        return a**2 + b**2