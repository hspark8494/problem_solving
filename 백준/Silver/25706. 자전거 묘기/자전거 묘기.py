import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
dp = [0] * (n+1)

for i in reversed(range(n)):
    if li[i] == 0:
        dp[i] = dp[i+1]+1
    else:
        if i+li[i]+1 < n:
            dp[i] = dp[i+li[i]+1]+1
        else:
            dp[i] = 1
dp.pop()
print(*dp)
