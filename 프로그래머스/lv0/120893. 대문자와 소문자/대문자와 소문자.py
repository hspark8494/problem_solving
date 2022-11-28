def solution(my_string):
    r = ""
    for c in my_string:
        if c>"Z":
            r += c.upper()
        else:
            r += c.lower()
    return r