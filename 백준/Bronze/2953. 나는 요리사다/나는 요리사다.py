l = [[i+1,sum(map(int,input().split()))] for i in range(5)]
l.sort(key=lambda x:-x[1])
print(*l[0])