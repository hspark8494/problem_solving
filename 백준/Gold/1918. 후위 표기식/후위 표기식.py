t = input()
r = [] # 출력
op = [] # 연산자
d = {"+":1, "-":1, "*":2, "/":2}
for i in t:
    if i not in "()+-*/":
        r.append(i)
        continue

    if i == "(":
        op.append("(")
        continue

    if i ==")":
        o = op.pop()
        while o != "(":
            r.append(o)
            o = op.pop()
        continue

    while True:
        if not op:
            op.append(i)
            break
        if op[-1] == "(":
            op.append(i)
            break
        if d[op[-1]] >= d[i]:
            r.append(op.pop())
            continue
        else:
            op.append(i)
            break
    else:
        op.append(i)


print("".join(r)+"".join(op[::-1]))