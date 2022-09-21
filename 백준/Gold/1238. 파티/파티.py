import heapq,sys

input = sys.stdin.readline

N, M, X = map(int, input().split(" "))
INF = 100000001

nodes = [[] for _ in range(N+1)]
r_nodes = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2, d = map(int, input().split(" "))
    nodes[n1].append((d, n2))
    r_nodes[n2].append((d,n1))

def dijkstra(nodes, start):
    dist = [INF for _ in range(N+1)]
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, X))

    while pq:
        d, curr = heapq.heappop(pq)
        if dist[curr] < d:
            continue
        for nd, next in nodes[curr]:
            if dist[curr]+nd < dist[next]:
                dist[next] = dist[curr]+nd
                heapq.heappush(pq, (nd, next))
    return dist

r1 = dijkstra(nodes, X)
r2 = dijkstra(r_nodes, X)
mx = 0
for i in range(1, N+1):
    mx = max(mx, r1[i]+r2[i])

print(mx)