n = int(input())

def fibo(n):
    p1 = 0
    p2 = 1
    while n>0:
        t = p1
        p1 = p2
        p2 = (t+p2) %1000000000
        n-=1
    return p1%1000000000

if n==0:
    print(0, 0, sep="\n")
elif n<0:
    r = fibo(-n)
    if n%2==0:
        print(-1)
    else:
        print(1)
    print(r)
else:
    print(1, fibo(n), sep="\n")