def solution(ingredient):
    stack, r = "", 0
    for c in ingredient:
        stack += str(c)
        if stack.endswith("1231"):
            r += 1
            stack = stack[:-4]
    return r