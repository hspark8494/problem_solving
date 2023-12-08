from functools import reduce
def solution(n, control):
    c = { "w" : 1,"s" : -1,"d" : 10,"a" : -10 }
    return reduce(lambda acc, curr: acc+c[curr], control, n)