import sys,heapq

input = sys.stdin.readline

N = int(input())
pq = []
for _ in range(N):
    heapq.heappush(pq, int(input()))
result = 0
while len(pq) > 1:
    r = heapq.heappop(pq) + heapq.heappop(pq)
    result += r
    heapq.heappush(pq, r)

print(result)