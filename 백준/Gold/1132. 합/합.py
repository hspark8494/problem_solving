import sys
input = sys.stdin.readline

N = int(input())
li = [0 for _ in range(10)]
start = [False for _ in range(10)]
for _ in range(N):
    x = 1
    S = input().rstrip()
    start[ord(S[0])-65] = True
    for s in reversed(S):
        li[(ord(s)-65)] += x
        x = x*10


if all(li):
    mn = sys.maxsize
    idx = 0
    for i in range(10):
        if not start[i] and mn>li[i]:
            mn = li[i]
            idx = i
    li[idx] = 0

li.sort()

result = 0
for i, val in enumerate(li):
    result += i * val
print(result)