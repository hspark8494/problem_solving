from collections import deque
from sys import stdin
input = stdin.readline

H, W = map(int, input().split(" "))
maps = [input().rstrip() for _ in range(H)]
pos = [(0,1), (0,-1), (1,0), (-1,0)]

mx = -1
for h in range(H):
    for w in range(W):
        if maps[h][w] != "L":
            continue

        dq = deque()
        dq.append((h,w))
        visited = [[False for _ in range(W)] for _ in range(H)]
        visited[h][w] = True
        dept = -1
        while dq:
            dept += 1
            mx = max(mx, dept)
            for _ in range(len(dq)):
                curr = dq.popleft()
                for p in pos:
                    nh, nw = curr[0] + p[0], curr[1] + p[1]
                    if nh>=0 and nh<H and nw>=0 and nw<W and (not visited[nh][nw] and maps[nh][nw] == "L"):
                        visited[nh][nw] = True
                        dq.append((nh,nw))

print(mx)
