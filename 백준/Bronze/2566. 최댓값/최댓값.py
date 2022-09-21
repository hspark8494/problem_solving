from sys import stdin
l = []
for _ in range(9):
    l.append(list(map(int, stdin.readline().split())))
mx = 0
x=0
y=0
for i in range(9):
    for j in range(9):
        if l[i][j] > mx:
            mx = l[i][j]
            x = i
            y = j
print(mx)
print(x+1, y+1)