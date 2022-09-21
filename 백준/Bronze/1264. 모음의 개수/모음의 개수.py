from sys import stdin
t ="aeiou"
while True:
	s = stdin.readline().rstrip()
	
	if s=="#":
		break
		
	i=0
	
	for x in s.lower():
		if t.find(x) >=0:
			i+=1
	print(i)