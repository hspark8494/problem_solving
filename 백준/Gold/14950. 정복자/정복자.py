import sys, heapq

input = sys.stdin.readline

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
        return True
    return False

N, M, T = map(int, input().split(" "))
parents = [i for i in range(N+1)]
pq = []
for _ in range(M):
    x, y, val = map(int, input().split(" "))
    heapq.heappush(pq, (val, x, y))

result = 0
cnt = 0
while cnt < N-1:
    val, x, y = heapq.heappop(pq)
    if union(x,y):
        result = result + val + cnt*T
        cnt+=1

print(result)
