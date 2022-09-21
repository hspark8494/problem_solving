import sys

s = sys.stdin.readline().rstrip()
ln = len(s)

mn = s[:1][::-1] + s[1:2][::-1] + s[2:][::-1]
for i in range(1, ln-1):
    for j in range(i+1, ln):
        t = s[:i][::-1] + s[i:j][::-1] + s[j:][::-1]
        if t<mn:
            mn = t

print(mn)
