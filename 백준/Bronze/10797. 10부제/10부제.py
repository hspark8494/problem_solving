a = int(input())
c = 0
for i in list(map(int, input().split())):
    if a==i:
        c=c+1
print(c)