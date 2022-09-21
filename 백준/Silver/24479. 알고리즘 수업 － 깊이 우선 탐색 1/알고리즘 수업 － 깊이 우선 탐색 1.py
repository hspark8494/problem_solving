import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
N, M, R = map(int, input().split(" "))
nodes = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split(" "))
    nodes[u].append(v)
    nodes[v].append(u)

for node in nodes:
    node.sort()
acc = 0
def dfs(i):
    global acc
    acc+=1
    visited[i] = acc
    for x in nodes[i]:
        if visited[x] == 0:
            dfs(x)
dfs(R)
print(*visited[1:], sep="\n")