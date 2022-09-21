import heapq, sys

input = sys.stdin.readline

class node:
    def __init__(self, name):
        self.name = name
        self.childern = []
        self.degree = 0
        self.visited = False

N = int(input())
nodes = {}

for _ in range(N):
    parent, child = input().rstrip().split(" ")
    if parent not in nodes:
        nodes[parent] = node(parent)
    if child not in nodes:
        nodes[child] = node(child)
    nodes[parent].childern.append(child)
    nodes[child].degree += 1

pq = []
buffer = []
result = []

for curr in nodes.values():
    if curr.degree == 0:
        curr.visited = True
        heapq.heappush(pq, curr.name)

while pq or buffer:
    if not pq:
        pq = buffer
        buffer = []
    curr = nodes[heapq.heappop(pq)]
    result.append(curr.name)
    for next in curr.childern:
        child = nodes[next]
        child.degree -= 1
        if child.degree == 0 and not child.visited:
            child.visited = True
            heapq.heappush(buffer, next)

if len(nodes) == len(result):
    print(*result, sep="\n")
else:
    print(-1)
