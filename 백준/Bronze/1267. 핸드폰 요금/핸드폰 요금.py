i = int(input())
l = list(map(int,input().split()))
y = sum(map(lambda x: x//30*10+10, l))
m = sum(map(lambda x: x//60*15+15, l))

if y<m:
    print("Y %d" % y)
elif y>m:
    print("M %d" % m)
else:
    print("Y M %d" % m)