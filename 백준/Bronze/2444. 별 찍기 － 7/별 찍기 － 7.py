s=int(input())
for i in range(s):
    print(" "*(s-i-1) + "*"*(1+i*2))
for i in reversed(range(s-1)):
    print(" "*(s-i-1) + "*"*(1+i*2))