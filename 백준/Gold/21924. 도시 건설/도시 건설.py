import heapq, sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))
parent = [i for i in range(N+1)]
nodes = [[] for _ in range(N+1)]

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        return True
    return False

pq = []
total = 0
for _ in range(M):
    p1, p2, val = map(int, input().rstrip().split(" "))
    total += val
    heapq.heappush(pq, (val, p1, p2))
    
result = 0

while N > 1 and pq:
    val, p1, p2 = heapq.heappop(pq)
    if union(p1, p2):
        result += val
        N -= 1
if N>1:
    print(-1)
else:
    print(total - result)
