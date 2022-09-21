i = int(input())
s = 0
c = 0
while True:
    if c+s > i:
        print(c-1)
        break
    else:
        s=s+c
        c=c+1
