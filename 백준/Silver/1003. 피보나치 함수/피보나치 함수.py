x = int(input())
fibo = [(1,0),(0,1)]
for _ in range(x):
    n = int(input())
    while len(fibo) <= n:
        f1 = fibo[-1]
        f2 = fibo[-2]
        fibo.append((f1[0]+f2[0], f1[1]+f2[1]))
    print(*fibo[n])