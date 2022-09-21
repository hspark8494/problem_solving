from collections import deque

y, x = map(int, input().split())
li = [list(map(int, input().split(" "))) for _ in range(x)]
pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = -1
que = deque()

for i in range(x):
    for j in range(y):
        if li[i][j] == 1:
            que.append((i, j))

def bfs(i, j, queue):
    for p in pos:
        ix, jy = i+p[0], j+p[1]
        if ix >= 0 and ix<x and jy>=0 and jy<y and li[ix][jy] == 0:
            queue.append((ix, jy))
            li[ix][jy] = 1

while True:
    tmpque = deque()
    while que:
        l = que.popleft()  
        bfs(l[0], l[1], tmpque)
    result+=1
    if not tmpque:
        break
    que = tmpque

for l in li:
    if not all(l):
        result = -1

print(result)