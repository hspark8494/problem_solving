def solution(n):
    s = set()
    for i in range(1, n+1):
        if n%i==0:
            s.add((i, n//i))
    return len(s)