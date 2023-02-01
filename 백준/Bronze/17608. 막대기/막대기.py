import sys
input = sys.stdin.readline
N = int(input())
L = [int(input()) for _ in range(N)]
r, mx = 0, 0

for i in reversed(L):
    if i > mx:
        r += 1
        mx = i
print(r)
