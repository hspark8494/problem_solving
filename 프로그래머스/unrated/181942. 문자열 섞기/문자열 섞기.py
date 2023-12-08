def solution(str1, str2):
    return "".join([x+y for x,y in zip(str1, str2)])