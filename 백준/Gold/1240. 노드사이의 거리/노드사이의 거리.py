from collections import deque
import sys


input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))

nodes = [[] for _ in range(N+1)]

for _ in range(N-1):
    x, y, val = map(int, input().rstrip().split(" "))
    nodes[x].append((y, val))
    nodes[y].append((x, val))

def bfs(x, y):
    global N
    visited = [False] * (N+1)
    visited[x] = True
    dq = deque()
    dq.append((x,0))
    while dq:
        curr, weight = dq.pop()
        if curr==y:
            return weight
        for next, val in nodes[curr]:
            if not visited[next]:
                visited[next] = True
                dq.append((next, weight+val))
    return -1

for _ in range(M):
    x, y = map(int, input().rstrip().split(" "))
    print(bfs(x, y))