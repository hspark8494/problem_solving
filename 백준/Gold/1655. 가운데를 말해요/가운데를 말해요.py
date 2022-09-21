import sys,heapq

input = sys.stdin.readline

N = int(input())

mx_pq, mn_pq = [], []

for _ in range(N):
    i = int(input())
    if len(mx_pq) == len(mn_pq):
        heapq.heappush(mx_pq,-i)
    else:
        heapq.heappush(mn_pq, i)

    if mx_pq and mn_pq and -mx_pq[0]>mn_pq[0]:
        c = heapq.heappushpop(mn_pq, -mx_pq[0])
        heapq.heappushpop(mx_pq, -c)

    print(-mx_pq[0])