import sys
input = sys.stdin.readline
N, T, P = map(int, input().rstrip().split(" "))
L = []
if N > 0:
    L = list(map(int, input().rstrip().split(" ")))
L.sort(reverse=True)
L = L[:P]
r = len(L)
for i, n in enumerate(L):
    if T >= n:
        r = i
        break

if (len(L) >= P and L[-1] >= T):
    print(-1)
else:
    print(r+1)
