import sys

input = sys.stdin.readline

d,h,m = map(int, input().rstrip().split(" "))

result = (d-11)*24*60 + (h-11)*60 + (m-11)

print(max(-1, result))