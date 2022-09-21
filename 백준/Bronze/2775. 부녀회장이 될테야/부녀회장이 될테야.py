for _ in range(int(input())):  
    floor = int(input())
    num = int(input())
    li = [x for x in range(1, num+1)]
    for k in range(floor):
        for i in range(1, num):
            li[i] += li[i-1]
    print(li[-1])