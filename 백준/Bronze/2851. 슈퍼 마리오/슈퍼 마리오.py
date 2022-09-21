board = [int(input()) for _ in range(10)]
curr = sum(board)
result = curr
for i in reversed(board):
    curr = curr-i
    if abs(100-curr) < abs(100-result):
        result = curr

print(result)
