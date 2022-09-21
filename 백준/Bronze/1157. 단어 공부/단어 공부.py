s = input()
li = [0 for i in range(26)]

for c in s:
    d = ord(c)
    if int(d)<=90:
        li[d-65] += 1
    else:
        li[d-97] += 1
mx = 0
i=1
b = False
while i<=25:
    if li[i] > li[mx]:
        mx = i
        b = False
    elif li[i]==li[mx]:
        b = True
    i=i+1

print("?" if b else chr(mx+65))
