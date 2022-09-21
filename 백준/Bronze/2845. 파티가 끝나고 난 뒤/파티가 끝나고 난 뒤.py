i,j = map(int,input().split())
for d in list(map((lambda x: int(x)-i*j), input().split())):
    print(d, end=" ")