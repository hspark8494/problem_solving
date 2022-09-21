import sys

input = sys.stdin.readline
for t in range(int(input())):
    N, M = int(input()), int(input())

    parent = [i for i in range(N)]

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
        union(x, y)

    K = int(input())
    print(f"Scenario {t+1}:")
    for _ in range(K):
        x, y = map(int, input().rstrip().split(" "))
        print(int(find(x)==find(y)))
    print()