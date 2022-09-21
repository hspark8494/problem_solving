A, B, C = input().split(" ")

if A==B==C:
    print("*")
elif A==B and B!=C:
    print("C")
elif A==C and B!=A:
    print("B")
else:
    print("A")