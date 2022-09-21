import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
N = int(input())
board = [list(input().strip()) for _ in range(N)]
pos = [(0,1), (0,-1), (1,0), (-1, 0)]
result = []

def dfs(x,y,idx,board):
    board[x][y] = "0"
    result[idx] += 1
    for p in pos:
        px, py = p[0]+x, p[1]+y
        if px >= 0 and px < N and py >= 0 and py < N and board[px][py] == "1":
            dfs(px,py,idx,board) 

for x in range(N):
    for y in range(N):
        if board[x][y] == "1":
            result.append(0)
            dfs(x,y,len(result)-1,board)

print(len(result))
print(*sorted(result), sep="\n")