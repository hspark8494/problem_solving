# Q12936 줄 서는 방법
# https://school.programmers.co.kr/learn/courses/30/lessons/12936?language=python3
def solution(n, k):
    fac = [1,1]
    arr = [i for i in range(1, n+1)]
    for i in range(2,n+1):
        fac.append(fac[i-1]*i)
    result = []
    k-=1
    while n!= 0:
        i, k = divmod(k, fac[n-1])
        result.append(arr.pop(i))
        n -= 1
    return result

print(solution(3,5))