import math

A1, P1 = map(int, input().split(" "))
R1, P2 = map(int, input().split(" "))
print("Slice of pizza" if A1/P1 > R1*R1*math.pi/P2 else "Whole pizza")