import sys, math
input = sys.stdin.readline
for _ in range(int(input())):
    a, b, x = map(int, input().split(" "))
    print(x//math.gcd(a, b))