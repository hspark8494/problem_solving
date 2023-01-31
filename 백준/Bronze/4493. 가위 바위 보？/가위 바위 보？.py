import sys

input = sys.stdin.readline

for _ in range(int(input())):
    p1, p2 = 0, 0
    for _ in range(int(input())):
        r1, r2 = input().rstrip().split(" ")
        if r1 == r2:
            continue
        elif (
            (r1 == "R" and r2 == "S")
            or (r1 == "S" and r2 == "P")
            or (r1 == "P" and r2 == "R")
        ):
            p1 += 1
        else:
            p2 += 1

    if p1 > p2:
        print("Player 1")
    elif p2 > p1:
        print("Player 2")
    else:
        print("TIE")
