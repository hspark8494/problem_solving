import sys
input = sys.stdin.readline

input()
stack = []
while True:
    s = input().rstrip()
    if s == "고무오리 디버깅 끝":
        break
    elif s == "문제":
        stack.append(0)
    else:
        if stack:
            stack.pop()
        else:
            stack.append(0)
            stack.append(0)

print("고무오리야 사랑해" if not stack else "힝구")
