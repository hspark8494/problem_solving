import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
L = [0 for _ in range(N)]

for _ in range(M):
    s, e, n = map(int, input().split(" "))
    for i in range(s-1, e):
        L[i] = n

print(*L)
