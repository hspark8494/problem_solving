def solution(myString):
    return "".join(map(lambda x: "l" if ord(x) < ord("l") else x, myString))