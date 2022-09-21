for k in range(int(input())):
    n = input().split()
    r = float(n[0])
    for s in n[1:]:
        if s == "@":
            r = r*3
        elif s == "%":
            r = r+5
        elif s == "#":
            r = r-7
    print("{:0.2f}".format(r))