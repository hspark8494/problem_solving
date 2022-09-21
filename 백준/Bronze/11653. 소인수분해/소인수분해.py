i = int(input())
c=2
while True:
    if i<=1:
        break
    if i%c == 0:
        print(c)
        i=i//c
    else:
        c=c+1