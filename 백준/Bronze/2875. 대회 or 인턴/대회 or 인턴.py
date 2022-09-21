import math
n,m,k = map(int,input().split())
d = min(n//2,m)
n=n-(2*d)
m=m-d
if n+m>=k:
    print(d)
else:
    k=math.ceil((k-n-m)/3)
    print(max(0,d-k))
    