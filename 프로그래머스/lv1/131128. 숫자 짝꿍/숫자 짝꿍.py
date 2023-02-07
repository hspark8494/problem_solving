from collections import defaultdict


def solution(X, Y):
    p, q = defaultdict(int), defaultdict(int)
    r = ""
    for c in X:
        p[int(c)] += 1
    for c in Y:
        q[int(c)] += 1

    for i in range(9, -1, -1):
        r += str(i) * min(p[i], q[i])
    if r == "":
        r = "-1"
    elif r[0] == "0":
        r = "0"
    return r