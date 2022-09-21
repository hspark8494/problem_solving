import sys

a,b,c = map(int, sys.stdin.readlines())

result = 91 + a + b*3 + c
print("The 1-3-sum is", result)