from collections import deque
import sys
input = sys.stdin.readline


def sol():
    M, N, H = map(int, input().split(" "))
    board = [[list(map(int, input().split(" ")))
              for _ in range(N)] for _ in range(H)]
    dq = deque()
    pos = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    tomato = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if board[h][n][m] == 1:
                    dq.append((h, n, m, 0))
                elif board[h][n][m] == 0:
                    tomato += 1
    if tomato == 0:
        return 0

    day = -1
    while dq:
        day += 1
        for _ in range(len(dq)):
            curr = dq.popleft()
            for p in pos:
                h, n, m = curr[0]+p[0], curr[1]+p[1], curr[2]+p[2]
                if h >= 0 and n >= 0 and m >= 0 and h < H and n < N and m < M and board[h][n][m] == 0:
                    board[h][n][m] = 1
                    dq.append((h, n, m))

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if board[h][n][m] == 0:
                    return -1

    return day


print(sol())
