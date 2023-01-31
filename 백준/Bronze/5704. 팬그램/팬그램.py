import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '*':
        break
    b = [False] * 26

    for c in s:
        if c.isalpha():
            b[ord(c)-97] = True

    print("Y" if all(b) else "N")