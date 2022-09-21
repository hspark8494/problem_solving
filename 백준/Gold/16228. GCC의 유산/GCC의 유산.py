import re

strings = input()
stack = []
calc = []
lex = re.findall("(([0-9]+)|[+\-*\/\(\)]|[<?]+|[>?]+)", strings)

for s in lex:
    s = s[0]
    if s.isnumeric():
        calc.append(s)
        continue

    if s == "(":
        stack.append(s)
    elif s == ")":
        while stack and stack[-1] != "(":
            calc.append(stack.pop())
        stack.pop()
    elif s == ">?" or s == "<?":
        while stack and (stack[-1] == ">?" or stack[-1] == "<?"):
            calc.append(stack.pop())
        stack.append(s)
    elif s == "+" or s == "-":
        while stack and stack[-1] != "(":
            calc.append(stack.pop())
        stack.append(s)
while stack:
    calc.append(stack.pop())
acc = []
for next in calc:
    if next.isnumeric():
        acc.append(int(next))
        continue
    if next == "+":
        acc.append(acc.pop() + acc.pop())
    elif next == "-":
        acc.append(-acc.pop() + acc.pop())
    elif next == "<?":
        acc.append(min(acc.pop(), acc.pop()))
    elif next == ">?":
        acc.append(max(acc.pop(), acc.pop()))

print(acc[0])