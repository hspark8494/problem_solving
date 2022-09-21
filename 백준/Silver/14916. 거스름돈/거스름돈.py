import sys
sys.setrecursionlimit(100000000)
N = int(input())
memo = [100001] * (N+1)
try:
    memo[0] = 0
    memo[2] = 1
    memo[5] = 1
except:
    pass
def recv(i):
    if i<0:
        return 100001
    if memo[i] != 100001:
        return memo[i]
    x2, x5 = recv(i-2), recv(i-5)
    if x2==100001 and x2==100001:
        memo[i] = 100001
    else:
        memo[i] = min(x2, x5)+1
    return memo[i]
print(-1 if recv(N)==100001 else memo[N])