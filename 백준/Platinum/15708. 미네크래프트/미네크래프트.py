import sys, heapq

input = sys.stdin.readline

N, T, P = map(int, input().split())
stones = list(map(int, input().split()))

result = 0
pq = []
curr = 0
cnt = 0
for i in range(min(N, T//P+1)):
    curr += stones[i]
    heapq.heappush(pq, -stones[i])
    while T-i*P < curr:
        curr += heapq.heappop(pq)
        cnt += 1
    result = max(result, i-cnt+1)

print(result)
