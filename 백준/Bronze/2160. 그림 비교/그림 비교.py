import sys
input = sys.stdin.readline


def compare(s1: list, s2: list) -> int:
    r = 0
    for i in range(5):
        for j, c in enumerate(s2[i]):
            if s1[i][j] == c:
                r += 1
    return r


N = int(input())

l = []
for i in range(N):
    s = [input().rstrip() for _ in range(5)]
    l.append(s)

mx, group = 0, (1, 2)
for i in range(N):
    for j in range(i, N):
        if i == j:
            continue
        r = compare(l[i], l[j])
        if r > mx:
            mx = r
            group = (i+1, j+1)
print(*group)
