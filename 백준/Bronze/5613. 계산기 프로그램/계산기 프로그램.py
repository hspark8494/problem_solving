import sys
f = sys.stdin.readlines()
r, op = 0, '+'

for s in f:
    if s.rstrip().isdecimal():
        i = int(s)
        if op == '+':
            r += i
        elif op == '-':
            r -= i
        elif op == '*':
            r *= i
        elif op == '/':
            r //= i
    else:
        op = s.rstrip()

print(r)