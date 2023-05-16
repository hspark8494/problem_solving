import math
N, X, Y = map(int, input().split(" "))
X, Y = min(X, Y), max(X, Y)
cnt = 0
while True:
    cnt += 1
    if X % 2 != 0 and X+1 == Y:
        print(cnt)
        break
    N = math.ceil(N/2)
    X = math.ceil(X/2)
    Y = math.ceil(Y/2)