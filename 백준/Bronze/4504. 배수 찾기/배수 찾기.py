x = int(input())
while True:
    i = int(input())
    if i==0:
        break
    t = int(i/x)
    if x*t == i:
        print("%d is a multiple of %d."%(i,x))
    else:
        print("%d is NOT a multiple of %d."%(i,x))