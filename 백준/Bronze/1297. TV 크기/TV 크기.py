import math
ih,a,b = map(int,input().split())
c=math.sqrt(a**2+b**2)
ih=ih/c
print(math.floor(a*ih), math.floor(b*ih))