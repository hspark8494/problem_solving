from collections import deque

class node:
    def __init__(self, n):
        self.edges = []
        self.visited = False
        self.val = n
    
def solution(n, edge):
    nodes = [node(i) for i in range(n+1)]
    for e in edge:
        nodes[e[0]].edges.append(nodes[e[1]])
        nodes[e[1]].edges.append(nodes[e[0]])
    
    que = deque()
    que.append(nodes[1])
    nodes[1].visited = True
    pre = 0
    last = 0
    while que:
        pre = last
        last = 0
        for _ in range(len(que)):
            curr = que.popleft()
            for next in curr.edges:
                if not next.visited:
                    last += 1
                    next.visited = True
                    que.append(next)

    return pre
