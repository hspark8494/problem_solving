from collections import deque
import math

N, T, G = map(int, input().split(" "))

visited = set()
visited.add(N)

dq = deque()
dq.append(N)

dept = -1
flag = False
while dq and T>=0:
    dept += 1
    T -= 1
    for _ in range(len(dq)):
        curr = dq.popleft()
        if curr == G:
            dq.clear()
            flag=True
            break
        if 0 <= curr+1 <= 99999 and curr+1 not in visited:
            visited.add(curr+1)
            dq.append(curr+1)
        if curr != 0:
            next = (curr*2) - 10**int(math.log10(curr*2))
            if curr * 2 <= 99999 and next not in visited:
                visited.add(next)
                dq.append(next)

print(dept if flag else "ANG")
