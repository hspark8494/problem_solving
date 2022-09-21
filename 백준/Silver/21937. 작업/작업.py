
import sys


input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))
nodes = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().rstrip().split(" "))
    nodes[B].append(A)
X = int(input())

result = 0
visited = [False] * (N+1)
stack = [X]

while stack:
    curr = stack.pop()
    visited[curr] = True
    result+=1
    for next in nodes[curr]:
        if not visited[next]:
            visited[next] = True
            stack.append(next)

print(result-1)