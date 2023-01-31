from collections import defaultdict
S1, S2 = input(), input()
d1, d2 = defaultdict(int), defaultdict(int)

for c in S1:
    d1[c] += 1
for c in S2:
    d2[c] += 1

result = 0
for key in set(d1.keys()).union(d2.keys()):
    mx, mn = max(d1[key], d2[key]), min(d1[key], d2[key])
    result += (mx - mn)

print(result)