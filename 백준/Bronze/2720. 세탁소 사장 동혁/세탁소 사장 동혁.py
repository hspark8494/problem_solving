import sys
input = sys.stdin.readline

coins = [25, 10, 5, 1]
for _ in range(int(input())):
    m = int(input())
    r = [0] * 4
    for i, c in enumerate(coins):
        r[i] = m//c
        m = m % c
    print(*r, sep=" ")