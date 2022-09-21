# Q42587 프린터
# https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3
from collections import deque

def solution(priorities, location):
    que = deque([(i, prio) for (i, prio) in enumerate(priorities)])
    answer = 0
    while True:
        flag = True
        for i in range(1, len(que)):
            if que[0][1] < que[i][1]:
                que.append(que.popleft())
                flag = False
                break
        if flag:
            doc = que.popleft()
            answer += 1
            if doc[0] == location:
                return answer
    