from collections import deque
import heapq
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    T, N, M = map(int, input().rstrip().split(" "))
    nodes = [[] for _ in range(N+1)]
    degrees = [0 for _ in range(N+1)]
    for _ in range(M):
        p1, p2 = map(int, input().rstrip().split(" "))
        nodes[p1].append(p2)
        degrees[p2] += 1

    dq = deque()
    for i in range(1, N+1):
        if degrees[i] == 0:
            dq.append((i, 1))

    result = [[] for _ in range(N+1)]
    mx = 0
    while dq:
        curr, idx = dq.popleft()
        mx = max(mx, idx)
        for next in nodes[curr]:
            result[next].append(idx)
            degrees[next] -= 1
            if degrees[next] == 0:
                result[next].sort(reverse=True)
                nidx = result[next][0]
                if len(result[next])>=2 and nidx == result[next][1]:
                    nidx+=1
                dq.append((next, nidx))
    print(T, mx)