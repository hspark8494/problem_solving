from collections import deque

N = int(input())
dq = deque()
dq.append(N)
visited = set()
visited.add(N)

result = -1

while dq:
    result += 1
    for _ in range(len(dq)):
        x = dq.popleft()
        if x == 0:
            dq.clear()
            break
        if x-1 not in visited:
            visited.add(x-1)
            dq.append(x-1)
        s = str(x)
        ln = len(s)
        for i in range(ln):
            if s[i] == '1':
                t = s[0:i] + s[i+1:]
                if t:
                    z = int(t)
                    if z not in visited:
                        visited.add(z)
                        dq.append(z)

print(result)
