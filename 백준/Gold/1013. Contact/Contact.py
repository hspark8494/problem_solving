import sys, re

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    s = input().rstrip()
    t = re.fullmatch("(100+1+|01)+", s)
    print("YES" if t else "NO")
