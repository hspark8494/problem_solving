import sys
input = sys.stdin.readline
N = int(input())
while True:
    print("? 1")
    sys.stdout.flush()
    r = input().rstrip()
    if r == "Y":
        print("! 1")
        break
