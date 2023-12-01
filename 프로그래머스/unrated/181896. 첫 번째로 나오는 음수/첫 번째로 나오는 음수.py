def solution(num_list):
    for i,e in enumerate(num_list):
        if e<0:
            return i
    return -1