def solution(board):
    pos = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
    N = len(board)
    for h in range(N):
        for w in range(N):
            if board[h][w] != 1:
                continue
            for p in pos:
                ph, pw = h+p[0], w+p[1]
                if N > ph >= 0 and N > pw >= 0 and board[ph][pw] != 1:
                    board[ph][pw] = 2
    r = 0
    for h in range(N):
        for w in range(N):
            if board[h][w] == 0:
                r += 1
    return r