s=int(input())
for i in reversed(range(s)):
    print(" "*(s-i-1) + "*"*(1+i*2))
for i in range(1,s):
    print(" "*(s-i-1) + "*"*(1+i*2))