import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    while n >= 10:
        t = 0
        for i in str(n):
            t += int(i)
        n = t
    print(n)
