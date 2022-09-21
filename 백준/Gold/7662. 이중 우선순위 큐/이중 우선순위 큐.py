import heapq, sys
input = sys.stdin.readline

for _ in range(int(input())):
    min_pq = []
    max_pq = []
    deleted = set()
    for i in range(int(input())):
        op, val = input().rstrip().split()
        if op == "I":
            heapq.heappush(min_pq, (int(val), i))
            heapq.heappush(max_pq, (-int(val), i))
        if op == "D":
            if val == "-1" and min_pq:
                p = heapq.heappop(min_pq)
                while p[1] in deleted and min_pq:
                    p = heapq.heappop(min_pq)
                deleted.add(p[1])
            elif val == "1" and max_pq:
                p = heapq.heappop(max_pq)
                while p[1] in deleted and max_pq:
                    p = heapq.heappop(max_pq)
                deleted.add(p[1])

    result = ["EMPTY", "EMPTY"]
    while min_pq:
        p = heapq.heappop(min_pq)
        if p[1] not in deleted:
            result[1] = p[0]
            break
    while max_pq:
        p = heapq.heappop(max_pq)
        if p[1] not in deleted:
            result[0] = -p[0]
            break
        
    if result[0] == "EMPTY" or result[1] == "EMPTY":
        print("EMPTY")
    else:
        print(result[0], result[1])