import sys
l=[]
for _ in range(int(input())):
	l.append(list(map(int,sys.stdin.readline().split())))
l.sort(key=lambda x:(x[1],x[0]))

for i in l:
	print(i[0], i[1])