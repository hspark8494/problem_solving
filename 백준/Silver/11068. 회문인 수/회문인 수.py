for _ in range(int(input())):
    i = int(input())
    r = 0
    for b in range(2,65):
        tmp = i
        s = []
        while tmp>=b:
            s.append(tmp%b)
            tmp=tmp//b
        s.append(tmp)
        if s==s[::-1]:
            r = 1
            break
    print(r)
