n, m = map(int, input().split())
l = list(map(int, input().split()))
max = 0
ans = []
for i in range(n):
	for j in range(i+1,n):
		for k in range(j+1,n):
			tmp = l[i]+l[j]+l[k]
			if tmp > max and tmp <= m:
				ans= [ l[i],l[j],l[k] ]
				max= tmp
print(max)