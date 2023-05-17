import sys
import math
input = sys.stdin.readline

X = int(input())

for _ in range(X):
    x1, y1, r1, x2, y2, r2 = map(int, input().rstrip().split(" "))

    D = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

    if D == 0 and r1 == r2:
        print(-1)
    elif r1+r2 > D and abs(r1-r2) < D:
        print(2)
    elif r1+r2 == D or abs(r1-r2) == D:
        print(1)
    elif D > r1 + r2:
        print(0)
    else:
        print(0)