import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a1, a2, b1, b2 = map(int, input().rstrip().split(" "))
    a, b = a1*a2, b1*b2
    if a > b:
        print("TelecomParisTech")
    elif a < b:
        print("Eurecom")
    else:
        print("Tie")