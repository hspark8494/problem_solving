import heapq
import sys


def dist(a, b):
    ax, ay = a
    bx, by = b
    return (abs(ax-bx)**2+abs(ay-by)**2) ** 0.5

input = sys.stdin.readline

N = int(input())
parent = [i for i in range(N)]
nodes = [tuple(map(float, input().rstrip().split(" "))) for _ in range(N)]

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

nodes.sort(key=lambda x: x[0]*x[0] + x[1]*x[1] ** 0.5)
result = 0
pq = []

for i in range(N-1):
    for j in range(i+1, N):
        heapq.heappush(pq, (dist(nodes[i], nodes[j]), i, j))

while N-1 > 0:
    val, i, j = heapq.heappop(pq)
    if union(i,j):
        result += val
        N-=1

print(round(result,2))
