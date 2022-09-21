from functools import reduce

def solution(clothes):
    d = {}
    for cloth in clothes:
        d.setdefault(cloth[1], [])
        d[cloth[1]].append(cloth[0])
    li = list(map(len, d.values()))
    return reduce(lambda acc,curr: acc*(1+curr), li, 1) -1