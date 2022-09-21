s = input()
r = 0

for i in s:
    c = ord(i)-65
    d = int(c / 3)
    if d >= 5:
        if c < 19:
            r = r+8
        elif c < 22:
            r = r+9
        else:
            r = r+10
    else:
        r = r+d+3

print(r)