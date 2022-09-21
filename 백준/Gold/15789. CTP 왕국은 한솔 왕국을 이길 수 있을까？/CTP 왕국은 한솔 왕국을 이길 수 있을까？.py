import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))

parent = [i for i in range(N+1)]
values = [1 for _ in range(N+1)]

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x!=y:
        values[x] += values[y]
        parent[y] = x
    return x

for _ in range(M):
    x, y = map(int, input().rstrip().split(" "))
    union(x,y)

ctp, h, K = map(int, input().rstrip().split(" "))
ctp = find(ctp)
h = find(h)
s = set()

for i in range(1, N+1):
    x = find(i)
    if x!=ctp and x!=h:
        s.add((values[x], x))

li = list(s)
li.sort(reverse=True)

result = values[ctp]
for i in range(min(K, len(li))):
    result += li[i][0]
print(result)
