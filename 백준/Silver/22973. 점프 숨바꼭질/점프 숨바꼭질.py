from collections import deque

N = int(input())
acc = 1

dq = deque()
dq.append(0)
visited = set()
visited.add(0)
dept = -1
flag = False
while dq:
    for _ in range(len(dq)):
        curr = dq.popleft()
        if curr == N:
            flag = True
            dq.clear()
            break
        next = curr+acc
        back = curr-acc
        if next <= 1000000000000 and next not in visited:
            visited.add(next)
            dq.append(next)
        if back >= (-1000000000000) and back not in visited:
            visited.add(back)
            dq.append(back)
    dept+=1
    acc=acc*2
print(dept if flag else -1)
