def solution(my_string):
    r = ""
    for c in my_string:
        if c=="2":
            r += "0"
        elif c=="0":
            r += "5"
        else:
            r += "2"
    return r   
