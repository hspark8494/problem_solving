a,b,c = map(int,input().split())

if a>=b and a<=c:
    print(a)
elif abs(a-b) > abs(a-c):
    print(c)
else:
    print(b)