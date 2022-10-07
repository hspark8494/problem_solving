import sys

input = sys.stdin.readline
for _ in range(int(input())):
    s = set(range(65, 91))
    for c in input().strip():
        s.discard(ord(c))
    print(sum(s))