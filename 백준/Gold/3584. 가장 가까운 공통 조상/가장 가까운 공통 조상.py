from collections import deque
import sys
input = sys.stdin.readline

class node:
    def __init__(self, val):
        self.val = val
        self.dept = -1
        self.parent = None
        self.childern = []

def find_root(e):
    while e.parent != None:
        e = e.parent
    e.dept = 0
    return e

for _ in range(int(input())):
    N = int(input())
    nodes = [node(i) for i in range(N+1)]
    for _ in range(N-1):
        p, c = map(int, input().split(" "))
        nodes[p].childern.append(nodes[c])
        nodes[c].parent = nodes[p]

    que = deque()
    que.append(find_root(nodes[1]))
    dept = 0
    while que:
        dept += 1
        for _ in range(len(que)):
            tmp = que.pop()
            tmp.dept = dept
            for e in tmp.childern:
                que.append(e)

    t1, t2 = map(int, input().split(" "))
    s1 = nodes[t1]
    s2 = nodes[t2]
    while s1 != s2:
        if s1.dept < s2.dept:
            s2 = s2.parent
        else:
            s1 = s1.parent

    print(s1.val)