import sys

input = sys.stdin.readline

print("Gnomes:")

for _ in range(int(input())):
    a,b,c = map(int, input().rstrip().split(" "))
    if a<=b<=c or c<=b<=a:
        print("Ordered")
    else:
        print("Unordered")