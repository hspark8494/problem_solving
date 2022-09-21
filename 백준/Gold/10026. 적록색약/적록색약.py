import sys
sys.setrecursionlimit(100000000)
N = int(input())
board = [input() for _ in range(N)]
pos = [(0,1), (0,-1), (1,0), (-1, 0)]

visited = [[False for _ in range(N)] for _ in range(N)]

def dfs(h, w, visited):
    if visited[h][w]:
        return
    visited[h][w] = True
    val = board[h][w]
    for p in pos:
        nh, nw = h+p[0], w+p[1]
        if nh>=0 and nh<N and nw>=0 and nw<N and not visited[nh][nw] and val == board[nh][nw]:
            dfs(nh, nw, visited)

n1 = 0
n2 = 0
for h in range(N):
    for w in range(N):
        if not visited[h][w]:
            n1+=1
            dfs(h, w, visited)

for i in range(N):
    board[i] = board[i].replace("G","R")
visited = [[False for _ in range(N)] for _ in range(N)]

for h in range(N):
    for w in range(N):
        if not visited[h][w]:
            n2+=1
            dfs(h, w, visited)

print(n1, n2)