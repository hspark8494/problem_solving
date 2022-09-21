A, B = map(int, input().split(" "))
if A==0 and B==0:
    print("Not a moose")
elif A==B:
    print("Even", A+B)
else:
    print("Odd", max(A,B)*2)