def dist(s1, s2):
    d=4
    for i in range(4):
        if s1[i]==s2[i]:
            d=d-1
    return d

from sys import stdin

for _ in range(int(stdin.readline())):
    x = int(stdin.readline())
    l = stdin.readline().rstrip().split()
    d = 100
    if x<4096:
        for i in range(x):
            if d == 0:
                break
            for j in range(i+1,x):
                if d == 0:
                    break
                for n in range(j+1,x):
                    k=dist(l[i],l[j])
                    k+=dist(l[j],l[n])
                    k+=dist(l[i],l[n])
                    d = min(k,d)
                    if d == 0:
                        break
    else:
        d=0

    print(d)