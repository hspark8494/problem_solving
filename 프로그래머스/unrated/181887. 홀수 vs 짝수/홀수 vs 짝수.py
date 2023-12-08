def solution(num_list):
    odd, even = 0, 0
    for i, x in enumerate(num_list):
        if i % 2 ==0:
            even += x
        else:
            odd += x
    return max(even, odd)