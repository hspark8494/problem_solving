from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split(" "))

def bfs(n):
    dq = deque()
    visited = set()
    dq.append(n)
    visited.add(n)
    dept = -1
    while dq:
        dept+=1
        for _ in range(len(dq)):
            curr = dq.popleft()
            if curr==K:
                return dept
            tmp = [curr+1, curr-1, curr*2]
            for t in tmp:
                if t not in visited and t<=100000 and t>=0:
                    visited.add(t)
                    dq.append(t)

print(bfs(N))