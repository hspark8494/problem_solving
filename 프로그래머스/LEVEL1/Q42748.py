 # Q42748 K번째 수
 # https://school.programmers.co.kr/learn/courses/30/lessons/42748?language=python3
def solution(array, commands):
    answer = []
    for cmd in commands:
        answer.append(sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1])
    return answer