x = int(input())
p1, p2 = 1, 2
if x==1:
    print(1)
else:
    for _ in range(x-2):
        t = p1
        p1 = p2
        p2=(t+p2)%15746
    print(p2)