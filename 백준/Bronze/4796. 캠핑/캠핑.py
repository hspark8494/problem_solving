import sys
input = sys.stdin.readline
t = 0
while True:
    a, b, c = map(int, input().split(" "))
    if a == 0 and b == 0 and c == 0:
        break
    r = c // b * a + min(c % b, a)
    t += 1
    print(f"Case {t}: {r}")
