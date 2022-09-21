while True:
	s = input()
	if s == "0":
		break
	t=1
	for i in s:
		if i=="1":
			t=t+3
		elif i=="0":
			t=t+5
		else:
			t=t+4
	print(t)