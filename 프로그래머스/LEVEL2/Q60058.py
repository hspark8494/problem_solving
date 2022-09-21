# Q60058 괄호변환
# https://school.programmers.co.kr/learn/courses/30/lessons/60058
def solution(p):
    result = ''
    if p == '' or check(p) == 1:
        return p
    splited = split_brace(p)
    if splited[2] == 1:
        result += (splited[0] + solution(splited[1]))
    else:
        result += f"({solution(splited[1])})"
        for c in splited[0][1:-1]:
            if c=='(':
                result += ')'
            else:
                result += '('
    return result

def check(s):
    open, close = 0, 0
    correct = True
    stack = []
    for c in s:
        if c == "(":
            open +=1
            stack.append(c)
        else:
            close +=1
            if not (stack and stack.pop()  == "(" ):
                correct = False

    correct = not stack and correct
    if correct and open==close:
        return 1
    elif open==close:
        return 0
    else:
        return -1

def split_brace(s):
    if check(s) == 1:
        return (s, "")
    for i in range(1,len(s)):
        ck = check(s[:i])
        if ck > -1:
            return (s[:i], s[i:], ck)

    return (s, "", check(s))

print(solution(")("))