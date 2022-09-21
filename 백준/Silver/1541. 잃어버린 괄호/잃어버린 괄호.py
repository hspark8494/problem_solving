import re

stack = re.findall(pattern="[+-]|[0-9]+", string=input())
stack.reverse()
minus = False
plus = False

result = int(stack.pop())
acc = 0
while stack:
    curr = stack.pop()
    if curr.isnumeric():
        curr = int(curr)
        if minus:
            acc += curr
        else:
            result += curr

    elif curr== "-":
        minus = True
        if minus:
            result -= acc
            acc = 0

print(result-acc)