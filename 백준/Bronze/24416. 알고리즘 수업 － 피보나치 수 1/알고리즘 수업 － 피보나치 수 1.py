x = int(input())
if x<=2:
    print(1, 1)
else:
    p1, p2 = 1, 1
    for _ in range(x-2):
        t = p1
        p1 = p2
        p2 = t+p2
    print(p2, x-2)