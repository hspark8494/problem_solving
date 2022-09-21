import heapq, sys
input = sys.stdin.readline

V, E = map(int, input().split())
nodes = [[] for _ in range(V)]
start = int(input())-1
pq = []
for _ in range(E):
    f, t, c = map(int, input().split())
    nodes[f-1].append((t-1, c))
dist = [sys.maxsize] * V
dist[start] = 0
heapq.heappush(pq, (0, start))

while pq:
    d, now = heapq.heappop(pq)
    if dist[now] < d:
        continue
    for node in nodes[now]:
        cost = d + node[1]
        if cost < dist[node[0]]:
            dist[node[0]] = cost
            heapq.heappush(pq, (cost, node[0]))

for i in dist:
    print(i if i != sys.maxsize else "INF")

