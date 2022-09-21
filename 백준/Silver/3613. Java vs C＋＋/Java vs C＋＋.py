import sys
t = input()

upper = any(map(lambda x : x.isupper(), t))
lower = t.islower()
underbar = t.find("_") >= 0

if t.find("__") >= 0 or t[-1]=="_" or t[0]=="_" or t[0].isupper() or (upper and underbar):
    print("Error!")
    sys.exit()

if lower and not underbar:
    print(t)
    sys.exit()

nt = []
if upper:
    for i in t:
        if i.isupper():
            nt.append("_")
            nt.append(i.lower())
        else:
            nt.append(i)
else:
    b = False
    for i in t:
        if i=="_":
            b=True
            continue
        elif b:
            nt.append(i.upper())
            b=False
        else:
            nt.append(i)

print("".join(nt))



