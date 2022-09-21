
from sys import stdin
input = stdin.readline

class node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.childern = []

N = int(input())
nodes = [node(i) for i in range(N)]
root = None
for (i,p) in enumerate(map(int, input().split(" "))):
    if p == -1:
        root = nodes[i]
        continue
    nodes[i].parent = nodes[p]
    nodes[p].childern.append(nodes[i])

deleted = nodes[int(input())]

result = 0

def dfs(curr):
    global result
    if curr==deleted:
        return
    if not curr.childern or (len(curr.childern) == 1 and curr.childern[0] == deleted):
        result+=1
        return
    for next in curr.childern:
        dfs(next)

dfs(root)
print(result)
