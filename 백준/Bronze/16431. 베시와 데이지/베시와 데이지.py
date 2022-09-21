bx, by = map(int,input().split())
dx, dy = map(int,input().split())
jx, jy = map(int,input().split())
b = max(abs(bx-jx),abs(by-jy))
d = abs(dx-jx)+abs(dy-jy)


if b==d:
	print("tie")
else:
	print("bessie" if b<d else "daisy")