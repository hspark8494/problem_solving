r = 0

for mm in range(int(input())):
    s = input()
    pre = ""
    t = []
    bol = True

    for i,j in enumerate(s):
        if j != pre:
            try:
                if t.index(j) >= 0:
                    bol = False
                    break
            except: 
                t.append(j)
        pre = j
        if not bol:
            break
    r=r+int(bol)

print(r)