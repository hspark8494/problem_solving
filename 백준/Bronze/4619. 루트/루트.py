while True:
    b, n = map(int, input().split())
    if not b and not n:
        break
    i = 1
    while True:
        if i**n >= b:
            break
        else:
            i+=1
    if abs(i**n-b)>abs((i-1)**n-b):
        print(i-1)
    else:
        print(i)