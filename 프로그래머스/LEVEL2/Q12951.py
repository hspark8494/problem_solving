# Q12951 JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=python3
def solution(s:str):
    return " ".join(list(map(str.capitalize, s.split(" "))))