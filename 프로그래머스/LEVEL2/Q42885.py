# Q42885 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885
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