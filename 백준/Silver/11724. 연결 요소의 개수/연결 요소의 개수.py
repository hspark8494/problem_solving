import sys
sys.setrecursionlimit(10000)

n,m = map(int, input().split())
nodes = [[] for _ in range(n)]
visited = [False for _ in range(n)]
result = 0
for l in range(m):
    u, v = map(int, input().split(" "))
    nodes[u-1].append(v-1)
    nodes[v-1].append(u-1)
    
def dfs(i):
    visited[i] = True
    for node in nodes[i]:
        if not visited[node]:
            dfs(node)

for i in range(len(nodes)):
    if not visited[i]:
        result += 1
        dfs(i)

print(result)