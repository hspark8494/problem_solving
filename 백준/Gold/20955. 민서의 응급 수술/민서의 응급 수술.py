import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))

parent = [i for i in range(N+1)]
result = 0

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x==y:
        return True
    parent[y] = x
    return False
for _ in range(M):
    x, y = map(int, input().rstrip().split(" "))
    if union(x,y):
        result+=1

p = find(1)
for i in range(1, N+1):
    if p != find(i):
        result += 1
        union(p, i)

print(result)