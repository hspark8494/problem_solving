from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
d = defaultdict(int)

for _ in range(N):
    d[input()[0]] += 1

r = sorted(list(filter(lambda x: d[x] >= 5, d.keys())))

if r:
    print("".join(r))
else:
    print("PREDAJA")