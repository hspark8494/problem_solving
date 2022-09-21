import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())

    parent = {}
    values = {}

    def find(x):
        if x not in parent:
            parent[x] = x
            values[x] = 1
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
        return values[x]

    for _ in range(N):
        x, y = input().rstrip().split(" ")
        print(union(x,y))