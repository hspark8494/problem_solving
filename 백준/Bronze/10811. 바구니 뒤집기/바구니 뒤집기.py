import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
L = [i+1 for i in range(N)]

for _ in range(M):
    e1, e2 = map(int, input().split(" "))
    e1 = e1-1
    L = L[:e1] + L[e1:e2][::-1] + L[e2:]

print(*L)
