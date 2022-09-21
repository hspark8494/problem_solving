from collections import deque

F, S, G, U, D = map(int, input().split(" "))

def bfs(start):
    dept = -1
    visited = set()
    dq = deque()
    dq.append(start)
    while dq:
        dept+=1
        for _ in range(len(dq)):
            curr = dq.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            if curr == G:
                return dept
            if curr+U <= F:
                dq.append(curr+U)
            if curr-D > 0:
                dq.append(curr-D)
    return "use the stairs"
print((bfs(S)))