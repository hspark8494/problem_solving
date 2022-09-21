from sys import stdin
input = stdin.readline
n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]
memo = [0 for _ in range(n+1)]
memo[1] = stairs[1]
if n >= 2:
    memo[2] = stairs[1]+stairs[2]

for i in range(3, n+1):
    memo[i] = max(memo[i-2], memo[i-3] + stairs[i-1]) + stairs[i]

print(memo[-1])