def solution(array):
    i = 0
    for c in "".join(map(str, array)):
        if c=="7":
            i+=1
    return i