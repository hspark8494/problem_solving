for p in range(int(input())):
    li = []
    for q in range(int(input())):
        li.append(list(input().split()))
    idx = 0
    for i,e in enumerate(li):
        if int(e[1]) >= int(li[idx][1]):
            idx=i
    print(li[idx][0])
