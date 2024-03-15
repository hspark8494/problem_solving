import sys
input = sys.stdin.readline

while True:
    L = list(map(int, input().split()))
    if L == [0, 0, 0]:
        break
    L.sort(reverse=True)
    if L[0] >= L[1] + L[2]:
        print("Invalid")
    elif L[0] == L[1] == L[2]:
        print("Equilateral")
    elif L[0] == L[1] or L[1] == L[2]:
        print("Isosceles")
    else:
        print("Scalene")
