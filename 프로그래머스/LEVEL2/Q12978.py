# Q12978 배달
# https://school.programmers.co.kr/learn/courses/30/lessons/12978
import heapq

def solution(N, road, K):
    nodes = [[] for _ in range(N+1)]
    dist = [1000000000 for _ in range(N+1)]
    li = []
    for r in road:
        nodes[r[0]].append((r[1],r[2]))
        nodes[r[1]].append((r[0],r[2]))

    dist[1] = 0
    heapq.heappush(li, (0, 1))

    while li:
        cost, curr = heapq.heappop(li)
        if dist[curr] < cost:
            continue
        for node in nodes[curr]:
            new_cost = node[1]+cost
            if new_cost < dist[node[0]]:
                dist[node[0]] = new_cost
                heapq.heappush(li, (new_cost, node[0]))
    result = 0
    for i in dist:
        if i<=K:
            result+=1
    return result

print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))
# print(solution(5, [[5,1,1], [1,2,2], [1,3,3], [2,3,4], [2,4,5], [3,4,6]], 3))
    