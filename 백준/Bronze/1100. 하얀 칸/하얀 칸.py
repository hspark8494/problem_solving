import sys

board = sys.stdin.readlines()
result = 0

for i, line in enumerate(board):
    for j, sell in enumerate(line.rstrip()):
        if sell=="F" and ((i%2==0 and j%2==0) or (i%2==1 and j%2==1)):
            result+=1

print(result)