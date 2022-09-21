# Q12953 N개의 최소공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12953
from functools import reduce
from math import gcd

def solution(arr:list):
    return reduce(lambda a,b: a*b//gcd(a,b), arr)