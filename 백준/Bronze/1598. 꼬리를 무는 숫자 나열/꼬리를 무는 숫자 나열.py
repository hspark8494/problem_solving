a,b = map(int,input().split())
aX = (a-1)//4
aY = a%4 if a%4 else 4
bX = (b-1)//4
bY = b%4 if b%4 else 4
print(abs(aX-bX)+abs(aY-bY))