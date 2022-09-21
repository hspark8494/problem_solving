from collections import deque

a, b = map(int, input().split())
que = deque()
que.append((a,1))
result = -1

while que:
    curr, cycle = que.popleft()
    if curr == b:
        result = cycle
        break
    if curr*2 <= b:
        que.append((curr*2, cycle+1))
    if (curr*10)+1 <= b:
        que.append(((curr*10)+1, cycle+1))

print(result)