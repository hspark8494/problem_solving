for _ in range(int(input())):
    i = int(input())
    l = []
    p = 1
    while True:
        if p>=i-p:
            break
        l.append(str(p)+" "+str(i-p))
        p=p+1
    print("Pairs for %d: " % i, end="")
    print(", ".join(l))
