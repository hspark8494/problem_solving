from collections import deque
import itertools
import sys
input = sys.stdin.readline
N, M = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(N)]
dq = deque()
pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
virus = []
safe = []
result = 0
for n in range(N):
    for m in range(M):
        if board[n][m] == 2:
            virus.append((n,m))
        elif board[n][m] == 0:
            safe.append((n,m))

def bfs(board):
    dq.extend(virus)
    while dq:
        curr = dq.pop()
        board[curr[0]][curr[1]] = 2
        for p in pos:
            x, y = curr[0]+p[0], curr[1]+p[1]
            if x >= 0 and y >= 0 and x < N and y < M and board[x][y] == 0:
                dq.append((x,y))
    x = 0
    for n in range(N):
        for m in range(M):
            if board[n][m] == 0:
                x += 1
    return x

def copy_board():
    return [b.copy() for b in board]

for comb in itertools.combinations(safe, 3):
    l = copy_board()
    for x in comb:
        l[x[0]][x[1]] = 1
    result = max(result, bfs(l))

print(result)
