input()
l = input()
n = 0
p = 1
for i in l:
    i = ord(i)-96
    n=n+i*p
    p=p*31

print(n%1234567891)