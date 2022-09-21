from functools import reduce
from math import gcd

def solution(arr:list):
    return reduce(lambda a,b: a*b//gcd(a,b), arr)