from collections import deque


def solution(t, p):
    que = deque()
    r = 0
    for c in t:
        if len(que) < len(p)-1:
            que.append(c)
        else:
            que.append(c)
            if int(p) >= int("".join(que)):
                r += 1
            que.popleft()
    return r