for _ in range(int(input())):
	x,y = map(lambda x: int(x,2), input().split())
	print(format(x+y,"b"))