from sys import stdin
l = stdin.read().rstrip().split("\n")
txt_l = list(l[0])
txt_r = []
l = l[2:]

for o in l:
    if o[0] == "P":
        txt_l.append(o[2])
    elif o=="L" and txt_l:
            txt_r.append(txt_l.pop())
    elif o=="D" and txt_r:
            txt_l.append(txt_r.pop())
    elif o=="B" and txt_l:
            txt_l.pop()

print("".join(txt_l)+"".join(txt_r[::-1]))