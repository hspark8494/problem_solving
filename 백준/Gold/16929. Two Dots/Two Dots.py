import sys
input = sys.stdin.readline
H, W = map(int, input().split(" "))
board = [list(input().rstrip()) for _ in range(H)]
pos = [(0,1),(0,-1),(1,0),(-1,0)]

def dfs(h, w, color, dept, start, visited):
    if visited[h][w]:
        return
    visited[h][w] = True
    for p in pos:
        nh, nw = h+p[0], w+p[1]
        if nh==start[0] and nw==start[1]:
            if dept >= 2:
                print("Yes")
                sys.exit()
            else:
                continue
        if 0<=nh<H and 0<=nw<W and board[nh][nw]==color and not visited[nh][nw]:
            dfs(nh, nw, color, dept+1, start, visited)

for h in range(H):
    for w in range(W):
        visited = [[False for _ in range(W)] for _ in range(H)]
        cnt = 0
        for p in pos:
            nh, nw = h+p[0], w+p[1]
            if 0<=nh<H and 0<=nw<W and board[nh][nw]==board[h][w]:
                cnt+=1
            if cnt>=2:
                dfs(h,w,board[h][w],0,(h,w), visited)
                break

print("No")