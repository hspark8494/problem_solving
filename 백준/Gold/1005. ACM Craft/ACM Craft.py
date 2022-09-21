from collections import deque
import heapq, sys

input = sys.stdin.readline
for _ in range(int(input())):
    N, M = map(int, input().rstrip().split(" "))
    nodes = [[] for _ in range(N+1)]
    times = list(map(int, input().rstrip().split(" ")))
    degrees = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]

    for _ in range(M):
        p1, p2 = map(int, input().rstrip().split(" "))
        degrees[p2] += 1
        nodes[p1].append(p2)

    W = int(input())

    pq = []
    for i in range(1,N+1):
        if degrees[i] == 0:
            heapq.heappush(pq, (times[i-1], i))
            visited[i]=True

    while pq:
        time, curr = heapq.heappop(pq)
        if curr==W:
            print(time)
            break
        for i in nodes[curr]:
            degrees[i] -= 1
            if degrees[i] == 0 and not visited[i]:
                visited[i] = True
                heapq.heappush(pq, (time+times[i-1], i))
