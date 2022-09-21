import sys

input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split(" "))

parent = [i for i in range(N+1)]
money = list(map(int, input().rstrip().split(" ")))

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x
    return x

for _ in range(M):
    x, y = map(int, input().rstrip().split(" "))
    union(x,y)

costs = {}
for i, cost in enumerate(money):
    x = find(i+1)
    if x not in costs or costs[x] > cost:
        costs[x] = cost

result = sum(costs.values())

print(result if result <= K else "Oh no")