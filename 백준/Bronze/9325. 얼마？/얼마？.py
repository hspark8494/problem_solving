for i in range(int(input())):
    s = int(input())
    for j in range(int(input())):
        n,m = map(int,input().split())
        s=s+n*m
    print(s)