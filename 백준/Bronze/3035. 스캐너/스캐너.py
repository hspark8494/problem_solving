import sys
input = sys.stdin.readline
R, C, ZR, ZC = map(int, input().rstrip().split(" "))

li = [input().rstrip() for _ in range(R)]

result = []

for line in li:
    r = ""
    for c in line:
        r += (c*ZC)
    for _ in range(ZR):
        result.append(r)

print(*result, sep="\n")