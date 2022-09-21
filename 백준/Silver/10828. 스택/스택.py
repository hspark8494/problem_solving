import sys 
l = []

for _ in range(int(input())):
	o = sys.stdin.readline().split()
	try:
		if o[0] == "push":
			l.append(o[1])
		elif o[0] == "pop":
			print(l.pop())
		elif o[0] == "size":
			print(len(l))
		elif o[0] == "empty":
			print(0 if l else 1)
		elif o[0] == "top":
			print(l[len(l)-1])
	except:
		print(-1)