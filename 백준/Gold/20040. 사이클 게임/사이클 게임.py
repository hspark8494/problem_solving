from re import L
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))
parent = [i for i in range(N)]

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x==y:
        return True
    else:
        parent[y] = x
        return False

for i in range(M):
    x, y = map(int, input().rstrip().split(" "))
    if union(x, y):
        print(i+1)
        break
else:
    print(0)