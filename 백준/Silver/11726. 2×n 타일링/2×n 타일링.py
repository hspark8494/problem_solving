n = int(input())
a = 1
b = 2
r = 2
while n>r:
    tmp = (a+b)
    a = b
    b = tmp
    r +=1
if n<=1:
    print(n)
else:
    print(b%10007)