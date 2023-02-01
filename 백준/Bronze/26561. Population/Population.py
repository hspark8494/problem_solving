import sys
input = sys.stdin.readline

for _ in range(int(input())):
    S, T = map(int, input().rstrip().split(" "))
    print(S + T//4 - T//7)