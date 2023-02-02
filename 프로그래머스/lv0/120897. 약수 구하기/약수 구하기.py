def solution(n):
    if n == 1:
        return [1]
    s = set()
    for i in range(1, (n//2)+1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    return sorted(list(s))