import heapq, sys

input = sys.stdin.readline

def dist(a, b):
    ax, ay = a
    bx, by = b
    return (abs(ax-bx)**2+abs(ay-by)**2) ** 0.5

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
        values[x] += values[y]
        return True
    return False
    

N, M = map(int, input().rstrip().split(" "))
parent = [i for i in range(N)]
values = [1 for _ in range(N)]
nodes = [tuple(map(float, input().rstrip().split(" "))) for _ in range(N)]

for _ in range(M):
    x,y = map(int, input().rstrip().split(" "))
    union(x-1,y-1)

result = 0.0
pq = []

for i in range(N-1):
    for j in range(i+1, N):
        heapq.heappush(pq, (dist(nodes[i], nodes[j]), i, j))

while values[find(0)] != N:
    val, i, j = heapq.heappop(pq)
    if union(i,j):
        result += val
        
print(f"{round(result,2):.2f}")