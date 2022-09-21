input()
c=1
r=0
li = map(int, input().split())
for i in li:
    if i:
        r=r+c
        c=c+1
    else:
        c=1

print(r)