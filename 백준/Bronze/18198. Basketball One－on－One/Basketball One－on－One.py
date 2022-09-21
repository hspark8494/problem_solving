s = input()
ln = len(s)
i, a, b = 0, 0, 0
d = False
while i < ln:
    t = s[i]
    p = int(s[i+1])
    if t == "A":
        a += p
    else:
        b += p
    i+=2
if a>b:
    print("A")
else:
    print("B")