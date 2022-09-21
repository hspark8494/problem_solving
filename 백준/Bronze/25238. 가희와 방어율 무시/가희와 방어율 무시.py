n, m = map(int, input().split(" "))
if n - (n * m/100) >= 100:
    print(0)
else:
    print(1)