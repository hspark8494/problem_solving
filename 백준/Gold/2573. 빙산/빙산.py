from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

H, W = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(H)]
visited = [[0 for _ in range(W)] for _ in range(H)]
pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

remains = 0
start = None
for h in range(H):
    for w in range(W):
        if board[h][w] > 0:
            remains+=1
            if start==None:
                visited[h][w]+=1
                start = (h,w)

que = deque()
que.append(start)
dept = 0
acc = []
while True:
    nums = 0
    while que:
        curr = que.popleft()
        nums+=1
        weight = 0
        for p in pos:
            h,w = curr[0]+p[0], curr[1]+p[1]
            if h >= 0 and h < H and w >= 0 and w < W:
                if board[h][w] <= 0:
                    weight += 1
                elif visited[h][w] == dept:
                    visited[h][w] += 1
                    que.append((h,w))
        acc.append((curr[0],curr[1],weight))
    if nums != remains:
        print(dept)
        break
    while acc:
        c = acc.pop()
        board[c[0]][c[1]] -= c[2]
        if not que and board[c[0]][c[1]]>0:
            que.append((c[0],c[1]))
            visited[c[0]][c[1]] += 1
        if board[c[0]][c[1]] <= 0:
            remains -=1
    if remains == 0:
        print(0)
        break
    dept+=1