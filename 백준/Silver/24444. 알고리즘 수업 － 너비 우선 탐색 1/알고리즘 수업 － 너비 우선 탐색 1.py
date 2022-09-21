from collections import deque
import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
N, M, R = map(int, input().split(" "))
nodes = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split(" "))
    nodes[u].append(v)
    nodes[v].append(u)

for node in nodes:
    node.sort()

dq = deque()
dq.append(R)
acc = 0
while dq:
    curr = dq.popleft()
    if visited[curr] == 0:
        acc+=1
        visited[curr] = acc
        for x in nodes[curr]:
            if visited[x] == 0:
                dq.append(x)

print(*visited[1:], sep="\n")