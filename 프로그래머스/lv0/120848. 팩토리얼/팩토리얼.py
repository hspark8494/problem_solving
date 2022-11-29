def solution(n):
    if(n<=1):
        return 1
    i = 1
    curr = 1
    while curr<n:
        curr = curr*i
        i+=1
    i-=1
    return i-1 if (curr>n) else i

print(solution(0))