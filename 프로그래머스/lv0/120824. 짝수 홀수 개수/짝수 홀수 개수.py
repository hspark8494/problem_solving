def solution(num_list):
    even = 0
    for i in num_list:
        if i%2 == 0:
            even += 1
    return [even, len(num_list) - even]