# Q12941 최솟값 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12941?language=python3
def solution(a:list, b:list):
    answer = 0
    a.sort()
    b.sort(reverse=True)
    while(a):
        answer+= a.pop()*b.pop()
    return answer