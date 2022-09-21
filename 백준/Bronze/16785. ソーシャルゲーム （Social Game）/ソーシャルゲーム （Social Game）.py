a,b,c = map(int,input().split())
d = r = 0
while r<c:
	d=d+1
	r=r+a
	if d%7==0 and d!=0:
		r=r+b
print(d)