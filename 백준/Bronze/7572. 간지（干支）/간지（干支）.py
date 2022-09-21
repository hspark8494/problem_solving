i = int(input())
s = "ABCDEFGHIJKL"[(i+8)%12] + str((i+6)%10)
print(s)