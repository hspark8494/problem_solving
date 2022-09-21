import sys

n,s = sys.stdin.readline().split()
l = []
aw = ""
x = 0
for i in range(int(n)):
	t1, t2=sys.stdin.readline().split()
	if t1==s:
		aw = t2
	l.append([t1,t2])
for e in l[:i]:
	if e[0] == s:
		break
	elif e[1] == aw:
		x=x+1
print(x)