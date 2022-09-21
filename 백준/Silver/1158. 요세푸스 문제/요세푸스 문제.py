from collections import deque
n, k = map(int, input().split())
dq = deque(range(1,n+1))
l = []
t = 0
while dq:
    t=t+1
    if t>=k:
        l.append(dq.popleft())
        t=0
    else:
        dq.append(dq.popleft())

print("<", end="")
print(*l, sep=", ", end=">")