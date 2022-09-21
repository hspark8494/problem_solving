n,h,w = map(int, input().split())
og = ["?" for _ in range(n)]
l = []
for _ in range(h):
	l.append(input())
for x in l:
	for i,j in enumerate(x):
		if j != "?":
			og[i//w]=j

print(*og, sep="")