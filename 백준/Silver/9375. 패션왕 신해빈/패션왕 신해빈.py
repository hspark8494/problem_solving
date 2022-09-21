from functools import reduce
from sys import stdin
def solution(clothes):
    d = {}
    for cloth in clothes:
        d.setdefault(cloth[1], [])
        d[cloth[1]].append(cloth[0])
    li = list(map(len, d.values()))
    return reduce(lambda acc,curr: acc*(1+curr), li, 1) -1
    
input = stdin.readline

for _ in range(int(input())):
	li = []
	for _ in range(int(input())):
		li.append(input().rstrip().split(" "))
	print(solution(li))