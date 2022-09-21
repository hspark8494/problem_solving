l =[]
for _ in range(int(input())):
	l.append(input())

t = True
for i in range(len(l)):
	for j in range(len(l)):
		if l[i][j] != l[j][i]:
		    t=False
		    break
	if not t:
		break
print("YES" if t else "NO")