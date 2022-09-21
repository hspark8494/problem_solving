from collections import deque

N, K = map(int, input().split(" "))
visited = set()
que = deque()
result = 0
dept = 0
que.append(N)
while que:
    curr_len = len(que)
    for i in range(curr_len):
        curr = que.popleft()
        visited.add(curr)
        if curr == K:
            result+=1
        else:
            for value in [curr-1, curr+1, curr*2]:
                if value >= 0 and value <= 100000 and not value in visited:
                    que.append(value)
    if result >= 1:
        print(dept, result, sep="\n")
        break
    else:
        dept += 1
