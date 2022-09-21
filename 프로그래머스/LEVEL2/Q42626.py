# Q42626 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3
import heapq

def solution(scoville:list, K):
    heapq.heapify(scoville)
    result = 0
    while scoville[0] < K and len(scoville) > 1:
        curr = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, curr)
        result+=1
    if scoville[0] < K:
        return -1
    else:
        return result
