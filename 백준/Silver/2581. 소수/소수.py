import math
m = int(input())
n = int(input())
li = [i for i in range(n+1)]
li[1] = 0
for i,j in enumerate(li):
    if j != 0:
        x=2
        while i*x<len(li):
            li[i*x]=0
            x=x+1

sm = 0
mn = 0
for i in range(m,n+1):
    if li[i] != 0:
        sm=sm+li[i]
    if li[i] != 0 and mn==0:
        mn=li[i]

if sm==0:
    print(-1)
else:
    print(sm, mn, end="\n")