from collections import deque
import sys
input = sys.stdin.readline

H, W = map(int, input().rstrip().split(" "))

board = [list(input().rstrip()) for _ in range(H)]
visited = [[False for _ in range(W)] for _ in range(H)]
pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

fire = deque()
dq = deque()
end = ""


def find(H, W):
    global end
    for i in range(H):
        for j in range(W):
            if board[i][j] == "S":
                dq.append((i, j))
                visited[i][j] = True
                board[i][j] = "."
            elif board[i][j] == "*":
                fire.append((i, j))
            elif board[i][j] == "D":
                end = (i, j)

find(H, W)
dept = -1
flag = False
while dq:
    dept += 1
    for _ in range(len(fire)):
        x, y = fire.popleft()
        for p in pos:
            h, w = x+p[0], y+p[1]
            if 0 <= h < H and 0 <= w < W and board[h][w] == ".":
                board[h][w] = "*"
                fire.append((h, w))

    for _ in range(len(dq)):
        x, y = dq.popleft()
        for p in pos:
            h, w = x+p[0], y+p[1]
            if 0 <= h < H and 0 <= w < W and (board[h][w] == "." or board[h][w] == "D") and not visited[h][w]:
                visited[h][w] = True
                dq.append((h, w))

        if board[x][y] == "D":
            dq.clear()
            fire.clear()
            flag = True
            break
print(dept if flag else "KAKTUS")