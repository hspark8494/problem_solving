import math
input()
li = list(map(int, input().split()))
for x,y in enumerate(li):
    for i in range(2, int(math.sqrt(y))+1):
        if y%i == 0 or y<2:
            li[x]=0
            break
c=0
for i in li:
    if i>1:
        c=c+1
print(c)