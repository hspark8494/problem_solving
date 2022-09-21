from collections import deque
import sys
input = sys.stdin.readline

H, W = map(int, input().rstrip().split(" "))

board = [list(input().rstrip()) for _ in range(H)]
visited = [[False for _ in range(W)] for _ in range(H)]
pos = [(0,1),(0,-1),(1,0),(-1,0)]

fire = deque()
dq = deque()

def find(H,W):
    for i in range(H):
        for j in range(W):
            if board[i][j] == "J":
                dq.append((i,j))
                visited[i][j] = True
                board[i][j] = "."
            elif board[i][j] == "F":
                fire.append((i,j))

find(H,W)
dept = 0
flag = False
while dq:
    dept +=1
    for _ in range(len(fire)):
        x, y = fire.popleft()
        for p in pos:
            h, w = x+p[0], y+p[1]
            if 0<=h<H and 0<=w<W and board[h][w] == ".":
                board[h][w] = "F"
                fire.append((h,w))

    for _ in range(len(dq)):
        x,y = dq.popleft()
        for p in pos:
            h, w = x+p[0], y+p[1]
            if 0<=h<H and 0<=w<W and board[h][w] == "." and not visited[h][w]:
                visited[h][w] = True
                dq.append((h,w))

        if x==0 or x==H-1 or y==0 or y==W-1:
            dq.clear()
            fire.clear()
            flag=True
            break

print(dept if flag else "IMPOSSIBLE")