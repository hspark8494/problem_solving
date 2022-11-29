def solution(i, j, k):
    r = 0
    k = str(k)
    for x in range(i,j+1):
        for c in str(x):
            if (c==k):
                r+=1
    return r