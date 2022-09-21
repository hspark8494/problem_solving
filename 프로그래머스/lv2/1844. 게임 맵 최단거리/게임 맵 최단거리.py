from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    pos = [(1,0), (-1,0), (0,1), (0,-1)]
    dq = deque()
    dq.append((0,0))
    maps[0][0] = 0
    dept = 0
    while dq:
        dept+=1
        for _ in range(len(dq)):
            x,y = dq.popleft()
            if x==N-1 and y==M-1:
                return dept
            for p in pos:
                xp, yp = x+p[0], y+p[1]
                if xp>=0 and xp<N and yp >=0 and yp<M and maps[xp][yp] == 1:
                    maps[xp][yp] = 0
                    dq.append((xp, yp))
    return -1