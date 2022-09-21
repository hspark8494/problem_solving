import sys

A, X, B, Y, T = map(int, sys.stdin.readlines())

a_value = (max(T-30,0)*X)*21+A
b_value = (max(T-45,0)*Y)*21+B
print(a_value, b_value)