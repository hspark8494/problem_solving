i = int(input())
if i == 0:
	print("divide by zero")
else:
	l=list(map(int,input().split()))
	s=0.0
	for n in l:
		s=s+(n/i)
	print("%.2f" % ((sum(l)/i)/s))