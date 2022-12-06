def solution(quiz):
    result = []
    for s in quiz:
        query, val = s.split("=")
        if eval(query) == int(val):
            result.append("O")
        else:
            result.append("X")
    return result