def solution(strArr):
    t = [0] * 31
    for s in strArr:
        t[len(s)] += 1
    return max(t)