n,m = map(int,input().split())
i=0
l = []
for x in range(n):
    l.append(list(range(i+1,i+m+1)))
    i=i+m
for x in l:
    print(*x)