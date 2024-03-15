import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))
names = {}

for _ in range(N):
    q = input().rstrip().split(" ")
    c = "".join(q[2:5])
    if c in names:
        names[c] = "?"
    else:
        names[c] = q[1]

for _ in range(M):
    x = input().rstrip().replace(" ", "")
    print(names[x] if x in names else "!")