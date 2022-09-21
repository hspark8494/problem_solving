s = list(input().rstrip())
t = list(input().rstrip())
result = False
ln = len(s)
while t:
    lnt = len(t)
    if ln==lnt and s == t:
        result = True
        break
    elif lnt<ln:
        break
    if t[-1] == "A":
        t.pop()
    else:
        t.pop()
        t.reverse()

print(int(result))