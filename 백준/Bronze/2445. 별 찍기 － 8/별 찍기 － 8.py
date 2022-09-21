n = int(input())

for i in range(1,n+1):
    d="*"*i
    d=d+" "*(n-i)*2
    d=d+"*"*i
    print(d)
for i in range(1,n):
    d="*"*(n-i)
    d=d+" "*i*2
    d=d+"*"*(n-i)
    print(d)