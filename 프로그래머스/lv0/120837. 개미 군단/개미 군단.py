def solution(hp):
    r = 0
    for i in [5,3,1]:
        r += hp//i
        hp = hp%i
    return r