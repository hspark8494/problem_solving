from collections import defaultdict
import math
d = defaultdict(int)
for s in input():
    if s == '9':
        s = '6'
    d[s] += 1

d['6'] = math.ceil(d['6'] / 2)
print(max(d.values()))