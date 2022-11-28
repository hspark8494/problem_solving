def solution(num, k):
    k = str(k)
    for i, c in enumerate(str(num)):
        if k == c:
            return i+1
    return -1