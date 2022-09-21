for _ in range(3):
	l = list(map(int,input().split()))
	t =  (l[3]*3600 + l[4]*60 + l[5]) - (l[0]*3600 + l[1]*60 + l[2])
	print(t//3600, t%3600//60, t%60)