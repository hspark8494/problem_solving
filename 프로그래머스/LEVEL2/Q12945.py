# Q12945 피보나치 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12945?language=python3
def solution(n):
    result = 0
    a = 0
    b = 1

    for i in range(0, n):
        result = a + b
        a = b
        b = result

    return result%1234567