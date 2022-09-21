import heapq

N, T = map(int, input().split(" "))
que = list(map(int, input().split(" ")))

first = 1
last = N
mn = N
while first<=last:
    mid = (first+last)//2
    pq = [0] * mid
    result = True
    for i in que:
        if pq[0]+i > T:
            result=False
            break
        heapq.heappush(pq, heapq.heappop(pq) + i)

    if result:
        last = mid-1
    else:
        first = mid+1

print(last+1)