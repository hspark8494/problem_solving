for i in range(int(input())):
    n, nn = 0, 1
    for c in input():
        if c =="O":
            n = n+nn
            nn = nn+1
        else:
            nn = 1
    print(n)