import sys 
for x in range(1,int(input())+1):
	l = sys.stdin.readline().split()[::-1]
	print("Case #%d: "%x, end="")
	print(*l)