from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
d = defaultdict(int)

for _ in range(N):
    d[int(input())] += 1

print(sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0])
