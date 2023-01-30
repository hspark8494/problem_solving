import sys
from collections import defaultdict
input = sys.stdin.readline

d = defaultdict(int)

for _ in range(int(input())):
    f, n = input().split(" ")
    d[f] = d[f] + int(n)

for k, v in d.items():
    if v == 5:
        print("YES")
        break
else:
    print("NO")