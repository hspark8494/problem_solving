s = input()
o = ""
for i in s:
    t = ord(i)
    if t<=ord("C"):
        t=t+26
    o=o+(chr(t-3))

print(o)