import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

H, W = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(H)]

pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(ch, cw, visited, buffer:set):
    if visited[ch][cw]:
        return
    visited[ch][cw] = True

    for p in pos:
        h, w = ch+p[0], cw+p[1]
        if 0 <= h < H and 0 <= w < W:
            if board[h][w] == 1:
                buffer.add((h,w))
            elif board[h][w] == 0 and not visited[h][w]:
                dfs(h, w, visited, buffer)

dept = -1
remains = 0
for b in board:
    remains += sum(b)

pre = remains
while True:
    buffer = set()
    visited = [[False for _ in range(W)] for _ in range(H)]
    dfs(0, 0, visited, buffer)
    dept += 1

    if not buffer:
        print(dept)
        print(pre)
        break
    
    pre = remains
    remains -= len(buffer)

    for s in buffer:
        board[s[0]][s[1]] = 0