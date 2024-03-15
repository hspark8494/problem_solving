N = int(input())
L = list(map(int, input().split(" ")))
X = [0] * 51

for i in L:
    X[i] += 1

for i in range(50, 0, -1):
    if X[i] == i:
        print(i)
        break
else:
    if X[0] >= 1:
        print(-1)
    else:
        print(0)
