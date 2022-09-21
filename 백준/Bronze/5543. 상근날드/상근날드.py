x = 2001
for i in range(3):
    d = int(input())
    if d<=x:
        x=d
m = int(input())
n = int(input())
print(x+m-50 if n>m else x+n-50)