c = 0
while True:
    a = int(input()) * 3
    if a ==0:
        break
    bol = (a%2==0)
    c=c+1
    a=a//2 if bol else (a+1)//2
    a=a*3
    a=a//9

    if bol:
        print("%d. %s %d" %(c, "even", a))
    else:
        print("%d. %s %d" %(c, "odd", a))
