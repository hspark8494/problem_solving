import sys

input = sys.stdin.readline

while True:
    N, M = map(int, input().rstrip().split(" "))
    if N==0 and M==0:
        break
    parent = [i for i in range(N)]
    values = [1 for _ in range(N)]

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


    for _ in range(M):
        li = list(map(int, input().rstrip().split(" ")))
        k = li[0]
        if k>0:
            p = find(li[1])
            for i in range(k-1):
                union(p, li[i+2])

    print(values[find(0)])