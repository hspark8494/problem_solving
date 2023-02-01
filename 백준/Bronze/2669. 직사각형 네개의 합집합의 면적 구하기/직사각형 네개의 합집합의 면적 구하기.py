board = [[0] * 101 for _ in range(101)]

for _ in range(4):
    lx, ly, rx, ry = map(int, input().split(" "))
    for i in range(lx, rx):
        for j in range(ly, ry):
            board[i][j] = 1

r = 0
for line in board:
    for l in line:
        r += l

print(r)