from sys import stdin

input = stdin.readline

N = int(input())

for _ in range(N):
    S, E = map(int, input().rstrip().split(" "))
    D = E-S
    t = int(D ** 0.5)
    if D==0:
        print(0)
    elif D==t*t:
        print(t*2-1)
    elif t*t<D and D<=t*t+t:
        print(t*2)
    else:
        print(t*2+1)