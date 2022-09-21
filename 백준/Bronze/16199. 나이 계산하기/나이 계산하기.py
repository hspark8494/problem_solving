n = list(map(int,input().split()))
m = list(map(int,input().split()))
o = m[0]-n[0]
if m[1]>n[1]:
    print(o)
elif m[1]<n[1]:
    print(o-1)
else:
    print(o if m[2]>=n[2] else o-1)

print(o+1)
print(o)