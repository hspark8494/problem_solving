def solution(array):
    mx = 0
    pos = 0
    for i, n in enumerate(array):
        if n>mx:
            mx = n
            pos = i

    return [mx, pos]