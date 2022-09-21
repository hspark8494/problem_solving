import sys

lines = sys.stdin.read()
chars = [0 for _ in range(26)]

for c in lines:
    x = ord(c)
    if x>=97:
        chars[x-97] += 1

result = []
mx = 0

for i, c in enumerate(chars):
    if mx==c:
        result.append(chr(i+97))
    elif c>mx:
        result = [chr(i+97)]
        mx = c

print("".join(result))