from functools import reduce
import sys
input = sys.stdin.readline
N = int(input())
nodes = [i for i in range(N+1)]

def find(x):
    while x != nodes[x]:
        nodes[x] = nodes[nodes[x]]
        x = nodes[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x <= y:
        nodes[y] = x
    else:
        nodes[x] = y

for _ in range(N-2):
    x, y = map(int, input().split(" "))
    union(x, y)

root = find(1)
for curr in range(1, N+1):
    next = find(curr)
    if root != next:
        print(root, next)
        break