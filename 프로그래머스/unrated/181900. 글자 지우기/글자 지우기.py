def solution(my_string, indices):
    t = list(my_string)
    for i in indices:
        t[i] = ''
    return ''.join(t)