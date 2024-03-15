import sys
input = sys.stdin.readline

L = [input().rstrip() for _ in range(5)]
x = max(map(len, L))
r = ''

for i in range(x):
    for j in range(5):
        if len(L[j]) > i:
            r += L[j][i]

print(r)
