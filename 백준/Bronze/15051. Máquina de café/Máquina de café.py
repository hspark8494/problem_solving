import sys
A, B, C = map(int, sys.stdin.readlines())
mn = 10000
mn = min(mn, B*2+C*4)
mn = min(mn, A*2+C*2)
mn = min(mn, A*4+B*2)

print(mn)