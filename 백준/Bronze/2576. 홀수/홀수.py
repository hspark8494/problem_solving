mn, s = 101, 0
for i in range(7):
    t = int(input())
    if t%2 == 1:
        s = s+t
        if t<mn:
            mn=t

if s==0:
    print(-1)
else:
    print(s, mn, end="\n")