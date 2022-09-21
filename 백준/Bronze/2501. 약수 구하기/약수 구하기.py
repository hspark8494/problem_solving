import math

a,b = map(int,input().split())
li=[]

for i in range(1,int(math.sqrt(a))+1):
    if a%i == 0:
        li.append(i)
        if i != int(a/i):
            li.append(int(a/i))

li.sort()
print(li[b-1] if len(li)>=b else 0)