s = input()
l=[]
for x in s:
	i = ord(x)
	if i>=97:
		l.append(chr(i-32))
	else:
		l.append(chr(i+32))
		
print("".join(l))