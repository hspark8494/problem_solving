f1=0
f2=1

x = int(input())

for i in range(x-1):
    r=f1+f2
    f1=f2
    f2=r
print(f2 if x!=0 else 0)