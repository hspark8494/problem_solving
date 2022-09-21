from collections import deque
import sys

input = sys.stdin.readline

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x!=y:
        parent[x] = y


N, M = map(int, input().rstrip().split(" "))
nodes = [[] for _ in range(N)]
parent = [i for i in range(N)]
degrees = [0] * N

buffer = []
for _ in range(M):
    p, op, q = input().rstrip().split(" ")
    p, q = int(p), int(q)
    if op==">":
        buffer.append((p,q))
    else:
        union(p,q)

for p,q in buffer:
    p = find(p)
    q = find(q)
    nodes[p].append(q)
    degrees[q] += 1

dq = deque()
for i in range(N):
    if degrees[i] == 0:
        dq.append(i)
result = 0

while dq:
    curr = dq.popleft()
    result+=1
    for next in nodes[curr]:
        degrees[next] -= 1
        if degrees[next] == 0:
            dq.append(next)

if result == N:
    print("consistent")
else:
    print("inconsistent")