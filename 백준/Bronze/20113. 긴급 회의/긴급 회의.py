n = int(input())
l = [0 for _ in range(n)]
for i in list(map(int,input().split())):
	if i:
		l[i-1]=l[i-1]+1
mx = max(l)
if l.count(mx)>=2:
	print("skipped")
else:
	print(l.index(mx)+1)