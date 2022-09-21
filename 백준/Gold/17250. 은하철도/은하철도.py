import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))

parent = [i for i in range(N+1)]
values = [0] + [int(input()) for _ in range(N)]

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

result = []
def union(x, y):
    x = find(x)
    y = find(y)
    if x!=y:
        values[x] += values[y]
        parent[y] = x
    return values[x]

for _ in range(M):
    x, y = map(int, input().rstrip().split(" "))
    result.append(union(x,y))

print(*result, sep="\n")