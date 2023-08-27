import sys
input = sys.stdin.readline

N = int(input())
L = [input().rstrip() for _ in range(N)]
result = len(L[0])

for i in range(1, result):
    s = set()
    for e in L:
        s.add(e[-i:])
    if len(s) == N:
        result = i
        break

print(result)
