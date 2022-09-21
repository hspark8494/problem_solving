def solution(n):
    if n<=2:
        return 1
    result = 1
    acc = 0
    end = 0
    for start in range(1, n+1):
        while (acc < n) and (end < n):
            acc += end
            end += 1
        if acc == n:
            result += 1
        acc -= start
    return result