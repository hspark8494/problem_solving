from collections import deque
import sys

input = sys.stdin.readline

H, W = map(int, input().split(" "))

board = [list(input().rstrip()) for _ in range(H)]
parent = [[(h, w) for w in range(W)] for h in range(H)]
pos = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def find(x):
    while x != parent[x[0]][x[1]]:
        px, py = parent[x[0]][x[1]]
        parent[x[0]][x[1]] = parent[px][py]
        x = parent[x[0]][x[1]]
    return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    parent[x[0]][x[1]] = y


def check(x):
    for p in pos:
        h, w = x[0]+p[0], x[1]+p[1]
        if 0 <= h < H and 0 <= w < W and (board[h][w] == "." or board[h][w] == "L"):
            union((h, w), x)


def eq(x, y):
    return find(x) == find(y)


dq = deque()
target = []

for h in range(H):
    for w in range(W):
        x = (h, w)
        if board[h][w] == ".":
            check(x)
        elif board[h][w] == "L":
            target.append(x)
            board[h][w] = "."
            check(x)
        else:
            for p in pos:
                nh, nw = x[0]+p[0], x[1]+p[1]
                if 0 <= nh < H and 0 <= nw < W and (board[nh][nw] == "." or board[nh][nw] == "L"):
                    dq.append(x)
                    break

dept = 0

ndq = deque()

while not eq(target[0], target[1]):
    dept += 1

    while dq:
        h,w = dq.pop()
        if board[h][w] == ".":
            continue
        check((h,w))
        for p in pos:
            nh, nw = h+p[0], w+p[1]
            if 0 <= nh < H and 0 <= nw < W and board[nh][nw] == "X":
                ndq.append((nh,nw))
        board[h][w] = "."
        
    dq, ndq = ndq, dq

print(dept)