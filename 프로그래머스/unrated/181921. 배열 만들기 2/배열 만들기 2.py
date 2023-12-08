def solution(l, r):
    t = []
    for i in range(l, r+1):
        for x in str(i):
            if x != "5" and x != "0":
                break
        else:
            t.append(i)
    return t if t else [-1]