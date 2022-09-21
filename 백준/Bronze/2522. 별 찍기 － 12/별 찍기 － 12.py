n = int(input())

for i in range(1,n+1):
    d=" "*(n-i)
    d=d+"*"*i
    print(d)
for i in range(1,n):
    d=" "*i
    d=d+"*"*(n-i)
    print(d)