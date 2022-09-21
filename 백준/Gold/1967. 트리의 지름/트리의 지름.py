from collections import deque
import sys
from unittest import result
input = sys.stdin.readline

class node:
    def __init__(self, idx):
        self.parent = None
        self.childern = []
        self.weight = 0
        self.idx = idx
        self.visited = False

n = int(input())
nodes = [node(i) for i in range(n+1)]
for _ in range(n-1):
    pidx, idx, weight = map(int, input().split(" "))
    nodes[pidx].childern.append(nodes[idx])
    nodes[idx].weight = weight
    nodes[idx].parent = nodes[pidx]

def bfs(init, nodes):
    que = deque()
    nodes[init].visited = True
    que.append((nodes[init], 0))
    result = []
    while que:
        curr, weight = que.popleft()
        weight = weight + curr.weight
        
        result.append((weight, curr.idx))
        for child in curr.childern:
            if not child.visited:
                child.visited= True
                if curr.parent and not curr.parent.visited:
                    que.append((child, weight-curr.weight))
                else:
                    que.append((child, weight))
        if curr.parent and not curr.parent.visited:
            curr.parent.visited = True
            que.append((curr.parent, weight))
    return result

r1 = max(bfs(1, nodes))
for n in nodes:
    n.visited = False
r2 = max(bfs(r1[1], nodes))

print(r2[0])