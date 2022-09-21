for _ in range(int(input())):
	s = str.upper(input())
	if s==s[::-1]:
		print("Yes")
	else:
		print("No")