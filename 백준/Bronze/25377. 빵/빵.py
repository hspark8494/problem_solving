from sys import stdin

input= stdin.readline

result = 2147483647
val = -1

for _ in range(int(input())):
    X, Y = map(int, input().rstrip().split(" "))
    if 0 <= Y-X < result:
        result = Y-X
        val = Y

print(val)
