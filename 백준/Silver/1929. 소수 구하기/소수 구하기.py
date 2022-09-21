import math
m, n = map(int,input().split())
li = [i for i in range(n+1)]
li[1] = 0
for i,j in enumerate(li):
    if j == 0:
        continue
    else:
        x=2
        while i*x<len(li):
            li[i*x]=0
            x=x+1

for i in range(m,n+1):
    if li[i] !=0 :
        print(li[i])
