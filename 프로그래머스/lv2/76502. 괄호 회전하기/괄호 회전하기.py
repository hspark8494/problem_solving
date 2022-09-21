def solution(s):
    result = 0
    for i in range(len(s)-1):
        result += int(check(s[i:]+s[:i]))
    return result

def check(s):
    open_bracket = "[{("
    close_bracket = "]})"
    stack = []
    for c in reversed(s):
        idx = open_bracket.find(c)
        if idx == -1:
            stack.append(c)
        elif stack and close_bracket[idx] == stack[-1]:
            stack.pop()
        else:
            return False
    return not stack