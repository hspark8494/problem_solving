import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))

kingdoms = {}
for _ in range(N):
    name = input().rstrip()
    kingdoms[name] = name

def find(x):
    while x != kingdoms[x]:
        kingdoms[x] = kingdoms[kingdoms[x]]
        x = kingdoms[x]
    return x

def union(x, y):
    px = find(x)
    py = find(y)
    if px==py:
        kingdoms[px] = x
        kingdoms[x] = x
        px = x
    kingdoms[py] = px
    return x

for _ in range(M):
    a, b, w = input().rstrip().split(",")
    if int(w)==2:
        a, b = b, a
    union(a,b)

result = sorted(set(map(find, kingdoms.values())))
print(len(result))
print(*result, sep="\n")