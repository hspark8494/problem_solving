def solution(a, b, n):
    r = 0
    while (n >= a):
        s = n // a * b
        n = n % a + s
        r += s
    return r
