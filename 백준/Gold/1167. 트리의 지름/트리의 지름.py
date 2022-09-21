import sys

input = sys.stdin.readline

N = int(input())

nodes = [[] for _ in range(N+1)]

for _ in range(N):
    li = list(map(int, input().rstrip().split()))
    curr = nodes[li[0]]
    i = 1
    while True:
        if li[i] == -1:
            break
        curr.append((li[i], li[i+1]))
        nodes[li[i]].append((li[0], li[i+1]))
        i+=2

mx = (0,0)
tmp = []
def dfs(curr, visited):
    global mx
    val, i = curr
    visited[i] = True
    for next in nodes[i]:
        if not visited[next[0]]:
            t = (val+next[1], next[0])
            tmp.append(t)
            mx = max(mx, t)
            dfs(t, visited)

visited = [False] * (N+1)
dfs((0, 1), visited)
visited = [False] * (N+1)
t = mx
mx = (0,0)
dfs((0, t[1]), visited)
print(mx[0])