from collections import deque
import heapq
import sys

input = sys.stdin.readline
N = int(input())
nodes = [[] for _ in range(N+1)]
times = [0 for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]
result = [-1 for _ in range(N)]

for i in range(1,N+1):
    li = list(map(int, input().rstrip().split(" ")))
    times[i] = li[0]
    li.pop()
    degrees[i] = len(li)-1
    for j in range(1, len(li)):
        nodes[li[j]].append(i)

pq = []
for i in range(1,N+1):
    if degrees[i] == 0:
        heapq.heappush(pq, (times[i], i))
        result[i-1] = times[i]

while pq:
    time, curr = heapq.heappop(pq)
    for i in nodes[curr]:
        degrees[i] -= 1
        if degrees[i] == 0 and result[i-1] == -1:
            result[i-1] = time+times[i]
            heapq.heappush(pq, (time+times[i], i))

print(*result, sep="\n")