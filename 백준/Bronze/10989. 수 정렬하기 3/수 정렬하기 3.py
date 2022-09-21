from sys import stdin
l = [0 for _ in range(0,10001)]
for _ in range(int(input())):
	l[int(stdin.readline())] += 1


for i,j in enumerate(l):
	if j>0:
		for _ in range(j):
			print(i)