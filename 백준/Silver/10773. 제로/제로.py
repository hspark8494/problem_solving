l = []
for _ in range(int(input())):
	i = int(input())
	if not i:
		l.pop()
	else:
		l.append(i)
		
print(sum(l))