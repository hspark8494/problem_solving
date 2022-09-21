import re
from collections import defaultdict
l=[]
d= defaultdict(int)

p = re.compile("[.][a-z]+")
for _ in range(int(input())):
    l.append(p.search(input()).group()[1:])

for t in l:
    d[t]+=1

for i in sorted(d):
    print(i,d[i])