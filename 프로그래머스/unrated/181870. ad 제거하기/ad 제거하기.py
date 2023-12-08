def solution(strArr):
    return list(filter(lambda x: "ad" not in x, strArr))