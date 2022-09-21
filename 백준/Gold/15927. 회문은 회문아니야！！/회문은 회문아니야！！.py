import sys
s = input()
if s==s[::-1]:
    for i in s:
        if i!=s[0]:
            print(len(s)-1)
            sys.exit()
    print(-1)
else:
    print(len(s))