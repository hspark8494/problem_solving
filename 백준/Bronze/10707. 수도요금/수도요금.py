li = [int(input()) for i in range(5)]
y = li[1] + max(0,(li[4]-li[2])*li[3])
print(min(li[0]*li[4],y))