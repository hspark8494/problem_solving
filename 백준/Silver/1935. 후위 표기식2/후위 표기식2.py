n = int(input())
l = list(input())
d = [int(input()) for _ in range(n)]
stack = []

for i in l:
    if i in "+-*/":
        s1 = str(stack.pop())
        s2 = str(stack.pop())
        stack.append(eval(s2+i+s1))
    else:
        stack.append(d[ord(i)-65])

print('%.2f' % stack[0])