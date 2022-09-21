from collections import defaultdict

i = input()
d = defaultdict(int)
l = list(map(int,input().split()))
j = input()
x = list(map(int,input().split()))

for i in l:
    d[i]+=1

for i in x:
    print(d[i], end=" ")