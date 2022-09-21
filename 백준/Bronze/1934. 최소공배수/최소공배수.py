for m in range(int(input())):
    a, b = map(int, input().split())
    n = a*b
    while b != 0:
        r = a % b
        a = b
        b = r
    print(n//a)