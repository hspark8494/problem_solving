def solution(str_list):
    for i, e in enumerate(str_list):
        if e == "r":
            return str_list[i+1:]
        elif e == "l":
            return str_list[:i]
    return []