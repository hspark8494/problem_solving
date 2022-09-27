import heapq
import sys

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
for _ in range(M):
    p1, p2, val = map(int, input().rstrip().split(" "))
    heapq.heappush(pq, (val, p1, p2))

result = 0

while N > 1:
    val, p1, p2 = heapq.heappop(pq)
    if union(p1, p2):
        print(f"CONNECTED : {p1}, {p2} [{val}]")
        N -= 1
