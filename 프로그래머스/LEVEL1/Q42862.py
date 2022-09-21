# Q42862 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862?language=python3#
def solution(n: int, lost: list, reserve: list):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
   
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)

    return n-len(lost_set)