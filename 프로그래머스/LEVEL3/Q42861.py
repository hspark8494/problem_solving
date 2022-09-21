# Q42861 섬 연결하기
# https://school.programmers.co.kr/learn/courses/30/lessons/42861
import heapq

def find(x, parent):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y, parent):
    x = find(x,parent)
    y = find(y,parent)
    if x!=y:
        parent[y] = x

def solution(n, costs:list):
    parent = [i for i in range(n)]
    pq = []
    for curr in costs:
        heapq.heappush(pq, (curr[2], curr[0], curr[1]))
    result = 0
    while n>1:
        cost, x, y = heapq.heappop(pq)
        if find(x,parent) != find(y,parent):
            union(x,y,parent)
            result += cost
            n-=1

    return result

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])