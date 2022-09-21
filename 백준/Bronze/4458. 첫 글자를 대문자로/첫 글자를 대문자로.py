from sys import stdin
for _ in range(int(input())):
	s = stdin.readline().rstrip()
	print(str.upper(s[0])+s[1:])