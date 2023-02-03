def solution(keyinput, board):
    pos = {'right': (1, 0), 'left': (-1, 0), 'up': (0, 1), 'down': (0, -1)}
    W, H = board[0] // 2, board[1]//2
    cw, ch = 0, 0

    for key in keyinput:
        nw, nh = pos[key]
        if W >= nw+cw >= -W:
            cw += nw
        if H >= nh+ch >= -H:
            ch += nh
    return [cw, ch]
