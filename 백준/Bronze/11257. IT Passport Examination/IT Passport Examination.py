import sys

input = sys.stdin.readline
for _ in range(int(input())):
    N, A, B, C = map(int, input().split(" "))
    result = A+B+C
    if result >= 55 and A>=10.5 and B>=7.5 and C>=12:
        print(N, result, "PASS")
    else:
        print(N, result, "FAIL")