from collections import deque
from sys import stdin
input = stdin.readline
N = int(input())
nodes = [set() for _ in range(N+1)]
for _ in range(N-1):
    o1, o2 = map(int, input().split())
    nodes[o1].add(o2)
    nodes[o2].add(o1)

parent = [0 for _ in range(N-1)]
dq = deque()
dq.append(1)

while dq:
    idx = dq.popleft()
    for child in nodes[idx]:
        nodes[child].remove(idx)
        parent[child-2] = idx
        dq.append(child)

print(*parent, sep="\n")
