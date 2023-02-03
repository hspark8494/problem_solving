import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
d = defaultdict(int)
for _ in range(N):
    S = input().rstrip()
    if len(S) >= M:
        d[S] += 1


def comparator(s: str):
    return (-d[s], -len(s), s)

print(*sorted(d.keys(), key=comparator), sep='\n')
