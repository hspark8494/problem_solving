li = []
for p in range(3):
    li.append(list(map(int, input().split())))

x = li[0][0] if li[1][0]==li[2][0] else (li[1][0] if li[0][0] == li[2][0] else li[2][0])
y = li[0][1] if li[1][1]==li[2][1] else (li[1][1] if li[0][1] == li[2][1] else li[2][1])

print(x,y)