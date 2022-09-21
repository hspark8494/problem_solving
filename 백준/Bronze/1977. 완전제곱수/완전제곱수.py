import math
x = math.ceil(math.sqrt(int(input())))
y = int(input())
li = []
for i in range(x, y):
    if i**2 <= y:
        li.append(i**2)
    else:
        break

if len(li) >0:
    print(sum(li), li[0], end="\n")
else:
    print(-1)