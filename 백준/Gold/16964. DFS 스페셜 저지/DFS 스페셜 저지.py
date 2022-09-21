import sys
input = sys.stdin.readline

N = int(input())
nodes = [set() for _ in range(N+1)]

for _ in range(N-1):
    e1, e2 = map(int, input().split(" "))
    nodes[e1].add(e2)
    nodes[e2].add(e1)

visited = [False] * (N+1)

order = list(map(int, input().split(" ")))
order.reverse()

def dfs(i):
    curr = nodes[i]
    if visited[i]:
        return
    visited[i] = True
    
    while curr and order:
        if order[-1] in curr:
            next = order.pop()
            curr.remove(next)
            dfs(next)
        else:
            break


if order.pop() != 1:
    print(0)
else:
    dfs(1)
    if not order:
        print(1)
    else:
        print(0)