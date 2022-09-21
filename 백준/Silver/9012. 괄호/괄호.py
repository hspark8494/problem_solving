import sys 
for _ in range(int(input())):
	l = input()
	t = True
	while t and l:
		if l.find("()") == -1:
			t = False
			break
		l = l.replace("()","")
	print("YES" if t else "NO")