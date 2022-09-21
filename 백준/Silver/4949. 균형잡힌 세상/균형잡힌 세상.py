import sys 
while True:
    s = sys.stdin.readline().rstrip("\n")
    if s==".":
        break
    l = []
    for i in s:
        if i in "[]()":
            l.append(i)
    l = "".join(l)
    t = True
    while t and l:
        if l.find("()") == -1 and l.find("[]") == -1:
            t = False
            break
        
        l = l.replace("()","")
        l = l.replace("[]","")

    print("yes" if t else "no")