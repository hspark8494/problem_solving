p1 = [500,300,200,50,30,10]
p2 = [512,256,128,64,32]
num = int(input())
for _ in range(num):
    i1,i2 = map(int,input().split())
    s = 0
    t = 0
    if i1:
        for x in range(1,7):
            t = t+x
            if i1<=t:
                s=s+p1[x-1]
                break
    t=0
    if i2:
        for x in range(5):
            t = t+(2**x)
            if i2<=t:
                s=s+p2[x]
                break

    print(s*10000)