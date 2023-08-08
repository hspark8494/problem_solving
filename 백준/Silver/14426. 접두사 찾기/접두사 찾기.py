import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
s = set()
for i in range(N):
    t = ""
    for j in input().rstrip():
        t += j
        s.add(t)

r = 0
for i in range(M):
    if input().rstrip() in s:
        r += 1

print(r)
