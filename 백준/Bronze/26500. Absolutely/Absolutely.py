import math, sys
input = sys.stdin.readline

for _ in range(int(input())):
    F1, F2 = map(float, input().rstrip().split(" "))
    print(round(math.fabs(F1 - F2), 1))