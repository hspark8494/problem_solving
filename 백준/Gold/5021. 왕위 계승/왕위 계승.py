from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))
root = input().rstrip()

class node:
    def __init__(self):
        self.name = ""
        self.parents = []
        self.childern = []
        self.dept = 0.0

names = defaultdict(node)

for _ in range(N):
    c, p1, p2 = input().rstrip().split(" ")
    n = names[c]
    n.name = c
    n.parents.append(p1)
    n.parents.append(p2)
    o1, o2 = names[p1], names[p2]
    o1.name = p1
    o2.name = p2
    o1.childern.append(c)
    o2.childern.append(c)

candidate = []
for _ in range(M):
    candidate.append(input().rstrip())

dq = deque()
names[root].dept = 10000.0
for next in names[root].childern:
    dq.append(next)

while dq:
    curr = names[dq.popleft()]
    curr.dept = names[curr.parents[0]].dept*0.5 + names[curr.parents[1]].dept *0.5
    for next in curr.childern:
        dq.append(next)

result = 0
result_name = ""
for x in candidate:
    curr = names[x]
    if result<curr.dept:
        result = curr.dept
        result_name = curr.name

print(result_name)