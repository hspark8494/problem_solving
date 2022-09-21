import sys

def find(x):
    while x!=parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if len(values[x]) < len(values[y]):
        x, y = y, x
    values[x].update(values[y])
    parents[y] = x

input = sys.stdin.readline

N, Q = map(int, input().rstrip().split(" "))
buffer = [int(input()) for _ in range(N-1)]
parents = list(range(N+1))

values = [set()]
for _ in range(N):
    s = set()
    s.add(int(input()))
    values.append(s)

queries = [tuple(map(int, input().rstrip().split(" "))) for _ in range(N+Q-1)]
stack = []

while queries:
    o, curr = queries.pop()
    if o == 1:
        union(buffer[curr-2], curr)
    else:
        stack.append(len(values[find(curr)]))

while stack:
    print(stack.pop())