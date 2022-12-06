import heapq
def solution(k, score):
    answer = []
    pq = []
    for i in score:
        if len(pq) < k:
            heapq.heappush(pq, i)
            answer.append(pq[0])
        else:
            if i>pq[0]:
                heapq.heappushpop(pq, i)
            answer.append(pq[0])
    return answer
