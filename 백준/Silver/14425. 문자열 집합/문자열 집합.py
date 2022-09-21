import sys
input = sys.stdin.readline
N, M = map(int, input().split(" "))
s = set([input().rstrip() for _ in range(N)])
r = 0
for _ in range(M):
    if input().rstrip() in s:
        r+=1
print(r)