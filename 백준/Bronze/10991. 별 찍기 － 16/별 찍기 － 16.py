n = int(input())

for i in range(1,n+1):
    d=" " * (n-i)
    d=d+" ".join(["*"]*i)
    print(d)