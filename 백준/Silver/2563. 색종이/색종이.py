import sys
input = sys.stdin.readline

N = int(input())
board = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

result = 0
for row in board:
    result += sum(row)

print(result)