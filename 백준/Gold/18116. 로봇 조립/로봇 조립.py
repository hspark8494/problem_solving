import sys

input = sys.stdin.readline

N = int(input())

parent = [i for i in range(1000001)]
values = [1 for _ in range(1000001)]

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

for _ in range(N):
    q = input().rstrip().split(" ")
    if q[0]=="I":
        union(int(q[1]),int(q[2]))
    else:
        print(values[find(int(q[1]))])