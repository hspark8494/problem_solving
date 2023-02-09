from collections import defaultdict


def solution(s):
    r = []
    d = defaultdict(lambda: -1)
    for i, v in enumerate(s):
        if d[v] == -1:
            r.append(-1)
        else:
            r.append(i - d[v])
        d[v] = i
    return r