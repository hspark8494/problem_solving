s=int(input())
for i in reversed(range(1,s+1)):
    print(" "*(s-i) + "*"*i)