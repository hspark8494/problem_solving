def solution(my_str, n):
    li = []
    p = 0
    for i in range(n, len(my_str)+n, n):
        li.append(my_str[p:i])
        p = i
    return li