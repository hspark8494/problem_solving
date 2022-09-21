import heapq, sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
nodes = [[] for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]
for _ in range(M):
    p1, p2 = map(int, input().split(" "))
    nodes[p1].append(p2)
    degrees[p2] += 1

pq = []
for i in range(1, N+1):
    if degrees[i] == 0:
        heapq.heappush(pq, i)

while pq:
    curr = heapq.heappop(pq)
    print(curr)
    for x in nodes[curr]:
        degrees[x] -= 1
        if degrees[x] == 0:
            heapq.heappush(pq, x)