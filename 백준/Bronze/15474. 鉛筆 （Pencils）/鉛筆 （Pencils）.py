import math
l = list(map(int, input().split()))

x = math.ceil(l[0]/l[1])*l[2]
y = math.ceil(l[0]/l[3])*l[4]

print(min(x,y))