def solution(my_string, letter):
    return "".join(filter(lambda x : x not in letter, my_string))