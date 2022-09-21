import sys

def find(x):
    while x!=parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x!=y:
        parents[y] = x

input = sys.stdin.readline

N, Q = map(int, input().rstrip().split(" "))
buffer = [int(input()) for _ in range(N-1)]
parents = list(range(N+1))

queries = [list(map(int, input().rstrip().split(" "))) for _ in range(N+Q-1)]
stack = []

while queries:
    curr = queries.pop()
    if curr[0] == 0:
        union(buffer[curr[1]-2], curr[1])
    else:
        stack.append(find(curr[1])==find(curr[2]))

while stack:
    print("YES" if stack.pop() else "NO")