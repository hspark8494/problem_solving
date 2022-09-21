import sys

input = sys.stdin.readline

while True:
    x = float(input())
    if x == 0:
        break
    result = 1
    result += x + x**2 + x**3 + x**4
    print(f"{result:.2f}")