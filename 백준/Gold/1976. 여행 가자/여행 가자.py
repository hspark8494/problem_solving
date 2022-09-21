from functools import reduce
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
nodes = [i for i in range(N+1)]

def find(x):
    while x!=nodes[x]:
        nodes[x] = nodes[nodes[x]]
        x = nodes[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x<=y:
        nodes[y] = x
    else:
        nodes[x] = y

for i in range(N):
    edges = list(map(int, input().rstrip().split(" ")))
    for (j, e) in enumerate(edges):
        if e:
            union(i+1, j+1)
acc = -1
for curr in list(map(int, input().rstrip().split(" "))):
    root = find(curr)
    if acc != -1 and acc != root:
        print("NO")
        break
    acc = root
else:
    print("YES")