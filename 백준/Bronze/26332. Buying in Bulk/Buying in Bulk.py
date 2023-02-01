import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, P = map(int, input().rstrip().split(" "))
    print(N, P)
    print(P + (N-1)*(P-2))