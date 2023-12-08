def solution(n):
    r = []
    for i in range(n):
        r.append([0 for i in range(n)])
        r[i][i] = 1
    return r