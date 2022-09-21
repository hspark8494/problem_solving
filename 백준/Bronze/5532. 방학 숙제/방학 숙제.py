import math
l = [int(input()) for _ in range(5)]
print(l[0]-math.ceil(max((l[2]/l[4]),(l[1]/l[3]))))