for x in range(int(input())):
    k,y = 0, 0

    for i in range(9):
        a,b = map(int, input().split())
        y=y+a
        k=k+b
    if y>k:
        print("Yonsei")
    elif k>y:
        print("Korea")
    else:
        print("Draw")