import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
L = [i for i in range(N+1)]

for _ in range(M):
    e1, e2 = map(int, input().split(" "))
    L[e1], L[e2] = L[e2], L[e1]

print(*L[1:])
