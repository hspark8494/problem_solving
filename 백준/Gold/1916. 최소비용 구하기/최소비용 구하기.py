from sys import stdin
input = stdin.readline
INF = int(1e9)

n, m = int(input()), int(input())
nodes = [[] for _ in range(n+1)]
dist = [INF]*(n+1)
visited = [False]*(n+1)
visited[0] = True
for _ in range(m):
    t = list(map(int, input().split()))
    nodes[t[0]].append((t[1], t[2]))

start, end = map(int, input().split())

def dijkstra(start):
    for node in nodes[start]:
        dist[node[0]] = min(dist[node[0]], node[1])
    visited[start] = True
    dist[start] = 0
    for _ in range(n-1):
        curr = get_short_node()
        visited[curr] = True
        for node in nodes[curr]:
            dist[node[0]] = min(dist[node[0]], dist[curr]+node[1])

def get_short_node(): 
    mn = INF
    idx = 0
    for i in range(1, n+1):
        if not visited[i] and dist[i] < mn:
            mn = dist[i]
            idx = i
    return idx

dijkstra(start)

print(dist[end])