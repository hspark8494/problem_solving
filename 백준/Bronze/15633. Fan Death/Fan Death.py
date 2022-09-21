import math

a = int(input())
li=[]

for i in range(1,int(math.sqrt(a))+1):
    if a%i == 0:
        li.append(i)
        if i != int(a/i):
            li.append(int(a/i))

print(sum(li)*5-24)