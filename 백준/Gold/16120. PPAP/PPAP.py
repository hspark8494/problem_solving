S = input()

stack = []
for c in S:
    if len(stack) >= 3 and c == "P" and stack[-1] == "A" and stack[-2] == "P" and stack[-3] == "P":
        stack.pop()
        stack.pop()
        stack.pop()
    stack.append(c)

r = "".join(stack)
if r == "PPAP" or r == "P":
    print("PPAP")
else:
    print("NP")
