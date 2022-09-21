a,b = map(int,input().split())
x = (a+b)//2
y = (a-b)//2
if (a+b)%2 or b>a:
	print(-1)
else:
	print(max(x,y),min(x,y))