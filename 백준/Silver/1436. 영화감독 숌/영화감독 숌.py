n = int(input())
m = 1
k = 666
while n!=m:
    k=k+1
    t = str(k)
    d = 0
    for i in range(0,len(t)):
        if t[i]=="6":
            d=d+1
        else: 
            d=0
        if d>=3:
            m=m+1
            break
print(k)