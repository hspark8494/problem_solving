import sys
x=1
for i in range(int(input())):
	s1, s2 = map(int,sys.stdin.readline().split())
	if s1==x:
		x=s2
	elif s2==x:
		x=s1
print(x)