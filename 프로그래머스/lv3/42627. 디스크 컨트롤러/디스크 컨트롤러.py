import heapq


def solution(jobs):
    heapq.heapify(jobs)
    pq = []
    result = []
    time = jobs[0][0]
    while jobs or pq:
        while jobs and jobs[0][0] <= time:
            tmp = heapq.heappop(jobs)
            heapq.heappush(pq, (tmp[1], tmp[0]))
        if pq:
            curr = heapq.heappop(pq)
            time = time+curr[0]
            result.append(time-curr[1])
        elif jobs:
            time = jobs[0][0]
            
    return sum(result) // len(result)
