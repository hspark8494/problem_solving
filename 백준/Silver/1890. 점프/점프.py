import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().rstrip().split(" "))) for _ in range(N)]
visited = [[-1 for _ in range(N)] for _ in range(N)]
visited[N-1][N-1] = 1
result = 0

def find(h, w):
    global result
    if visited[h][w] != -1:
        return visited[h][w]

    visited[h][w] = 0
    x = board[h][w]
    xh, xw = x+h, x+w

    if xh < N:
        if visited[xh][w] == -1:
            visited[h][w] += find(xh, w)
        else:
            visited[h][w] += visited[xh][w]
    if xw < N:
        if visited[h][xw] == -1:
            visited[h][w] += find(h, xw)
        else:
            visited[h][w] += visited[h][xw]
    return visited[h][w]


print(find(0, 0))
