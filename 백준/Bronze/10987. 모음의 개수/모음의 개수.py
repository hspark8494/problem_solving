s = input()
t ="aeiou"
i=0
for x in s:
	if t.find(x) >=0:
		i+=1
print(i)