import collections
n = int(input())
l = collections.deque(range(1,n+1))
c = 0
while len(l) > 1:
    if c%2 == 0:
        del l[0]
    else:
        l.append(l[0])
        del l[0]
    c=c+1

print(l[0])
