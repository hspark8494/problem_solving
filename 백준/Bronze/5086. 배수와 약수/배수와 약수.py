while True:
    i, j = map(int, input().split())
    if i==0 and j==0:
        break

    if j%i == 0:
        print("factor")
    elif i%j == 0:
        print("multiple")
    else:
        print("neither")