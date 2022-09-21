import math
import sys
input = sys.stdin.readline

i = int(input())

while i > 0:
    i-=1
    n = int(input())
    result = 1
    for x in range(1,n+1):
        result = result + math.log10(x)
    print(int(result))