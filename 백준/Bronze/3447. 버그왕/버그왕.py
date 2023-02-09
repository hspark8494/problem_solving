import sys
S = sys.stdin.read()
stack = []
for c in S:
    stack.append(c)
    if len(stack) >= 3 and stack[-3:] == ["B", "U", "G"]:
        stack.pop()
        stack.pop()
        stack.pop()
print("".join(stack))
