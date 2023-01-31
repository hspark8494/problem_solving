import sys
input = sys.stdin.readline

N = int(input())
li = [int(input()) for _ in range(N)]

if li[1] - li[0] == li[2] - li[1]:
    print(li[-1] + li[1] - li[0])
else:
    print(li[-1] * (li[1] // li[0]))