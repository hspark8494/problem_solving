from collections import deque
import heapq
import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))
nodes = [[] for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    li = list(map(int, input().rstrip().split(" ")))
    ln = li[0]
    for i in range(1, ln):
        for j in range(i+1, ln+1):
            nodes[li[i]].append(li[j])
            degrees[li[j]] += 1

result = []

dq = deque()
for i in range(1, N+1):
    if degrees[i] == 0:
        dq.append(i)

while dq:
    curr = dq.popleft()
    result.append(curr)
    if visited[curr]:
        dq.clear()
        result = []
        break
    visited[curr] = True
    for next in nodes[curr]:
        degrees[next] -= 1
        if degrees[next] == 0:
            dq.append(next)

if len(result) != N:
    print(0)
else:
    print(*result, sep="\n")