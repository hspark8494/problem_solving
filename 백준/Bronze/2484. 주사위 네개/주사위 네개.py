import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
mx = 0

for _ in range(N):
    li = input().rstrip().split(" ")
    d = defaultdict(int)
    for i in li:
        d[int(i)] += 1
    curr = 0
    keys = list(d.keys())
    keys.sort(key=lambda x: d[x], reverse=True)

    if len(keys) == 1:
        curr = keys[0] * 5000 + 50000
    elif len(keys) == 2 and d[keys[0]] != 2:
        curr = keys[0] * 1000 + 10000
    elif len(keys) == 2:
        curr = keys[0] * 500 + keys[1] * 500 + 2000
    elif len(keys) == 3:
        curr = keys[0] * 100 + 1000
    else:
        curr = max(keys) * 100
    mx = max(mx, curr)

print(mx)