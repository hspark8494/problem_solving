for _ in range(int(input())):
    d = int(input())
    l = []
    for i,j in enumerate(reversed(format(d,'b'))):
        if j == "1":
            l.append(i)
    print(*l)
