from math import ceil
def solution(N,A,AV,B,BV):
    if AV*B < BV*A:
        A,AV,B,BV = B,BV,A,AV

    result = float("inf")

    for i in range(B):
        j = max(0, ceil((N-i*A)/B))
        result = min(result, i*AV + j*BV)
        if j==0:
            break

    return result

print(solution(*map(int, input().split(" "))))