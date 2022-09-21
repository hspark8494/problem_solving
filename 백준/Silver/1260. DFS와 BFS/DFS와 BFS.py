from collections import defaultdict, deque

n, m, v = map(int, input().split())
nodes = defaultdict(list)
for _ in range(m):
    i, j = map(int, input().split())
    nodes[i].append(j)
    nodes[j].append(i)

visited = [False for _ in range(n+1)]

for node in nodes.values():
    node.sort()

def bfs(i):
    if visited[i]:
        return
    visited[i] = True
    print(i, end=" ")
    for node in nodes[i]:
        bfs(node)
    
bfs(v)
print()

dq = deque()
visited_bfs = [False for _ in range(n+1)]

dq.append(v)
visited_bfs[v] = True

while dq:
    curr = dq.popleft()
    print(curr, end=" ")
    for i in nodes[curr]:
        if not visited_bfs[i]:
            visited_bfs[i] = True
            dq.append(i)