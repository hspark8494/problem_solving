r = 0
for _ in range(6):
	r = r+(1 if input() == "W" else 0)

print([-1,3,3,2,2,1,1][r])