n = int(input())

for i in range(1,n):
    d=""
    d=d+" "*(n-i)
    d=d+"*"
    if i >1:
        d=d+" "*(((i-1)*2)-1)
        d=d+"*"
    print(d)
print("*"*(n*2-1))