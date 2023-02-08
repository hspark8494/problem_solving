A, B, C, D = map(int, input().split(" "))
if A*B > C*D:
    print("M")
elif A*B < C*D:
    print("P")
else:
    print("E")