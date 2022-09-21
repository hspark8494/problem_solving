from collections import deque
import heapq
import sys

input = sys.stdin.readline
N = int(input())
nodes = [[] for _ in range(N+1)]
times = [0 for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i in range(1,N+1):
    li = list(map(int, input().rstrip().split(" ")))
    times[i] = li[0]
    degrees[i] = li[1]
    for j in range(li[1]):
        nodes[li[j+2]].append(i)

pq = []
for i in range(1,N+1):
    if degrees[i] == 0:
        heapq.heappush(pq, (times[i], i))
        visited[i]=True

mx = 0
while pq:
    time, curr = heapq.heappop(pq)
    mx = max(mx, time)
    for i in nodes[curr]:
        degrees[i] -= 1
        if degrees[i] == 0 and not visited[i]:
            visited[i] = True
            heapq.heappush(pq, (time+times[i], i))

print(mx)