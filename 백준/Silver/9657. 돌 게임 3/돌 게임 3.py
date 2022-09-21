import sys
sys.setrecursionlimit(100000)

N = int(input())

dp = [True, True, False, True, True, True]

for i in range(len(dp), N+1):
    dp.append(not (dp[i-1] and dp[i-3] and dp[i-4]))

print("SK" if dp[N] else "CY")
