import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b = input().rstrip().split(" ")
    if sorted(a) == sorted(b):
        print("Possible")
    else:
        print("Impossible")
