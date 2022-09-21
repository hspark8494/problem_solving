def selfNum(a) -> int:
    r = 0
    s = str(a)
    for c in s:
        r=r+int(c)
    return r+a


l = list(range(0,10000))

for i in range(1,10000):
    t = selfNum(i)
    if t <= 9999:
        l[t] = 0

for i in l:
    if i != 0:
        print(i)        