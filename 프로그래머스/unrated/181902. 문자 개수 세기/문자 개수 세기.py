def solution(my_string):
    a = [0] * 52
    for i in my_string:
        if ord(i) >= 97:
            a[ord(i) - 97 + 26] += 1
        else:
            a[ord(i) - 65] += 1
    return a