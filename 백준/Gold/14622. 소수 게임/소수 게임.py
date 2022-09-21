import heapq, sys
input = sys.stdin.readline

li = [list(map(int, input().rstrip().split(" "))) for _ in range(int(input().rstrip()))]

mx = -1
for x in li:
    mx = max(mx, *x)
seive = [i%2!=0 for i in range(mx+1)]
seive[1] = False
seive[2] = True
test = []
for i in range(3, mx+1, 2):
    if seive[i]:
        for j in range(i+i, mx+1, i):
            seive[j] = False

points = [0, 0]
pq = [[],[]]
all_set = set()

for l in li:
    if seive[l[0]]:
        if l[0] in all_set:
            points[0] -= 1000
        else:
            all_set.add(l[0])
            heapq.heappush(pq[0], -l[0])
    else:
        if len(pq[1]) >= 3:
            t1, t2, t3 = heapq.heappop(pq[1]), heapq.heappop(pq[1]), heapq.heappop(pq[1])
            points[1] -= t3
            heapq.heappush(pq[1], t1)
            heapq.heappush(pq[1], t2)
            heapq.heappush(pq[1], t3)
        else:
            points[1] += 1000
    
    if seive[l[1]]:
        if l[1] in all_set:
            points[1] -= 1000
        else:
            all_set.add(l[1])
            heapq.heappush(pq[1], -l[1])
    else:
        if len(pq[0]) >= 3:
            t1, t2, t3 = heapq.heappop(pq[0]), heapq.heappop(pq[0]), heapq.heappop(pq[0])
            points[0] -= t3
            heapq.heappush(pq[0], t1)
            heapq.heappush(pq[0], t2)
            heapq.heappush(pq[0], t3)
        else:
            points[0] += 1000

if points[0] > points[1]:
    print("소수의 신 갓대웅")
elif points[1] > points[0]:
    print("소수 마스터 갓규성")
else:
    print("우열을 가릴 수 없음")