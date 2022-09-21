a, b = map(int, input().split())
if a>b:
    c=a
    a=b
    b=c

print(b-a-1 if b-a>0 else 0)
for i in range(a+1, b):
    print(i, end=" ")