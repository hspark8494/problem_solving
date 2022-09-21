mx = 0
c = 0
for i in range(10):
    a, b= map(int, input().split())
    c = c-a+b
    if c>mx:
        mx=c
print(mx)