from sys import stdin

input = stdin.readline

N, W, H = map(int, input().split(" "))
M = (W*W+H*H)**0.5
for _ in range(N):
    if int(input()) > M:
        print("NE")
    else:
        print("DA")