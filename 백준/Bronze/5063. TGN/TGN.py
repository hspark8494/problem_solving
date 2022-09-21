for x in range(int(input())):
    li = list(map(int, input().split()))
    
    if li[1] > li[0]+li[2]:
        print("advertise")
    elif li[1] < li[0]+li[2]:
        print("do not advertise")
    else:
        print("does not matter")