input()
l = list(input().split())
t = l[0][-1]
r = 1
for s in l:
    if s[-1]!=t:
        r=0
        break
print(r)