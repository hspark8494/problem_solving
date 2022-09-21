from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
visited = [False for _ in range(101)]
ladders = [-1 for _ in range(101)]

for _ in range(M+N):
    f, t = map(int, input().split(" "))
    ladders[f] = t

dq = deque()
dq.append(1)
dept = -1

while dq:
    dept+=1
    for _ in range(len(dq)):
        curr = dq.popleft()
        visited[curr] = True
        if ladders[curr] > -1:
            if not visited[ladders[curr]]:
                curr = ladders[curr]
                ladders[curr] = True
            else:
                continue
        if curr == 100:
            print(dept)
            sys.exit()

        for i in range(1,7):
            if curr+i <= 100 and not visited[curr+i]:
                dq.append(curr+i)