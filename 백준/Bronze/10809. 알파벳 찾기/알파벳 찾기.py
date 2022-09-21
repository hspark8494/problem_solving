s = input()
l = [-1 for i in range(26)]

for i,c in enumerate(reversed(s)):
    l[ord(c)-97] = len(s)-i-1

for s in l:
    print(s, end=" ")