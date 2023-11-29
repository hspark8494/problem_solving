def solution(str_list, ex):
    return ''.join(filter(lambda x: not ex in x, str_list))