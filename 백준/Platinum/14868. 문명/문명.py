import sys

def find(x):
    while x != parent[x[0]][x[1]]:
        px, py = parent[x[0]][x[1]]
        parent[x[0]][x[1]] = parent[px][py]
        x = parent[x[0]][x[1]]
    return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    parent[x[0]][x[1]] = y


def eq(cvils):
    p = None
    for next in cvils:
        if p == None:
            p = find(next)
        elif p != find(next):
            return False
    return True


input = sys.stdin.readline
pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
after = [(0, 2), (0, -2), (2, 0), (-2, 0)]

N, K = map(int, input().rstrip().split(" "))
parent = [[(h, w) for w in range(N)] for h in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

cvils = set()
for _ in range(K):
    i, j = map(int, input().rstrip().split(" "))
    cvils.add((j-1, i-1))

for curr in cvils:
    visited[curr[0]][curr[1]] = True
    for p in pos:
        h, w = curr[0]+p[0], curr[1]+p[1]
        if 0 <= h < N and 0 <= w < N and (h,w) in cvils:
            union(curr, (h, w))

stack = list(cvils)
dept = 0

while not eq(cvils):
    next = []
    for curr in stack:
        for p in pos:
            h, w = curr[0]+p[0], curr[1]+p[1]
            if 0 <= h < N and 0 <= w < N and not visited[h][w]:
                visited[h][w] = True
                next.append((h, w))

    for curr in stack:
        for p in pos:
            h, w = curr[0]+p[0], curr[1]+p[1]
            if 0 <= h < N and 0 <= w < N:
                union(curr, (h, w))

    for curr in stack:
        for p in after:
            h, w = curr[0]+p[0], curr[1]+p[1]
            if 0 <= h < N and 0 <= w < N and visited[h][w]:
                union(curr, (h, w))

    dept += 1
    stack = next

print(dept)
