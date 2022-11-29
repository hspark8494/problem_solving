def solution(my_string):
    s = set()
    r = ""
    for c in my_string:
        if c not in s:
            s.add(c)
            r+=c
    return r