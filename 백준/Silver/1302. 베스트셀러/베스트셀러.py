from sys import stdin
from collections import defaultdict
stdin.readline()
d = defaultdict(int)
for l in stdin.readlines():
    d[l.rstrip()] += 1

print(sorted(list(d.keys()), key=lambda x: (-d[x], x))[0])
