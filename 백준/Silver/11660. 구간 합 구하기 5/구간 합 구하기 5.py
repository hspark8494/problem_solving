import sys
input = sys.stdin.readline
N, M = map(int, input().split(" "))
board = [] 
for _ in range(N):
    tmp = [0]
    for l in list(map(int, input().split(" "))):
        tmp.append(tmp[-1] + l)
    board.append(tmp)

sums = [list(map(int, input().split(" "))) for _ in range(M)]

for x1, y1, x2, y2 in sums:
    result = 0
    for i in range(x1-1, x2):
        result += (board[i][y2] - board[i][y1-1])
    print(result)