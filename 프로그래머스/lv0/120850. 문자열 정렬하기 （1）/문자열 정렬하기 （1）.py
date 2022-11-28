def solution(my_string):
    return sorted(map(int, filter(str.isnumeric, my_string)))