import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

pos = [(1, -1), (1, 0), (1, 1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
while True:
    W, H = map(int, input().split(" "))
    if H == 0 and W == 0:
        break
    board = [list(map(int, input().split())) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]

    def dfs(h, w):
        if visited[h][w]:
            return
        visited[h][w] = True
        for p in pos:
            nh, nw = h+p[0], w+p[1]
            if H > nh >= 0 and W > nw >= 0 and not visited[nh][nw] and board[nh][nw] == 1:
                dfs(nh, nw)
    cnt = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] == 1 and not visited[i][j]:
                cnt += 1
                dfs(i, j)
    print(cnt)
