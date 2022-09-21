import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().rstrip().split(" "))
unable = list(map(int, input().rstrip().split(" ")))
unable[-1] = 0
nodes = [[] for _ in range(N)]

for _ in range(M):
    p1, p2, d = map(int, input().split(" "))
    if unable[p1] or unable[p2]:
        continue
    nodes[p1].append((d, p2))
    nodes[p2].append((d, p1))

dist = [INF for _ in range(N)]
dist[0] = 0
pq = [(0,0)]

while pq:
    d, curr = heapq.heappop(pq)
    if dist[curr] < d:
        continue
    for nd, next in nodes[curr]:
        if nd+dist[curr] < dist[next]:
            dist[next] = nd+dist[curr]
            heapq.heappush(pq, (dist[next], next))


print(dist[-1] if dist[-1] != INF else -1)