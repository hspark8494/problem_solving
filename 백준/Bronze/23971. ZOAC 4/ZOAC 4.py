import math
H, W, i, j = map(int, input().split())
print(math.ceil(H/(i+1)) * math.ceil(W/(j+1)))
