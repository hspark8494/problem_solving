import heapq

def popnext(heap):
    while heap and heap[0][1][0]:
        heapq.heappop(heap)

    return heapq.heappop(heap) if heap else [0, [False]] 

def solution(operations):
    minpq = []
    maxpq = []
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