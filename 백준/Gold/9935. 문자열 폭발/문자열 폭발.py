left = list(reversed(input()))
boom = list(input())
right = []
ln = len(boom)

while left:
    right.append(left.pop())
    if len(right) >= ln and right[-ln:] == boom:
        for i in range(ln):
            right.pop()

if right:
    print("".join(right))
else:
    print("FRULA")