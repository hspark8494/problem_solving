c, b = 0, 0
for l in input():
    if l == 'C':
        c += 1
    elif l == 'B':
        b += 1

print(c//2 + b//2)
