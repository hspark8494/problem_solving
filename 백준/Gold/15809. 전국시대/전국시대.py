import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))

parent = [i for i in range(N)]
values = [int(input()) for _ in range(N)]

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x!=y:
        values[x] += values[y]
        parent[y] = x
    return x

def war(x, y):
    x = find(x)
    y = find(y)
    if values[y]>values[x]:
        y, x = x, y
    values[x] -= values[y]
    parent[y] = x

for _ in range(M):
    o, x,y = map(int, input().rstrip().split(" "))
    if o == 1:
        union(x-1,y-1)
    else:
        war(x-1,y-1)

s = set()
for p in parent:
    x = find(p)
    if values[x]>0:
        s.add((values[x], x))

result = list(map(lambda x : x[0] , s))
result.sort()
print(len(result))
print(*result)