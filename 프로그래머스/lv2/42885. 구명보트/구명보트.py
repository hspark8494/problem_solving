from collections import deque
def solution(people:list, limit):
    d = deque(sorted(people))
    result = 0
    while len(d)>1:
        result += 1
        if d[0] + d[-1] <= limit:
            d.pop()
            d.popleft()
        else:
            d.pop()
    return result + len(d)