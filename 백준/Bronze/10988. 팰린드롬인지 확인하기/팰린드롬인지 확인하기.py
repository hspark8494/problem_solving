import math
s = input()
l = len(s)
s1 = s[:int(l/2)]
s2 = s[:math.ceil(l/2)-1:-1]

print(int(s1==s2))