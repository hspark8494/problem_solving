s = 0
for i in range(int(input())):
    n,m = map(int,input().split())
    s=s+m%n
print(s)