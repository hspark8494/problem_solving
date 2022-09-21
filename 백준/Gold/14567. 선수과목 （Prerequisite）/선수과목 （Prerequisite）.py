from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
nodes = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
result = [0 for _ in range(N)]
for _ in range(M):
    p1, p2 = map(int, input().split(" "))
    nodes[p1].append(p2)
    degree[p2]+=1

dq = deque()
for i in range(1,N+1):
    if degree[i] == 0:
        dq.append(i)
dept = 1
while dq:
    for _ in range(len(dq)):
        d = dq.popleft()
        result[d-1] = dept
        for i in nodes[d]:
            degree[i] -= 1
            if degree[i] == 0:
                dq.append(i)
    dept+=1
print(*result)