# Q42628 이중우선순위큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628?language=python3

import heapq

def popnext(heap):
    while heap and heap[0][1][0]:
        heapq.heappop(heap)
    return heapq.heappop(heap) if heap else [0, [False]] 

def solution(operations):
    minpq, maxpq = [], []
    for o in operations:
        op, val = o.split(" ")
        if op == "I":
            curr = [False]
            val = int(val)
            heapq.heappush(minpq, (val, curr))
            heapq.heappush(maxpq, (-val, curr))
        elif op == "D" and val == "-1":
            curr = popnext(minpq)
            curr[1][0] = True
        elif op == "D" and val == "1":
            curr = popnext(maxpq)
            curr[1][0] = True

    return [-popnext(maxpq)[0], popnext(minpq)[0]]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	))