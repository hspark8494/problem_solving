import math
i = int(input())
c=0
for x in reversed(str(math.factorial(i))):
    if x == "0":
        c=c+1
    else:
        break
print(c)