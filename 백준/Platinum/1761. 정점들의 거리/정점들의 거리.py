import sys

sys.setrecursionlimit(int(1e5))
lines = sys.stdin.readline

N = int(input())

parents = [0 for _ in range(N+1)]
parents_dist = [0 for _ in range(N+1)]
depts = [0 for _ in range(N+1)]
nodes = [[] for _ in range(N+1)]

for _ in range(N-1):
    x, y, d = map(int, input().rstrip().split(" "))
    nodes[x].append((y, d))
    nodes[y].append((x, d))

def dfs(i, dept):
    if depts[i]:
        return
    depts[i] = dept
    for next in nodes[i]:
        if not depts[next[0]]:
            parents[next[0]] = i
            parents_dist[next[0]] = next[1]
            dfs(next[0], dept+1)
dfs(1, 1)

def lca(x, y):
    result = 0
    if depts[x] > depts[y]:
        x, y = y, x
    while depts[x] < depts[y]:
        result += parents_dist[y]
        y = parents[y]
    while x!=y:
        result += parents_dist[x] + parents_dist[y]
        x, y = parents[x], parents[y]
    return result

for _ in range(int(input())):
    x, y = map(int, input().rstrip().split(" "))
    print(lca(x, y))