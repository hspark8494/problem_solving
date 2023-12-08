from functools import reduce
def solution(num_list):
        return sum(num_list) if len(num_list) > 10 else reduce(lambda acc, cur: acc * cur, num_list, 1)