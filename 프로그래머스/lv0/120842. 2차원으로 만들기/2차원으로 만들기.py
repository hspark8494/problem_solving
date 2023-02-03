def solution(num_list, n):
    li = []
    pre = 0
    for i in range(n, len(num_list)+n, n):
        li.append(num_list[pre:i])
        pre = i

    return li
