import heapq, sys
input = sys.stdin.readline

N, E = map(int, input().split())
nodes = [[] for _ in range(N+1)]
INF = 30000000001
for _ in range(E):
    p1, p2, d = map(int, input().split(" "))
    nodes[p1].append((d, p2))
    nodes[p2].append((d, p1))

def dijkstra(start):
    dist = [INF for _ in range(N+1)]
    pq = [(0, start)]
    dist[start] = 0
    while pq:
        d, curr = heapq.heappop(pq)
        if dist[curr] < d:
            continue
        for nd, next in nodes[curr]:
            if dist[curr]+nd < dist[next]:
                dist[next] = dist[curr]+nd
                heapq.heappush(pq, (dist[next], next))
    return dist

v1, v2 = map(int, input().split(" "))
o_dist = dijkstra(1)
d1_dist = dijkstra(v1)
d2_dist = dijkstra(v2)

result = min(o_dist[v1] + d1_dist[v2] + d2_dist[N], o_dist[v2] + d2_dist[v1] + d1_dist[N])

print(result if result<INF else -1)