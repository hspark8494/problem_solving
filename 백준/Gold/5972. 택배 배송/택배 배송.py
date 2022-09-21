import heapq,sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
INF = 100000001

nodes = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2, d = map(int, input().split(" "))
    nodes[n1].append((d, n2))
    nodes[n2].append((d, n1))

dist = [INF for _ in range(N+1)]
dist[1] = 0
pq = []
heapq.heappush(pq, (0, 1))

while pq:
    d, curr = heapq.heappop(pq)
    if dist[curr] < d:
        continue
    for nd, next in nodes[curr]:
        if dist[curr]+nd < dist[next]:
            dist[next] = dist[curr]+nd
            heapq.heappush(pq, (nd, next))

print(dist[N])