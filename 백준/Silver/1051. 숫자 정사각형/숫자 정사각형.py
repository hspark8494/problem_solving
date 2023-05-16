import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))
board = []
for line in range(N):
    board.append(list(map(int, list(input().rstrip()))))

S = min(N, M)-1
x, y = 0, 0
while True:
    if x+S >= N:
        x, y = 0, y+1
    if y+S >= M:
        x, y, S = 0, 0, S-1
        continue
    if (board[x][y] == board[x+S][y] == board[x][y+S] == board[x+S][y+S]):
        print((S+1)**2)
        break
    x += 1