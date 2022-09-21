import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))

parent = [i for i in range(N+1)]
visited = [False for _ in range(N+1)]

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x

for _ in range(M):
    x, y = map(int, input().rstrip().split(" "))
    union(x,y)

li = list(map(int, input().rstrip().split(" ")))
result = -1
pre = 0

for i in li:
    x = find(i)
    if x != pre:
        result += 1
        pre = x

print(result)