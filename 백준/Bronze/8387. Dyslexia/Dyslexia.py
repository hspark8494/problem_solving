input()
c = 0
s1 = input()
s2 = input()
for i,j in enumerate(s1):
    if j == s2[i]:
        c=c+1

print(c)