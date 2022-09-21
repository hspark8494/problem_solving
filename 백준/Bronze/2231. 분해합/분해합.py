n = int(input())
con = 1
while True:
	if con==n:
		con=0
		break
	r = con
	for i in str(con):
		r=r+int(i)
	if r==n:
		break
	con=con+1
print(con)