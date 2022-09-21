def solution(s:str):
    return " ".join(list(map(str.capitalize, s.split(" "))))