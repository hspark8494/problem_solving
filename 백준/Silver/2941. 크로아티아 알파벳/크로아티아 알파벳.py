s = input()
ca = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in ca:
    s = s.replace(c, "1")

print(len(s))