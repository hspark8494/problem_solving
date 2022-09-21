for t in range(int(input())):
    l = list(map(int, input().split()))
    sum = 0
    for i in l[1:]:
        sum = sum+i
    avg = sum/l[0]
    c=0
    for i in l[1:]:
        if i>avg:
            c=c+1
    print("{:0.3f}%".format(c/l[0]*100))