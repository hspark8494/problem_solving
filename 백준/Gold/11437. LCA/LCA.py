from collections import deque
import sys
input = sys.stdin.readline

class node:
    def __init__(self, val):
        self.val = val
        self.dept = -1
        self.parent = None
        self.childern = []

    def __str__(self):
        return str(self.val)

N = int(input())
nodes = [node(i) for i in range(N+1)]

for _ in range(N-1):
    e1, e2 = map(int, input().split())
    nodes[e1].childern.append(nodes[e2])
    nodes[e2].childern.append(nodes[e1])
    
dq = deque()
dept = 0
dq.append(nodes[1])

while dq:
    dept+=1
    for _ in range(len(dq)):
        e = dq.popleft()
        e.dept = dept
        for child in e.childern:
            child.parent = e
            child.childern.remove(e)
            dq.append(child)

def find_parent():
    t1, t2 = map(int, input().split(" "))
    s1 = nodes[t1]
    s2 = nodes[t2]
    while s1 != s2:
        if s1.dept < s2.dept:
            s2 = s2.parent
        else:
            s1 = s1.parent
    print(s1.val)

for _ in range(int(input())):
    find_parent()