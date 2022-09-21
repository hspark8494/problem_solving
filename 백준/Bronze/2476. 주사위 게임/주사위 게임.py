mx = 0
for i in range(int(input())):
    a,b,c = map(int,input().split())
    d = 0
    if a==b and b==c:
        d=10000+(a*1000)
    elif a==b or b==c or c==a:
        d=1000+(a*100) if a==b or c==a else 1000+(b*100)
    else:
        d=a*100 if a>b else (b*100 if b>c else c*100)
    if d>mx:
        mx=d
print(mx)
