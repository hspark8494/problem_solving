import math
while True:
    a = int(input())
    if a == -1:
        break

    li=[]

    for i in range(1,int(math.sqrt(a))+1):
        if a%i == 0:
            li.append(i)
            if i != int(a/i):
                li.append(int(a/i))

    li.remove(a)
    if a == sum(li):
        li.sort()
        print(("%d = "%a)+ " + ".join(map(str,li)))
    else:
        print("%d is NOT perfect." % a)