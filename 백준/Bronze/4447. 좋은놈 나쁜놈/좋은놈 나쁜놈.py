import sys
input = sys.stdin.readline

for _ in range(int(input())):
    name = input().rstrip()
    g, b = 0, 0
    for c in name.lower():
        if c == 'g':
            g += 1
        elif c == 'b':
            b += 1
    r = ""
    if g>b:
        r = "GOOD"
    elif b>g:
        r = "A BADDY"
    else:
        r = "NEUTRAL"
    print(f"{name} is {r}")