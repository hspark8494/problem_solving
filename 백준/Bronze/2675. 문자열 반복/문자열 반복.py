for z in range(int(input())):
    n, s = input().split()
    n = int(n)
    for c in s:
        print(c*n, end="")
    print()