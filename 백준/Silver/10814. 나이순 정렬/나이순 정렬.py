import sys
l =[]
for _ in range(int(input())):
	n,m = sys.stdin.readline().split()
	l.append([int(n),m])
l.sort(key=lambda x:x[0])
for d in l:
	print(*d)
