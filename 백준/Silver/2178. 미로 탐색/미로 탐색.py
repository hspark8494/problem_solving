from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
board = [list(input().rstrip()) for _ in range(N)]
pos = [(1,0), (-1,0), (0,1), (0,-1)]
dq = deque()
dq.append((0,0))
board[0][0] = "0"
dept = 0
while dq:
    dept+=1
    for _ in range(len(dq)):
        x,y = dq.popleft()
        if x==N-1 and y==M-1:
            print(dept)
            sys.exit()
        for p in pos:
            xp, yp = x+p[0], y+p[1]
            if xp>=0 and xp<N and yp >=0 and yp<M and board[xp][yp] == "1":
                board[xp][yp] = "0"
                dq.append((xp, yp))