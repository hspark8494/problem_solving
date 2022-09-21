from collections import deque

N, K = map(int, input().split(" "))
visited = set()
que = deque()
result = 0
dept = 0
que.append(N)
while que:
    curr_len = len(que)
    while curr_len:
        curr = que.popleft()
        curr_len -= 1
        if curr == K:
            print(dept)
            que.clear()
            break
        else:
            for value in [curr-1, curr+1]:
                if value >= 0 and value <= 100000 and not value in visited:
                    visited.add(curr)
                    que.append(value)
            curr = curr*2
            if curr <= 100000 and not curr in visited:
                curr_len+=1
                visited.add(curr)
                que.appendleft(curr)
    else:
        dept += 1
