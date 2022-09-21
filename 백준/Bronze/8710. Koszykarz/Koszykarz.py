from math import ceil
K, W, M = map(int, input().split(" "))
print(max(0, ceil((W-K)/M)))