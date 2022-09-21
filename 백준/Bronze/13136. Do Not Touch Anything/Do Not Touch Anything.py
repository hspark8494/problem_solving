import math
v,h,s = map(int,input().split())
print(math.ceil(v/s) * math.ceil(h/s))