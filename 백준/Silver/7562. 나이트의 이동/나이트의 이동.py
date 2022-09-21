from collections import deque
import sys
input = sys.stdin.readline
pos = [(2,1),(1,2),(1,-2),(2,-1),(-1,2),(-2,1),(-1,-2),(-2,-1)]

def bfs():
    L = int(input())
    sx, sy = map(int, input().split(" "))
    end = tuple(map(int, input().split(" ")))
    visited = [[False for _ in range(L)] for _ in range(L)]
    dq = deque()
    dq.append((sx,sy))
    visited[sx][sy] = True
    dept = -1
    while dq:
        dept+=1
        for _ in range(len(dq)):
            curr = dq.popleft()
            if curr == end:
                return dept
            for p in pos:
                x, y = curr[0]+p[0], curr[1]+p[1]
                if 0<=x<L and 0<=y<L and not visited[x][y]:
                    visited[x][y]=True
                    dq.append((x,y))
    return 0


for _ in range(int(input())):
    print(bfs())
