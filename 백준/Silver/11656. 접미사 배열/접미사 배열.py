s = input()
r = set()
for i in range(len(s)):
	r.add(s[i:])
	
print(*sorted(list(r)), sep="\n")