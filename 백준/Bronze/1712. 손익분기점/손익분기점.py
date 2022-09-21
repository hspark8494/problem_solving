a,b,c = map(int, input().split())
d = c-b

if d<=0:
    print(-1)
else:
    e = a/d
    print(int(e)+1)