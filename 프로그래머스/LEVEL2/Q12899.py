# Q12899 124 나라의 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12899?language=python3
def solution(n):
    result = ""
    while n > 0:
        n -= 1
        result = result + "124"[n % 3]
        n = n//3
    return result[::-1]
